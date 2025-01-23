typedef unsigned char   undefined;

typedef unsigned char    byte;
typedef unsigned char    dwfenc;
typedef unsigned int    dword;
typedef unsigned char    undefined1;
typedef unsigned short    undefined2;
typedef unsigned int    undefined4;
typedef unsigned short    word;
typedef struct eh_frame_hdr eh_frame_hdr, *Peh_frame_hdr;

struct eh_frame_hdr {
    byte eh_frame_hdr_version; // Exception Handler Frame Header Version
    dwfenc eh_frame_pointer_encoding; // Exception Handler Frame Pointer Encoding
    dwfenc eh_frame_desc_entry_count_encoding; // Encoding of # of Exception Handler FDEs
    dwfenc eh_frame_table_encoding; // Exception Handler Table Encoding
};

typedef struct fde_table_entry fde_table_entry, *Pfde_table_entry;

struct fde_table_entry {
    dword initial_loc; // Initial Location
    dword data_loc; // Data location
};

typedef struct Elf32_Shdr Elf32_Shdr, *PElf32_Shdr;

typedef enum Elf_SectionHeaderType_x86 {
    SHT_NULL=0,
    SHT_PROGBITS=1,
    SHT_SYMTAB=2,
    SHT_STRTAB=3,
    SHT_RELA=4,
    SHT_HASH=5,
    SHT_DYNAMIC=6,
    SHT_NOTE=7,
    SHT_NOBITS=8,
    SHT_REL=9,
    SHT_SHLIB=10,
    SHT_DYNSYM=11,
    SHT_INIT_ARRAY=14,
    SHT_FINI_ARRAY=15,
    SHT_PREINIT_ARRAY=16,
    SHT_GROUP=17,
    SHT_SYMTAB_SHNDX=18,
    SHT_ANDROID_REL=1610612737,
    SHT_ANDROID_RELA=1610612738,
    SHT_GNU_ATTRIBUTES=1879048181,
    SHT_GNU_HASH=1879048182,
    SHT_GNU_LIBLIST=1879048183,
    SHT_CHECKSUM=1879048184,
    SHT_SUNW_move=1879048186,
    SHT_SUNW_COMDAT=1879048187,
    SHT_SUNW_syminfo=1879048188,
    SHT_GNU_verdef=1879048189,
    SHT_GNU_verneed=1879048190,
    SHT_GNU_versym=1879048191
} Elf_SectionHeaderType_x86;

struct Elf32_Shdr {
    dword sh_name;
    enum Elf_SectionHeaderType_x86 sh_type;
    dword sh_flags;
    dword sh_addr;
    dword sh_offset;
    dword sh_size;
    dword sh_link;
    dword sh_info;
    dword sh_addralign;
    dword sh_entsize;
};

typedef enum Elf32_DynTag_x86 {
    DT_NULL=0,
    DT_NEEDED=1,
    DT_PLTRELSZ=2,
    DT_PLTGOT=3,
    DT_HASH=4,
    DT_STRTAB=5,
    DT_SYMTAB=6,
    DT_RELA=7,
    DT_RELASZ=8,
    DT_RELAENT=9,
    DT_STRSZ=10,
    DT_SYMENT=11,
    DT_INIT=12,
    DT_FINI=13,
    DT_SONAME=14,
    DT_RPATH=15,
    DT_SYMBOLIC=16,
    DT_REL=17,
    DT_RELSZ=18,
    DT_RELENT=19,
    DT_PLTREL=20,
    DT_DEBUG=21,
    DT_TEXTREL=22,
    DT_JMPREL=23,
    DT_BIND_NOW=24,
    DT_INIT_ARRAY=25,
    DT_FINI_ARRAY=26,
    DT_INIT_ARRAYSZ=27,
    DT_FINI_ARRAYSZ=28,
    DT_RUNPATH=29,
    DT_FLAGS=30,
    DT_PREINIT_ARRAY=32,
    DT_PREINIT_ARRAYSZ=33,
    DT_RELRSZ=35,
    DT_RELR=36,
    DT_RELRENT=37,
    DT_ANDROID_REL=1610612751,
    DT_ANDROID_RELSZ=1610612752,
    DT_ANDROID_RELA=1610612753,
    DT_ANDROID_RELASZ=1610612754,
    DT_ANDROID_RELR=1879040000,
    DT_ANDROID_RELRSZ=1879040001,
    DT_ANDROID_RELRENT=1879040003,
    DT_GNU_PRELINKED=1879047669,
    DT_GNU_CONFLICTSZ=1879047670,
    DT_GNU_LIBLISTSZ=1879047671,
    DT_CHECKSUM=1879047672,
    DT_PLTPADSZ=1879047673,
    DT_MOVEENT=1879047674,
    DT_MOVESZ=1879047675,
    DT_FEATURE_1=1879047676,
    DT_POSFLAG_1=1879047677,
    DT_SYMINSZ=1879047678,
    DT_SYMINENT=1879047679,
    DT_GNU_XHASH=1879047924,
    DT_GNU_HASH=1879047925,
    DT_TLSDESC_PLT=1879047926,
    DT_TLSDESC_GOT=1879047927,
    DT_GNU_CONFLICT=1879047928,
    DT_GNU_LIBLIST=1879047929,
    DT_CONFIG=1879047930,
    DT_DEPAUDIT=1879047931,
    DT_AUDIT=1879047932,
    DT_PLTPAD=1879047933,
    DT_MOVETAB=1879047934,
    DT_SYMINFO=1879047935,
    DT_VERSYM=1879048176,
    DT_RELACOUNT=1879048185,
    DT_RELCOUNT=1879048186,
    DT_FLAGS_1=1879048187,
    DT_VERDEF=1879048188,
    DT_VERDEFNUM=1879048189,
    DT_VERNEED=1879048190,
    DT_VERNEEDNUM=1879048191,
    DT_AUXILIARY=2147483645,
    DT_FILTER=2147483647
} Elf32_DynTag_x86;

