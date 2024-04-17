# Selection of Test Task from the previous workload signature

def main():
    MAX = 256
    input_data = [[0, 0] for _ in range(MAX)]
    output_data = [[0, 0] for _ in range(MAX)]
    k = 0

    # get the number of tasks from the user
    job_list = int(input("Enter the number of tasks: "))

    # get the task entries from the user
    print("Enter your task entries:")
    for i in range(job_list):
        input_data[i][0] = int(input("Task[{}]: ".format(i)))
        input_data[i][1] = 0

    # store the unique task and its frequency in output array
    for i in range(job_list):
        if input_data[i][1]:
            continue
        count = 1
        for j in range(i + 1, job_list):
            if input_data[i][0] == input_data[j][0]:
                input_data[j][1] = 1
                count += 1

        output_data[k][0] = input_data[i][0]
        output_data[k][1] = count
        k += 1

    job_list = k

    # print the task and its frequency in output array
    print("Tasks and its frequency:")
    print(" Task   Frequency")
    for i in range(job_list):
        print("   {}     {}".format(output_data[i][0], output_data[i][1]))

    # sort the task in output array based on frequencies
    for i in range(job_list - 1):
        temp = output_data[i][1]
        for j in range(i + 1, job_list):
            if temp < output_data[j][1]:
                temp = output_data[j][1]
                output_data[j][1], output_data[i][1] = output_data[i][1], temp
                temp = output_data[j][0]
                output_data[j][0], output_data[i][0] = output_data[i][0], temp

    # print the sorted task in output array
    print("\nSorted Tasks based on their frequency:")
    print(" Task   Frequency")
    for i in range(job_list):
        print("   {}    {}    ".format(output_data[i][0], output_data[i][1]))


    # select the number of test tasks
    test_task = int(input("Enter the number of test tasks to be selected: "))


    # print the test task from the highest workload (i.e. maximum frequency tasks) of the previous test window
    print("\nTest Tasks List:")
    print(" Task   Frequency")
    for i in range(test_task):
        if test_task<job_list:
            print("   {}    {}    ".format(output_data[i][0], output_data[i][1]))

if __name__ == "__main__":
    main()
