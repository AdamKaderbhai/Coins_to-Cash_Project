def get_coins():
    num_quarters = int(input("Enter the number of quarters: "))
    num_dimes = int(input("Enter the number of quarters: " ))
    num_nickels = int(input("Enter the number of nickels: "))
    num_pennies = int(input("Enter the number of pennies: "))

    total_value = (num_quarters * 0.25) + (num_dimes * 0.10) + (num_nickels * 0.05) + (num_pennies * 0.01)
    
    print(f"The total value of your coins is: ${total_value:.2f}")

    return total_value

def make_change(money=0):

    hundred_bills = int(money // 100)
    money %= 100
    fifty_bills = int(money // 50)
    money %= 50
    twenty_bills = int(money // 20)
    money %= 20
    ten_bills = int(money // 10)
    money %= 10
    five_bills = int(money // 5)
    money %= 5
    one_bills = int(money // 1)
    money %= 1
    num_quarters = int(money // 0.25)
    money %= 0.25
    num_dimes = int(money // 0.10)
    money %= 0.10
    num_nickels = int(money // 0.05)
    money %= 0.05
    num_pennies = int(money // 0.01)
    money %= 0.01

    print({hundred_bills}, "hundred dollar bills")
    print({fifty_bills}, "fifty dollar bills")
    print({twenty_bills}, "twenty dollar bills")
    print({ten_bills}, "ten dollar bills")
    print({five_bills}, "five dollar bills")
    print({one_bills}, "one dollar bills")
    print({num_quarters}, "quarters")
    print({num_dimes}, "dimes")
    print({num_nickels}, "nickels")
    print({num_pennies}, "pennies")

def coins_to_cash():
    cash_value = get_coins()
    make_change(cash_value)

coins_to_cash()
    

