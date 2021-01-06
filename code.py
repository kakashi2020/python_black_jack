import random


deck = {"Ace of Spades": 11, "2 of Spades": 2, "3 of Spades": 3, "4 of Spades": 4,
        "5 of Spades": 5, "6 of Spades": 6, "7 of Spades": 7, "8 of Spades": 8,
        "9 of Spades": 9, "10 of Spades": 10, "Jack of Spades": 10,
        "Queen of Spades": 10, "King of Spades": 10,
        "Ace of Hearts": 11, "2 of Hearts": 2, "3 of Hearts": 3, "4 of Hearts": 4,
        "5 of Hearts": 5, "6 of Hearts": 6, "7 of Hearts": 7, "8 of Hearts": 8,
        "9 of Hearts": 9, "10 of Hearts": 10, "Jack of Hearts": 10,
        "Queen of Hearts": 10, "King of Hearts": 10,
        "Ace of Clovers": 11, "2 of Clovers": 2, "3 of Clovers": 3, "4 of Clovers": 4,
        "5 of Clovers": 5, "6 of Clovers": 6, "7 of Clovers": 7, "8 of Clovers": 8,
        "9 of Clovers": 9, "10 of Clovers": 10, "Jack of Clovers": 10,
        "Queen of Clovers": 10, "King of Clovers": 10,
        "Ace of Diamonds": 11, "2 of Diamonds": 2, "3 of Diamonds": 3, "4 of Diamonds": 4,
        "5 of Diamonds": 5, "6 of Diamonds": 6, "7 of Diamonds": 7, "8 of Diamonds": 8,
        "9 of Diamonds": 9, "10 of Diamonds": 10, "Jack of Diamonds": 10,
        "Queen of Diamonds": 10, "King of Diamonds": 10}

###################################################################################################################
#####                                   DEFINING DEAL |BJ - SPECIFIC|                                         #####


def deal(deck_: dict, value_: int, cards_in_hand_: list, show_list_: list):
    """
    Deals a card for the Black Jack game and provides the added value of the card.
    :param deck_: A Dictionary. Same for everybody.
    :param value_: A score. Dependant on the player.
    :param cards_in_hand_: A list. Dependant on the player.
    :param show_list_: This list the one that's printed in the end.
    :return: Returns a random selected card, its int value and the updated deck without
    the drawn card
    """
    card = random.choice(list(deck_))
    cards_in_hand_.append(card)
    show_list_.append(card)
    hand_value = deck_.get(card) + value_
    deck_.pop(card)
    for card_ in cards_in_hand_:
        if hand_value > 21 and "Ace" in card_:
            hand_value = hand_value - 10
            cards_in_hand_.remove(card_)
    return card, hand_value

###################################################################################################################
#####                                                    RESET                                                #####


def reset(list1: list, list2: list, list3: list, list4: list,
          int1: int, int2: int, my_choice_: str, bot_choice_: str, deck_: dict):
    """
    Resets all the factors of the game to begin from scratch everytime you begin a new game.
    :param list1: Your hand related to value.
    :param list2: Your hand related to figures (or cards).
    :param list3: The bots hand related to value.
    :param list4: The bots related to figures (or cards).
    :param int1: The value or score of your cards.
    :param int2: The value or score of the bots hand.
    :param my_choice_: The decision to 'hit' or 'stand'.
    :param bot_choice_: The bots decision to 'hit' or 'stand'.
    :param deck_: The dictionary containing the full deck of cards.
    :return: Gives you back all the values as originals.
    """
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    int1 = 0
    int2 = 0
    bot_choice_ = ""
    my_choice_ = ""
    deck_ = {"Ace of Spades": 11, "2 of Spades": 2, "3 of Spades": 3, "4 of Spades": 4,
             "5 of Spades": 5, "6 of Spades": 6, "7 of Spades": 7, "8 of Spades": 8,
             "9 of Spades": 9, "10 of Spades": 10, "Jack of Spades": 10,
             "Queen of Spades": 10, "King of Spades": 10,
             "Ace of Hearts": 11, "2 of Hearts": 2, "3 of Hearts": 3, "4 of Hearts": 4,
             "5 of Hearts": 5, "6 of Hearts": 6, "7 of Hearts": 7, "8 of Hearts": 8,
             "9 of Hearts": 9, "10 of Hearts": 10, "Jack of Hearts": 10,
             "Queen of Hearts": 10, "King of Hearts": 10,
             "Ace of Clovers": 11, "2 of Clovers": 2, "3 of Clovers": 3, "4 of Clovers": 4,
             "5 of Clovers": 5, "6 of Clovers": 6, "7 of Clovers": 7, "8 of Clovers": 8,
             "9 of Clovers": 9, "10 of Clovers": 10, "Jack of Clovers": 10,
             "Queen of Clovers": 10, "King of Clovers": 10,
             "Ace of Diamonds": 11, "2 of Diamonds": 2, "3 of Diamonds": 3, "4 of Diamonds": 4,
             "5 of Diamonds": 5, "6 of Diamonds": 6, "7 of Diamonds": 7, "8 of Diamonds": 8,
             "9 of Diamonds": 9, "10 of Diamonds": 10, "Jack of Diamonds": 10,
             "Queen of Diamonds": 10, "King of Diamonds": 10}
    return list1, list2, list3, list4, int1, int2, my_choice_, bot_choice_, deck_

###################################################################################################################
#####                                                 BOT PLAYER                                              #####


