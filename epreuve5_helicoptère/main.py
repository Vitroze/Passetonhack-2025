#Valeur d'entrée: variable input_s
#Sortie: résultat de print()

input_s = "[10, 15, 5, 3]"


input_s = input_s.replace("[", "")
input_s = input_s.replace("]", "")
tTable = input_s.split(",")

tTable = [int(iNumber) for iNumber in tTable]

iCycle = 0

while len(tTable) > 1:
    
    tTable.sort(reverse=True)
    print(tTable)

    iNumberMax1, iNumberMax2 = tTable.pop(0), tTable.pop(0) 

    iDifference = iNumberMax1 - iNumberMax2
    if iNumberMax1 == iNumberMax2 or iDifference <= 0:
        iCycle += 1 
        
        continue
    
    tTable.append(iDifference)
    
    iCycle += 1 

print("Cycle : ", iCycle)