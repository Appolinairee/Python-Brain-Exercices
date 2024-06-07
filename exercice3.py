def isPalindrome(t):
    if len(t) <= 1:
        return True
    
    if t[0] == t[-1] and  isPalindrome(t[1:-1]):
        return True

    return False
   

text = "toot" 
if isPalindrome(text) :
    print(f"{text} est un palindrome")
else:
    print(f"{text} n'est pas un palindrome")