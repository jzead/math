def prime(n):
    for i in range(2,int(n**(1/2))+1):
        if n%i == 0:
            return print("no prime number")
        
    return print("prime number")


n = int(input())
prime(n)

    
# github commit test