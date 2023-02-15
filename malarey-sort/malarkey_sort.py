def malarkey_sort(arr):
    '''
        input is an array of size n
        array contains unsorted numbers

        need to sort them: largest, smallest, 2nd largest, 2nd smallest


        [6,9,1,-15,100]

        [-15, 1, 6 , 9, 100]
                 sl


    '''
    arr.sort()
    res = []

    small, large = 0, len(arr) - 1

    while small < large:
        res.append(arr[large])
        res.append(arr[small])
        large -= 1
        small += 1

    if small == large:
        res.append(arr[small])
    return res
