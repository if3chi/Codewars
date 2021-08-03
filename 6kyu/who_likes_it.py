"""
You probably know the "like" system from Facebook and other pages. People can "like" blog posts, 
pictures or other items. We want to create the text that should be displayed next to such an item.

Implement a function likes :: [String] -> String, which must take in input array, containing the names 
of people who like an item. It must return the display text as shown in the examples:

likes([]) # must be "no one likes this"
likes(["Peter"]) # must be "Peter likes this"
likes(["Jacob", "Alex"]) # must be "Jacob and Alex like this"
likes(["Max", "John", "Mark"]) # must be "Max, John and Mark like this"
likes(["Alex", "Jacob", "Mark", "Max"]) # must be "Alex, Jacob and 2 others like this"

For 4 or more names, the number in and 2 others simply increases.
"""


def likes(names):

    count = len(names)

    if count >= 4:
        return f"{names[0]}, {names[1]} and {len(names[2:])} others like this"
    elif count == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    elif count == 2:
        return f"{names[0]} and {names[1]} like this"
    elif count == 1:
        return f"{names[0]} likes this"
    else:
        return "no one likes this"


def likes2(names):
    # make a dictionary d of all the possible answers. Keys are the respective number
    # of people who liked it.

    # {} indicate placeholders. They do not need any numbers but are simply replaced/formatted
    # in the order the arguments in names are given to format
    # {others} can be replaced by its name; below the argument "others = length - 2"
    # is passed to str.format()
    d = {
        0: "no one likes this",
        1: "{} likes this",
        2: "{} and {} like this",
        3: "{}, {} and {} like this",
        4: "{}, {} and {others} others like this",
    }
    length = len(names)
    # d[min(4, length)] insures that the appropriate string is called from the dictionary
    # and subsequently returned. Min is necessary as len(names) may be > 4

    # The * in *names ensures that the list names is blown up and that format is called
    # as if each item in names was passed to format individually, i. e.
    # format(names[0], names[1], .... , names[n], others = length - 2
    return d[min(4, length)].format(*names, others=length - 2)


print(likes(["Alex", "Jacob", "Mark", "Max"]))
print(likes(["Max", "John", "Mark"]))
print(likes(["Jacob", "Alex"]))
print(likes(["Peter"]))
print(likes([]))
