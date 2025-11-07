# 🎓 Student Result Processing System

A **Python and MySQL-based application** designed to simplify and automate the management of student academic results.  
The system allows administrators to manage student records, store marks, and generate final results efficiently through a command-line interface.

---

## 🚀 Overview

The **Student Result Processing System** provides a structured way to handle examination data digitally.  
It connects **Python (frontend logic)** with **MySQL (backend database)** to manage student details, marks, and computed results securely.

This project demonstrates the implementation of database connectivity in Python using the **PyMySQL** connector, performing CRUD operations, and executing SQL queries to process results.

---

## 🧩 Features

- 🔐 **Admin Login System** — Secure authentication using a user table.
- 👨‍🎓 **Student Record Management** — Add, update, and view student details.
- 🧾 **Marks Management** — Stores scores for Minor 1, Minor 2, and Major exams.
- 🧮 **Automatic Result Calculation** — Computes total marks and percentage.
- 🗄️ **Database Integration** — All data stored in a MySQL database.
- 🖥️ **Simple CLI Interface** — Interactive menu for user-friendly navigation.

---

## 🧠 Technology Stack

| Component | Technology Used |
|------------|-----------------|
| Language | Python 3 |
| Database | MySQL 8 |
| Connector | PyMySQL |
| Interface | Command-Line (CLI) |
| Tool Used | MySQL Workbench |

---

## 🧱 Database Schema

### **Tables Used**

#### 1️⃣ `users`
| Column | Type | Description |
|---------|------|-------------|
| enrollment_num | VARCHAR | Unique user/student ID |
| username | VARCHAR | User login name |
| password | VARCHAR | Hashed or plain password |
| role | VARCHAR | Role of user (Admin/Student) |

#### 2️⃣ `students`
| Column | Type | Description |
|---------|------|-------------|
| enrollment_num | VARCHAR | Unique student ID |
| name | VARCHAR | Full name |
| branch | VARCHAR | Branch name (e.g., CSE, ECE) |
| department | VARCHAR | Department name |

#### 3️⃣ `marks`
| Column | Type | Description |
|---------|------|-------------|
| enrollment_num | VARCHAR | Student reference ID |
| minor1 | INT | Marks out of 25 |
| minor2 | INT | Marks out of 25 |
| major | INT | Marks out of 50 |
| total | INT | Computed total marks |

#### 4️⃣ `result`
| Column | Type | Description |
|---------|------|-------------|
| enrollment_num | VARCHAR | Student reference ID |
| total_marks | INT | Aggregate marks |
| percentage | FLOAT | Computed percentage |
| grade | VARCHAR | Grade based on percentage |

---

## ⚙️ How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/OliveishPraveen/macro_project1.git
   cd macro_project1
2. **Install dependencies**
   ` pip install pymysql `
3. **Setup MySQL Database**
   1. Open MySQL Workbench
   2. Create a new schema
   3. Import or execute the provided .sql file to create tables
4. **Run the Application**
   ` python app.py `
5. **Use the CLI Menu**
   1. Login as Admin
   2. Add Students, Enter Marks and View Results
6. **Working Flow**
   1. **Login →** Verify credentials from the users table
   2. **Student Management →** Add student details into students
   3. **Marks Entry →** Insert marks for each exam in marks
   4. **Result Calculation →** Automatically computes total and percentage
   5. **Display Result →** Shows formatted result summary for each student
7. **Future Enhancements**
   1. 🖥️ GUI interface using Tkinter or Flask
   2. 📊 Report card generation (PDF export)
   3. 🔔 Email notifications for result updates
   4. 🧑‍💻 Role-based dashboards (Admin/Faculty/Student)
