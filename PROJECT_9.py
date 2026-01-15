# project 9 is a basic banking system simulation
# it uses functions, conditionals, and loops and classes
# allows user to open an account, deposit, withdraw, and check balance



 
class BankAccount:
    def __init__(self, account_holder,aadhar_number):
        self.account_holder = account_holder
        self.aadhar_number = aadhar_number
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"amount debited : ${amount:.2f}")

    def check_balance(self):
        print(f"Current balance: ${self.balance:.2f}")

def main():
    print("welcome to basic banking system")
    name=input("Enter account holder name: ")
    aadhar=input("Enter Aadhar number: ")
    account=BankAccount(name,aadhar)
    while True:
        print("\nOptions:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")
        match choice:
            case '1':
                
                    amount = float(input("Enter amount to deposit: "))
                    account.deposit(amount)
                
            case '2':
                
                    amount = float(input("Enter amount to withdraw: "))
                    account.withdraw(amount)
            case '3':
                account.check_balance()
            case '4':
                print("Thank you for using the banking system. Goodbye!")
                break
            case _:
                print("Invalid option, please try again.")

main()
