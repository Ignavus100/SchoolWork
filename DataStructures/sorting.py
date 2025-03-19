def numberBubble(arr):
    for n in range(len(arr) - 1, 0, -1):
        swapped = False  
        for i in range(n):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        if not swapped:
            break
    return arr

def nameBubble(arr):
    temparr = [tuple(ord(char) for char in name) for name in arr]  # Convert names to ASCII tuples

    for n in range(len(arr) - 1, 0, -1):
        swapped = False  
        for i in range(n):
            if temparr[i] > temparr[i + 1]:  # Compare tuples instead of single letters
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                temparr[i], temparr[i + 1] = temparr[i + 1], temparr[i]
                swapped = True
        if not swapped:
            break

    return arr  # Return sorted names

def numberMerge(arr):
    if len(arr) <= 1:
        return arr
    halfarr = len(arr) // 2
    firsthalf = numberMerge(arr[:halfarr])
    secondhalf = numberMerge(arr[halfarr:])

    finarr = []
    i, j = 0, 0

    # Merge the two sorted halves
    while i < len(firsthalf) and j < len(secondhalf):
        if firsthalf[i] < secondhalf[j]:
            finarr.append(firsthalf[i])
            i += 1
        else:
            finarr.append(secondhalf[j])
            j += 1

    # Add any remaining elements
    finarr.extend(firsthalf[i:])
    finarr.extend(secondhalf[j:])

    return finarr


def nameMerge(arr):
    if isinstance(arr[0], str):  # Check if the first element is a string
        arr = [tuple(ord(char) for char in i) for i in arr]  # Convert full string to tuple of ASCII values

    if len(arr) <= 1:
        return arr  # Base case for recursion

    halfarr = len(arr) // 2
    firsthalf = numberMerge(arr[:halfarr])  # Recursively sort the first half
    secondhalf = numberMerge(arr[halfarr:])  # Recursively sort the second half

    finarr = []
    i, j = 0, 0

    # Merge the two sorted halves
    while i < len(firsthalf) and j < len(secondhalf):
        if firsthalf[i] < secondhalf[j]:  # Tuple comparison maintains lexicographical order
            finarr.append(firsthalf[i])
            i += 1
        else:
            finarr.append(secondhalf[j])
            j += 1

    # Add any remaining elements
    finarr.extend(firsthalf[i:])
    finarr.extend(secondhalf[j:])

    return ["".join(chr(num) for num in item) for item in finarr]  # Convert back to strings



with open("names1000.txt", "r") as f:
    arr = f.readlines()  # Reads all lines into a list

print(nameMerge(arr) == nameBubble(arr))