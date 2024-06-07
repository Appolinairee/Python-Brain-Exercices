def sousSequencesCroissantes(t):
    if not t:
        return 0, 0, 0
    
    sequences_numbers = 1
    begin = end = temp_begin = 0
    max_len = 1
    
    print("<", t[0], end="")
    
    for i in range(1, len(t)):
        if t[i-1] >= t[i]:
            print("> , <", t[i], end="")
            sequences_numbers += 1
            temp_begin = i
        else:
            print(",", t[i], end="")
        
        temp_len = i - temp_begin + 1
        if temp_len > max_len:
            max_len = temp_len
            begin = temp_begin
            end = i
        
    print(">")
    
    return sequences_numbers, begin + 1, end + 1



t = [1, 2, 5, 3, 12, 25, 13, 8, 4, 7, 24, 28, 32, 11, 14]

sequences_numbers, begin, end = sousSequencesCroissantes(t)

print(f"\nLe nombre de sous-séquences croissantes est : {sequences_numbers}")

print("\nPlus grande sous-séquence:")
print(f"\tIndice de début: {begin}")
print(f"\tIndice de fin : {end}")