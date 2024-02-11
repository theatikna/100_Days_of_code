import pandas as pd
data = pd.read_csv("C:/Users/AMAN/Downloads/NATO-alphabet-start/NATO-alphabet-start/nato_phonetic_alphabet.csv")
new = {values.letter : values.code for (key, values) in data.iterrows()}
user = input("Enter the Word").upper()
print(new)
result = [new[i] for i in user  ]
print(result)
