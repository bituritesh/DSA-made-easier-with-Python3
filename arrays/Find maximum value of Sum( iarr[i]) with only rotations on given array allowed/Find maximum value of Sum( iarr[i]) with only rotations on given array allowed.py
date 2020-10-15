#When the array is rotated in RIGHT order(clockwise Rotate)
#sum_i = sum_(i-1) + summation of all elements in the array(a[0] + a[1] + ... + a[n-2] + a[n-1]) -n*a[n-i]
#When the array is rotated in LEFT order(anti-clockwise Rotate)
#sum_i = sum_(i-1) - summation of all elements in the array(a[0] + a[1] + ... + a[n-2] + a[n-1]) + n*a[i-1]

def SumOfElementsInArray(a,n):
    sum=0
    for i in range(0,n):
        sum+=a[i] # we can use sum() an inbuilt python function to do the same
    return sum
def MAxSum_RIGHT_RotatedArray(a,ElementSUM,n):
    previous_sum=0
    for i in range(0,n):
        previous_sum += i*a[i]
    Max_Sum_value=0
    for i in range(1,n):
        i_rotation_sum = previous_sum + ElementSUM - n*a[n-i]
        if previous_sum<i_rotation_sum:
            Max_Sum_value=i_rotation_sum
        previous_sum=   i_rotation_sum
    return Max_Sum_value
def MAxSum_LEFT_RotatedArray(a,ElementSUM,n):
    previous_sum=0
    for i in range(0,n):
        previous_sum += i*a[i]
    Max_Sum_value=0
    for i in range(1,n):
        i_rotation_sum = previous_sum - ElementSUM + n*a[i-1]
        if previous_sum<i_rotation_sum:
            Max_Sum_value=i_rotation_sum
        previous_sum=   i_rotation_sum
    return Max_Sum_value
n=int(input('enter the size of the array'))
arr=list(map(int,input().split(' ')[:n]))#slicing method it takes only up to n even if user enters more than N numbers
Element_sum=SumOfElementsInArray(arr,n)
print('Maximum sum in a right rotated(clockwise) array')
print(MAxSum_RIGHT_RotatedArray(arr,Element_sum,n))
print('Maximum sum in a left rotated(anti-clockwise) array')
print(MAxSum_LEFT_RotatedArray(arr,Element_sum,n))
