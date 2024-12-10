def calculate_bmi(weight, height):
    # Formula for BMI
    bmi = weight / (height ** 2)
    return bmi

def classify_bmi(bmi):
    # BMI classification
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def main():
    print("Welcome to the BMI Calculator!")

    # Input from the user
    try:
        weight = float(input("Please enter your weight in kilograms: "))
        height = float(input("Please enter your height in meters: "))

        # Validate inputs
        if weight <= 0 or height <= 0:
            print("Weight and height must be positive values.")
            return

        # Calculate BMI
        bmi = calculate_bmi(weight, height)

        # Classify the BMI
        category = classify_bmi(bmi)

        # Display the result
        print(f"Your BMI is: {bmi:.2f}")
        print(f"Your BMI category is: {category}")
    
    except ValueError:
        print("Invalid input! Please enter numeric values for weight and height.")

if __name__ == "__main__":
    main()
