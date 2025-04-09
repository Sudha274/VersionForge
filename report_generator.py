def export_feedback_to_txt(feedback_file="feedback_data.txt", output_file="exported_feedback.txt"):
    """
    Reads feedback data and exports it to a new .txt file.

    Args:
        feedback_file (str, optional): Path to the source feedback file.
                                       Defaults to "feedback_data.txt".
        output_file (str, optional): Path to the output .txt file.
                                     Defaults to "exported_feedback.txt".
    """
    try:
        with open(feedback_file, "r") as infile, open(output_file, "w") as outfile:
            for line in infile:
                outfile.write(line)
        print(f"Feedback exported to '{output_file}' successfully.")
    except FileNotFoundError:
        print(f"Error: File '{feedback_file}' not found.")
    except Exception as e:
        print(f"An error occurred during export: {e}")

if __name__ == "__main__":
    export_feedback_to_txt() # Exports to 'exported_feedback.txt'
    # Or specify different file names:
    # export_feedback_to_txt("feedback_data.txt", "backup_feedback.txt")
