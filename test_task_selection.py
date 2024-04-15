# Selection of Test Task from the previous workload signature

def main():
    MAX = 256
    input_data = [[0, 0] for _ in range(MAX)]
    output_data = [[0, 0] for _ in range(MAX)]
    k = 0

    # get the number of elements from the user
    n = int(input("Enter the number of elements: "))

    # get the array entries from the user
    print("Enter your array entries:")
    for i in range(n):
        input_data[i][0] = int(input("Data[{}]: ".format(i)))
        input_data[i][1] = 0

    # store the unique elements and its frequency in output array
    for i in range(n):
        if input_data[i][1]:
            continue
        count = 1
        for j in range(i + 1, n):
            if input_data[i][0] == input_data[j][0]:
                input_data[j][1] = 1
                count += 1

        output_data[k][0] = input_data[i][0]
        output_data[k][1] = count
        k += 1

    n = k

    # print the data and its frequency in output array
    print("Array Elements and its frequency:")
    print(" Data   Frequency")
    for i in range(n):
        print("   {}     {}".format(output_data[i][0], output_data[i][1]))

    # sort the data in output array based on frequencies
    for i in range(n - 1):
        temp = output_data[i][1]
        for j in range(i + 1, n):
            if temp < output_data[j][1]:
                temp = output_data[j][1]
                output_data[j][1], output_data[i][1] = output_data[i][1], temp
                temp = output_data[j][0]
                output_data[j][0], output_data[i][0] = output_data[i][0], temp

    # print the sorted data in output array
    print("\nSorted Array Elements based on their frequency:")
    print(" Data   Frequency")
    for i in range(n):
        print("   {}    {}    ".format(output_data[i][0], output_data[i][1]))


if __name__ == "__main__":
    main()
