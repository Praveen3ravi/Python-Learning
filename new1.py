n = int(input())
#def prime(n):

for i in range(1, n+1):
    if i % 11 == 0:
        print("Prime")
        if i % 3 == 0:
            print("prime")
            if i % 5 == 0:
                print("prime")
                if i % 7 == 0:
                    print("prime")
    elif i%2==0:
        print("Even")
    print(i)
