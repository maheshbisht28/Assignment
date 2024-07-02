import pandas as pd
import json
import os


def assess_missing_values(df, columns_thresholds):
    """
    Assess the missing values in the specified columns and compare them against the provided thresholds.

    Parameters:
    df (pd.DataFrame): The DataFrame to be analyzed.
    columns_thresholds (dict): A dictionary where keys are column names and values are thresholds for missing values.

    Returns:
    dict: A dictionary with missing values count and threshold comparison for each specified column.
    """
    missing_report = {}
    for column, threshold in columns_thresholds.items():
        if column in df.columns:
            missing_count = df[column].isnull().sum()
            missing_report[column] = {
                "missing_count": int(missing_count),
                "threshold_exceeded": bool(missing_count > threshold)
            }
    return {"missing_values": missing_report}

def identify_duplicate_rows(df, columns=None):
    """
    Identify the number of duplicate rows in the DataFrame based on specified columns.

    Parameters:
    df (pd.DataFrame): The DataFrame to be analyzed.
    columns (list, optional): A list of column names to check for duplicates. If None, all columns are used.

    Returns:
    dict: A dictionary with the count of duplicate rows.
    """
    if columns is None:
        columns = df.columns.tolist()
    duplicate_count = int(df.duplicated(subset=columns).sum())
    return {"duplicate_rows": duplicate_count}

task_mapping = {
    "assess_missing_values": assess_missing_values,
    "identify_duplicate_rows": identify_duplicate_rows,
}



def add_task(task_name, task_func):
    """
    Add a new task to the task mapping.

    Parameters:
    task_name (str): The name of the task to be added.
    task_func (function): The function implementing the task.

    Raises:
    ValueError: If the task already exists in the task mapping.
    """
    if task_name in task_mapping:
        raise ValueError(f"Task '{task_name}' already exists. Use update_task to modify it.")
    task_mapping[task_name] = task_func

def update_task(task_name, task_func):
    """
    Update an existing task in the task mapping.

    Parameters:
    task_name (str): The name of the task to be updated.
    task_func (function): The new function implementing the task.

    Raises:
    ValueError: If the task does not exist in the task mapping.
    """
    
    if task_name not in task_mapping:
        raise ValueError(f"Task '{task_name}' does not exist. Use add_task to add it first.")
    task_mapping[task_name] = task_func
