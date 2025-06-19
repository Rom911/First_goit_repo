def get_cats_info(path):
    cats = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) != 3:
                    continue  # Skip malformed lines
                cat_id, name, age = parts
                cats.append({
                    "id": cat_id,
                    "name": name,
                    "age": age
                })

        return cats

    except FileNotFoundError:
        print(f"File not found: {path}")
        return []
    except Exception as e:
        print(f"Error reading file: {e}")
        return []
