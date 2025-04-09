def count_total_feedback_entries(feedback_file="feedback_data.txt"):
    """
    Counts the total number of feedback entries in the file.

    Args:
        feedback_file (str, optional): Path to the feedback data file.
                                       Defaults to "feedback_data.txt".

    Returns:
        int: The total number of lines (entries) in the file.
             Returns 0 if the file is not found or empty.
    """
    count = 0
    try:
        with open(feedback_file, "r") as f:
            for line in f:
                count += 1
    except FileNotFoundError:
        return 0
    return count

if __name__ == "__main__":
    total_count = count_total_feedback_entries()
    print(f"Total number of feedback entries: {total_count}")
