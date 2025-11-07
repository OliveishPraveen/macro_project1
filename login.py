from db_connect import get_connection

def login():
    conn = get_connection()
    if not conn:
        print("❌ Database connection error. Cannot proceed.")
        return None

    cursor = conn.cursor()

    print("\n===== Admin Login =====")
    username = input("Enter username: ")
    password = input("Enter password: ")

    try:
        query = "SELECT username, role FROM users WHERE username=%s AND password=%s"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()

        if result:
            print(f"\n✅ Login successful! Welcome, {result[0]} ({result[1]})")
            conn.close()
            return result[1]  # Return the role (admin/teacher/etc.)
        else:
            print("\n❌ Invalid username or password. Try again.")
            conn.close()
            return None

    except Exception as e:
        print(f"⚠️ Error during login: {e}")
        conn.close()
        return None

# Test the login system independently
if __name__ == "__main__":
    role = login()
    if role:
        print(f"Access granted for role: {role}")
    else:
        print("Access denied.")
