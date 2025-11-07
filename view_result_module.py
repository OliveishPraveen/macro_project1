import mysql.connector
from db_connect import get_connection

def view_result():
    conn = get_connection()
    if not conn:
        print("❌ Database connection failed.")
        return

    cursor = conn.cursor(dictionary=True)

    print("\n===== View Student Result =====")
    print("1. View Single Student Result")
    print("2. View All Results")

    choice = input("Enter your choice (1 or 2): ").strip()

    try:
        if choice == '1':
            enrollment = input("Enter Enrollment Number: ").strip()
            query = """
                SELECT s.enrollment_no, s.name, s.branch, s.department, 
                       r.semester, r.total_marks, r.percentage, r.grade
                FROM students s
                JOIN result r ON s.enrollment_no = r.enrollment_no
                WHERE s.enrollment_no = %s
            """
            cursor.execute(query, (enrollment,))
            result = cursor.fetchone()

            if not result:
                print("⚠️ No result found for this enrollment number.")
            else:
                print("\n🎓 ----- Student Result ----- 🎓")
                print(f"Enrollment No : {result['enrollment_no']}")
                print(f"Name          : {result['name']}")
                print(f"Branch        : {result['branch']}")
                print(f"Department    : {result['department']}")
                print(f"Semester      : {result['semester']}")
                print(f"Total Marks   : {result['total_marks']}")
                print(f"Percentage    : {result['percentage']}%")
                print(f"Grade         : {result['grade']}")
                print("--------------------------------")

        elif choice == '2':
            query = """
                SELECT s.enrollment_no, s.name, s.branch, r.semester, 
                       r.total_marks, r.percentage, r.grade
                FROM students s
                JOIN result r ON s.enrollment_no = r.enrollment_no
                ORDER BY s.enrollment_no
            """
            cursor.execute(query)
            results = cursor.fetchall()

            if not results:
                print("⚠️ No results found!")
            else:
                print("\n===== All Student Results =====")
                print(f"{'Enroll No':<12} {'Name':<15} {'Branch':<8} {'Sem':<4} {'Total':<6} {'%':<6} {'Grade':<6}")
                print("-" * 65)
                for row in results:
                    print(f"{row['enrollment_no']:<12} {row['name']:<15} {row['branch']:<8} {row['semester']:<4} {row['total_marks']:<6} {row['percentage']:<6} {row['grade']:<6}")

        else:
            print("⚠️ Invalid choice. Please enter 1 or 2.")

    except mysql.connector.Error as err:
        print(f"❌ Database Error: {err}")
    finally:
        cursor.close()
        conn.close()
