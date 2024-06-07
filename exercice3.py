def isPalindrome(t):
    if len(t) <= 1:
        return True
    
    if t[0] == t[-1]:
        return isPalindrome(t[1:-1])

    return False
   

text = "non" 
if isPalindrome(text) :
    print(f"{text} est un palindrome")
else:
    print(f"{text} n'est pas un palindrome")