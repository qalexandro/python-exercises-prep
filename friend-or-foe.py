'''Make a program that filters a list of strings and returns a list with only your friends name in it.

If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...

Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]'''

def friend(x):
    return list(filter(lambda name: len(name) == 4, x))

# with deconstructing
def friend_d(x):
    return [f for f in x if len(f) == 4]

print(friend(["Ryan", "Kieran", "Mark",]))