print("Today we are learning multiple condition sentences using elif")
marks = int(input("enter your marks:"))

if marks >= 90:
    print("Excellent")

elif marks >=60:
    print("good")

elif marks >=40:
    print("passed")


else:
    print("you failed")   


age = int(input("Enter your age:"))
if age < 5:
    print("you are a child")

elif age < 18:
    print("you are a teen")

elif age < 60:
    print("you are an adult")

else:
    print(" you are in your old age")

colour = (input("enter a colour:"))
if colour == "red":
  print("TO STOP")

elif colour == "yellow":
    print("To Wait") 

else:
    print("TO GO WHEN GREEN") 

issue = input("enter your issue:")  
if issue == "water":
    print(" emergency issue")

elif issue == "road":
    print("medium issue")

elif issue == "Electricity":
    print("medium issue")

else:
    print("Low issuse")

salary =int(input("Enter your salary:"))
if salary <= 2500000:
    print("no Tax")

elif salary <=500000:
    print("5% of tax")

elif salary <=1500000:
    print("20% of tax")

else:
    print("30% of tax")




