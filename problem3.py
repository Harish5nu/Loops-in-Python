#Q>Attempt problem 1 with while loop. 
#promlem 1 is

#Q. Write a program to print multiplication table of given number using for loop.
'''n=int(input("Enter a number : "))
for i in range(1,11):
    print(f"{n} X {i}= {n*i}")'''

n=int(input("Enter a number : "))
i=1
while(i<11):
     print(f"{n} X {i}= {n*i}")
     i=i+1