typedef struct Elf32_Dyn_x86 Elf32_Dyn_x86, *PElf32_Dyn_x86;

struct Elf32_Dyn_x86 {
    enum Elf32_DynTag_x86 d_tag;
    dword d_val;
};

typedef struct Elf32_Phdr Elf32_Phdr, *PElf32_Phdr;

typedef enum Elf_ProgramHeaderType_x86 {
    PT_NULL=0,
    PT_LOAD=1,
    PT_DYNAMIC=2,
    PT_INTERP=3,
    PT_NOTE=4,
    PT_SHLIB=5,
    PT_PHDR=6,
    PT_TLS=7,
    PT_GNU_EH_FRAME=1685382480,
    PT_GNU_STACK=1685382481,
    PT_GNU_RELRO=1685382482
} Elf_ProgramHeaderType_x86;

struct Elf32_Phdr {
    enum Elf_ProgramHeaderType_x86 p_type;
    dword p_offset;
    dword p_vaddr;
    dword p_paddr;
    dword p_filesz;
    dword p_memsz;
    dword p_flags;
    dword p_align;
};

typedef struct GnuBuildId GnuBuildId, *PGnuBuildId;

struct GnuBuildId {
    dword namesz; // Length of name field
    dword descsz; // Length of description field
    dword type; // Vendor specific type
    char name[4]; // Vendor name
    byte hash[20];
};

typedef struct Elf32_Rel Elf32_Rel, *PElf32_Rel;

struct Elf32_Rel {
    dword r_offset; // location to apply the relocation action
    dword r_info; // the symbol table index and the type of relocation
};

typedef struct Elf32_Sym Elf32_Sym, *PElf32_Sym;

struct Elf32_Sym {
    dword st_name;
    dword st_value;
    dword st_size;
    byte st_info;
    byte st_other;
    word st_shndx;
};

typedef struct NoteAbiTag NoteAbiTag, *PNoteAbiTag;

struct NoteAbiTag {
    dword namesz; // Length of name field
    dword descsz; // Length of description field
    dword type; // Vendor specific type
    char name[4]; // Vendor name
    dword abiType; // 0 == Linux
    dword requiredKernelVersion[3]; // Major.minor.patch
};

typedef struct Elf32_Ehdr Elf32_Ehdr, *PElf32_Ehdr;

struct Elf32_Ehdr {
    byte e_ident_magic_num;
    char e_ident_magic_str[3];
    byte e_ident_class;
    byte e_ident_data;
    byte e_ident_version;
    byte e_ident_osabi;
    byte e_ident_abiversion;
    byte e_ident_pad[7];
    word e_type;
    word e_machine;
    dword e_version;
    dword e_entry;
    dword e_phoff;
    dword e_shoff;
    dword e_flags;
    word e_ehsize;
    word e_phentsize;
    word e_phnum;
    word e_shentsize;
    word e_shnum;
    word e_shstrndx;
};




