#Write a code to print a Fibonacci series upto the nth term. 
# Use the int(input()) to get an input from the user as well for the value of n.)
nth=int(input())
num1,num2=0,1
result=num1+num2
print(nth)
print(num1)
print(num2)
for i in range(3,nth+1):
    print(result)
    num1=num2
    num2=result
    result=num1+num2
    
    


    
       
        
        







   



