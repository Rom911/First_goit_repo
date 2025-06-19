def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            total = 0
            count = 0

            for line in file:
                parts = line.strip().split(',')
                if len(parts) != 2:
                    continue  # Skip malformed lines
                name, salary_str = parts
                try:
                    salary = float(salary_str)
                    total += salary
                    count += 1
                except ValueError:
                    continue  # Skip lines where salary is not a valid number

        if count == 0:
            return (0, 0)  # Avoid division by zero

        average = total / count
        return (total, average)

    except FileNotFoundError:
        print(f"File not found: {path}")
        return (0, 0)
    except Exception as e:
        print(f"Error while processing the file: {e}")
        return (0, 0)
