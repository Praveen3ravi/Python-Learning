# Write a code to get an integer N and print the even values from 1 till N in a separate line.

# Input Description:
# A single line contains an integer N.

# Output Description:
# Print the even values from 1 to N in a separate line.

# Sample Input :
# 6
# Sample Output :
# 2
# 4
# 6
num=int(input())
for i in range(1,num):
    if i%2==0:
        print(i)
    
    # else:12

    #     print("Enter a even number")


