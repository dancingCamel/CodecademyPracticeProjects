import random
import re
money = 100

# Write your game of chance functions here


def valid_stake(stake):
    if type(stake) != int:
        print("Invalid Stake")
        return False
    if stake < 0:
        print("You must bet more than 0!")
        return False
    if stake > money:
        print("You can't bet more than you have!")
        return False
    return True


def valid_choice(choice):
    if type(choice) != str:
        print("Invalid Choice")
        return False
    return True


def check_win(stake, choice, result):
    global money
    before = money
    after = money
    choice = re.sub('\W+', '', choice)
    choice = re.sub('\d', '', choice)
    print("You chose {0}, it was {1}.".format(choice, result))
    after = (after + stake) if choice.lower() == result else (after - stake)
    if after > before:
        print("You Win!")
        return stake
    else:
        print("You Lose!")
        return -(stake)


def coin_flip(stake, choice):
    results = ["heads", "tails"]
    result = results[random.randint(0, 1)]
    if not valid_stake(stake) or not valid_choice(choice):
        return 0
    return check_win(stake, choice, result)


def cho_han(stake, choice):
    result = "even" if (random.randint(
        1, 6) + random.randint(1, 6)) % 2 == 0 else "odd"

    if not valid_stake(stake) or not valid_choice(choice):
        return 0
    return check_win(stake, choice, result)


def pick_card(deck):
    rand = random.randint(0, len(deck)-1)
    card = deck[rand]
    del deck[rand]
    return card


def card_draw(stake):
    # suit, face, value
    deck = [
        ["Hearts", "Ace", 1],
        ["Hearts", "2", 2],
        ["Hearts", "3", 3],
        ["Hearts", "4", 4],
        ["Hearts", "5", 5],
        ["Hearts", "6", 6],
        ["Hearts", "7", 7],
        ["Hearts", "8", 8],
        ["Hearts", "9", 9],
        ["Hearts", "10", 10],
        ["Hearts", "Jack", 11],
        ["Hearts", "Queen", 12],
        ["Hearts", "King", 13],
        ["Clubs", "Ace", 1],
        ["Clubs", "2", 2],
        ["Clubs", "3", 3],
        ["Clubs", "4", 4],
        ["Clubs", "5", 5],
        ["Clubs", "6", 6],
        ["Clubs", "7", 7],
        ["Clubs", "8", 8],
        ["Clubs", "9", 9],
        ["Clubs", "10", 10],
        ["Clubs", "Jack", 11],
        ["Clubs", "Queen", 12],
        ["Clubs", "King", 13],
        ["Diamonds", "Ace", 1],
        ["Diamonds", "2", 2],
        ["Diamonds", "3", 3],
        ["Diamonds", "4", 4],
        ["Diamonds", "5", 5],
        ["Diamonds", "6", 6],
        ["Diamonds", "7", 7],
        ["Diamonds", "8", 8],
        ["Diamonds", "9", 9],
        ["Diamonds", "10", 10],
        ["Diamonds", "Jack", 11],
        ["Diamonds", "Queen", 12],
        ["Diamonds", "King", 13],
        ["Spades", "Ace", 1],
        ["Spades", "2", 2],
        ["Spades", "3", 3],
        ["Spades", "4", 4],
        ["Spades", "5", 5],
        ["Spades", "6", 6],
        ["Spades", "7", 7],
        ["Spades", "8", 8],
        ["Spades", "9", 9],
        ["Spades", "10", 10],
        ["Spades", "Jack", 11],
        ["Spades", "Queen", 12],
        ["Spades", "King", 13]
    ]

    if not valid_stake(stake):
        return 0

    player = pick_card(deck)
    opponent = pick_card(deck)

    if player[2] > opponent[2]:
        print(
            "You chose the {0} of {1}. Your opponent chose {2} of {3}. You Win!".format(player[1], player[0], opponent[1], opponent[0]))
        return stake
    elif player[2] < opponent[2]:
        print(
            "You chose the {0} of {1}. Your opponent chose {2} of {3}. You Lose!".format(player[1], player[0], opponent[1], opponent[0]))
        return -(stake)
    else:
        print(
            "You chose the {0} of {1}. Your opponent chose {2} of {3}. It's a Draw!".format(player[1], player[0], opponent[1], opponent[0]))
        return 0


def roulette(stake, choice):
    # European style, no 00

    low_return = ["even", "odd"]
    high_return = [x for x in range(0, 37)]
    all = low_return + high_return

    if choice not in all:
        print("Invalid Choice")
        return 0

    if not valid_stake(stake):
        return 0

    house = high_return[random.randint(0, len(high_return)-1)]

    if type(choice) == str:
        choice = re.sub('\W+', '', choice)
        choice = re.sub('\d', '', choice)
        choice = choice.lower()
        statement = "You bet on {0}, the ball landed on {1}. ".format(
            choice, house)

        if choice in low_return:
            mod = house % 2
            win = choice == low_return[mod]
            if house == 0 or not win:
                statement += "You Lose!"
                print(statement)
                return -stake

            statement += "You Win!"
            print(statement)
            return stake

    if type(choice) == int:

        if (choice < 0) or (choice > 36):
            print("Invalid Choice")
            return 0

        statement = "You bet on {0}, the ball landed on {1}. ".format(
            choice, house)

        if choice == house:
            statement += "You Win!"
            print(statement)
            return stake * 35

        statement += "You Lose!"
        print(statement)
        return -stake

    print("Invalid Choice")
    return 0


# Test
print("\nCoin Flip:")
money += coin_flip(10, 4)
print(money)
money += coin_flip(10, "heads")
print(money)
money += coin_flip(30, "tails")
print(money)
money += coin_flip(-5, "Tails")
print(money)
money += coin_flip(100, "tails")
print(money)
money += coin_flip(10, "!2tails!")
print(money)

print("\nCho Han:")
money += cho_han(10, "Even")
print(money)
money += cho_han(40, "Odd")
print(money)
money += cho_han(-5, "even")
print(money)
money += cho_han(100, "Odd")
print(money)
money += cho_han(1, 10)
print(money)

print("\nCard Draw:")
money += card_draw(10)
print(money)
money += card_draw(100)
print(money)
money += card_draw(-5)
print(money)
money += card_draw(500)
print(money)
money += card_draw('a')
print(money)

print("\nRoulette:")
money += roulette(20, "odd")
print(money)
money += roulette(20, "even")
print(money)
money += roulette(10, 10)
print(money)
money += roulette(10, "pink")
print(money)
money += roulette(10, "10odd10!")
print(money)
money += roulette(10, -10)
print(money)
money += roulette(10, 0)
print(money)

money += roulette(10, 15)
print(money)
