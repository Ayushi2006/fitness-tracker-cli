import os
from dotenv import load_dotenv 
import mysql.connector 

# Load environment variables from .env file
load_dotenv()  # Must have a file named ".env" in the same folder 

# Connect to the MySQL database safely
def connect_to_db():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        port=int(os.getenv("DB_PORT")),
        auth_plugin='caching_sha2_password'
    )

# Create tables for users and activities
def create_tables():
    conn = connect_to_db()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(255),
            email VARCHAR(255),
            age INT,
            weight FLOAT,
            height FLOAT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS activities (
            activity_id INT AUTO_INCREMENT PRIMARY KEY,
            activity_name VARCHAR(255),
            duration_minutes INT,
            calories_burned INT,
            user_id INT,
            FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
        )
    """)
    conn.close()

# Add a new user
def add_user():
    username = input("Enter username: ")
    email = input("Enter email: ")
    age = int(input("Enter age: "))
    weight = float(input("Enter weight (kg): "))
    height = float(input("Enter height (cm): "))

    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO users (username, email, age, weight, height)
        VALUES (%s, %s, %s, %s, %s)
    """, (username, email, age, weight, height))
    conn.commit()
    conn.close()
    print("User added successfully!")

# View all users
def view_users():
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users ORDER BY user_id ASC")
    users = cursor.fetchall()

    print("\nUsers List:")
    for idx, user in enumerate(users, start=1):
        print(f"{idx}. ID: {user[0]}, Username: {user[1]}, Email: {user[2]}, Age: {user[3]}, Weight: {user[4]}, Height: {user[5]}")
    conn.close()

# Add a new activity
def add_activity():
    user_id = int(input("Enter user ID for the activity: "))
    activity_name = input("Enter activity name: ")
    duration = int(input("Enter duration (minutes): "))
    calories = int(input("Enter calories burned: "))

    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO activities (activity_name, duration_minutes, calories_burned, user_id)
        VALUES (%s, %s, %s, %s)
    """, (activity_name, duration, calories, user_id))
    conn.commit()
    conn.close()
    print("Activity added successfully!")

# View all activities
def view_activities():
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM activities ORDER BY activity_id ASC")
    activities = cursor.fetchall()

    print("\nActivities List:")
    for idx, activity in enumerate(activities, start=1):
        print(f"{idx}. ID: {activity[0]}, Activity: {activity[1]}, Duration: {activity[2]} mins, Calories: {activity[3]}, User ID: {activity[4]}")
    conn.close()

# Update activity
def update_activity():
    activity_id = int(input("Enter activity ID to update: "))
    new_name = input("Enter new activity name: ")
    new_duration = int(input("Enter new duration (minutes): "))
    new_calories = int(input("Enter new calories burned: "))
    new_user_id = int(input("Enter new user ID: "))

    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE activities
        SET activity_name = %s, duration_minutes = %s, calories_burned = %s, user_id = %s
        WHERE activity_id = %s
    """, (new_name, new_duration, new_calories, new_user_id, activity_id))
    conn.commit()

    if cursor.rowcount:
        print("Activity updated successfully!")
    else:
        print("No activity found with that ID.")
    conn.close()

# Update user
def update_user():
    user_id = int(input("Enter user ID to update: "))
    new_age = int(input("Enter new age: "))
    new_weight = float(input("Enter new weight: "))

    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE users
        SET age = %s, weight = %s
        WHERE user_id = %s
    """, (new_age, new_weight, user_id))
    conn.commit()

    if cursor.rowcount:
        print("User updated successfully!")
    else:
        print("No user found with that ID.")
    conn.close()

# Delete activity
def delete_activity():
    activity_id = int(input("Enter activity ID to delete: "))
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM activities WHERE activity_id = %s", (activity_id,))
    conn.commit()

    if cursor.rowcount:
        print("Activity deleted successfully!")
    else:
        print("No activity found with that ID.")
    conn.close()

# Delete user
def delete_user():
    user_id = int(input("Enter user ID to delete: "))
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE user_id = %s", (user_id,))
    conn.commit()

    if cursor.rowcount:
        print("User deleted successfully!")
    else:
        print("No user found with that ID.")
    conn.close()

# Show user progress
def show_progress():
    user_id = int(input("Enter user ID to view progress: "))
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT COUNT(activity_id), SUM(duration_minutes), SUM(calories_burned)
        FROM activities WHERE user_id = %s
    """, (user_id,))
    progress = cursor.fetchone()
    total_activities, total_duration, total_calories = progress if progress else (0, 0, 0)

    print(f"\nUser Progress - Total Activities: {total_activities}, Total Duration: {total_duration} mins, Total Calories: {total_calories}")
    conn.close()

# Main menu
def main():
    create_tables()
    while True:
        print("""
Menu:
1. Add User
2. View Users
3. Add Activity
4. View Activities
5. Update Activity
6. Update User
7. Delete Activity
8. Delete User
9. Show User Progress
10. Exit
""")
        choice = input("Choose an option: ")

        if choice == "1":
            add_user()
        elif choice == "2":
            view_users()
        elif choice == "3":
            add_activity()
        elif choice == "4":
            view_activities()
        elif choice == "5":
            update_activity()
        elif choice == "6":
            update_user()
        elif choice == "7":
            delete_activity()
        elif choice == "8":
            delete_user()
        elif choice == "9":
            show_progress()
        elif choice == "10":
            print("Bye! Enjoy your fitness journey :)")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
