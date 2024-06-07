def cmToInch(val):
    return val / 2.54

cmValue = float(input("Entrez une mesure en centimètres : "))
inches = cmToInch(cmValue)

print(f"{cmValue} cm = {inches} inch.")