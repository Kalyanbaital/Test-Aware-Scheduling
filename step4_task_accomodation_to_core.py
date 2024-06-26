#Assign selected user jobs and K test tasks from local queue to cores maintaining constraints

# Define job_accommodation structure
job_accommodation = {
    'core': 0,  # Sample initial values
    'release_time': 0,  # Sample initial values
    'execution_time': 0,  # Sample initial values
    'period': 0,  # Sample initial values
    'deadline': 0,  # Sample initial values
    'completion_time': 0  # Sample initial values
}

# Define core_idle_time dictionary
core_idle_time = {
    'idle_time': 0  # Sample initial values
}

def job_local_queue_to_core(job_accommodation_to_core):
    job_number = None  # Variable to store the job with matching release time
    core_number = None  # Variable to store the core number

    for job in job_accommodation_to_core:
        if job['release_time'] == core_idle_time[job['core']]['idle_time']:
            job['completion_time'] = job['release_time'] + job['execution_time']
            if job['completion_time'] < job['period'] and job['completion_time'] < job['deadline']:
                # Job accommodated to the core
                core_number = job['core']
                job_number = job

    return job_number, core_number

# Define test_task_accommodation structure
test_task_accommodation = {
    'core': 0,  # Sample initial values
    'release_time': 0,  # Sample initial values
    'execution_time': 0,  # Sample initial values
    'period': 0,  # Sample initial values
    'completion_time': 0  # Sample initial values
}

# Define test_task_accommodation_to_core list
test_task_accommodation_to_core = []

def test_task_local_queue_to_core(test_task_accommodation_to_core):
    test_task_number = None  # Variable to store the test task with matching release time
    core_number = None  # Variable to store the core number

    for test_task in test_task_accommodation_to_core:
        if test_task['release_time'] == core_idle_time[test_task['core']]['idle_time']:
            test_task['completion_time'] = test_task['release_time'] + test_task['execution_time']
            if test_task['completion_time'] < test_task['period']:
                # Test task accommodated to the core
                core_number = test_task['core']
                test_task_number = test_task

    return test_task_number, core_number
