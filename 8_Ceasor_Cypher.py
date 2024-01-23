import string


def encrypt():
    code = input("Enter the Code: ")
    shift = int(input("Enter the Shift Number: "))
    newcode = ""

    for char in code:
        if char.isalpha():
            x = alpbhate.index(char)
            new = (x + shift) % len(alphbate)
            j = alpbhate[new]
            newcode += j
        else:
            # Skip spaces
            newcode += char

    print(f"New Message: {newcode} and Previous Message: {code}")
    return restart()


def decrypt():
    print("Decrypt")
    code = input("Enter the Message to decode: ")
    shift = int(input("Enter the Shift: "))
    newcode = ""

    for char in code:
        if char.isalpha():
            x = alpbhate.index(char)
            new = (x - shift) % len(alpbhate)
            j = alpbhate[new]
            newcode += j
        else:
            newcode += char

    print(f"Original code: {newcode} and the Decoded message: {code}")
    return restart()


def restart():
    while True:
        code = input("Do you want to try again? (Y or N): ").lower()
        if code == "y":
            return False
        elif code == "n":
            return True
        else :
            print("Try Again ")
def start():
    game = False
    while not game:
        print("Type \"encrypt\" to encrypt or type \"decrypt\" to decrypt")
        ans = input().lower()

        if ans == "encrypt":
            game = encrypt()
        elif ans == "decrypt":
            game = decrypt()
        else:
            print("Invalid Input. Try Again.")


if __name__ == "__main__":
    alpbhate = list(string.ascii_letters)
    start()
