from flask import Flask, request, jsonify
import pandas as pd
import io
from .pipeline import DataPipeline
from .tasks import task_mapping, add_task, update_task

app = Flask(__name__)

@app.route('/run_pipeline', methods=['POST'])
def run_pipeline():
    try:
        data = request.get_json()
        tasks = data['tasks']
        csv_data = data['csv_data']
        df = pd.read_csv(io.StringIO(csv_data))

        pipeline = DataPipeline(tasks)
        report = pipeline.run(df)

        return jsonify(report)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/add_task', methods=['POST'])
def add_task_endpoint():
    try:
        data = request.get_json()
        task_name = data['task_name']
        task_code = data['task_code']
        print("data ",data)
        exec(task_code)
        task_func = locals()[task_name]
        
        add_task(task_name, task_func)
        return jsonify({"message": f"Task '{task_name}' added successfully."})
    except Exception as e:
        print("task_func ",task_func)
        return jsonify({"error": str(e)}), 500

@app.route('/update_task', methods=['POST'])
def update_task_endpoint():
    try:
        data = request.get_json()
        task_name = data['task_name']
        task_code = data['task_code']
        
        exec(task_code)
        task_func = locals()[task_name]
        
        update_task(task_name, task_func)
        return jsonify({"message": f"Task '{task_name}' updated successfully."})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/list_tasks', methods=['GET'])
def list_tasks():
    try:
        return jsonify(list(task_mapping.keys()))
    except Exception as e:
        return jsonify({"error": str(e)}), 500
