import sys

def parse_log_line(line: str) -> dict:
    # Parse a log line into a dictionary with date, time, level, and message
    parts = line.strip().split(' ', 3)
    if len(parts) < 4:
        return None
    return {
        'date': parts[0],
        'time': parts[1],
        'level': parts[2],
        'message': parts[3]
    }

def load_logs(file_path: str) -> list:
    logs = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                log = parse_log_line(line)
                if log:
                    logs.append(log)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"Error reading file: {e}")
    return logs

def filter_logs_by_level(logs: list, level: str) -> list:
    # Return logs filtered by level using list comprehension
    return [log for log in logs if log['level'].lower() == level.lower()]

def count_logs_by_level(logs: list) -> dict:
    counts = {}
    for log in logs:
        level = log['level']
        counts[level] = counts.get(level, 0) + 1
    return counts

def display_log_counts(counts: dict):
    print("\nLogging Level  | Count")
    print("---------------|------")
    for level, count in counts.items():
        print(f"{level:<15}| {count}")

def display_logs(logs: list):
    for log in logs:
        print(f"{log['date']} {log['time']} - {log['message']}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <path_to_logfile> [level]")
        return

    file_path = sys.argv[1]
    level_filter = sys.argv[2] if len(sys.argv) > 2 else None

    logs = load_logs(file_path)

    # Count logs by level
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    # If a level filter is provided, display filtered logs
    if level_filter:
        filtered_logs = filter_logs_by_level(logs, level_filter)
        print(f"\nLog details for level '{level_filter.upper()}':")
        display_logs(filtered_logs)

if __name__ == "__main__":
    main()
