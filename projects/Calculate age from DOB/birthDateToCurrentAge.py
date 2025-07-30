from datetime import date, datetime

def ageCalculator(birth_date):
    today = date.today()
    
    # Calculate initial age
    age_year = today.year - birth_date.year
    age_month = today.month - birth_date.month
    age_day = today.day - birth_date.day

    # Adjust if the current month/day hasn't occurred yet this year
    if age_day < 0:
        age_month -= 1
        previous_month = (today.month - 1) if today.month > 1 else 12
        year_for_month = today.year if today.month > 1 else today.year - 1
        last_day_prev_month = (date(year_for_month, previous_month + 1, 1) - date.resolution).day
        age_day += last_day_prev_month

    if age_month < 0:
        age_year -= 1
        age_month += 12

    print(f"Your age today is: {age_year} years, {age_month} months, {age_day} days.")
    print(f"Today's date is: {today.strftime('%Y-%m-%d')}")


# --- Input Handling ---

birth_input = input("Enter your birth date in YYYY-MM-DD format: ")

try:
    birth_date = datetime.strptime(birth_input, "%Y-%m-%d").date()
    if birth_date > date.today():
        print("Invalid date: Birth date is in the future.")
    else:
        print(f"Your date of birth is: {birth_date}")
        ageCalculator(birth_date)
except ValueError:
    print("Invalid date format or value. Please enter a valid date in YYYY-MM-DD format.")
