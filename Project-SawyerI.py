# Isaac Sawyer
# Recipe Creator/Nutrition Info Application
# 12/02/2022

# This program allows the user to see nutrition info of selected foods/ingredients, and to be able
# to compile those ingredients together to form a recipe, which is written to a file.

# Create arrays

RecipeList = []
NutritionList = [0.0, 0.0, 0.0, 0.0]
MasterListForPrompt = ["Chicken Thighs = 1", "Chicken Breast = 2", "Ground Beef = 3", "Chuck Roast = 4"]
MasterListForFile = ["Chicken Thighs", "Chicken Breast", "Ground Beef", "Chuck Roast"]

# Arrays to hold ingredients of each food family

ChickenList = ["Thighs", "Breast"]
BeefList = ["Ground Beef, Chuck Roast"]

# Arrays to hold each ingredient's nutrition info
# Chicken ingredients nutrition

ChickenThighsNutrition = ["Per 100g: Calories: 177, Fat: 8g, Carbs: 0g, Protein: 24g"]
ChickenThighsParallel = [177.0, 8.0, 0.0, 24.0]
ChickenBreastNutrition = ["Per 100g: Calories: 165, Fat: 3.6g, Carbs: 0g, Protein: 31g"]
ChickenBreastParallel = [165.0, 3.6, 0.0, 31.0]

# Beef ingredients nutrition

GroundBeefNutrition = ["Per 100g: Calories: 254, Fat: 20g, Carbs: 0g, Protein: 17g"]
GroundBeefParallel = [254.0, 20.0, 0.0, 17.0]
ChuckRoastNutrition = ["Per 100g: Calories: 295, Fat: 19g, Carbs: 0g, Protein: 30g"]
ChuckRoastParallel = [295.0, 19.0, 0.0, 30.0]

# Declare variables
Prompt1 = ""
Prompt2 = ""
Prompt3 = ""

# Loop to prompt user for input and hold selection structures for viewing nutrition info
while Prompt1 != "X" and Prompt1 != "R" and Prompt2 != "X" and Prompt2 != "R":
    print("Chicken = 1, Beef = 2,")

    Prompt1 = input("Enter number corresponding to ingredient family to see ingredients"
    " or R to go to recipe creator or X to quit: ")

    # Selection structures for user to choose food family and particular ingredient
    # Also prints nutrition info for chosen ingredient

    if Prompt1 == str(1):
        print(ChickenList[0] + " = 1, " + ChickenList[1] + " = 2")
        Prompt2 = input("Enter number corresponding to ingredient to see nutrition info"
        " or R to go to recipe creator or X to quit: ")

        if Prompt2 == str(1):
            print(ChickenThighsNutrition)

        if Prompt2 == str(2):
            print(ChickenBreastNutrition)

    if Prompt1 == str(2):
        print(BeefList)
        print("Ground Beef = 1, Chuck Roast = 2")
        Prompt2 = input("Enter number corresponding to ingredient to see nutrition info"
        " or R to go to recipe creator or X to quit: ")

        if Prompt2 == str(1):
            print(GroundBeefNutrition)

        if Prompt2 == str(2):
            print(ChuckRoastNutrition)

# Loop to hold selection structures for adding ingredients to recipe

while (Prompt1 == "R" or Prompt2 == "R" or Prompt3 == "R") and Prompt3 != "X":

    print(MasterListForPrompt)

    Prompt3 = input("Enter number corresponding to ingredient to add to recipe or X to quit: ")

# Selection structures for user to select ingredients to add to recipe

    if Prompt3 == str(1):

        RecipeList.append(MasterListForFile[0])

        NutritionList[0] = NutritionList[0] + ChickenThighsParallel[0]
        NutritionList[1] = NutritionList[1] + ChickenThighsParallel[1]
        NutritionList[2] = NutritionList[2] + ChickenThighsParallel[2]
        NutritionList[3] = NutritionList[3] + ChickenThighsParallel[3]

    if Prompt3 == str(2):

        RecipeList.append(MasterListForFile[1])

        NutritionList[0] = NutritionList[0] + ChickenBreastParallel[0]
        NutritionList[1] = NutritionList[1] + ChickenBreastParallel[1]
        NutritionList[2] = NutritionList[2] + ChickenBreastParallel[2]
        NutritionList[3] = NutritionList[3] + ChickenBreastParallel[3]

    if Prompt3 == str(3):

        RecipeList.append(MasterListForFile[2])

        NutritionList[0] = NutritionList[0] + GroundBeefParallel[0]
        NutritionList[1] = NutritionList[1] + GroundBeefParallel[1]
        NutritionList[2] = NutritionList[2] + GroundBeefParallel[2]
        NutritionList[3] = NutritionList[3] + GroundBeefParallel[3]

    if Prompt3 == str(4):

        RecipeList.append(MasterListForFile[3])

        NutritionList[0] = NutritionList[0] + ChuckRoastParallel[0]
        NutritionList[1] = NutritionList[1] + ChuckRoastParallel[1]
        NutritionList[2] = NutritionList[2] + ChuckRoastParallel[2]
        NutritionList[3] = NutritionList[3] + ChuckRoastParallel[3]

# Open and write recipe and nutrition info to file, and close

file = open("Recipe.txt", "a")

for item in RecipeList:
    file.write(item + ": 100g" + "\n")

file.write("Total Nutrition: " + "\n")
file.write("Calories: " + str(NutritionList[0]) + " Fat: " + str(NutritionList[1]) +
               " Carbs: " + str(NutritionList[2]) + " Protein: " + str(NutritionList[3]) + "\n")

file.close()
