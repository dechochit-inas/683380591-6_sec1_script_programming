
# Final Project: Enhanced Task Manager CLI

This project is a complete command-line interface (CLI) application for managing tasks,
showcasing the application of various software development principles learned throughout the course.
It leverages Object-Oriented Programming (OOP), modular design, data persistence, and advanced data manipulation techniques.

## Implemented Features

* **Task Types**: Supports standard tasks, tasks with a `due_date` (`DueDateTask`), and tasks with a `priority` (`PriorityTask`).
* **Tags**: Assign multiple customizable tags to any task for better organization.
* **Comprehensive CRUD Operations**:
  * **Add Tasks**: Create normal, due date, or priority tasks with descriptions and optional tags.
  * **List Tasks**: View all tasks, with detailed information including tags, due dates, and priorities.
  * **Complete Tasks**: Mark tasks as completed by their ID.
  * **Delete Tasks**: Remove tasks by their ID.
* **Advanced Search**: Find tasks by keywords in their description or tags (case-insensitive).
* **Flexible Filtering**: Filter tasks by:
  * Completion status (completed/pending).
  * Due date range (tasks due before or after a specific date).
  * Priority level (High, Medium, Low).
  * Specific tag(s) (tasks must contain ALL specified tags).
* **Dynamic Sorting**: Sort tasks by various criteria:
  * Task ID (default)
  * Description
  * Completion Status
  * Due Date (for `DueDateTask`s; other tasks are grouped)
  * Priority (for `PriorityTask`s; other tasks are grouped)
* **Robust Data Persistence**: All tasks are automatically saved to `data/tasks.json` and loaded on startup, preserving all task details and types.
* **Modular Design**: Application is structured into distinct modules for clear separation of concerns:
  * `task.py`: Data models (Task classes).
  * `data_persistence.py`: Handles all file I/O.
  * `task_manager.py`: Contains core business logic (search, filter, sort).
  * `cli_interface.py`: Manages all user interaction.
  * `main.py`: The application entry point.

## How to Run

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/final-task-manager-project.git](https://github.com/YOUR_USERNAME/final-task-manager-project.git)
   cd final-task-manager-project
   ```
2. **Run the application:**
   ```bash
   python main.py
   ```

## Project Structure

final-task-manager-project/
├── src/
│ ├── init.py # Makes 'src' a Python package
│ ├── task.py # Task models (Task, DueDateTask, PriorityTask with tags)
│ ├── data_persistence.py # Handles JSON file operations
│ ├── task_manager.py # Core task logic (add, delete, complete, search, filter, sort)
│ └── cli_interface.py # Handles user interaction (menu, input/output)
├── data/
│ └── tasks.json # Stores your tasks (created/updated automatically)
├── main.py # Application entry point
├── .gitignore # Specifies files/folders to ignore in Git
├── README.md # This project overview
└── PLAN.md # Project planning, design notes, and reflections

## Extension Ideas (Future Work)

* **Graphical User Interface (GUI)**: Implement a GUI using libraries like `Tkinter`, `PyQt`, or `Kivy` to provide a more visual and interactive experience.
* **Database Integration**: Replace the JSON file persistence with a more robust database system like SQLite, PostgreSQL, or MongoDB.
* **Reminders/Notifications**: Implement a feature to notify the user about upcoming due dates (e.g., pop-up, email, or a simple command-line alert on startup).
* **User Accounts**: Add a basic user authentication system to allow multiple users to manage their own separate task lists.
* **Recurring Tasks**: Allow creation of tasks that repeat daily, weekly, or monthly.
* **Export/Import**: Add functionality to export tasks to CSV, PDF, or import from other formats.
* **Unit Testing**: Develop a comprehensive suite of unit tests for the `task.py` and `task_manager.py` modules to ensure code correctness and prevent regressions.
* **Web Interface**: Explore building a simple web interface using a framework like Flask or Django.

## Contributing

Feel free to fork this repository and build upon this foundation.

## License

This project is open source. (You might add a specific license here later, e.g., MIT)
