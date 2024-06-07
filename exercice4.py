def zeroOfFunction(f, a, b, err):
    mid = (a+b)/2
    
    if abs(a - b) <= err: 
        return mid
    
    if f(mid) > 0:
        return zeroOfFunction(f, a, mid, err)
    else:
        return zeroOfFunction(f, mid, b, err)
    

def f(x):
    return x ** 2 - 4

a = 0
b = 3
err = 1e-9

zero = zeroOfFunction(f, a, b, err)
print("Approximation du zéro de la fonction :", zero)