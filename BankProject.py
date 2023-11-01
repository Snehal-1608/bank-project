class User():
    usercount = 0
    def __init__(self, name, gender, salary):
        self.name = name
        self.gender = gender
        self.salary = salary
        User.usercount = User.usercount + 1
        self.accountno = User.usercount
        
    def showdetails(self):
        print(f"Name: {self.name}\nGender: {self.gender}\nSalary: {self.salary}")

class Bank(User):
    __bankname = "BOM BANK".center(30)
    __balance = 0
    __usercount = 0
    def __init__(self, name, gender, salary, pin):
        super().__init__(name, gender, salary)
        self.__balance = 0
        self.__name = name
        self.__pin = pin
        Bank.__usercount += 1
        self.__accountno = f"bnkaccno000{Bank.__usercount}"

    def deposit(self, amount):
        self.amount = amount
        self.__balance += self.amount

    def withdraw(self, amount):
        self.withdraw = amount
        if self.withdraw > self.__balance:
            print(f"Insufficient balance {self.__balance}")
        elif self.withdraw >= 100:
            print("Thank you for visiting")
            self.__balance -= self.withdraw
            print(f"Your Current balance: {self.__balance}")
        else:
            print(f"You cannot withdraw less than 100 and Your Current balance: {self.__balance}")

    def viewbalance(self):
        print("Your available balance: ", self.__balance)

    def transfer(self, amount, User):
        self.amount = amount
        self.User=User
        if self.amount > self.__balance:
            print(f"Insufficient balance and current balance: {self.__balance}")
        elif self.amount >= 1 and self.amount <= self.__balance:
            self.__balance -= self.amount
            self.User.deposit(amount)
            print(f"Transferred Successfully and current balance: {self.__balance}")
        elif self.amount <= 1:
            print(f"You cannot transfer less than 1 and current balance: {self.__balance}")

    def getusername(self):
        return self.__name

    def getpin(self):
        return self.__pin

    def logindata(self):
        return [self.__name, self.__pin]

    def __str__(self):
        return f"{self.__name}{self.__pin}"

users = {}
while True:
    print("1. Create Account\n2. Login\n3. Exit\n")
    c = input("Enter your selection: ")

    if c == "1":
        name = input("Enter your name: ")
        gender = input("Enter your gender: ")
        salary = int(input("Enter your salary: "))
        pin = int(input("Enter your pin: "))          
        users[name] = Bank(name, gender, salary, pin)

    elif c == "2":
        name = input("Enter your name: ")
        pin = int(input("Set your password: "))
        obj = users.get(name, None)

        if obj is None or obj.logindata() != [name, pin]:
            print("No Match Found")
        else:
            print("Access Granted")
            while True:
                print("Menu:\n1. Deposit\n2. Withdraw\n3. View Balance\n4. Transfer\n5. Logout")
                s = input("Enter the selection: ")
                
                if s == "1":
                    amount = int(input("Enter the amount to deposit: "))
                    obj.deposit(amount)
                    print("Deposit successful.")
                elif s == "2":
                    amount = int(input("Enter the amount to withdraw: "))
                    obj.withdraw(amount)
                elif s == "3":
                    obj.viewbalance()
                elif s == "4":
                    user_name = input("Enter the user's name: ")
                    user = users.get(user_name, None)
                    if user is None:
                        print("user not found.")
                        continue
                    amount = int(input("Enter the amount to transfer: "))
                    obj.transfer(amount, user)
                elif s == "5":
                    break
                else:
                    print("Invalid selection.")
    elif c == "3":
        break
    else:
        print("Invalid selection. Please try again.")

print("Exiting...")



