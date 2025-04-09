def collect_feedback():
    """Function that collects feedback"""
    student_name = input("Enter your name: ")
    try:
        rating = int(input("Rate the course you are learning on a scale of 1 to 5: "))
        if not 1 <= rating <= 5:
            print("Invalid rating. Please enter a number between 1 and 5.")
            return
    except ValueError:
        print("Invalid input. Please enter a number for the rating.")
        return

    feedback = input("Any additional feedback comments? ")

    with open("feedback_data.txt", "a") as f:
        f.write(f"{student_name},{rating},{feedback}\n")
    print("Thank you for your feedback!")

if __name__ == "__main__":
    collect_feedback()
