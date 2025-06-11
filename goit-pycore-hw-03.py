from datetime import datetime

def get_days_from_today(date):
    try:
        # Convert string to date
        input_date = datetime.strptime(date, '%Y-%m-%d').date()
        # Current date (without time)
        today = datetime.today().date()
        # Difference in days
        delta = today - input_date
        return delta.days
    except ValueError:
        # If the format is incorrect
        return "Invalid date format. Use 'YYYY-MM-DD'."
