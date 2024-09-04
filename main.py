import random
print("Welcome To Snake-Water-Gun Game")
print("Choose \n 1 for Snake \n 2 for Water \n 3 for Gun") 
user=int(input("Enter your choice : "))
computer=random.randint(1, 3)
if (user==computer):
  print("You Chose :", user)
  print("Computer Chose :", computer)
  print(" It's a Draw!! ")
elif (user==1 and computer==3) or     (user==2 and computer==1) or       (user==3 and computer==2):
  print("You Chose :", user)
  print("Computer Chose:", computer)
  print("You Lose!! ")
elif (computer==1 and user==3) or (computer==2 and user==1) or (computer==3 and user==2):
  print("You Chose :", user)
  print("Computer Chose :", computer)
  print("You Win!! ")
else:
  print("Invalid Choice, Please Try Again")
