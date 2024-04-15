#Calculate the energy of each core for selection of particular core if any job finds more than one core for scheduling

# Define job_entry structure
job_entry = {
    'core': 0,  # Sample initial values
    'energy': 0.0  # Sample initial values
}

# Define energies list
energies = [0.0] * core_count  # Assuming core_count is known

def sum_core_energies(Q_local):
    # Initialize energies list with zeros
    energies = [0.0] * core_count  # Assuming core_count is known

    # Iterate through each job in the local queue
    for job in Q_local:
        # Increment the energy for the corresponding core
        energies[job['core']] += job['energy']

    # Return the computed energies
    return energies
