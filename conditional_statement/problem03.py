                        #   3rd problem     
# create a grade calculator when marks 90 or above grade is A, 80 or above grade is B, 70 or above 60 grade is C, Else less than 60 print you are failed
Marks =int(input("Enter Your Marks\n"))
if Marks >= 101:
    print("Verify Your Marks")
    exit()
if Marks >= 90:
    print("Congratulations you get a Grade A")
elif Marks >= 80:
    print("Congratulations you get a Grade B")
elif Marks >= 70:
    print("Congratulations you get a Grade C")
else:
    print("You are failed, please work hard and try again")            
