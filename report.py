from datetime import date
import progress_data


def report_menu():
    while True:
        print("\n" + "=" * 55)
        print("                     REPORT")
        print("=" * 55)
        print("1. Overall Report")
        print("2. Topic Performance")
        print("3. Recommendations")
        print("4. Generate Certificate")
        print("0. Back")

        choice = input("Choose an option: ").strip()

        if choice == "0":
            return
        elif choice == "1":
            overall_report()
        elif choice == "2":
            topic_performance()
        elif choice == "3":
            recommendations()
        elif choice == "4":
            certificate()
        else:
            print("Invalid choice.")


def overall_report():
    attempted, correct, wrong, accuracy, topic_data = progress_data.get_statistics()

    print("\nOVERALL REPORT")
    print("Questions Attempted:", attempted)
    print("Correct:", correct)
    print("Incorrect:", wrong)
    print(f"Accuracy: {accuracy:.2f}%")
    print("(Includes both Practice and Question Bank)")
    input("Press Enter to go back...")


def topic_performance():
    topic_data = progress_data.get_statistics()[4]

    print("\nTOPIC PERFORMANCE")
    if not topic_data:
        print("No practice data available.")
        input("Press Enter to go back...")
        return

    print(f"{'Topic':<18}{'Attempted':<12}{'Correct':<10}Accuracy")
    for topic in topic_data:
        attempted, correct = topic_data[topic]
        accuracy = correct / attempted * 100
        print(f"{topic:<18}{attempted:<12}{correct:<10}{accuracy:.2f}%")

    input("Press Enter to go back...")


def recommendations():
    topic_data = progress_data.get_statistics()[4]

    print("\nRECOMMENDATIONS")
    if not topic_data:
        print("Complete some questions first.")
        input("Press Enter to go back...")
        return

    shown = False
    for topic in topic_data:
        attempted, correct = topic_data[topic]
        score = correct / attempted * 100

        if score < 60:
            print(f"- Practice {topic} again. Accuracy: {score:.2f}%")
            shown = True
        elif score < 80:
            print(f"- Revise {topic}. Accuracy: {score:.2f}%")
            shown = True

    if not shown:
        print("Good progress. Keep going!")

    input("Press Enter to go back...")


def certificate():
    attempted, correct, wrong, accuracy, topic_data = progress_data.get_statistics()

    print("\nGENERATE CERTIFICATE")

    # need at least 20 questions and 60% accuracy
    if attempted < 20 or accuracy < 60:
        print("Certificate not available yet.")
        print("Need: minimum 20 questions + 60% accuracy")
        print("Questions Attempted:", attempted)
        print(f"Accuracy: {accuracy:.2f}%")
        input("Press Enter to go back...")
        return

    name = input("Enter your name: ").strip()
    if name == "":
        name = "Python Learner"

    today = date.today().strftime("%d-%m-%Y")

    print("\n" + "=" * 60)
    print("                   MINI VITYARTHI")
    print("\n            PYTHON LEARNING CERTIFICATE")
    print("\nThis is presented to")
    print("\n                   " + name)
    print("\nfor completing the Mini Vityarthi Python program.")
    print("\nDate:", today)
    print(f"Accuracy: {accuracy:.2f}%")
    print("=" * 60)
    print("(Project generated certificate)")
    input("Press Enter to go back...")
