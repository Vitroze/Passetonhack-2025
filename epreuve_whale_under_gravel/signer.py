#! /usr/bin/env python3

import argparse
import functools
import logging
import os
import random
import re
import socketserver
import string
import sys

from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from pyasn1.type.univ import OctetString, ObjectIdentifier, Sequence
from pyasn1.type.namedtype import NamedType, NamedTypes
from pyasn1.codec.der.decoder import decode

logging.basicConfig(
    stream=sys.stderr,
    format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
    level=getattr(logging, os.environ.get('LOG_LEVEL', 'INFO').upper())
)
logger = logging.getLogger(os.path.splitext(os.path.basename(__file__))[0])


PUBKEY = '''\
-----BEGIN PUBLIC KEY-----
MIICIDANBgkqhkiG9w0BAQEFAAOCAg0AMIICCAKCAgEAr1i24dJXtg5bHUOY4Kkv
oSDkjSVJfjsWwQcfGuNpXBg3rUpcIxQhJTfdmXSaXCNhfxUWO2ZJmIUBAh0ACgf+
3hz1HPLt9/Ey+vRGOtMOB8oCTIHfQifDRAaqUga6mGDRsT8Q3pN34yQ+9cHjZsyH
8xoYjBaUj+abOoyfkVetrLzKSAY0xi6aXbP6UHdkuCSt0mW0O54pT/hONBCH1Xf0
qC9naFmPnZgIGdHGuUOpXkgL41eZPSCVt9AT1WSIbS9VyzIscF0J2kvGvXoHUzBr
8PoB80MR/32JCoYYfMyrS3QrjT3/RUr6R9sKZVbjKC+b5DmUJcWn2VKIWIiITyfJ
eq8eSiztUFv7M06iEO6n2glTMpetxHT7dEBIvxh4D0uppUO/23MTHKAm+f56wyLq
Glc/qhUw+xRB1RXbgepm2ojjCu65LP9cg080ixVfSJD+G3kZasWVUrbIxLoeM/Gp
DVJXczgfeIvars7Km4OxKet+qFyBgCAnTLZDeSNy/20My9WLtpfTtvySSYEFbitf
uRQOy2JuPv58A56oesK8c0+3adGy5QFicEmNMbWLfYveRc9wJ3UrWi1FOkfknIf/
FINKg3tMKNNuYfgqPH3cDXW2Q7HGrtw/mxksjTbJfxCRv5bNEFEk3px9RubRnfRd
5hdxo2NKbskEXw5VPDiZyA0CAQM=
-----END PUBLIC KEY-----
'''

key = RSA.import_key(PUBKEY)
try:
    with open('/flag.txt', 'rt') as f:
        flag = f.readline().strip()
except FileNotFoundError:
    flag = 'flag{test}'


    def verify_signature(msg: bytes, signature: bytes) -> bool:
        try:
            print("=============================")
            print(len(signature), key.size_in_bytes())
            if len(signature) != key.size_in_bytes():
                print("Invalid signature length")
                return False
    
            print(1, msg)
            msg_hash = SHA256.new(msg)

            print(msg_hash.oid, msg_hash)
            print(2)
            print(len(signature))
            asn1_sig = (int.from_bytes(signature) ** key.e).to_bytes(key.size_in_bytes())
            print(3, {asn1_sig.hex()})
            # Search for begining of ASN1 in PKCS #1 v1.5 signature
            nul_byte = asn1_sig.find(b'\x00', 1)
            print(4, nul_byte)
            print(asn1_sig[nul_byte + 1:])
            sig, _ = decode(asn1_sig[nul_byte + 1:], asn1Spec=Sequence())
            print(5)
            digest_algo = sig[0][0]
            print(6)
            if msg_hash.oid != str(digest_algo):
                logger.warning('Bad hash OID (expected: %s, got: %s)', msg_hash.oid, str(digest_algo))
                return False

            print(7)
            received_hash = bytes(sig[1])
            if len(received_hash) != msg_hash.digest_size:
                return False
            same = 0
            for a, b in zip(received_hash, msg_hash.digest()):
                same |= a ^ b
            return same == 0
        except (IndexError, ValueError, TypeError) as e:
            print("Error", e)
            return False


def needs_auth(func):
    @functools.wraps(func)
    def needs_auth_helper(this: 'Client', *args, **kwargs):
        if not this.is_authenticated:
            return 'Authentification requise'
        return func(this, *args, **kwargs)
    return needs_auth_helper


