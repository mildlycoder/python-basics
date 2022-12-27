import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 5

ROWS = 3
COLS = 3

SYMBOLS = {
    "A": 3,
    "B": 5,
    "C": 7,
    "D": 9
}

SYMBOL_VALUES = {
    "A": 3,
    "B": 5,
    "C": 7,
    "D": 9
}

def spin_slots(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _  in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = []
    for _ in range(cols):
        column = []
        curr_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(curr_symbols)
            curr_symbols.remove(value)
            column.append(value)
        
        columns.append(column)
    
    return columns


def print_slots(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) -1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()


def check_winnings(columns, lines, bet, values):
        winnings = 0
        winning_line = []
        for line in range(lines):
            symbol = columns[0][line]
            for column in columns:
                symbol_to_check = column[line]
                if symbol != symbol_to_check:
                    break
            else:
                winnings += values[symbol] * bet
                winning_line.append(line+1)
        
        return winnings, winning_line        

    
def deposit():
    while True: 
        amount = input("enter the deposit amount? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("amount must be greater than zero")
        else:
            print("enter a valid amount")
    return amount

def get_lines():
    while True: 
        lines = input("enter the number of lines you want to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("enter within the range")
        else:
            print("enter a valid amount")
    return lines

def get_bet():
    while True: 
        bet = input("enter the betting amount for each line? $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"enter within range of ${MIN_BET}-${MAX_BET}")
        else:
            print("enter a valid amount")
    return bet

def spin(balance):
    lines = get_lines()
    while True:
        bet = get_bet()
        total_bet = bet*lines
        if total_bet > balance:
            print(f"you don't have enough to bet. your current balance is ${balance}")
        else:
            break

    print(f"you're betting ${bet} on {lines} each. Your total bet is ${total_bet}")

    slots = spin_slots(ROWS, COLS, SYMBOLS)
    print_slots(slots)
    winnings, winning_line = check_winnings(slots , lines, bet, SYMBOL_VALUES)

    print(f"you won ${winnings}")

    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"current balance: ${balance}")
        choice = input("press enter to spin(or q to quit)")
        if choice == 'q':
            break
        balance += spin(balance)
    print(f"you're left with {balance}")
    

main()