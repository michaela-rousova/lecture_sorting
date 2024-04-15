import os
import csv


def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, mode="r", newline="\n") as csv_file:
        reader = csv.DictReader(csv_file)
        data = {}
        iter = 0
        for row in reader:
            for key, value in row.items():
                if iter == 0:
                    data[key] = [int(value)]
                else:
                    data[key].append(int(value))
            iter = iter + 1
        return data

def selection_sort(rada, smer='rostouci'):
    n = len(rada)
    for j in range(n):
        min_idx = j
        for num_idx in range(j + 1, n):
            if 'rostouci' in smer:
                if rada[num_idx] < rada[min_idx]:
                    min_idx = num_idx
            if 'klesajici' in smer:
                if rada[num_idx] < rada[min_idx]:
                    min_idx = num_idx
        rada[j], rada[min_idx] =\
            rada[min_idx], rada[j]
    return rada

def bubble_sort(rada):
    n = len(rada)
    for j in range(n - 1):
        for num_idx in range(n - j - 1):
            if rada[num_idx] > rada[num_idx+1]:
                rada[num_idx], rada[num_idx+1] =\
                    rada[num_idx + 1], rada[num_idx]
    return rada


def main():
    pass
    # data = read_data("numbers.csv")
    # return data
    rada = data["series_1"]
    # selection = selection_sort(data["series_1"])
    # return selection
    bubble = bubble_sort(rada)
    return bubble


if __name__ == '__main__':
    data = read_data("numbers.csv")
    print(data)
    selection = selection_sort(data["series_1"])
    print(selection)
    main()
