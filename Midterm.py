
db ={}

def checkAccount (account):
  CorrectAccount = True
  if len(account) != 5:
      print ("incorrect account number")
      CorrectAccount = False
  for i in range(2,len(account)):
    if account[i].isdigit() == False:
      CorrectAccount = False
  if account[0] != "T" or account[1] != "B":
      CorrectAccount = False
  return CorrectAccount

def accountExists (account):
  for i in db:
    if i == account:
      return True
  return False

while (True):       
  name = input("Please enter your name:")
  surname = input("Please enter your surname:")
  account= input("Please enter your bank account :")
  
  if (checkAccount(account)):
    print("You are registered")
    userInfo = {"name": name, "surname": surname, "account": account}
    db[account] = userInfo
    break
  else:
    print("Your Account number is incorrect")

while(True):
  accountNumber = input("Please enter your bank account :") 
  moneyAmount = input ("Please enter the amount you want :")
    
  if accountExists(accountNumber):
    if moneyAmount.isdigit():
          db[accountNumber].update({"Balance": int(moneyAmount)})
          print (moneyAmount + "has been added to your account")
          break
    else:
          print("Please enter correct amount of the money")
  else:
        print("Please enter correct account number")
        
while(True):
  accountNumber1 = input("Please enter your bank account :") 
  if accountExists(accountNumber1):
      accountNumber2 = input("Please enter bank account you want to send money to :")
      if accountExists(accountNumber2):
        money = input ("Please enter the amount you want :")
      else:
       print("Account number is incorrect")  
  else:
    print("Account number is incorrect")  
  
  if db[accountNumber1][4] >= int(money):
    db[accountNumber1][4] = [accountNumber1][4] - int(money)
    db[accountNumber2][4] = db[accountNumber2][4] + int(money)
    print("You've succesfully transfered money to:" + db[accountNumber2][0] +" " + db[accountNumber2][1] )
  else: 
    print ("You have not enough money to do the transaction")
  
  
