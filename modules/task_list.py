# Functions to complete:

## Get a list of uncompleted tasks
def get_uncompleted_tasks(list):
    uncompleted_task = []
    for task in list:
        if task['completed'] == False:
            uncompleted_task.append(task)
    return uncompleted_task 
            
## Get a list of completed tasks
def get_completed_tasks(list):
    completed_task = []
    for task in list:
        if task['completed'] == True:
            completed_task.append(task)
    return completed_task

## Get tasks where time_taken is at least a given time
def get_tasks_taking_at_least(list, time):
    minimum_time = []
    for task in list:
        if task['time_taken'] >= time:
            minimum_time.append(task)
    return minimum_time

## Find a task with a given description
def get_task_with_description(list, description):
    description_task = []
    for task in list:
        if task['description'] == description:
            description_task.append(task)
    return description_task


# Extention (Function): 

## Get a list of tasks by status
# def get_tasks_by_status(list, status):
#     task_status_complete = []
#     task_status_incomplete = []
#     for task in list:
#         if task['completed'] == False:
#             task_status_incomplete.append(task)
#     print(task_status_incomplete)
#     for task in list:
#         if task['completed'] == True:
#             task_status_complete.append(task)
#     return task_status_complete


def mark_task_complete(task):
    task["completed"] = True

def create_task(description, time_taken):
    task = {}
    task["description"] = description
    task["completed"] = False
    task["time_taken"] = time_taken

    return task

def add_to_list(list, task):
    list.append(task)


