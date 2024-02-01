
#collect user deposit
def deposit():
    while True:
        amount = input("Lay down a deposit ($): ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Deposit must be greater than zero!\n")
        else:
            print("Deposit must be a valid number!\n")
        
    return amount

deposit()
