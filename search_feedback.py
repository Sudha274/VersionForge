def search_feedback_by_name_and_count(feedback_file="feedback_data.txt", search_name=""):
    """
    Searches feedback for entries by a specific name and counts total entries.

    Args:
        feedback_file (str, optional): Path to the feedback data file.
                                       Defaults to "feedback_data.txt".
        search_name (str, optional): The name to search for. Defaults to "".

    Returns:
        tuple: A tuple containing:
               - list: A list of feedback entries matching the search name.
               - int: The total number of feedback entries in the file.
    """
    matching_feedback = []
    total_entries = 0
    try:
        with open(feedback_file, "r") as f:
            for line in f:
                total_entries += 1
                name, _, comment = line.strip().split(",", 2)
                if search_name.lower() in name.lower():
                    matching_feedback.append(line.strip())
    except FileNotFoundError:
        return [], 0
    return matching_feedback, total_entries

if __name__ == "__main__":
    search_term = input("Enter name to search (leave blank for all): ")
    results, total = search_feedback_by_name_and_count(search_name=search_term)
    print(f"\nTotal Feedback Entries: {total}")
    if search_term:
        print(f"Feedback matching '{search_term}':")
        if results:
            for entry in results:
                print(f"- {entry}")
        else:
            print("No feedback found for that name.")
    else:
        print("All Feedback:")
        for entry in results:
            print(f"- {entry}")
