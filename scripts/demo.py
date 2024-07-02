import requests

csv_data = """
id,name,age,salary,bonus
1,Alice,25,50000,1000
2,Bob,30,,1000
3,Charlie,35,60000,1000
4,Alice,25,50000,1000
5,Eve,40,70000,1000
5,Eve,40,70000,1000
"""

#  Addind new task
new_task_code = """
def add_salary_bonus(df, columns):
    # Example new task logic
    if not set(columns).issubset(df.columns):
        missing_cols = [col for col in columns if col not in df.columns]
        raise ValueError(f"Columns not found in DataFrame: {missing_cols}")
    print("columns ",columns )    
    # Dynamically calculate the sum using list comprehension for efficiency
    result = df[columns].sum(axis=1)
    return {"result": result.tolist()}
"""



data = {
    "task_name": "add_salary_bonus",
    "task_code": new_task_code
}

response = requests.post("http://127.0.0.1:5000/add_task", json=data)

# Check if the request was successful
if response.status_code == 200:
    try:
        print(response.json())       
    except requests.exceptions.JSONDecodeError as e:
        print("Error decoding JSON response:")
        print(response.text)
else:
    print(f"Request failed with status code {response.status_code}")
    print(response.text)



# Checking if new task is added or not
response = requests.get("http://127.0.0.1:5000/list_tasks")
if response.status_code == 200:
    print("Available tasks:", response.json())

else:
    print("Failed to list tasks:", response.json())


#  Calling new task
data = {
    "tasks": [
        {
            "name": "identify_duplicate_rows",
            "params": {
                "columns": ["id", "name"]
            }
        },
        {
            "name": "assess_missing_values",
            "params": {
                "columns_thresholds": {
                    "age": 0,
                    "salary": 1
                }
            }
        },
        {
            "name": "add_salary_bonus",
            "params": {
                      "columns": ["salary","bonus"]
            }
        }
    ],
    "csv_data": csv_data
}

response = requests.post("http://127.0.0.1:5000/run_pipeline", json=data)

if response.status_code == 200:
    try:
        print("Result ",response.json())
    except requests.exceptions.JSONDecodeError as e:
        print("Error decoding JSON response:")
        print(response.text)
    except requests.exceptions.JSONDecodeError as e:
        print("Error decoding JSON response:")
        print(response.text)
else:
    print("Failed to list tasks:", response.json())

#  Updating Task
update_task_code = """
def add_salary_bonus(df, columns):
    # Example new task logic
    if not set(columns).issubset(df.columns):
        missing_cols = [col for col in columns if col not in df.columns]
        raise ValueError(f"Columns not found in DataFrame: {missing_cols}")
    # Validate the data types of the specified columns
    for col in columns:
        if not pd.api.types.is_numeric_dtype(df[col]):
            raise ValueError(f"Column '{col}' must be numeric")
    
    # Dynamically calculate the sum using list comprehension for efficiency
    result = df[columns].sum(axis=1)

    # Logging for debugging
    print(f"Columns: {columns}")
    print(f"Result: {result}")
    return {"result": result.tolist()}
"""

data = {
    "task_name": "add_salary_bonus",
    "task_code": update_task_code
}

response = requests.post("http://127.0.0.1:5000/update_task", json=data)
# Check if the request was successful
if response.status_code == 200:
    try:
        print(response.json())
    except requests.exceptions.JSONDecodeError as e:
        print("Error decoding JSON response:")
        print(response.text)
else:
    print(f"Request failed with status code {response.status_code}")
    print(response.text)


# Testing if task is updated or not
data = {
    "tasks": [
        {
            "name": "identify_duplicate_rows",
            "params": {
                "columns": ["id", "name"]
            }
        },
        {
            "name": "assess_missing_values",
            "params": {
                "columns_thresholds": {
                    "age": 0,
                    "salary": 1
                }
            }
        },
        {
            "name": "add_salary_bonus",
            "params": {
                      "columns": ["salary","bonus"]
            }
        }
    ],
    "csv_data": csv_data
}

response = requests.post("http://127.0.0.1:5000/run_pipeline", json=data)

if response.status_code == 200:
    print(response.json())
else:
    print("Failed to list tasks:", response.json())



# Note: If you run above code , output will be the following
# {'message': "Task 'add_salary_bonus' added successfully."}
# Available tasks: ['assess_missing_values', 'identify_duplicate_rows', 'add_salary_bonus']
# Result  [{'identify_duplicate_rows': {'duplicate_rows': 1}},
#          {'assess_missing_values': 
#             {'missing_values': 
#                 {'age': 
#                     {'missing_count': 0, 'threshold_exceeded': False}, 
#                  'salary': 
#                     {'missing_count': 1, 'threshold_exceeded': False}}
#             }
#          },
#          {'add_salary_bonus': 
#             {'result': 
#                 [51000.0, 1000.0, 61000.0, 51000.0, 71000.0, 71000.0]
#             }
#           }
#         ]
# {'message': "Task 'add_salary_bonus' updated successfully."}
# [{'identify_duplicate_rows': {'duplicate_rows': 1}}, 
#  {'assess_missing_values': 
#     {'missing_values': 
#         {'age': 
#             {'missing_count': 0, 'threshold_exceeded': False}, 
#          'salary': 
#             {'missing_count': 1, 'threshold_exceeded': False}
#         }
#     }
#  },
#  {'add_salary_bonus': 
#     {'result': 
#         [51000.0, 1000.0, 61000.0, 51000.0, 71000.0, 71000.0]
#     }
#  }
# ]
