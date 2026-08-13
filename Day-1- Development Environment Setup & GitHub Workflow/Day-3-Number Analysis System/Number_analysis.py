numbers = []

while True:
    user_input = input("Enter a number (or type 'exit' to stop): ")

    if user_input.lower() == "exit":
        break

    if user_input.strip() == "":
        print("Invalid input! Please enter a number.")
        continue

    try:
        number = float(user_input)
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        continue

    numbers.append(number)

    if number == 0:
        sign = "Zero"
    elif number > 0:
        sign = "Positive"
    else:
        sign = "Negative"

    if number % 2 == 0:
        even_odd = "Even"
    else:
        even_odd = "Odd"

    if number > 100:
        greater_100 = "Greater than 100"
    else:
        greater_100 = "Not greater than 100"

    print("\nAnalysis:")
    print("Number:", number)
    print("Type:", even_odd)
    print("Sign:", sign)
    print("100 Check:", greater_100)
    print("-" * 30)


print("\n===== FINAL SUMMARY REPORT =====")

if len(numbers) == 0:
    print("No numbers were entered.")
else:
    print("Total numbers entered:", len(numbers))

    print("\nAll numbers:")
    for number in numbers:
        print(number)

    print("\nSummary:")
    print("Even numbers:", sum(1 for n in numbers if n % 2 == 0))
    print("Odd numbers:", sum(1 for n in numbers if n % 2 != 0))
    print("Positive numbers:", sum(1 for n in numbers if n > 0))
    print("Negative numbers:", sum(1 for n in numbers if n < 0))
    print("Zero:", sum(1 for n in numbers if n == 0))
    print("Greater than 100:", sum(1 for n in numbers if n > 100))

print("\nProgram ended successfully!")