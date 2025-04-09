def summarize_feedback_basic(feedback_file="feedback_data.txt"):
    """
    Reads feedback and counts ratings (1-5).
    """
    counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    try:
        with open(feedback_file, "r") as f:
            for line in f:
                try:
                    rating = int(line.strip().split(",")[1])
                    if 1 <= rating <= 5:
                        counts[rating] += 1
                except (ValueError, IndexError):
                    pass  # Ignore invalid lines
    except FileNotFoundError:
        return "Error: Feedback file not found."
    return counts

if __name__ == "__main__":
    summary = summarize_feedback_basic()
    if isinstance(summary, dict):
        print("Rating Counts:")
        for rating, count in summary.items():
            print(f"{rating}: {count}")
    else:
        print(summary)
