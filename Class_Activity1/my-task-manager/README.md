
# My Simple Task Manager CLI

A command-line interface (CLI) application for managing your daily tasks.
You can add, list, complete, and delete tasks, and your tasks are saved automatically.

## Features

* **Add Tasks**: Add new tasks with a description.
* **List Tasks**: View all your tasks, showing their ID, description, and status.
* **Complete Tasks**: Mark tasks as completed by their ID.
* **Delete Tasks**: Remove tasks by their ID.
* **Persistence**: Tasks are saved to `data/tasks.json` and loaded automatically.

## How to Run

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/my-task-manager.git](https://github.com/YOUR_USERNAME/my-task-manager.git)
   cd my-task-manager
   ```
2. **Run the application:**
   ```bash
   python main.py
   ```

## Project Structure

my-task-manager/
├── src/
│ ├── init.py # Makes 'src' a Python package
│ ├── task_data.py # Handles reading from/writing to tasks.json
│ └── task_logic.py # Contains core task management functions (add, list, complete, delete)
├── data/
│ └── tasks.json # Stores your tasks (created automatically)
├── main.py # The main entry point of the application
├── .gitignore # Specifies files/folders to ignore in Git
└── README.md # This file!

## Contributing

Feel free to fork this repository, add features, or improve existing ones!

## License

This project is open source. (You might add a specific license here later, e.g., MIT)