// WARNING: Function: __i686.get_pc_thunk.bx replaced with injection: get_pc_thunk_bx

void _DT_INIT(void)

{
  __gmon_start__();
  return;
}



void FUN_00011030(void)

{
  (*(code *)(undefined *)0x0)();
  return;
}



void __libc_start_main(void)

{
  __libc_start_main();
  return;
}



// WARNING: Unknown calling convention -- yet parameter storage is locked

int printf(char *__format,...)

{
  int iVar1;
  
  iVar1 = printf(__format);
  return iVar1;
}



void __stack_chk_fail(void)

{
                    // WARNING: Subroutine does not return
  __stack_chk_fail();
}



// WARNING: Unknown calling convention -- yet parameter storage is locked

int puts(char *__s)

{
  int iVar1;
  
  iVar1 = puts(__s);
  return iVar1;
}



void errx(void)

{
  errx();
  return;
}



void __cxa_finalize(void)

{
  __cxa_finalize();
  return;
}



// WARNING: Function: __i686.get_pc_thunk.bx replaced with injection: get_pc_thunk_bx

void processEntry entry(undefined4 param_1,undefined4 param_2)

{
  undefined auStack_4 [4];
  
  __libc_start_main(FUN_00011326,param_2,&stack0x00000004,0,0,param_1,auStack_4);
  do {
                    // WARNING: Do nothing block with infinite loop
  } while( true );
}



// WARNING: This is an inlined function

void __i686_get_pc_thunk_bx(void)

{
  return;
}



// WARNING: This is an inlined function

void __i686_get_pc_thunk_bx(void)

{
  return;
}



// WARNING: Function: __i686.get_pc_thunk.dx replaced with injection: get_pc_thunk_dx
// WARNING: Removing unreachable block (ram,0x000110fb)
// WARNING: Removing unreachable block (ram,0x00011105)

void FUN_000110e0(void)

{
  return;
}



// WARNING: Function: __i686.get_pc_thunk.dx replaced with injection: get_pc_thunk_dx
// WARNING: Removing unreachable block (ram,0x0001114e)
// WARNING: Removing unreachable block (ram,0x00011158)

void FUN_00011120(void)

{
  return;
}



// WARNING: Function: __i686.get_pc_thunk.bx replaced with injection: get_pc_thunk_bx

void _FINI_0(void)

{
  if (DAT_00014010 == '\0') {
    __cxa_finalize(PTR_LOOP_00014004);
    FUN_000110e0();
    DAT_00014010 = '\x01';
  }
  return;
}



void _INIT_0(void)

{
  FUN_00011120();
  return;
}



// WARNING: This is an inlined function

void __i686_get_pc_thunk_dx(void)

{
  return;
}



// WARNING: Function: __i686.get_pc_thunk.ax replaced with injection: get_pc_thunk_ax

int FUN_000111cd(int param_1)

{
  undefined4 local_8;
  
  for (local_8 = 0; *(char *)(local_8 + param_1) != '\0'; local_8 = local_8 + 1) {
  }
  return local_8;
}



// WARNING: Function: __i686.get_pc_thunk.ax replaced with injection: get_pc_thunk_ax

void FUN_000111fe(int param_1,int param_2)

{
  undefined local_5;
  
  for (local_5 = 0; local_5 < 0x11; local_5 = local_5 + 1) {
    *(undefined *)(param_1 + (uint)local_5) = *(undefined *)(param_2 + (uint)local_5);
  }
  *(undefined *)(param_1 + 0x11) = 0;
  return;
}



// WARNING: Function: __i686.get_pc_thunk.ax replaced with injection: get_pc_thunk_ax

undefined4 FUN_00011252(int param_1,int param_2)

{
  byte local_5;
  
  local_5 = 0;
  while( true ) {
    if (0x10 < local_5) {
      return 1;
    }
    if (*(char *)(param_1 + (uint)local_5) != *(char *)(param_2 + (uint)local_5)) break;
    local_5 = local_5 + 1;
  }
  return 0;
}



// WARNING: Function: __i686.get_pc_thunk.bx replaced with injection: get_pc_thunk_bx

undefined4 FUN_000112a9(int param_1)

{
  uint local_10;
  
  for (local_10 = 0; local_10 < 0x11; local_10 = local_10 + 1) {
    *(byte *)(local_10 + param_1) =
         (char)local_10 + (*(byte *)(local_10 + param_1) ^ PTR_DAT_00014008[local_10 % 3]) + -5;
  }
  return 0;
}



