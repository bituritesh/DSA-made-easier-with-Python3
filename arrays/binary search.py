# Iterative Binary Search Function
# It returns index of x in given array arr if present, 
# else returns -1 
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:

        mid = (high + low) // 2

        # Check if x is present at mid 
        if arr[mid] < x:
            low = mid + 1

        # If x is greater, ignore left half 
        elif arr[mid] > x:
            high = mid - 1

        # If x is smaller, ignore right half 
        else:
            return mid

            # If we reach here, then the element was not present
    return -1


# Test array 
arr = [ 2, 3, 4, 10, 40, 45, 50 ]
x = 5

# Function call 
result = binary_search(arr, x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")

#time complexity T(n) = T(n/2) + c i.e. O(log n)
#Auxiliary Space: O(1) in case of iterative implementation.
# In case of recursive implementation, O(Logn) recursion call stack space.
