import json
from datetime import datetime

FILE_NAME = "expenses.json"


def load_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            expenses = json.load(file)
        print("Expense records loaded successfully.")
        return expenses

    except FileNotFoundError:
        print("No previous records found. Starting with an empty list.")
        return []

    except json.JSONDecodeError:
        print("File contains invalid data. Starting with an empty list.")
        return []

    except Exception as error:
        print(f"Error loading expenses: {error}")
        return []

    finally:
        print("Load operation completed.")


def save_expenses(expenses):
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(expenses, file, indent=4)
        print("Expenses saved successfully.")

    except Exception as error:
        print(f"Error saving expenses: {error}")

    finally:
        print("Save operation completed.")


def add_expense(expenses):
    print("\n--- Add New Expense ---")

    title = input("Enter expense title: ").strip()
    category = input("Enter expense category: ").strip()

    if not title or not category:
        print("Title and category cannot be empty.")
        return

    try:
        amount = float(input("Enter expense amount: "))

        if amount <= 0:
            print("Amount must be greater than 0.")
            return

    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    date = input("Enter expense date (YYYY-MM-DD): ").strip()

    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date. Please use YYYY-MM-DD format.")
        return

    expense = {
        "title": title,
        "category": category,
        "amount": amount,
        "date": date
    }

    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added successfully.")


def view_expenses(expenses):
    print("\n--- All Expenses ---")

    if not expenses:
        print("No expenses found.")
        return

    for index, expense in enumerate(expenses, start=1):
        print(f"\nExpense #{index}")
        print(f"Title: {expense['title']}")
        print(f"Category: {expense['category']}")
        print(f"Amount: Rs. {expense['amount']:.2f}")
        print(f"Date: {expense['date']}")


def search_by_category(expenses):
    print("\n--- Search Expense by Category ---")

    category = input("Enter category: ").strip().lower()

    found = False

    for expense in expenses:
        if expense["category"].lower() == category:
            print(
                f"Title: {expense['title']} | "
                f"Amount: Rs. {expense['amount']:.2f} | "
                f"Date: {expense['date']}"
            )
            found = True

    if not found:
        print("No expenses found in this category.")


def delete_expense(expenses):
    print("\n--- Delete Expense Record ---")

    if not expenses:
        print("No expenses available to delete.")
        return

    view_expenses(expenses)

    try:
        number = int(input("\nEnter expense number to delete: "))

        if number < 1 or number > len(expenses):
            print("Invalid expense number.")
            return

        deleted = expenses.pop(number - 1)
        save_expenses(expenses)

        print(f"Expense '{deleted['title']}' deleted successfully.")

    except ValueError:
        print("Please enter a valid number.")

    finally:
        print("Delete operation completed.")


def expense_summary(expenses):
    print("\n--- Expense Summary ---")

    if not expenses:
        print("No expenses available.")
        return

    total = sum(expense["amount"] for expense in expenses)

    print(f"Total Expenses: {len(expenses)}")
    print(f"Total Spending: Rs. {total:.2f}")

    categories = {}

    for expense in expenses:
        category = expense["category"]
        categories[category] = categories.get(category, 0) + expense["amount"]

    print("\nSpending by Category:")

    for category, amount in categories.items():
        print(f"- {category}: Rs. {amount:.2f}")


def main():
    expenses = load_expenses()

    while True:
        print("\n" + "=" * 45)
        print("        PERSONAL EXPENSE TRACKER")
        print("=" * 45)
        print("1. Add New Expense")
        print("2. View All Expenses")
        print("3. Search Expense by Category")
        print("4. Delete Expense Record")
        print("5. View Expense Summary")
        print("6. Exit")
        print("=" * 45)

        try:
            choice = input("Enter your choice (1-6): ").strip()

            if choice == "1":
                add_expense(expenses)

            elif choice == "2":
                view_expenses(expenses)

            elif choice == "3":
                search_by_category(expenses)

            elif choice == "4":
                delete_expense(expenses)

            elif choice == "5":
                expense_summary(expenses)

            elif choice == "6":
                print("Thank you for using Personal Expense Tracker!")
                break

            else:
                print("Invalid choice. Please select 1-6.")

        except Exception as error:
            print(f"Unexpected error: {error}")

        finally:
            print("\nOperation completed.")


if __name__ == "__main__":
    main()