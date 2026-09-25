import csv
import os
from datetime import date

FILE_NAME = "expenses.csv"


def add_expense():
    expense_date = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()

    if not expense_date:
        expense_date = str(date.today())

    category = input("Enter category: ").strip()
    description = input("Enter description: ").strip()

    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    file_exists = os.path.exists(FILE_NAME)

    with open(FILE_NAME, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["Date", "Category", "Description", "Amount"])

        writer.writerow([expense_date, category, description, amount])

    print("Expense added successfully!")


def view_expenses():
    if not os.path.exists(FILE_NAME):
        print("No expenses found.")
        return

    with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        print("\n========== ALL EXPENSES ==========")

        found = False

        for row in reader:
            found = True
            print(
                f"Date: {row['Date']} | "
                f"Category: {row['Category']} | "
                f"Description: {row['Description']} | "
                f"Amount: ₹{float(row['Amount']):.2f}"
            )

        if not found:
            print("No expenses found.")


def filter_expenses():
    if not os.path.exists(FILE_NAME):
        print("No expenses found.")
        return

    category = input("Enter category to filter: ").strip().lower()

    with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        print(f"\n===== EXPENSES IN CATEGORY: {category} =====")

        found = False

        for row in reader:
            if row["Category"].lower() == category:
                found = True
                print(
                    f"Date: {row['Date']} | "
                    f"Description: {row['Description']} | "
                    f"Amount: ₹{float(row['Amount']):.2f}"
                )

        if not found:
            print("No expenses found in this category.")


def category_summary():
    if not os.path.exists(FILE_NAME):
        print("No expenses found.")
        return

    summary = {}

    with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            category = row["Category"]
            amount = float(row["Amount"])

            summary[category] = summary.get(category, 0) + amount

    print("\n========== CATEGORY SUMMARY ==========")

    if not summary:
        print("No expenses found.")
        return

    for category, total in summary.items():
        print(f"{category}: ₹{total:.2f}")


def main():
    while True:
        print("\n=================================")
        print("     PERSONAL EXPENSE TRACKER")
        print("=================================")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Filter Expenses by Category")
        print("4. Category Summary")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            filter_expenses()
        elif choice == "4":
            category_summary()
        elif choice == "5":
            print("Thank you!")
            break
        else:
            print("Invalid choice. Please enter 1-5.")


if __name__ == "__main__":
    main()