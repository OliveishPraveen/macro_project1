import mysql.connector
from db_connect import get_connection

def generate_result():
    conn = get_connection()
    if not conn:
        print("❌ Database connection failed.")
        return

    cursor = conn.cursor(dictionary=True)

    print("\n===== Generate Student Results =====")

    # Fetch all marks data
    cursor.execute("SELECT * FROM marks")
    marks_data = cursor.fetchall()

    if not marks_data:
        print("⚠️ No marks found! Please enter marks first.")
        return

    for row in marks_data:
        enrollment = row['enrollment_no']
        semester = row['semester']
        total = row['minor1'] + row['minor2'] + row['major']
        percentage = round((total / 100) * 100, 2)

        # Grade logic
        if percentage >= 90:
            grade = 'A+'
        elif percentage >= 80:
            grade = 'A'
        elif percentage >= 70:
            grade = 'B+'
        elif percentage >= 60:
            grade = 'B'
        elif percentage >= 50:
            grade = 'C'
        else:
            grade = 'F'

        insert_query = """
            INSERT INTO result (enrollment_no, semester, total_marks, percentage, grade)
            VALUES (%s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
                total_marks = VALUES(total_marks),
                percentage = VALUES(percentage),
                grade = VALUES(grade)
        """
        cursor.execute(insert_query, (enrollment, semester, total, percentage, grade))

    conn.commit()
    print("✅ Results generated and saved successfully for all students!")

    cursor.close()
    conn.close()
