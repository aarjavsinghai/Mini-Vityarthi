import progress_data


def view_progress():
    while True:
        print("\n" + "=" * 55)
        print("                 VIEW PROGRESS")
        print("=" * 55)
        print("1. Overall Progress")
        print("2. Topic-wise Progress")
        print("3. Mistake Analysis")
        print("4. Recommendations")
        print("5. Bookmarked Questions")
        print("0. Back to Main Menu")

        choice = input("Choose an option: ").strip()

        if choice == "0":
            return
        elif choice == "1":
            overall()
        elif choice == "2":
            topic_progress()
        elif choice == "3":
            mistakes()
        elif choice == "4":
            recommendations()
        elif choice == "5":
            bookmarks()
        else:
            print("Invalid choice.")


def overall():
    attempted, correct, wrong, accuracy, topic_data = progress_data.get_statistics()

    print("\nOVERALL PROGRESS")
    print("Questions Attempted:", attempted)
    print("Correct:", correct)
    print("Incorrect:", wrong)
    print(f"Accuracy: {accuracy:.2f}%")
    input("Press Enter to go back...")


def topic_progress():
    topic_data = progress_data.get_statistics()[4]

    print("\nTOPIC-WISE PROGRESS")
    if not topic_data:
        print("No data yet. Try some practice questions first.")
        input("Press Enter to go back...")
        return

    print(f"{'Topic':<18}{'Attempted':<12}{'Correct':<10}Accuracy")
    for topic in topic_data:
        attempted, correct = topic_data[topic]
        accuracy = correct / attempted * 100
        print(f"{topic:<18}{attempted:<12}{correct:<10}{accuracy:.2f}%")

    input("Press Enter to go back...")


def mistakes():
    results = progress_data.read_results()
    wrong_answers = [r for r in results if r["correct"] == 0]

    print("\nMISTAKE ANALYSIS")
    if not wrong_answers:
        print("Nice! No wrong answers recorded yet.")
        input("Press Enter to go back...")
        return

    number = 1
    for item in wrong_answers:
        print(f"\n{number}. {item['topic']}")
        print("Q:", item["question"])
        print("Your answer:", item["user_answer"])
        print("Correct answer:", item["correct_answer"])
        print("Explanation:", item["explanation"])
        number += 1

    input("Press Enter to go back...")


def recommendations():
    # using same 60 and 80 cutoffs as report
    topic_data = progress_data.get_statistics()[4]

    print("\nRECOMMENDATIONS")
    if not topic_data:
        print("Not enough data yet. Do some practice first.")
        input("Press Enter to go back...")
        return

    shown = False
    for topic in topic_data:
        attempted, correct = topic_data[topic]
        score = correct / attempted * 100

        if score < 60:
            print(f"- Focus more on {topic} (Accuracy: {score:.2f}%)")
            shown = True
        elif score < 80:
            print(f"- Revise {topic} a bit more (Accuracy: {score:.2f}%)")
            shown = True

    if not shown:
        print("Looking good! Keep practicing the topics.")

    input("Press Enter to go back...")


def bookmarks():
    bookmark_list = progress_data.read_bookmarks()

    print("\nBOOKMARKED QUESTIONS")
    if not bookmark_list:
        print("No bookmarks yet.")
        input("Press Enter to go back...")
        return

    number = 1
    for source, topic, question, answer in bookmark_list:
        print(f"\n{number}. [{source}] {topic}")
        print(question)
        print("Answer:", answer)
        number += 1

    input("Press Enter to go back...")
