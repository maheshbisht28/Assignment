# Data Cleaning Pipeline

This project provides a configurable data processing pipeline framework that allows users to configure and trigger data pipelines through an API call.

## Project Structure

- `app/`: Contains the main application code.
  - `__init__.py`: Initializes logging.
  - `api.py`: Defines the API for running the pipeline.
  - `pipeline.py`: Contains the `DataPipeline` class and functions to manage tasks.
  - `tasks.py`: Contains the task functions.
- `scripts/`: Contains scripts for demo and testing.
  - `demo.py`: Demonstrates how to use the API.
- `main.py`: Runs the Flask app.
- `requirements.txt`: Lists the dependencies.
- `README.md`: Project documentation.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
