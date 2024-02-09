import pandas as pd

# Read data from CSV file
data = pd.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# Extract the "Primary Fur Color" column
categories = data["Primary Fur Color"]

# Initialize a dictionary to count occurrences of each fur color
count = {}

# Count occurrences of each fur color
for color in categories:
    if pd.isna(color):  # Check for NaN values
        continue
    if color in count:
        count[color] += 1
    else:
        count[color] = 1

# Create a DataFrame from the count dictionary
data_frame = pd.DataFrame.from_dict(count, orient="index", columns=["Count"])

# Reset index and rename columns
data_frame = data_frame.reset_index().rename(columns={"index": "Fur Color"})
# Print the DataFrame
print(data_frame)
data_frame.to_csv("squirrels.csv")
