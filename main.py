MAX_LINES = 3


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

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + "): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Number of lines must be in the range!\n")
        else:
            print("Number of lines must be a valid number!\n")
        
    return lines  

def main():
    balance = deposit()
    lines = get_number_of_lines()
    print(balance,lines)


main()
