def is_prime(num):
    if num <= 1:
        return False
    for i in range(2,num):
        
        if num%i==0:
            return False
    return True

res=is_prime(31)
if res:
    print("PRIME NO")
else:
    print("NOT A PRIME")
