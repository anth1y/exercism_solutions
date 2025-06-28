"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""

def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """
    rounds = []
    base_num = number
    for num in range(3):
        rounds.append(base_num)
        base_num += 1
    return rounds


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """
    both_rounds = rounds_1 + rounds_2
    return both_rounds


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """
    if number in rounds:
        return True
    else:
        return False


def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """
    get_average = sum(hand) / len(hand)

    return float(get_average)


def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """
    first_last_avg = (hand[0] + hand[-1]) / 2
    mid_card = hand[len(hand) // 2] 
    true_avg = sum(hand) / len(hand)

    return first_last_avg == true_avg or mid_card == true_avg
        


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    even_values = [hand[i]for i in range(len(hand)) if i % 2 == 0]
    odd_values = [hand[i] for i in range(len(hand)) if i % 2 ==1]

    even_avg = sum(even_values) / len(even_values) if even_values else 0
    odd_avg = sum(odd_values) / len(odd_values) if odd_values else 0
    return even_avg == odd_avg
       
            

def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """
    if hand and hand[-1] == 11:
        hand[-1] *= 2
    return hand
