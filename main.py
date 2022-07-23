
def twoNumberSum(array, targetSum):
    # Write your code here.

    # find the length of the list, into variable arrayLength
    arrayLength = len(array)
    lastIndex = arrayLength - 1

    # list indexed from 0 to (arrayLength-1) = from 0 to lastIndex

    # description says it's a non-empty array
    # if the length of the list is 1, return an empty list

    if arrayLength == 1:
        returnArray = []
        return returnArray

    # write a second function that creates an array from the two indexes passed to it ?
    #

    # else continue, we have a list of size 2 or more
    # initialize a variable to sumNotfound is false
    targetSumFound = False

    # sort the list
    # not necessary to do this unless I have some efficiency built into this somehow
    # array.sort()   # changes the array, puts the integers in sorted order

    leftIndex = 0  # initialize to the first element
    # rightIndex = 1 # initialize to the second element

    while not targetSumFound and leftIndex < lastIndex:
        # check pairs of numbers, comparing their sum to the targetSum
        # if they are the same, set targetSumFound to True

        rightIndex = leftIndex + 1

        # compare pairs of numbers, comparing leftIndex to leftIndex + rightIndex
        while not targetSumFound and rightIndex <= lastIndex:
            print("left index is: ", leftIndex, "right index is: ", rightIndex)
            testSum = array[leftIndex] + array[rightIndex]
            if testSum == targetSum:
                targetSumFound = True
            else:
                rightIndex += 1

        # all pairs with element leftIndex have been checked,
        # so increment leftIndex
        if not targetSumFound:
            leftIndex += 1

    # if targetSumFound, then return an array of the values at left and right index
    # else return an empty array

    if targetSumFound:
        returnArray = []
        returnArray.append(array[leftIndex])
        returnArray.append(array[rightIndex])
        return returnArray
    else:
        returnArray = []
        return returnArray
    #
    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
