from games.roulette import play_roulette
from games.fruit_machine import fruit_machine
from games.blackjack import blackjack

from datetime import datetime

#Step 1: Start Menu
name = input("What is your name? ")
surname = input("What is your surname? ")
birthdate = input("Whats your birthdate? (dd-mm-yyyy) ")
#Step 2: Calculate Age
def calculate_age(birthdate):
    date_of_birth = datetime.strptime(birthdate, "%d-%m-%Y")
    today = datetime.today()
    age = today.year - date_of_birth.year
    print(age)
    if age >= 18:
        return True
    else:
        return False

print(calculate_age(birthdate))

if calculate_age(birthdate):
    print("Welcome to De Goude Driehoek Casino!")
else:
    print("Unfortunately you are not old enough to enter the Casino.")
    exit()
#Step 3
gender = input("What is your gender? m/f/x ")

if gender == "m":
    greeting = "Mr"
elif gender == "f":
    greeting = "Miss"
else: #Anything apart from M/F
    greeting = "Xy"
#Step 4
budget = float(input("What is your budget? € "))
#Fixed cost
entrance_fee = 10
parking_fee = 10.50
drinks_fee = 10
balance = budget - entrance_fee - parking_fee - drinks_fee

if balance < 0:
    print("Unfortunately you don't have sufficient funds to enter the casino.")
    exit()

print("Your balance is €",balance)
#step 5
def main_menu(balance):
    #Main menu
    print("             Main Menu              ")
    print("------------------------------------")
    print("Welcome", greeting, name, surname, "to De Goude Driehoek Casino!")
    print("------------------------------------")
    print("1. Games")
    print("2. Account Information")
    print("3. Balance")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        balance = games_menu(balance)

    elif choice == "2":
        account_information()

    elif choice == "3":
        balance_menu()

    elif choice == "4":
        exit()
#step 6
def games_menu(balance):
    #Games menu
    while True:
        print("Games Menu")
        print("1. Roulette")
        print("2. Fruit machine")
        print("3. Blackjack")
        print("4. Return to the main menu")

        choice = input("Choose an option: ")

        if choice == "1":
            balance = play_roulette(balance)
        elif choice == "2":
            balance = fruit_machine(balance)
        elif choice == "3":
            balance = blackjack(balance)
        elif choice == "4":
            main_menu(balance)

            return
#Step 7
def account_information():
    #Account Info
    print("Account Information")
    print("1.", gender + name + surname )
    print("2.", birthdate )
    print("3. Main Menu ")

    choice = input("Choose an option: ")

    if choice == "3":
        main_menu(balance)
    else:
        account_information()
#Step 8
def balance_menu():
    print("1. ", balance)
    print("0. Main Menu")

    choice = input("Choose an option: ")
    if choice == "1":
        print("Your balance is", balance)
    elif choice == "0":
        main_menu(balance)
    else:
        balance_menu()

#Start menu
main_menu(balance)





