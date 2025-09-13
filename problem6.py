#Q> write a program to calculate the factorial of a given number using for loop.

n=int(input("Enter the number : "))
i=1
product=1
for i in range (i,n+1):
    product=product*i

print(f"The factorial of {n} is {product}")