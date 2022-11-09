# Isaac Sawyer
# Recipe Calculator and Kitchen Measurement Converter
# 10/31/2022

# My idea for the final project is a recipe calculator application. This application will prompt the user to enter an ingredient/food and then display
# information that would commonly be found on a nutrition label (based on 100g of the ingredient and read from file). The user will also be able to enter
# their own amount of an ingredient and see the nutrition info based on their amount inputted.
# In addition, the user will be able to add any amount of an ingredient and compile it into a recipe, which will be written to a file. The user will be
# able to input for saved recipe and have recipe displayed. I would also like to incorporate a measurement converter into this application.

# Declare variables and constants


# Declare arrays/lists


### Nutrition info based on 100g Module ###


# Prompt user to input an ingredient

input = input("Enter an ingredient to see nutrition info: ")

# Open ingredient nutrition data file and display nutrition data

with open("Ingredients.txt", "r", encoding="utf-8") as Ingredients:
        Lines = [line.rstrip("\n") for line in Ingredients]
if input == "Chicken Thighs":
    print(Lines[0:4])
if input == "Ground Beef":
    print(Lines[5:9])



### Module to take custom amount of inputted ingredient and calculate/convert from 100g ###



### Module for user to add custom amount of an ingredient and write it to a recipe file ###



### Module for user to input to have a saved recipe displayed ###



### Module for user to be able to convert between common kitchen measurments ###
