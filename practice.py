import random
import progress_data
from questions import PRACTICE_QUESTIONS


def practice_questions():
    topic_names = list(PRACTICE_QUESTIONS.keys())

    while True:
        print("\n" + "=" * 50)
        print("              PRACTICE PROBLEMS")
        print("=" * 50)

        for i in range(len(topic_names)):
            print(str(i + 1) + ". " + topic_names[i])
        print("0. Back")

        try:
            choice = int(input("Choose a topic: "))
        except ValueError:
            print("Please enter a number.")
            continue

        if choice == 0:
            return

        if choice < 1 or choice > len(topic_names):
            print("Invalid choice.")
            continue

        topic = topic_names[choice - 1]

        
        question_list = list(PRACTICE_QUESTIONS[topic])
        random.shuffle(question_list)

        attempted = 0
        correct = 0
        q_num = 0

        print("\n" + topic + " - Practice Mode")
        print("Type B to bookmark, 0 to quit\n")

        for item in question_list:
            q_num += 1
            question, options, answer, explanation = item

            print("-" * 55)
            print("Q" + str(q_num) + ". " + question)
            print("Topic:", topic)

            for i in range(len(options)):
                print(str(i + 1) + ". " + options[i])
            print("0. Quit   B. Bookmark")

            while True:
                user_input = input("Your answer: ").strip()

                if user_input.lower() == "b":
                    if progress_data.is_bookmarked(question):
                        print("Already bookmarked.")
                    else:
                        progress_data.add_bookmark("Practice", topic, question, answer)
                        print("Bookmarked!")
                    continue

                if user_input == "0":
                    print("Practice stopped. Results saved.")
                    input("Press Enter...")
                    return

                if user_input.isdigit() and 1 <= int(user_input) <= len(options):
                    selected = options[int(user_input) - 1]

                    if selected == answer:
                        result = 1
                    else:
                        result = 0

                    progress_data.save_result("Practice", topic, question, selected, answer, result, explanation)
                    attempted += 1
                    correct += result

                    if result == 1:
                        print("Correct!")
                    else:
                        print("Wrong. Correct answer:", answer)
                        print("Explanation:", explanation)
                    break

                print("Enter option number, B, or 0.")

        print("\nPRACTICE COMPLETE")
        print("Attempted:", attempted)
        print("Correct:", correct)
        print("Incorrect:", attempted - correct)
        if attempted > 0:
            print(f"Accuracy: {correct / attempted * 100:.2f}%")
        input("Press Enter to go back...")