def bot(bot_score_: int) -> str:
    """
    This bot is made to decide if s/he want to get another card from the dealer or not, depending on
    the value of his hand in relation to 21.
    :param bot_score_: An int score of the sum value of cards
    :return: A decision of [Y/N] for 'Yes' or 'No' depending on card values.
    """
    if bot_score_ <= 16:
        bots_choice = "Y"
    else:
        bots_choice = "N"
    return bots_choice


###################################################################################################################
#####                                                    REFEREE                                              #####


def referee(bot_score_: int, score_: int, show_of_human_: list, show_of_robot_: list):
    """
    Compares the scores of the player and the bot and dictates a winner.
    :param bot_score_: The int value of the sum of values of the cards of the bot.
    :param score_: The int value of the sum of values of the cards of the player.
    :param show_of_human_: This is the list that will be printed at the end as the users played hand.
    :param show_of_robot_: This is the list that will be printed at the end as the bots played hand.
    :return: A decision of [Y/N] for 'Yes' or 'No' depending on card values.
    """
    if bot_score_ >= 22 and score_ <= 21:
        referee_says = "DEALER: Ruben went over 21. You win!"
    elif score_ >= 22 and bot_score_ <= 21:
        referee_says = "DEALER: You went over 21. Ruben win!"
    elif bot_score_ and score_ >= 22:
        referee_says = "DEALER: You both went over 21. Nobody wins!"
    else:
        if bot_score_ == score_:
            referee_says = "DEALER: It's a tie!"
        elif bot_score_ < score_:
            referee_says = "DEALER: You win!"
        else:
            referee_says = "DEALER: Ruben win!"
    return "YOUR HAND: {1}\nRUBEN'S HAND: {0}\n\nWith a score of:\nYOU: {3}\nRUBEN: {2}\n" \
        .format(show_of_robot_, show_of_human_, bot_score_, score_) + referee_says


###################################################################################################################
#####                                             SCORES & HAND                                               #####


score = 0
bot_score = 0
my_cards = []
bots_cards = []
show_of_hand = []
show_of_bot = []
another_bot_card = ""
another_card = ""
hit = "Y"
stand = "N"
continue_playing = True


###################################################################################################################
#####                                              INTRO & GAME                                               #####


input("Press ENTER to play some Black Jack")
print()
ready_payer_one = input("DEALER: 'Are you ready to begin?'[Y/N]: ")
print("-" * 72)

while continue_playing:
    while ready_payer_one.upper() != hit or stand:
        if ready_payer_one.upper() == hit:
            hand, score = deal(deck, score, my_cards, show_of_hand)
            hand2, score = deal(deck, score, my_cards, show_of_hand)
            bot_hand, bot_score = deal(deck, bot_score, bots_cards, show_of_bot)
            bot_hand2, bot_score = deal(deck, bot_score, bots_cards, show_of_bot)
            print("You got dealt a {} and a {}\n&".format(hand, hand2))
            print("Ruben, the robot, got dealt a {} and a face-down card".format(bot_hand))
            print("-" * 72)
            while another_bot_card.upper() != stand or another_card.upper() != stand:
                if another_card.upper() != stand:
                    another_card = input("DEALER: Would you like another card?[Y/N]: ")
                    another_bot_card = bot(bot_score)
                    print("-" * 72)
                    if another_card.upper() != hit or stand:
                        if another_card.upper() == hit:
                            hand, score = deal(deck, score, my_cards, show_of_hand)
                            print("You draw a {},".format(hand))
                        elif another_card.upper() == stand:
                            print("You stand,")
                        elif another_card.upper() != hit or stand:
                            another_card = input("DEALER: Dude, that's not a valid option. 'Y' to Hit or 'N' to Stand: "
                                                 )
                            print("-" * 72)
                            if another_card.upper() == hit:
                                hand, score = deal(deck, score, my_cards, show_of_hand)
                                print("You draw a {}".format(hand))
                            elif another_card.upper() == stand:
                                print("You stand")

                    if another_bot_card.upper() != stand:
                        bot_hand, bot_score = deal(deck, bot_score, bots_cards, show_of_bot)
                        print("Ruben draw a {}\n".format(bot_hand) + "-" * 72)
                    else:
                        print("Ruben stands\n" + "-" * 72)
                else:

                    while another_bot_card.upper() != stand:
                        another_bot_card = bot(bot_score)
                        if another_bot_card.upper() == hit:
                            input("Press ENTER for Ruben to make a move..\n" + "-" * 72)
                            bot_hand, bot_score = deal(deck, bot_score, bots_cards, show_of_bot)
                            print("Ruben draw a {}\n".format(bot_hand) + "-" * 72)
                    else:
                        input("Press ENTER for Ruben to make a move..\n" + "-" * 72)
                        print("Ruben stands\n" + "-" * 72)

            final = referee(bot_score, score, show_of_hand, show_of_bot)
            print(final + "\n" + ("-" * 72))
            my_cards, bots_cards, show_of_hand, show_of_bot, score, bot_score, another_card, another_bot_card, deck = \
                reset(my_cards, bots_cards, show_of_hand, show_of_bot, score, bot_score, another_card, another_bot_card,
                      deck)
            break

        elif ready_payer_one.upper() == "N":
            print("DEALER: Thanks for the interest. Later!")
            break
        else:
            ready_payer_one = input("DEALER: That's not a valid choice. Please, choose 'Y' for Play or 'N' to Quit. ")
            print("-" * 72)
    again = input("DEALER: Type 'Iztaccihuatl' to PLAY AGAIN or 'N' to quit: ")
    print("DEALER: Haha trolled you. For next time, you can type anything to PLAY AGAIN...")
    print("-" * 72)
    if again.upper() == "N":
        print("MAURICIO: Thanks for playing!")
        continue_playing = False
