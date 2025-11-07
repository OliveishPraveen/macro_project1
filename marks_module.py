import mysql.connector
from db_connect import get_connection

def add_marks():
    conn = get_connection()
    if not conn:
        print("❌ Database connection failed.")
        return

    cursor = conn.cursor()

    print("\n===== Enter Student Marks =====")
    enrollment = input("Enter Enrollment Number: ").strip()

    # Check if student exists
    check_query = "SELECT name FROM students WHERE enrollment_no = %s"
    cursor.execute(check_query, (enrollment,))
    student = cursor.fetchone()

    if not student:
        print("⚠️ Student not found. Please add the student first.")
        cursor.close()
        conn.close()
        return

    print(f"🧾 Found Student: {student[0]}")

    try:
        subject = input("Enter Subject Name: ").strip()
        semester = int(input("Enter Semester Number: "))

        minor1 = int(input("Enter Minor 1 Marks (out of 25): "))
        minor2 = int(input("Enter Minor 2 Marks (out of 25): "))
        major = int(input("Enter Major Marks (out of 50): "))

        # Validation
        if not (0 <= minor1 <= 25 and 0 <= minor2 <= 25 and 0 <= major <= 50):
            print("⚠️ Marks out of valid range. Please check again.")
            return

        insert_query = """
            INSERT INTO marks (enrollment_no, subject, semester, minor1, minor2, major)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(insert_query, (enrollment, subject, semester, minor1, minor2, major))
        conn.commit()
        print("✅ Marks added successfully!")

    except ValueError:
        print("⚠️ Invalid input! Please enter numeric marks.")
    except mysql.connector.IntegrityError:
        print("⚠️ Marks for this subject already exist for this student.")
    except mysql.connector.Error as err:
        print(f"❌ Database Error: {err}")
    finally:
        cursor.close()
        conn.close()
