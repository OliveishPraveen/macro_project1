from login import login
from main_menu import main_menu

def run_app():
    print("===== Welcome to Student Result Processing System =====")
    role = login()

    if role == "admin":
        print("\n🔓 Access granted to Admin Panel.")
        main_menu()
    elif role:
        print(f"\n🔒 Access restricted for role: {role}. Only admins can access the dashboard.")
    else:
        print("\n❌ Login failed. Exiting...")

if __name__ == "__main__":
    run_app()
