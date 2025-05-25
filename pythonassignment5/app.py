class ATM:

# Initializing ATM balance, PIN, and authentication status
    def __init__(self):
        self.balance = 5000.0
        self.pin = "1234"
        self.authenticated = False

# Verify PIN
    def check_pin(self, input_pin):
        if input_pin == self.pin:
            self.authenticated = True
            print("PIN verified successfully.")
        else:
            self.authenticated = False
            print("Invalid PIN.")

# Displaying current balance of user
    def check_balance(self):
        if self.authenticated:
            print(f"Your current balance is Rs. {self.balance}.")
        else:
            print("Authentication failed. Please verify your PIN first.")
        
# Deposit amount 
    def deposit(self, amount):
        if self.authenticated:
            if amount > 0:
                self.balance += amount
                print(f"You deposited Rs. {amount}. Your new balance is Rs. {self.balance}.")
            else:
                print("Invalid deposit amount. Amount must be greater than zero.")
        else:
            print("Authentication failed. Please verify your PIN first.")        

# Withdraw amount 
    def withdraw(self, amount):
        if self.authenticated:
            if amount <= 0:
                print("Invalid withdrawal amount. Amount must be greater than zero.")
            elif amount > self.balance:
                print("Insufficient balance to withdraw.")
            else:
                self.balance -= amount
                print(f"You withdraw Rs. {amount}. Your remaining balance is Rs. {self.balance}.")
        else:
                print("Authentication failed. Please verify your PIN first.")
            
# Exit the ATM system
    def exit(self):
        print("Thank you for using the ATM. Take Care!")
        exit()

# Display ATM menu for user 
    def menu(self):
        print("~~~ Welcome to the ATM menu ~~~")
        attempts = 0

# PIN verification 
        while attempts<3:
            input_pin = input("Enter your 4-digit pin number: ")
            if input_pin == self.pin:
                self.authenticated = True
                print("PIN verified successfully.")
                break
            else:
                attempts += 1
                print(f"Invalid PIN. Attempts left: {3 - attempts}.")
        else:
            print("Too many incorrect attempts. Please retry next time with correct password.")
            return
        
# Main menu         
        while True:
            print("~~~~ ATM Menu ~~~~")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Exit")
            choice = input("Select an option (1-4): ")

            if choice == '1':
                atm.check_balance()
            elif choice == '2':
                try:
                    amount = float(input("Enter deposited amount: "))
                    atm.deposit(amount)
                except ValueError:
                    print("Invalid input. Amount must be a number.")
            elif choice == '3':
                try:
                    amount = float(input("Enter withdrawal amount: "))
                    atm.withdraw(amount)
                except ValueError:
                    print("Invalid input. Amount must be a number.")
            elif choice == '4':
                atm.exit()
            else:
                print("Invalid option. Please try again.")

# Run the ATM program
if __name__ == "__main__":
    atm = ATM()
    atm.menu()