with open("invited_names.txt", "r" ) as name:
    names = name.readlines()
    print(name)

with open("format.txt" , mode="r") as file:
    content = file.read()
    print(content)
    for name in names:
        new_letter = content.replace("{NAME}",name.strip())
        print(new_letter)
        with open(f"INVITE_{name.strip()}.txt", mode = "w" ) as invite :
            invite.write(new_letter)
