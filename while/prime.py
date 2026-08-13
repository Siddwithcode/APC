#prime number 
n = int(input("Enter a number: "))

i = 2
while i<n:
    if n%i==0:
        print(n,"is not a prime number")
        break
    else:
        print(n,"is a prime number") 
        break   
    i=i+1