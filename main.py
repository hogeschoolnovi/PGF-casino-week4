# Week 3 oplossing: Casino de Gouden Driehoek hoofdmenu, functies, vaste kosten en spellen

from games.blackjack import play_blackjack
from games.fruitmachine import play_fruitmachine
from games.roulette import play_roulette

TICKET_PRICE = 10.00
CONSUMPTION_PRICE = 4.50
GAMBLING_TAX = 2.00
MIN_AGE = 18
DIVIDER_LENGTH = 35
TOTAL_COST = TICKET_PRICE + CONSUMPTION_PRICE + GAMBLING_TAX


def show_main_menu():
    """
    Show the casino's main menu.
    :return:
    """
    print("\nCasino de Gouden Driehoek - hoofdmenu")
    print("-" * DIVIDER_LENGTH)
    print("1. Spellen")
    print("2. Saldo")
    print("3. Account")
    print("0. Stop")
    print()


def show_games_menu():
    """
    Show the game menu.
    :return:
    """
    print("\nCasino de Gouden Driehoek - spellen")
    print("-" * DIVIDER_LENGTH)
    print("1. Fruitmachine")
    print("2. Roulette")
    print("3. Blackjack")
    print("0. Terug")
    print()


def show_account(name, birthdate, salutation):
    """
    Show a player's account statistics:
    - name
    - salutation
    - birthdate
    - age
    :param name:
    :param birthdate:
    :param salutation:
    :return:
    """
    print("\nCasino de Gouden Driehoek - account")
    print("-" * DIVIDER_LENGTH)
    print(f"Naam: {name}")
    print(f"Aanspreekvorm: {salutation}")
    print(f"Geboortedatum: {birthdate}")
    print(f"Leeftijd: {calculate_age(birthdate)}")


def show_balance(balance):
    """
    Show a player's current balance.
    :param balance:
    :return:
    """
    print("\nCasino de Gouden Driehoek - saldo")
    print("-" * DIVIDER_LENGTH)
    print(f"Huidig saldo: € {balance:.2f}")


def determine_salutation(name, gender):
    """
    Determine a salutation based on gender.
    :param name:
    :param gender:
    :return:
    """
    if gender == "m":
        return f"meneer {name}"
    elif gender == "v":
        return f"mevrouw {name}"
    return f"speler {name}"


def calculate_age(birthdate):
    """
    Calculate someone's age based on their birth year.
    :param birthdate:
    :return:
    """
    birth_day, birth_month, birth_year = birthdate.split("-")
    return 2026 - int(birth_year)


def show_welcome_message(startbalance, balance, salutation):
    """
    Show the welcome message and fixed costs from week 2.
    :param startbalance:
    :param balance:
    :param salutation:
    :return:
    """
    has_budget = TOTAL_COST <= startbalance
    conclusion = "Je hebt nog genoeg budget voor toegang tot het casino." \
        if has_budget \
        else "Je hebt niet voldoende budget voor toegang tot het casino."

    print("\nCasino de Gouden Driehoek")
    print("-" * DIVIDER_LENGTH)
    print(f"Welkom, {salutation}")
    print()
    print(f"Startbudget:    € {startbalance:.2f}")
    print(f"Vaste kosten:   € {TOTAL_COST:.2f}")
    print(f"Saldo:          € {balance:.2f}")
    print()
    print(conclusion)

def check_age(birthdate):
    """
    Check whether the player is at least 18 years old.
    :param birthdate
    :return:
    """
    age = calculate_age(birthdate)
    if age < MIN_AGE:
        print(f"\nSorry, je moet 18 jaar of ouder zijn om deze applicatie te gebruiken.")
        exit(1)
    else:
        return birthdate

def main():
    # We bouwen verder op de gegevens uit week 1 en de leeftijdscheck plus vaste kosten uit week 2.
    name = input("Wat is je naam? ").capitalize()
    birthdate = check_age(input("Wat is je geboortedatum? (dd-mm-yyyy) "))
    gender = input("Wat is je gender? (m/v/x) ").strip().lower()
    startbudget = float(input("Met hoeveel geld begin je in Casino de Gouden Driehoek? € "))

    salutation = determine_salutation(name, gender)


    balance = startbudget - TOTAL_COST
    show_welcome_message(startbudget, balance, salutation)



    while True:
        show_main_menu()
        choice = int(input("Kies een optie: ").strip().lower())

        match choice:
            case 0:
                break
            case 1:
                show_games_menu()
                game_choice = int(input("Kies een spel: ").strip().lower())
                match game_choice:
                    case 0:
                        pass
                    case 1:
                        balance = play_fruitmachine(balance)
                    case 2:
                        balance = play_roulette(balance)
                    case 3:
                        balance = play_blackjack(balance)
                    case _:
                        print("Ongeldige keuze, probeer opnieuw.")
            case 2:
                show_balance(balance)
            case 3:
                show_account(name, birthdate, salutation)
            case _:
                print("Ongeldige keuze, probeer opnieuw.")


    print(f"Eindsaldo: € {balance:.2f}")


main()
