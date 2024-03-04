
def rövare(x):
    return x + "o" + x


for char in "saga":
    if char not in "aeiouyåäö":
        print(rövare(char), end="")
    else:
        print(char, end="")
'''
def eko(namn):
    print(namn*3)

eko("då")
