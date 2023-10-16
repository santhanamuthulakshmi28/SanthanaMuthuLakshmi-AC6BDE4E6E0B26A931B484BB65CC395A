class BankAccount:

  def __init__(self, account_number, account_holder_name, initial_balance = 0.0):
    self.__account_number = account_number
    self.__account_holder_name = account_holder_name
    self.__account_balance = initial_balance

  def deposit(self, amount):
   if amount > 0:
      self.__account_balance += amount
      print(end="\n")
      print("Deposited â‚¹{}. New balance: â‚¹{}".format(amount, self.__account_balance))

   else:
     print(end="\n")
     print("Invalid deposit amount. Please deposit a positive amount.")

  def withdraw(self, amount):
    if amount > 0 and amount <= self.__account_balance:
     self.__account_balance -= amount
     print(end="\n")
     print("Withdrew â‚¹{}. New balance: â‚¹{}".format(amount,self.__account_balance))

    else:
      print("Invalid withdrawal amount or insufficient balance.")
  
  def display_balance(self):
    print(end="\n")
    print("Account balance for {} (Account #{}): â‚¹{}".format(
              self.__account_holder_name, self.__account_number, self.__account_balance))


#Create an instance of the BankAccount class
account = BankAccount(account_number="123456789", account_holder_name="Nilofer", initial_balance=5000.0)

#Test deposit and withdrawl functionality
d=int(input("Enter the amount to deposit: "))
print(end="\n")
w=int(input("Enter the amount to withdraw: "))
account.display_balance()
account.deposit(d)
account.withdraw(w)
account.display_balance()500 