print("""The idea behind this simple program is to encourage people to embrace
      change. This application will first ask you for your age, sex and height
      in order to calculate your optimal weight. After that, it will ask you for
      your activity level, current bodyweight and the goal you want to achieve.
      Finally, it will generate a user friendly macros calculator for you.""")

print("Let's start by a quick overview of what your optimal weight is.")

age = float(input("What's your age?: "))
sex = input("What's your gender - M or F?: ")
height = float(input("What's your current height in cm's?: "))

if sex == "M":
    opt_bw = round(float(50 + 0.91 * (height - 152.4)))
else:
    opt_bw = round(float(45.5 + 0.91 * (height - 152.4)))
  
print(f"Your optimal bodyweight, not based on your activity level is {opt_bw} kgs.")

print("Now let's examine your activity level, current weight and your goals.")

activity_level = float(input("What is your activity level from 1 to 3: "))
bw = float(input("What is your current weight in KG's?: "))
goal = float(input("""What is your goal? To gain muscle(1), to maintain your
                   current weight(2) or to lose weight(3)?: """))

if activity_level == 1:
    basecal = float(round((bw * 2.05) * 14))
    print("Your physical activity is low.")
elif activity_level == 2:
    basecal = float(round((bw*2.05) * 17))
    print("Your physical activity is moderate.")
else:
    basecal = float(round((bw*2.05) * 20))
    print("Your physical activity is high.")
    
print(f"Based on your activity level, your optimal calorie intake is {basecal}.")

if goal == 1:
    carb_cals = round(0.5 * basecal)
    fat_cals = round(0.2 * basecal)
    protein_cals = round(0.3 * basecal)
    carb_grams = round(carb_cals / 4)
    fat_grams = round(fat_cals / 9 )
    protein_grams = round(protein_cals / 4)
elif goal == 2:
    carb_cals = round(0.4 * basecal)
    fat_cals = round(0.3 * basecal)
    protein_cals = round(0.3 * basecal)
    carb_grams = round(carb_cals / 4)
    fat_grams = round(fat_cals / 9 )
    protein_grams = round(protein_cals / 4  ) 
else:
    carb_cals = round(0.2 * basecal)
    fat_cals = round(0.35 * basecal)
    protein_cals = round(0.45 * basecal)
    carb_grams = round(carb_cals / 4)
    fat_grams = round(fat_cals / 9)
    protein_grams = round(protein_cals / 4)

print("Your optimal macronutrient calorie intake should be:")
print(f"Calories for carbs: {carb_cals}, in grams: {carb_grams} grams.")
print(f"Calories for fats: {fat_cals}, in grams: {fat_grams} grams.")
print(f"Calories for protein: {protein_cals}, in grams: {protein_grams} grams.") 

print("We can also recommend a balanced split diet.")

meal_count = int(input("Do you prefer 3, 4 or 5 meals a day?: "))

if meal_count == 3:
    bfcals = round(basecal / 3)
    bfcarbs = round(carb_cals / 3)
    bffats = round(fat_cals / 3)
    bfprotein = round(protein_cals /3)
    bf_carb_grams = round(carb_grams / 3)
    bf_fat_grams = round(fat_grams / 3)
    bf_protein_grams = round(protein_grams / 3)
    print(f"If you prefer {meal_count} counts:")
    print(f"Your total calorie intake should be {bfcals} per meal.")
    print(f"You should consume, as per carbs: {bfcarbs} kcal / {bf_carb_grams} grams per meal.")
    print(f"You should consume, as per fats: {bffats} kcal / {bf_fat_grams} grams per meal.")
    print(f"You should consume, as per protein: {bfprotein} kcal / {bf_protein_grams} grams per meal.")
elif meal_count == 4:
    bfcals = round(basecal / 4)
    bfcarbs = round(carb_cals / 4)
    bffats = round(fat_cals / 4)
    bfprotein = round(protein_cals / 4)
    bf_carb_grams = round(carb_grams / 4)
    bf_fat_grams = round(fat_grams / 4)
    bf_protein_grams = round(protein_grams / 4)
    print(f"If you prefer {meal_count} counts:")
    print(f"Your total calorie intake should be {bfcals} per meal.")
    print(f"You should consume, as per carbs: {bfcarbs} kcal / {bf_carb_grams} grams per meal.")
    print(f"You should consume, as per fats: {bffats} kcal / {bf_fat_grams} grams per meal.")
    print(f"You should consume, as per protein: {bfprotein} kcal / {bf_protein_grams} grams per meal.")
else:
    bfcals = round(basecal / 5)
    bfcarbs = round(carb_cals / 5)
    bffats = round(fat_cals / 5)
    bfprotein = round(protein_cals / 5)
    bf_carb_grams = round(carb_grams / 5)
    bf_fat_grams = round(fat_grams / 5)
    bf_protein_grams = round(protein_grams / 5)
    print(f"If you prefer {meal_count} counts:")
    print(f"Your total calorie intake should be {bfcals} per meal.")
    print(f"You should consume, as per carbs: {bfcarbs} kcal / {bf_carb_grams} grams per meal.")
    print(f"You should consume, as per fats: {bffats} kcal / {bf_fat_grams} grams per meal.")
    print(f"You should consume, as per protein: {bfprotein} kcal / {bf_protein_grams} grams per meal.")


