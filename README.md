# Fitness Tracker CLI

A command-line fitness tracker built using Python and MySQL that allows users to record workouts, manage users, and track overall fitness progress. The application provides a simple menu-driven interface for managing activities and viewing statistics. 

## Features

* Add and manage users
* Record fitness activities
* Track workout duration and calories burned
* Update or delete users and activities 
* View all stored records
* Track total workout progress for each user
* Secure database configuration using environment variables  

## Technologies Used
 
* Python
* MySQL
* python-dotenv (for secure environment variable management)

## Project Structure

```
fitness-tracker/
│
├── main.py
├── .env
├── requirements.txt
└── README.md
```

## Database Structure

### Users Table

Stores user information:

* user_id (Primary Key)
* username
* email
* age
* weight
* height

### Activities Table

Stores workout activities:

* activity_id (Primary Key)
* activity_name
* duration_minutes
* calories_burned
* user_id (Foreign Key)

## Installation

1. Clone the repository

```bash
git clone https://github.com/yourusername/fitness-tracker.git
cd fitness-tracker
```

2. Install dependencies

```bash
pip install mysql-connector-python python-dotenv
```

3. Create a `.env` file

```
DB_HOST=localhost
DB_USER=your_username
DB_PASSWORD=your_password
DB_NAME=fitness_db
DB_PORT=3306
```

4. Run the application

```bash
python main.py
```

## Example Menu

```
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
```

## Learning Outcomes

This project helped in understanding:

* Python CLI application development
* Database integration with MySQL
* CRUD operations
* Environment variable management
* Basic database design and relationships

## Future Improvements

* Add input validation
* Add search functionality
* Export reports
* Add graphical visualization of progress
* Convert CLI to a web dashboard

## Author

Ayushi 
