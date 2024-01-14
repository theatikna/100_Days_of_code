print("The Love Calculator is calculating your score...")
name1 = input("What is your name? ").lower()
name2 = input("What is their name? ").lower()

combined_names = name1 + name2 
score = combined_names.count("l") + combined_names.count("o") + combined_names.count("v") + combined_names.count("e")
score2 = combined_names.count("t") + combined_names.count("r") + combined_names.count("u") + combined_names.count("e")

final_score = int(str(score2) + str(score))
print(final_score)

if 10 <= final_score <= 90:
    if 40 <= final_score <= 50:
        print("You are Alright")
    else:
        print(f"You scored {final_score}. You go together like coke and mentos.")
else:
    print(f"You scored {final_score}.")
