tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

# 1. Print a list of uncompleted task

# trial
# def uncompleted_task( list, task_status ):
#    task_uncompleted = None
#    for task in list:
#        if task["completed"] == task_status:
#            task_uncompleted = task

#    return task_uncompleted

# print(uncompleted_task(tasks, False))

# correct answer

def uncompleted_task(list):
    tasks_uncompleted = []
    for task in list:
        if task["completed"] == False:
            tasks_uncompleted.append(task)
    return tasks_uncompleted

# 2. Print a list of completed tasks

def completed_task(list):
    tasks_completed = []
    for task in list:
        if task["completed"] == True:
            tasks_completed.append(task)
    return tasks_completed

# 3. Print a list of all task descriptions

def print_task_descriptions(list):
    for task in list:
        print(task["description"])

# 4. Print a list of tasks where time_taken is at least a given time

def get_tasks_taking_longer_than(list, time):
    tasks = []
    for task in list:
        if task["time_taken"] >= time:
            tasks.append(task)
    return tasks

print(get_tasks_taking_longer_than(tasks, 10))

# 5. Print any task with a given description

def get_task_with_description(list, description):
    for task in list:
        if task["description"] == description:
            return task
    return "Task Not Found"

def print_task(task):
    print(f'Description: { task["description"] }')
    print(f'Status: { "Completed" if task["completed"] else "Incomplete"}')
    print(f'Time Taken: {task["time_taken"]} mins')

def print_list(list):
    for task in list:
        print_task(task)

# 6. Given a description update that task to mark it as complete.

def mark_task_complete(description):
    task = get_task_with_description(description)
    task["completed"] = True

# 7. Add a task to the list
# create
def create_task(description, time_taken):
    task = {}
    task["description"] = description
    task["completed"] = False
    task["time_taken"] = time_taken

    return task

# add
def add_to_list (list, task):
    list.append(task)
