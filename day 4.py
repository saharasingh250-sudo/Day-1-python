for i in range(5):
    print("hello")

for i in range (1,6):
    print("how are you")

for i in range(1,10):
    print("Have a great day")   

for i in range (3):
    print("\nComplaint",i+1)
    name = input("Enter your name:")
    area = input("Enter your area:")
    issue = input("Enter your issue:").lower()
  
    if "water" in issue or "emergency" in issue:
      print("priority high")
    elif "road" in issue:
      print("priority medium")   
    elif "electricity" in issue:
      print("priority medium")  
    else:
      print("priority is low")

for i in range (3):
   print("\nAttempts to login a page",i+1)
   username = input("enter your username:")
   password = input("Enter your password:")

   if username == "admin" and password == "1234":
    print("Login succesfully")
    break
   elif username != "admin" and password !="1234":
      print("login failed")
   elif password != "1234":
      print("wrong password")
   else:
      print("wrong username")

 

 
  