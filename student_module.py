import mysql.connector
from db_connect import get_connection

def add_student():
    conn = get_connection()
    if not conn:
        print("❌ Database connection failed.")
        return

    cursor = conn.cursor()

    print("\n===== Add New Student =====")
    enrollment = input("Enter Enrollment Number: ").strip()
    name = input("Enter Student Name: ").strip()
    branch = input("Enter Branch: ").strip()
    department = input("Enter Department: ").strip()

    if not enrollment or not name:
        print("⚠️ Enrollment number and name cannot be empty.")
        return

    try:
        query = """
            INSERT INTO students (enrollment_no, name, branch, department)
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (enrollment, name, branch, department))
        conn.commit()
        print(f"✅ Student '{name}' added successfully!")

    except mysql.connector.IntegrityError:
        print("⚠️ Enrollment number already exists.")
    except mysql.connector.Error as err:
        print(f"❌ Error: {err}")
    finally:
        cursor.close()
        conn.close()
