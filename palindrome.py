key = "SOORAJ"
def is_palindrome(key):
    return key == key[::-1]

res =  is_palindrome(key)
if res:
    print(key,"IS PALINDROME")
else:
    print(key,"IS NOT A PALINDROME")