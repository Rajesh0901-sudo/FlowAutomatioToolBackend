

from numpy import random

class Account:
    
    def __init__(self):
        self.account_number = 0
        self.holderName = ''
        self.account_balance = 0
        
    def openNewAccount(self,name,initialBalance):
        self.holderName = name
        self.account_number = random.randint(5545545)
        self.account_balance = initialBalance
        return self.account_number
        
    def checkExistingAccount(self,name,account_number):
        
        print(self.account_number,account_number,self.holderName,name)
        
        if(self.account_number == account_number and self.holderName == name):
            return True
        else:
            return False
        
    def showAccountDetails(self):
        print("Hello {}\nYour Account No is {}\nYour Balance is {}".format(self.holderName,self.account_number,self.account_balance))
        
    def depositeMoney(self,amount):
        self.account_balance+=amount
        
    def withdrawMoney(self,amount):
        self.account_balance-=amount

class Customer(Account):
    def __init__(self,name):
        self.myName = name
        self.myAccountNumber = 0
        print("Hello {}".format(self.myName))
        
 
name = str(input("Enter Your Name: "))       

newCustomer = Customer(name)

while True:
    print("\n############################################################\n")
    print("1. Create New Account.")
    print("2. Access Existing Account.")
    print("3. Quit.")
    num = int(input("Enter Your Choice number: "))

    if num == 1:
        newCustomer.myAccountNumber = newCustomer.openNewAccount(newCustomer.myName,100)
        newCustomer.showAccountDetails()
        
    elif num == 2:
        account = int(input("Enter Your Account Number: "))
        
        check = newCustomer.checkExistingAccount(newCustomer.myName,newCustomer.myAccountNumber)
        
        print(check)
        if check:
            while True:
                print("11. Check Balance.")
                print("22. Withdraw.")
                print("33. Deposite.")
                print("44. Back To Previous Menu.")
                print("55. Quit.")
                
                existingCustomersChoice = int(input("Enter Your Choice number: "))
                
                print(existingCustomersChoice)
                
                if existingCustomersChoice == 11:
                    newCustomer.showAccountDetails()
                
                elif existingCustomersChoice == 33:
                    newCustomer.depositeMoney(int(input("Enter Amount: ")))
                    
                elif existingCustomersChoice == 22:
                    newCustomer.withdrawMoney(int(input("Enter Amount: ")))
                    
                elif existingCustomersChoice == 44:
                    break
                
                else:
                    quit()
                    
                    
                
        
    elif num == 3:
        quit()
    
    

    


    
    
    



