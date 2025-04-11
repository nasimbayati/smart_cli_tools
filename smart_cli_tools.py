# smart_cli_tools.py
import json
import os
import time
from datetime import datetime

# Create results folder if it doesn't exist
if not os.path.exists("results"):
    os.makedirs("results")

def get_number_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer.")

def temperature_converter():
    celsius = get_number_input("Enter temperature in Celsius: ")
    fahrenheit = (celsius * 9 / 5) + 32
    result = f"{celsius}°C = {fahrenheit:.2f}°F"
    print(result)
    with open("results/temperature.txt", "w") as f:
        f.write(result)

def age_calculator():
    birth_year = get_int_input("Enter your birth year: ")
    current_year = datetime.now().year
    age = current_year - birth_year
    result = f"You are {age} years old."
    print(result)
    with open("results/age.txt", "w") as f:
        f.write(result)

def discount_calculator():
    items = get_int_input("How many items are you buying? ")
    total_price = 0
    total_savings = 0
    details = []
    for i in range(items):
        price = get_number_input(f"Enter price for item #{i+1}: ")
        discount = get_number_input(f"Enter discount (%) for item #{i+1}: ")
        savings = price * (discount / 100)
        total_price += price
        total_savings += savings
        details.append({"item": i+1, "price": price, "discount": discount, "savings": savings})

    final_price = total_price - total_savings
    result = f"Total savings: ${total_savings:.2f}\nFinal price to pay: ${final_price:.2f}"
    print(result)

    with open("results/discount.txt", "w") as f:
        f.write(result)
    with open("results/discount.json", "w") as f:
        json.dump({"total_savings": total_savings, "final_price": final_price, "items": details}, f, indent=4)

def grade_converter():
    grade = get_int_input("Enter your grade (0-100): ")
    while grade < 0 or grade > 100:
        print("Grade must be between 0 and 100.")
        grade = get_int_input("Enter your grade (0-100): ")

    if grade < 60:
        letter = "F"
    elif grade < 70:
        letter = "D"
    elif grade < 80:
        letter = "C"
    elif grade < 90:
        letter = "B"
    else:
        letter = "A"
    print(f"Your letter grade: {letter}")

def counter_tool():
    direction = input("Type 'up' to count up or 'down' to count down: ").strip().lower()
    limit = get_int_input("Enter the limit: ")
    step = get_int_input("Enter step value (e.g., 1): ")
    if step <= 0:
        print("Step must be a positive number.")
        return

    print("Counting:")
    if direction == "up":
        for i in range(0, limit + 1, step):
            print(i)
    elif direction == "down":
        for i in range(limit, -1, -step):
            print(i)
    else:
        print("Invalid direction.")

def heads_or_tails_game():
    total_score = 0
    result_log = []
    print("Choose heads or tails (5 rounds):")
    for i in range(5):
        choice = input(f"Round {i+1}: ").strip().lower()
        if choice == "heads":
            total_score += 5
            result_log.append("+5")
        elif choice == "tails":
            total_score -= 5
            result_log.append("-5")
        else:
            result_log.append("0 (invalid)")
    result = f"Score per round: {', '.join(result_log)}\nFinal score: {total_score}"
    print(result)
    with open("results/heads_or_tails.txt", "w") as f:
        f.write(result)

def main():
    while True:
        print("\n==============================")
        print("SMART CLI TOOLS MENU")
        print("==============================")
        print("1. Temperature Converter")
        print("2. Age Calculator")
        print("3. Discount Calculator")
        print("4. Grade Converter")
        print("5. Counter Tool")
        print("6. Heads or Tails Game")
        print("0. Exit")

        choice = input("Choose a tool (0-6): ")

        if choice == "1":
            temperature_converter()
        elif choice == "2":
            age_calculator()
        elif choice == "3":
            discount_calculator()
        elif choice == "4":
            grade_converter()
        elif choice == "5":
            counter_tool()
        elif choice == "6":
            heads_or_tails_game()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 0 and 6.")

if __name__ == "__main__":
    main()
