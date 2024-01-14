def tipGenerator():
  print("Welcome to the Tip Generator ")
  bill = float(input("Total Bill :\n"))
  tip = int(input("Tip 10,12,15 (in Percentage)"))
  total_person= int(input("How Many People to Split the Bill"))
  total_bill = bill + (bill * tip / 100)
  split_bill = total_bill / total_person
  split_bill = "{:.2f}".format(split_bill)
  print(f"Total Bill Generatated {split_bill} among {total_person}")

if __name__ == "__main__":
  tipGenerator()
