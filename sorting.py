sequence = [9,3,5,7,6,1,7,2,3,4,5]

def bubblesort(sequence=[]):
    index = len(sequence) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, index):

            if sequence[i] > sequence[i + 1]:
                sorted = False
                sequence[i], sequence[i + 1] = sequence[i + 1], sequence[i]

    return sequence

def selectionsort(sequence=[]):
    if len(sequence) <= 1:
        return sequence

    min_position = 0
    min = sequence[min_position]

    for i in range(1,len(sequence)):
        if sequence[i] < min:
            min = sequence[i]
            min_position = i

    return [sequence.pop(min_position)] + selectionsort(sequence)

def insertionsort(sequence=[]):

    def sort_sorted(sorted_list):

        if len(sorted_list) == 1:
            return sorted_list

        to_sort_index = len(sorted_list) - 1
        to_sort = sorted_list[to_sort_index]

        for i in range(len(sorted_list) - 1, -1, -1):
            if to_sort < sorted_list[i]:

                sorted_list[to_sort_index], sorted_list[i] = sorted_list[i], sorted_list[to_sort_index]

                to_sort_index = i

        return sorted_list

    if len(sequence) <= 1:
        return sequence

    sorted = [sequence.pop(0)]

    for i in range(0, len(sequence)):
        sorted.append(sequence.pop(0))
        sorted = sort_sorted(sorted)

    return sorted

def quicksort(sequence=[]):
    if len(sequence) <= 1:
        return sequence

    pivot = sequence.pop()

    # More elegant but it's O(2n)
    lower = [x for x in sequence if x <= pivot]
    greater = [x for x in sequence if pivot < x]

    return quicksort(lower) + [pivot] + quicksort(greater)
