
# Task scheduling programme with sample data (finding idle time of the core, selection of matching core, and forwarding the jobs to the selected cores)

import math

def main():
    """
    Main function to demonstrate idle cores and their corresponding idle times.
    """
    # Initialize a 2D list with zeros to store idle times of cores
    I = [[0]*10 for _ in range(5)]
    
    # List to iterate through idle times
    k = 0

    # Periods of tasks
    P = [
        [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],
        [4, 8, 12, 16, 20, 24, 28, 32, 36, 40],
        [6, 12, 18, 24, 30, 36, 42, 48, 54, 60],
        [8, 16, 24, 32, 40, 48, 56, 64, 72, 80],
        [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    ]

    # Execution times of tasks
    e = [
        [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],
        [2, 6, 10, 14, 18, 22, 26, 30, 34, 38],
        [3, 9, 15, 21, 27, 33, 39, 45, 51, 57],
        [4, 12, 20, 28, 36, 44, 52, 60, 68, 76],
        [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]
    ]

    # Iterate through each core
    for T in range(5):
        print(f"\t\nIdle core is Core [{T+1}] and Idle time at following ms:\n")

        # Iterate through each time slot
        for k in range(10):
            # Check if execution time is less than period
            if e[T][k] < P[T][k]:
                I[T][k] = e[T][k]
                print(f"{I[T][k]}\t")

    print("\n\nComplete Idle time at following ms:\n")
    for T in range(5):
        for k in range(10):
            print(f"{I[T][k]}\t", end="")
    print()


def period_core():
    """
    Function to print period of each core.
    """
    # Periods of tasks
    P = [
        [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],
        [4, 8, 12, 16, 20, 24, 28, 32, 36, 40],
        [6, 12, 18, 24, 30, 36, 42, 48, 54, 60],
        [8, 16, 24, 32, 40, 48, 56, 64, 72, 80],
        [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    ]

    # Iterate through each core
    for i in range(5):
        print(f"\nCore Number: C[{i+1}] and Period is at following ms:\n\n")
        for j in range(10):
            print(f"{P[i][j]}\t", end="")
        print()


def pseudo_release():
    """
    Function to calculate pseudo release and deadline times of jobs.
    """
    p = [2, 30, 10, 21, 50, 42, 51, 40, 92, 50]
    e = [1, 10, 2, 3, 5, 3, 3, 2, 4, 2]
    w = [1/2, 10/30, 2/10, 3/21, 5/50, 3/42, 3/51, 2/40, 4/92, 2/50]

    r = [[0] * 5 for _ in range(10)]
    d = [[0] * 5 for _ in range(10)]

    # Calculate release and deadline times for each job
    for i in range(10):
        for j in range(5):
            r[i][j] = math.floor((p[i] - 1) / w[i])
            d[i][j] = math.ceil((p[i] / w[i]) - 1)

    # Print release times
    for T in range(10):
        print(f"\nRelease Time of Jobs for Task : {T+1} \n")
        for k in range(5):
            print(f"\t\Release time of Job [{k+1}] at {r[T][k]} ms\n")

    # Print deadline times
    for TT in range(10):
        print(f"\nDeadline of Jobs for Task : {TT+1} \n")
        for kk in range(5):
            print(f"\t\Deadline of Job [{kk+1}] at {d[TT][kk]} ms\n")


def time_core_release():
    """
    Function to match release times of jobs with idle times of cores.
    """
    R = [
        [0, 2, 4, 6, 8],
        [0, 3, 6, 9, 12],
        [0, 5, 10, 15, 20],
        [0, 6, 13, 20, 27],
        [0, 10, 20, 30, 40],
        [0, 13, 27, 41, 55],
        [0, 16, 33, 50, 67],
        [0, 20, 40, 60, 80],
        [0, 22, 45, 68, 90],
        [0, 25, 50, 75, 100]
    ]

    D = [
        [1, 3, 5, 7, 9],
        [3, 6, 9, 12, 15],
        [4, 9, 14, 19, 24],
        [6, 13, 20, 27, 34],
        [9, 19, 29, 39, 49],
        [13, 27, 41, 55, 69],
        [16, 33, 50, 67, 84],
        [19, 39, 59, 79, 99],
        [22, 45, 68, 90, 113],
        [24, 49, 74, 99, 124]
    ]

    I = [
        [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],
        [2, 6, 10, 14, 18, 22, 26, 30, 34, 38],
        [3, 9, 15, 21, 27, 33, 39, 45, 51, 57],
        [4, 12, 20, 28, 36, 44, 52, 60, 68, 76],
        [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]
    ]

    # Iterate through each job and core to match their times
    for row1 in range(10):
        for column1 in range(5):
            for row2 in range(5):
                for column2 in range(10):
                    if I[row2][column2] == R[row1][column1]:
                        print(f"\nRelease time {I[row2][column2]} ms of Job J[{row1+1}][{column1+1}] matches the Idle time {I[row2][column2]} ms of Core {row2+1}")
                        #print()


def localqueue_tocore():
    """
    Function to accomodation of selected job to selecte core for execution.
    """
    # Assume Job J [3][4] (Release time 15 ms, Deadline 19 ms) from local queue of C1 needs to be assigned to Core C1 (Idle time 15 ms)
    # Assume Execution time of J[3][4] is 2/5 ms i.e 0.4 ms as the Job is 1/5th of the Task 3 (execution time 2)
    C1p = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]    # period
    C1i = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]    # idle time
    Rj = 15
    Ej = 0.4
    Dj = 19.0
    Total_Time = Rj + Ej

    for i in range(10):
        if Rj == C1i[i] and (Total_Time < C1p[i] and Total_Time < Dj):
            print("\n\nAssigned the Job J to the Core C1 Successfully at {} ms and will be completed before next period {} ms!!".format(C1i[i], C1p[i]))


if __name__ == "__main__":
    # Call main function
    main()
    # Call other functions
    period_core()
    pseudo_release()
    time_core_release()
    localqueue_tocore()
