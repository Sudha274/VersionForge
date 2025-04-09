def compute_average():
    """Reads feedback data and computes average"""
    try:
        with open("feedback_data.txt", "r") as f:
            ratings = []
            for line in f:
                data = line.strip().split(",")
                if len(data) >= 2:  
                    try:
                        rating = int(data[1])
                        ratings.append(rating)
                    except ValueError:
                        print(f"Warning: Skipping invalid rating in line: {line.strip()}")

        if ratings:
            average_rating = sum(ratings) / len(ratings)
            print(f"Average rating: {average_rating:.2f}")
        else:
            print("No feedback data found.")

    except FileNotFoundError:
        print("Error: feedback_data.txt not found. Please run collect_feedback.py first.")

if __name__ == "__main__":
    compute_average()
