#Select K number of test tasks with their resource requirements from the most common workload signature of the previous time period

# Define test_task_selection structure
test_task_selection = {
    'core': 0,  # Sample initial values
    'count': 0,  # Sample initial values
    'execution_time': 0  # Sample initial values
}

# Define job_list list
job_list = []

def find_test_task(test_window):
    count = {}  # Dictionary to store the count of jobs per core
    execution_time = 0  # Variable to store the execution time of the selected job
    test_task = None  # Variable to store the selected job
    core_number = None  # Variable to store the core number of the selected job

    # Count the occurrences of jobs in the test window
    for job in test_window:
        count[job['core']] = count.get(job['core'], 0) + 1

    # Iterate through each job in the job_list
    for job in job_list:
        temp = count.get(job, 0)
        count1 = count.get(job, 0) + 1
        if temp < count.get(job, 0) + 1:
            temp = count.get(job, 0) + 1
            count[job] = count
            count = temp
            execution_time = job['execution_time']
            test_task = job
            core_number = job['core']

    # Return the selected job, count, execution time, and core number
    return test_task, count, execution_time, core_number

