MAX_LINES = 3
MAX_BET = 100
MIN_BET = 10


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

def get_bet():
    while True:
        amount = input("Lay down a bet for each line ($" + str(MIN_BET) + " - $" + str(MAX_BET) + "): ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount<= MAX_BET:
                break
            else:
                print(f"Bet must be between ${MIN_BET} - ${MAX_BET}!\n")
        else:
            print("Bet must be a valid number!\n")
        
    return amount


def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet*lines
        
        if total_bet > balance:
            print(f"You do not have sufficient balance. Current balance: ${balance}")
        else:
            break


    print(f"You are betting ${bet} on {lines} lines. Total bet: ${total_bet}\n")

    print(balance,lines,bet)


main()
