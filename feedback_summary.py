def summarize_feedback_basic(feedback_file="feedback_data.txt"):
    """
    Reads feedback from file and summarizes ratings (1–5 stars).
    Returns:
        dict: Summary with counts, percentages, total responses.
    """
    counts = {i: 0 for i in range(1, 6)}
    invalid_entries = 0

    try:
        with open(feedback_file, "r") as f:
            for line in f:
                try:
                    rating = int(line.strip().split(",")[1])
                    if 1 <= rating <= 5:
                        counts[rating] += 1
                    else:
                        invalid_entries += 1
                except (ValueError, IndexError):
                    invalid_entries += 1
    except FileNotFoundError:
        return "Error: Feedback file not found."

    total = sum(counts.values())
    percentages = {k: f"{(v / total * 100):.1f}%" for k, v in counts.items()} if total > 0 else {}

    return {
        "total_feedback": total,
        "rating_counts": counts,
        "rating_percentages": percentages,
        "invalid_entries": invalid_entries
    }


if __name__ == "__main__":
    summary = summarize_feedback_basic()
    if isinstance(summary, dict):
        print("Feedback Summary\n----------------")
        print(f"Total Responses: {summary['total_feedback']}")
        print(f"Invalid Entries Skipped: {summary['invalid_entries']}")
        print("\nRating Distribution:")
        for rating in range(1, 6):
            count = summary['rating_counts'][rating]
            percent = summary['rating_percentages'].get(rating, "0%")
            print(f"{rating} Stars: {count} ({percent})")
    else:
        print(summary)
