# count a positive number 

number = [2,4,6,8,10,-6,-4,-2,0,1,-3,5,-7,9]
positive = 0
for num in number:
    
    if num > 0:
        positive += 1
print("The number of positive numbers is", positive)