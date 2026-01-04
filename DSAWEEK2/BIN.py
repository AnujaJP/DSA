def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = int((low + high)/2)
        guess = list[mid]
        if guess == item:
            return mid
        if item > guess:
            low = mid + 1
        else:
            high = mid - 1
    return None
    
    
nos = [1,3,5,7,9] 
print(binary_search(nos, 5)) 
print(binary_search(nos, 11)) 