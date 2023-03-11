print("====================================")
print(" COVID CHECKER ")
print("====================================")

# Ask the user to answer some questions about their symptoms
cough = (input("Do you have a Cough? ")).lower() == "y"
shortnessOfBreath = (input("Do you have shortness of breath? ")).lower() == "y"
fever = (input("Do you have a fever? ")).lower() == "y"
lossOfTaste = (input("Have you lost your taste or smell? ")).lower() == "y"

# Define a dictionary that maps symptom names to their respective weights
symptomFactorWeight = {
    "fever": [3, -2],
    "cough": [2, -1],
    "breath": [3, -2],
    "taste": [2, 0],
}

# Calculate the value predictor based on the user's symptoms and their weights
valuePredictor = 0
if fever:
    valuePredictor += symptomFactorWeight["fever"][0]
else:
    valuePredictor += symptomFactorWeight["fever"][1]

if cough:
    valuePredictor += symptomFactorWeight["cough"][0]
else:
    valuePredictor += symptomFactorWeight["cough"][1]

if shortnessOfBreath:
    valuePredictor += symptomFactorWeight["breath"][0]
else:
    valuePredictor += symptomFactorWeight["breath"][1]

if lossOfTaste:
    valuePredictor += symptomFactorWeight["taste"][0]
else:
    valuePredictor += symptomFactorWeight["taste"][1]

# Print the result based on the value predictor
if valuePredictor > 0:
    print("You show the symptoms of Covid 19. Go for a checkup as soon as possible")
else:
    print("You do not show the symptoms of Covid 19")
