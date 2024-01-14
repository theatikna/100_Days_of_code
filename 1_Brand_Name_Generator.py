def generate_brand_name():
    print("Welcome to My Brand Name Generator\n")
    city = input("What is your Birth City\n")
    pet = input("What is your favourite Pet\n")
    brand_name = city + pet
    print("Here's your Brand Name\n" + brand_name)

if __name__ == "__main__":
    generate_brand_name()
    input("Press Enter to exit")
