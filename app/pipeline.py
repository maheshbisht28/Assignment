import logging
from .tasks import task_mapping, add_task

class DataPipeline:
    def __init__(self, tasks):
        self.tasks = tasks
        self.logger = logging.getLogger('DataPipeline')
    
    def run(self, df):
        report = []
        for task_info in self.tasks:
            task_name = task_info['name']
            task_func = task_mapping[task_name]
            params = task_info.get('params', {})
            result = task_func(df, **params)
            self.logger.info(f"Task {task_name} completed. Result: {result}")
            report.append({task_name: result})
        return report

def add_task(task_name, task_func):
    task_mapping[task_name] = task_func

def update_task(task_name, task_func):
    task_mapping[task_name] = task_func