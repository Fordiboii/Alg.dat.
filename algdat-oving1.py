#!/usr/bin/python3

from sys import stdin


def sort_list(A):
    for i in range(1, len(arr)):
        key = arr[i]
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and key < arr[j] :
                A[j+1] = A[j]
                j -= 1
        A[j+1] = key
    print(A)
    return A


def find(A, lower, upper):
    # NOTICE: The result must be returned.
    # SKRIV DIN KODE HER
    pass

def main():
    input_list = []
    for x in stdin.readline().split():
        input_list.append(int(x))

    sorted_list = sort_list(input_list)

    for line in stdin:
        word = line.split()
        minimum = int(word[0])
        maximum = int(word[1])
        result = find(sorted_list, minimum, maximum)
        print(str(result[0]) + " " + str(result[1]))


if __name__ == "__main__":
    main()