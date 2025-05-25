# sum of even number 

num = int(input("\nSelect a number for count how many even\n"))
even_num = 0
for i in range(1, num+1):
    if i %2 ==0:
      even_num +=1
print("The number of even numbers is", even_num)