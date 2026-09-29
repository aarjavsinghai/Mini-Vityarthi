import random
import progress_data
from questions import QUESTION_BANK


def run_bank():
    print("\n" + "=" * 50)
    print("               QUESTION BANK")
    print("=" * 50)
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    print("0. Back")

    choice = input("Choose difficulty: ").strip()

    if choice == "0":
        return

    if choice not in ("1", "2", "3"):
        print("Invalid choice.")
        return

    difficulty_map = {"1": "Easy", "2": "Medium", "3": "Hard"}
    difficulty = difficulty_map[choice]

    
    question_list = [q for q in QUESTION_BANK if q[0] == difficulty]
    random.shuffle(question_list)

    attempted = 0
    correct = 0
    q_num = 0

    print("\nDifficulty:", difficulty)
    print("Type B to bookmark, 0 to quit\n")

    for item in question_list:
        q_num += 1
        level, question, options, answer, explanation = item

        print("-" * 55)
        print("Q" + str(q_num) + ". " + question)
        print("Level:", level)

        for i in range(len(options)):
            print(str(i + 1) + ". " + options[i])
        print("0. Quit   B. Bookmark")

        while True:
            user_input = input("Your answer: ").strip()

            if user_input.lower() == "b":
                if progress_data.is_bookmarked(question):
                    print("Already bookmarked.")
                else:
                    progress_data.add_bookmark("Question Bank", difficulty, question, answer)
                    print("Bookmarked!")
                continue

            if user_input == "0":
                print("Stopped. Results saved.")
                input("Press Enter...")
                return

            if user_input.isdigit() and 1 <= int(user_input) <= len(options):
                selected = options[int(user_input) - 1]

                if selected == answer:
                    result = 1
                else:
                    result = 0

                progress_data.save_result("Question Bank", difficulty, question, selected, answer, result, explanation)
                attempted += 1
                correct += result

                if result == 1:
                    print("Correct!")
                else:
                    print("Wrong. Correct answer:", answer)
                    print("Explanation:", explanation)
                break

            print("Enter option number, B, or 0.")

    print("\nQUESTION BANK COMPLETE")
    print("Attempted:", attempted)
    print("Correct:", correct)
    print("Incorrect:", attempted - correct)
    if attempted > 0:
        print(f"Accuracy: {correct / attempted * 100:.2f}%")
    input("Press Enter to go back...")
