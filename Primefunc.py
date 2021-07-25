num=int(input())
def prime(num):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                print(num,"Not a prime number");
                break
        else:    
            print(num,"Is a prime number");
prime(num)

