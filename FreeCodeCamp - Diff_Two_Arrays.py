#Diff Two Arrays
#Compare two arrays and return a new array with any items only found in one of the two given arrays, but not both. 
#In other words, return the symmetric difference of the two arrays.
#Note: You can return the array with its elements in any order.

def main():
    result = diff_array([1, 2, 3, 5], [1, 2, 3, 4, 5])
    print(result)


def diff_array(arr1, arr2):
    arr3 = []

    for x in arr1:
        if x not in arr2:
            arr3.append(x)

    for y in arr2:
        if y not in arr1:
            arr3.append(y)
    
    return arr3


if __name__ == "__main__":
    main()
