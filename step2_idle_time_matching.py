#Compare idle time-core map table with release times of user jobs to find suitable cores for allocation of jobs and 
# Process test tasks for designated cores  

# Define job_matching structure
job_matching = {
    'core': 0,  # Sample initial values
    'release_time': 0,  # Sample initial values
    'execution_time': 0,  # Sample initial values
    'power_level': 0  # Sample initial values
}

# Define core_idle_time dictionary
core_idle_time = {
    'idle_time': 0  # Sample initial values
}

# Define core_number list
core_number = []

def job_release_time_idle_core_time(idle_time_matching):
    job_energy = {}  # Dictionary to store job energies
    job_number = None  # Variable to store the job with matching release time
    core_number = None  # Variable to store the core number

    for job in idle_time_matching:
        if job['release_time'] == core_idle_time[job['core']]['idle_time']:
            job_energy[job['core']] = job['execution_time'] * job['power_level']
            core_number = job['core']
            job_number = job

    return core_number, job_number, job_energy

# Define test_task_matching structure
test_task_matching = {
    'core': 0,  # Sample initial values
    'release_time': 0,  # Sample initial values
    'execution_time': 0  # Sample initial values
}

# Define test_task_entry list
test_task_entry = []

# Define idle_time dictionary
idle_time = {}

def test_task_to_designated_core(test_task_entry):
    test_task_execution_time = {}  # Dictionary to store test task execution times

    for test_task in test_task_entry:
        if test_task['release_time'] == core_idle_time[test_task['core']]['idle_time']:
            test_task_execution_time[test_task['core']] = test_task['execution_time']
            idle_time[test_task['core']] = core_idle_time[test_task['core']]['idle_time']

    return test_task_execution_time, idle_time
