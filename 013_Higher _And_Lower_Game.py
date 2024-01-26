import random
data = {
    "Dhoni" : 400,
    "Ronaldo": 200,
    "Messi": 300,
    "Virat": 350,
    "Rohit" : 375
}
result = 0
def guess():
    text = random.choice(list(data))
    return text

def correct(opt1, opt2, user ):
    if user == 1 and data[opt1] > data[opt2]:
        return 1
    elif user == 2 and data[opt2] > data[opt1]:
        return 1
    else :
        return 0
def same(opt1, opt2):
    while opt2 == opt1:
        opt2 = guess()
    return opt2
def game():
    opt1 = guess()
    true = True
    result1 = 0
    while true:
        opt2 = guess()
        opt2 = same(opt1, opt2)
        print(opt1)
        print(opt2)
        user = int(input("Enter the Choice 1 or 2 "))
        outcome = correct(opt1, opt2, user)
        if outcome == 1 :
            result1 += 1
            print(result1)
        else :
            print(f"Lost Your Final Score {result1}")
            true = False
        opt1 = opt2


if __name__ == "__main__":

    game()

