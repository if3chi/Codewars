"""
The new "Avengers" movie has just been released! There are a lot of people at the cinema box office standing in a huge line. Each of them has a single 100, 50 or 25 dollar bill. An "Avengers" ticket costs 25 dollars.

Vasya is currently working as a clerk. He wants to sell a ticket to every single person in this line.

Can Vasya sell a ticket to every person and give change if he initially has no money and sells the tickets strictly in the order people queue?

Return YES, if Vasya can sell a ticket to every person and give change with the bills he has at hand at that moment. Otherwise return NO.

Exam
"""


def tickets(people):
    change = {
        '25': 0,
        '50': 0
    }
    for person in people:
        if person == 25:
            change['25'] += 1
        elif person == 50:
            change['50'] += 1
            change['25'] -= 1
        else:
            if change['50'] > 0:
                change['50'] -= 1
                change['25'] -= 1
            else:
                change['25'] -= 3
        if change['25'] < 0:
            return 'NO'
    return 'YES'


print(tickets([25, 25, 50, 50, 100]))
