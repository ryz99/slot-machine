import random
import time

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 10

ROWS = 3
COLS = 3

#number of symbols in each column
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def get_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

#get slot machine spin
def get_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)


    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        
        columns.append(column)
    
    return columns


#transposes columns before printing - with fancy animations
def print_spin(columns):
#    for row in range(len(columns[0])):
#        for i, column in enumerate(columns):
#            if i != len(column) - 1: #this might be wrong: if i != len(columns) - 1
#                print(column[row], end=" | ")
#            else:
#                print(column[row])
#    print()
    symbols = ["A", "B", "C", "D"]

    for row in range(len(columns[0])):
        goal = 5
        current = 0
        while current < goal:
            print(f"{random.choice(symbols)} | {random.choice(symbols)} | {random.choice(symbols)}", end="\r")
            time.sleep(0.2)
            current += 1
        print(f"{columns[row][0]} | {columns[row][1]} | {columns[row][2]}")


#get user deposit
def deposit():
    while True:
        amount = input(f"Lay down a deposit (minimum ${MIN_BET}): ")
        if amount.isdigit():
            amount = int(amount)
            if amount >= MIN_BET:
                break
            else:
                print(f"Deposit must be greater than ${MIN_BET}!\n")
        else:
            print("Deposit must be a valid number!\n")
        
    return amount


#get number of lines
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


#get user bet
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

def game(balance):
    while True:
        lines = get_number_of_lines()
        bet = get_bet()
        total_bet = bet*lines
        
        if total_bet > balance:
            print(f"You do not have sufficient balance. Current balance: ${balance}")
        else:
            break

    if lines>1:
        print(f"You are betting ${bet} on 1 line. Total bet: ${total_bet}\n")
    else:
        print(f"You are betting ${bet} on {lines} lines. Total bet: ${total_bet}\n")

    slots = get_spin(ROWS, COLS, symbol_count)
    print_spin(slots)

    winnings, winning_lines = get_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}! \nYou won on lines: ", *winning_lines)
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        if balance >= 10:
            print(f"Current balance: ${balance}")
            play = input("Press enter to play (q to quit). ")
            if play == "q":
                break
            else:
                balance += game(balance)
        else:
            break
    
    if balance > 10:
        print(f"You left with ${balance}!")
    else:
        print("Game over! You lost all your cash!!")

main()
