#Calculate idle times of cores for the time period Tp (Tp is the user defined time)

# Define core_entry structure
core_entry = {
    'core': 0,  # Sample initial values
    'period': 0,  # Sample initial values
    'execution_time': 0  # Sample initial values
}

# Define core_idle_time dictionary
core_idle_time = {
    'idle_time': 0  # Sample initial values
}

# Define core_number list
core_number = []

def idle_time_core(core_list):
    # Initialize idle_time dictionary
    idle_time = {}

    # Iterate through each job in the core_list
    for job in core_list:
        # Check if execution time is less than period
        if job['execution_time'] < job['period']:
            idle_time[job['core']] = job['period'] - job['execution_time']
        # Update core_number
        core_number.append(job['core'])

    # Return idle_time and core_number
    return idle_time, core_number
