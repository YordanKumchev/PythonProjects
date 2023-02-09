print("""The idea behind this simple calculator is to get an user input for his
      bodyweight in kg's/lbs and then convert it to the other unit of measure""")

weight = float(input("Please enter your current weight: "))
unit = input("Is your weight in kgs(K) or pounds (L): ")

if unit == "K":
    weight = round(weight * 2.05)
    unit = "Lbs"
    print(f"Your weight in {unit} is: {weight} {unit}")
elif unit == "L":
    weight = round(weight / 2.05)
    unit = "Kgs"
    print(f"Your weight in {unit} is: {weight} {unit}")
else:
    print("You haven't selected a valid unit of measure")