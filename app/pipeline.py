import logging
from .tasks import task_mapping, add_task

class DataPipeline:
    """
    A class to represent a data processing pipeline.

    Attributes:
    tasks (list): A list of tasks to be executed in the pipeline.
    logger (logging.Logger): A logger instance for logging task execution details.

    Methods:
    run(df): Executes the tasks in the pipeline on the given DataFrame.
    """
    def __init__(self, tasks):
        """
        Initializes the DataPipeline with a list of tasks.

        Parameters:
        tasks (list): A list of dictionaries, where each dictionary contains:
            - 'name': The name of the task (str).
            - 'params': A dictionary of parameters to be passed to the task (dict, optional).
        """
        self.tasks = tasks
        self.logger = logging.getLogger('DataPipeline')
    
    def run(self, df):
        """
        Executes the tasks in the pipeline on the given DataFrame.

        Parameters:
        df (pd.DataFrame): The DataFrame to be processed.

        Returns:
        list: A list of dictionaries, where each dictionary contains the task name and its result.
        """
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
    """
    Add a new task to the task mapping.

    Parameters:
    task_name (str): The name of the task to be added.
    task_func (function): The function implementing the task.

    Raises:
    ValueError: If the task already exists in the task mapping.
    """
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
    task_mapping[task_name] = task_func