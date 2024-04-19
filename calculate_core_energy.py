# Calculation of Core Energy with Sample data

core_count = 5  # Sample value for the number of cores
Q_local = [
    {'core': 0, 'energy': 10.5},
    {'core': 1, 'energy': 8.2},
    {'core': 2, 'energy': 12.3},
    {'core': 0, 'energy': 9.7},
    {'core': 3, 'energy': 11.1},
    {'core': 2, 'energy': 7.1}
]

# Define job_entry structure
job_entry = {
    'core': 0,  # Sample initial value
    'energy': 0.0  # Sample initial value
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

# Calculate and print the sum of energies for each core
energies = sum_core_energies(Q_local)
for core, energy in enumerate(energies):
    print(f"Energy for Core {core}: {energy}")
