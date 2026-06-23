username = "Mewanya"
password = "2008"

attempts = 3

while attempts > 0:
    user = input("Enter username: ")
    pw = input("Enter password: ")

    if user == username and pw == password:
        print("Login successful!\n")
        break
    else:
        attempts -= 1
        print("Invalid login! Attempts left:", attempts)

if attempts == 0:
    print("Too many failed attempts. Exiting...")
    exit()


def show_balance(acc1, acc2):
    print("Account 1 Balance:", acc1)
    print("Account 2 Balance:", acc2)


def deposit(acc1, acc2):
    account = input("Deposit to (1 or 2): ")
    amount = float(input("Enter amount to deposit: "))

    if amount <= 0:
        print("Invalid amount!")
        return acc1, acc2

    if account == "1":
        acc1 += amount
    elif account == "2":
        acc2 += amount
    else:
        print("Invalid account!")

    print("Deposit successful!")
    return acc1, acc2


def withdraw(acc1, acc2):
    account = input("Withdraw from (1 or 2): ")
    amount = float(input("Enter amount to withdraw: "))

    if amount <= 0:
        print("Invalid amount!")
        return acc1, acc2

    if account == "1":
        if amount > acc1:
            print("Insufficient balance!")
        else:
            acc1 -= amount
            print("Withdrawal successful!")

    elif account == "2":
        if amount > acc2:
            print("Insufficient balance!")
        else:
            acc2 -= amount
            print("Withdrawal successful!")
    else:
        print("Invalid account!")

    return acc1, acc2


def transfer(acc1, acc2):
    from_acc = input("Transfer FROM (1 or 2): ")
    to_acc = input("Transfer TO (1 or 2): ")
    amount = float(input("Enter amount to transfer: "))

    if amount <= 0:
        print("Invalid amount!")
        return acc1, acc2

    if from_acc == "1" and to_acc == "2":
        if amount > acc1:
            print("Insufficient balance!")
        else:
            acc1 -= amount
            acc2 += amount
            print("Transfer successful!")

    elif from_acc == "2" and to_acc == "1":
        if amount > acc2:
            print("Insufficient balance!")
        else:
            acc2 -= amount
            acc1 += amount
            print("Transfer successful!")
    else:
        print("Invalid account selection!")

    return acc1, acc2


# Initial balances
acc1 = 10000
acc2 = 30000

while True:
    print("\n--- Menu ---")
    print("1. Check balance")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Transfer money")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        show_balance(acc1, acc2)

    elif choice == "2":
        acc1, acc2 = deposit(acc1, acc2)

    elif choice == "3":
        acc1, acc2 = withdraw(acc1, acc2)

    elif choice == "4":
        acc1, acc2 = transfer(acc1, acc2)

    elif choice == "5":
        print("Thank you! Exiting program.")
        break

    else:
        print("Invalid choice!")
