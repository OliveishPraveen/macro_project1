from student_module import add_student
from marks_module import add_marks
from result_module import generate_result
from view_result_module import view_result

def main_menu():
    while True:
        print("\n===== Student Result Processing System =====")
        print("1. Add Student")
        print("2. Enter Marks")
        print("3. Generate Result")
        print("4. View Result")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            add_marks()
        elif choice == '3':
            generate_result()
        elif choice == '4':
            view_result()
        elif choice == '5':
            print("\n👋 Exiting the system. Goodbye!")
            break
        else:
            print("\n⚠️ Invalid choice. Please enter a number between 1 and 5.")