class Client(socketserver.StreamRequestHandler):
    def setup(self):
        super().setup()
        self.is_authenticated = False
        self.keep_serving = True
        self.username = ''

    def handle(self):
        try:
            self.handle_helper()
        except Exception as e:
            self.wfile.write(b'Erreur survenue, fermeture de la connexion\n')
            logger.warning('Got exception %s: %s with %r', type(e).__name__, str(e), self.client_address)

    def prompt_for_input(self, prompt: str = '> ') -> str:
        self.wfile.write(f'{prompt}\n'.encode())
        while True:
            line = self.rfile.readline().strip().decode()
            if not line:
                continue
            return line

    def handle_helper(self):
        self.send_banner()
        while self.keep_serving:
            line = self.prompt_for_input()
            if not line:
                continue
            try:
                cmd, args = line.split(' ', 1)
            except ValueError:
                cmd, args = line, ''
            logger.debug('cmd = %r, args = %r', cmd, args)
            cmd = cmd.lower()
            try:
                method = getattr(self, f'do_{cmd}')
                ret = method(args)
                if not ret:
                    ret = ''
                self.wfile.write(f'{ret}\n'.encode())
            except AttributeError:
                self.wfile.write(f'Méthode {cmd!r} inexistante\n'.encode())

    def send_banner(self):
        banner = 'Vous accédez à un système d\'information classifié.\n' + \
        'Entrer `help` afin de lister les commandes possibles.\n' + \
        'Certaines commandes nécessitent d\'être authentifié.\n'
        self.wfile.write(banner.encode())

    def do_quit(self, _):
        self.keep_serving = False

    def do_help(self, method: str) -> str:
        """
        Afficher l'ensemble des commandes possibles
        """
        def get_doc(m) -> str:
            doc = getattr(m, '__doc__', None)
            if not doc:
                doc = 'Aucune aide fournie pour cette commande'
            return re.sub(r'[ \t]+', ' ', doc.strip())

        try:
            m = getattr(self, f'do_{method.strip()}')
            return get_doc(m)
        except AttributeError:
            pass
        help_msg = ''
        for attr in dir(self):
            if attr.startswith('do_'):
                m = getattr(self, attr)
                name = attr.removeprefix('do_')
                method_help = get_doc(m)
                help_msg += f'{name}: {method_help}\n'
        return help_msg

    def do_auth(self, username: str) -> str:
        """
        authentification de l'utilisateur passé en argument.
        La réponse attendue est une signature encodée en hexadecimal en retour du challenge.
        """
        username = username.strip()
        charset = string.ascii_letters + string.digits
        if not username:
            username = 'root'
        chal = ''.join(random.choice(charset) for _ in range(32))
        self.wfile.write(f'challenge: {chal}\n'.encode())
        hex_signature = self.prompt_for_input('signature hexadecimal> ')
        signature = bytes.fromhex(hex_signature)
        if verify_signature(chal.encode(), signature):
            self.is_authenticated = True
            self.username = username
            return 'OK'
        return 'FAIL'

    @needs_auth
    def do_whoami(self, _) -> str:
        """
        retourne le nom de l'utilisateur authentifié
        """
        return self.username

    @needs_auth
    def do_flag(self, _) -> str:
        """
        retourne le flag en cas d'authentification complétée
        """
        return flag


def main():
    def parse_args():
        parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        parser.add_argument(
            '-p', '--port', dest='port', type=int, default=12345, help='Listen port'
        )
        parser.add_argument(
            'bind_addr', nargs='?', default='127.0.0.1', help='Listen address'
        )
        args = parser.parse_args()
        return args

    args = parse_args()
    logger.debug('args = %r', args)
    server = None
    try:
        server = socketserver.ThreadingTCPServer((args.bind_addr, args.port), Client, False)
        server.allow_reuse_address = True
        server.server_bind()
        server.server_activate()
        server.serve_forever()
    except KeyboardInterrupt:
        if server:
            server.server_close()
    except Exception as e:
        te = type(e)
        show_bt = logger.getEffectiveLevel() <= logging.DEBUG
        logger.error(
            'Caught exception %s.%s: %s',
            te.__module__, te.__name__, str(e), exc_info=show_bt
        )
        return 1
    else:
        return 0


if __name__ == '__main__':
    sys.exit(main())
