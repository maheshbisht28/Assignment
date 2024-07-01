import pandas as pd
import json
import os


def assess_missing_values(df, columns_thresholds):
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
    if columns is None:
        columns = df.columns.tolist()
    duplicate_count = int(df.duplicated(subset=columns).sum())
    return {"duplicate_rows": duplicate_count}

task_mapping = {
    "assess_missing_values": assess_missing_values,
    "identify_duplicate_rows": identify_duplicate_rows,
}



def add_task(task_name, task_func):
    if task_name in task_mapping:
        raise ValueError(f"Task '{task_name}' already exists. Use update_task to modify it.")
    task_mapping[task_name] = task_func

def update_task(task_name, task_func):
    if task_name not in task_mapping:
        raise ValueError(f"Task '{task_name}' does not exist. Use add_task to add it first.")
    task_mapping[task_name] = task_func