// WARNING: Function: __i686.get_pc_thunk.bx replaced with injection: get_pc_thunk_bx

undefined4 FUN_00011326(int param_1,int param_2)

{
  undefined4 uVar1;
  int iVar2;
  undefined4 *puVar3;
  int in_GS_OFFSET;
  undefined4 uStack_50;
  char *pcStack_4c;
  undefined4 uStack_44;
  undefined auStack_40 [12];
  int local_34;
  char local_2d;
  int local_2c;
  undefined4 local_26;
  undefined4 local_22;
  undefined4 local_1e;
  undefined4 local_1a;
  undefined2 local_16;
  int local_14;
  undefined4 *local_10;
  
  local_10 = &param_1;
  puVar3 = (undefined4 *)auStack_40;
  uStack_44 = 0x1133d;
  local_34 = param_2;
  local_14 = *(int *)(in_GS_OFFSET + 0x14);
  if (param_1 < 2) {
    pcStack_4c = "Pas assez d\'arguments";
    puVar3 = &uStack_50;
    uStack_50 = 1;
    errx();
  }
  *(undefined4 *)((int)puVar3 + -0x10) = *(undefined4 *)(local_34 + 4);
  *(undefined4 *)((int)puVar3 + -0x14) = 0x1137e;
  local_2c = FUN_000111cd();
  if (local_2c == 0x11) {
    local_26 = 0;
    local_22 = 0;
    local_1e = 0;
    local_1a = 0;
    local_16 = 0;
    *(undefined4 *)((int)puVar3 + -0xc) = *(undefined4 *)(local_34 + 4);
    *(undefined4 **)((int)puVar3 + -0x10) = &local_26;
    *(undefined4 *)((int)puVar3 + -0x14) = 0x113e1;
    FUN_000111fe();
    *(undefined4 **)((int)puVar3 + -0x10) = &local_26;
    *(undefined4 *)((int)puVar3 + -0x14) = 0x113f0;
    local_2d = FUN_000112a9();
    if (local_2d == -1) {
      *(char **)((int)puVar3 + -0x10) = "C\'est un echec ...";
      *(undefined4 *)((int)puVar3 + -0x14) = 0x1140b;
      puts(*(char **)((int)puVar3 + -0x10));
      uVar1 = 1;
    }
    else {
      *(undefined **)((int)puVar3 + -0xc) = PTR_s_9xr_J_<[nDSqRd_)X_0001400c;
      *(undefined4 **)((int)puVar3 + -0x10) = &local_26;
      *(undefined4 *)((int)puVar3 + -0x14) = 0x11428;
      iVar2 = FUN_00011252();
      if (iVar2 == 0) {
        *(char **)((int)puVar3 + -0x10) = "C\'est un echec ...";
        *(undefined4 *)((int)puVar3 + -0x14) = 0x11460;
        puts(*(char **)((int)puVar3 + -0x10));
        uVar1 = 1;
      }
      else {
        *(undefined4 *)((int)puVar3 + -0xc) = *(undefined4 *)(local_34 + 4);
        *(char **)((int)puVar3 + -0x10) = "Bravo, le flag est : %s\n";
        *(undefined4 *)((int)puVar3 + -0x14) = 0x11447;
        printf(*(char **)((int)puVar3 + -0x10));
        uVar1 = 0;
      }
    }
  }
  else {
    *(char **)((int)puVar3 + -0x10) = "C\'est un echec ...";
    *(undefined4 *)((int)puVar3 + -0x14) = 0x1139d;
    puts(*(char **)((int)puVar3 + -0x10));
    uVar1 = 1;
  }
  if (local_14 != *(int *)(in_GS_OFFSET + 0x14)) {
    *(undefined4 *)((int)puVar3 + -4) = 0x11479;
    uVar1 = FUN_00011490();
  }
  return uVar1;
}



// WARNING: This is an inlined function

undefined4 __i686_get_pc_thunk_ax(void)

{
  undefined4 unaff_retaddr;
  
  return unaff_retaddr;
}



// WARNING: Function: __i686.get_pc_thunk.bx replaced with injection: get_pc_thunk_bx

void FUN_00011490(void)

{
                    // WARNING: Subroutine does not return
  __stack_chk_fail();
}



// WARNING: Function: __i686.get_pc_thunk.bx replaced with injection: get_pc_thunk_bx

void _DT_FINI(void)

{
  return;
}


