# Airbnb Clone CLI

This project is a command-line interface (CLI) tool that replicates the core functionalities of the Airbnb platform. It allows users to manage objects like users, places, amenities, cities, states, and reviews, simulating the backend operations of Airbnb.

## Features

- **User Management**: Create, update, delete, and display users.
- **Place Management**: Manage places, including creation, updates, and deletion.
- **Review Management**: Add and manage reviews for various places.
- **Storage System**: Saves and retrieves data from a local JSON file.
- **Object Management**: Supports multiple objects, including `User`, `Place`, `State`, `City`, `Amenity`, and `Review`.
- **Modular Design**: Divided into models, storage engine, and tests for easy management and extension.
- **Command-line Interface**: Interact with the system via terminal commands.

## Project Structure

```bash
├── models                 # Contains all model classes for objects like User, Place, etc.
│   ├── engine             # Contains the storage engine for saving objects
│   │   ├── __init__.py
│   │   └── file_storage.py # Manages saving/loading to and from JSON
│   ├── amenity.py         # Amenity class
│   ├── base_model.py      # Base class for all objects
│   ├── city.py            # City class
│   ├── place.py           # Place class
│   ├── review.py          # Review class
│   ├── state.py           # State class
│   └── user.py            # User class
├── tests                  # Unit tests for the project
│   ├── test_models        # Test cases for models
│   │   └── test_engine    # Test cases for the storage engine
│   └── __init__.py
├── AUTHORS                # List of contributors to the project
├── console.py             # Main entry point for the CLI program
├── datafile.json          # JSON file for data storage
└── README.md              # Project documentation (this file)
```
## Requirements
- **Python 3.8+**
- **UnitTest module** (for testing)
- **Json module** (built-in)

## Installation

1. **Clone the repositor**
```bash
git clone https://github.com/PcNerd9/AirBnB_clone
```
2. **Navigate to the project directory**
```bash
cd AirBnB_clone
```
3. **Run the program**
```bash
python3 console.py
```

## Usage
Once you run the CLI (`console.py`), you will be in an interactive mode where you can run several commands. The available commands include:

**Creating an object**
```bash
(hbnb) create <class_name>
```

Example:
```bash
(hbnb) create User
```
**Showing an object by ID**
```bash
(hbnb) show <class_name> <id>
```

Example:
```bash
(hbnb) show User 1234-5678-9012
```

**Updating an object by ID**
```bash
(hbnb) update <class_name> <id> <attribute_name> <attribute_value>
```

Example:
```bash
(hbnb) update User 1234-5678-9012 email "new_email@example.com"
```

**Deleting an object by ID**
```bash
(hbnb) destroy <class_name> <id>
```

Example:
```bash
(hbnb) destroy User 1234-5678-9012
```

**Listing all objects**
```bash
(hbnb) all <class_name>
```

Example:
```bash
(hbnb) all User
```

**Exiting the CLI**
```bash
(hbnb) quit
```

## Storage System
The system uses a JSON file (`datafile.json`) to store objects. When the application runs, it loads previously saved objects from this file. Any changes (additions, updates, or deletions) made through the CLI will be reflected in this file.

## File Storage Engine
- **file_storage.py**: Handles serialization and deserialization of objects to/from the JSON file.

## Testing
The project contains unit tests for each model and the storage engine. To run the test suite, use:

```bash
python3 -m unittest discover tests/
```
This command will automatically discover and run all tests within the `tests/` directory.


