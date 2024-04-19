#Accomodation of user job and test task to core from local queue

# Define job_accommodation structure
job_accommodation = {
    'core': 0,  # Sample initial values
    'release_time': 0,  # Sample initial values
    'execution_time': 0,  # Sample initial values
    'period': 0,  # Sample initial values
    'deadline': 0,  # Sample initial values
    'completion_time': 0  # Sample initial values
}

# Sample data for job_accommodation
job_accommodation_to_core = [
    {'core': 0, 'release_time': 0, 'execution_time': 5, 'period': 20, 'deadline': 15, 'completion_time': 0},
    {'core': 1, 'release_time': 2, 'execution_time': 3, 'period': 25, 'deadline': 18, 'completion_time': 0},
    {'core': 2, 'release_time': 4, 'execution_time': 6, 'period': 30, 'deadline': 22, 'completion_time': 0}
]

# Define core_idle_time dictionary
core_idle_time = {
    0: {'idle_time': 0},  # Sample initial values for core 0
    1: {'idle_time': 0},  # Sample initial values for core 1
    2: {'idle_time': 0}   # Sample initial values for core 2
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

# Sample data for test_task_accommodation
test_task_accommodation_to_core = [
    {'core': 0, 'release_time': 1, 'execution_time': 4, 'period': 15, 'completion_time': 0},
    {'core': 1, 'release_time': 3, 'execution_time': 2, 'period': 20, 'completion_time': 0},
    {'core': 2, 'release_time': 5, 'execution_time': 3, 'period': 25, 'completion_time': 0}
]

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

# Testing the functions
job_assigned, assigned_core = job_local_queue_to_core(job_accommodation_to_core)
print("Job assigned to core:", job_assigned)
print("Assigned core:", assigned_core)

test_task_assigned, assigned_core = test_task_local_queue_to_core(test_task_accommodation_to_core)
print("Test task assigned to core:", test_task_assigned)
print("Assigned core:", assigned_core)
