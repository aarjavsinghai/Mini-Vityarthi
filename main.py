import learn
import practice
import question_bank
import analysis
import report
import progress_data

def show_menu():
    print("\n" + "=" * 50)
    print("            MINI VITYARTHI")
    print("     Python Learning & Progress Tracker")
    print("=" * 50)
    print("1. Learn Python")
    print("2. Practice Problems")
    print("3. Question Bank")
    print("4. View Progress")
    print("5. Report")
    print("0. Exit")
    print("=" * 50)


def main():
    progress_data.reset_progress()

    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            learn.learn_python()
        elif choice == "2":
            practice.practice_questions()
        elif choice == "3":
            question_bank.run_bank()
        elif choice == "4":
            analysis.view_progress()
        elif choice == "5":
            report.report_menu()
        elif choice == "0":
            print("\nThanks for using Mini Vityarthi!")
            print("Keep practicing Python :)")
            break
        else:
            print("Invalid choice. Enter a number from 0 to 5.")


if __name__ == "__main__":
    main()
