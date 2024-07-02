
# Data Pipeline Framework

## Overview

This project provides a configurable data processing pipeline framework for data cleaning tasks. It allows users to configure and trigger data pipelines through an API call, ensuring reusability of code and better data quality. The framework includes a library of atomic data cleaning tasks that can be used to process datasets.

## Features

- Assess missing values in any dataset
- Identify duplicate rows
- Easily add or update tasks in the task library
- Configure and trigger data pipelines through an API call
- Generate a report based on the tasks executed

## Getting Started

### Prerequisites

- Python 3.7+
- Flask
- Pandas

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-repo/data-pipeline-framework.git
    ```
2. Change to the project directory:
    ```bash
    cd data-pipeline-framework
    ```
3. Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
4. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```


### Project Structure

assignment_project/
│
├── app/
│ ├── init.py
│ ├── pipeline.py
│ ├── tasks.py
│ └── api.py
│
├── scripts/
│ ├── demo.py
│
├── requirements.txt
├── README.md
└── run.py



## Usage

### Running the Application

To start the Flask application, run:

```bash
python run.py
```

The application will be available at `http://127.0.0.1:5000`.

### API Endpoints

#### 1. Run Pipeline

- **URL:** `/run_pipeline`
- **Method:** `POST`
- **Request Body:**
    ```json
    {
        "tasks": [
            {
                "name": "task_name",
                "params": {"param1": value1, "param2": value2, ...}
            },
            ...
        ],
        "csv_data": "csv_data_string"
    }
    ```
- **Response:**
    ```json
    [
        {"task_name": {"result_key": result_value, ...}},
        ...
    ]
    ```
- **Example Request:**
    ```bash
    curl -X POST http://127.0.0.1:5000/run_pipeline     -H "Content-Type: application/json"     -d '{
        "tasks": [
            {
                "name": "assess_missing_values",
                "params": {"columns_thresholds": {"column1": 10, "column2": 5}}
            },
            {
                "name": "identify_duplicate_rows",
                "params": {"columns": ["column1", "column2"]}
            }
        ],
        "csv_data": "column1,column2
                    1,2
                    3,
                     ,5
                    1,2"
    }'
    ```

#### 2. Add Task

- **URL:** `/add_task`
- **Method:** `POST`
- **Request Body:**
    ```json
    {
        "task_name": "task_name",
        "task_code": "def task_name(df, **params): ... "
    }
    ```
- **Response:**
    ```json
    {
        "message": "Task 'task_name' added successfully."
    }
    ```
- **Example Request:**
    ```bash
    curl -X POST http://127.0.0.1:5000/add_task     -H "Content-Type: application/json"     -d '{
        "task_name": "add_salary_bonus",
        "task_code": "def add_salary_bonus(df, columns):
    result = df[columns].sum(axis=1)
    return {"result": result.tolist()}"
    }'
    ```

#### 3. Update Task

- **URL:** `/update_task`
- **Method:** `POST`
- **Request Body:**
    ```json
    {
        "task_name": "task_name",
        "task_code": "def task_name(df, **params): ... "
    }
    ```
- **Response:**
    ```json
    {
        "message": "Task 'task_name' updated successfully."
    }
    ```
- **Example Request:**
    ```bash
    curl -X POST http://127.0.0.1:5000/update_task     -H "Content-Type: application/json"     -d '{
        "task_name": "add_salary_bonus",
        "task_code": "def add_salary_bonus(df, columns):
    result = df[columns].mean(axis=1)
    return {"result": result.tolist()}"
    }'
    ```

#### 4. List Tasks

- **URL:** `/list_tasks`
- **Method:** `GET`
- **Response:**
    ```json
    [
        "task_name1",
        "task_name2",
        ...
    ]
    ```
- **Example Request:**
    ```bash
    curl -X GET http://127.0.0.1:5000/list_tasks
    ```

## Adding and Updating Tasks

### Adding a New Task

To add a new task, send a POST request to the `/add_task` endpoint with the task name and task code. The task code should be a valid Python function.

### Updating an Existing Task

To update an existing task, send a POST request to the `/update_task` endpoint with the task name and updated task code.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.