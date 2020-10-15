#Given a sorted and rotated array, find if there is a pair with a given sum and count there presence
#enter sorted and rotated array in arr
#now we gonna use a technique that there will be 2 pointers L and R
#L will point to smallest element and R will point to largest element
'''
Below are the 2 cases for our approach
arr = [11, 15, 26, 38, 9, 10] sum =48
here L=9 and R=38
step 1:L+R=47<48
so L+R is lesser than expected sum then keep the R constant and forward L in rotational fashion
step 2: L=10 and R=38 sum=48 break and we print the pairs
find if there is a pair with a given sum which gives 16
arr=[11, 15, 6, 8, 9, 10]
L is 6 and R is 15
step 1: L+R=21 > 16
step2: R shifts backwards in rotational fashion R=11 and L remains same, R+L=17>16
step3: R shifts backwards in rotational fashion R=10 and L remains same,R+L=16 break and we print the pairs

to start this problem we need to locate the minimum element for which binary search is the best way
to find in sorted array
this problem is a special kind where the array is sorted but also rotated by right. I will explain you with various examples
**In rotated array the minimum element is the one whose previous value is greater than it.**
Ex 1
arr1=[11, 15, 6, 8, 9, 10]
here we find that the mid value=8 which is smaller than mid+1 but greater than mid-1,
that says the smaller no lies is left half
now arr1=[11, 15, 6, 8
now binary search again
mid_value=6 which is smaller than mid+1 but greater than mid-1 which satisfies our query
Ex 2
arr2=[11,12,14, 15,6, 8, 9, 10]
mid_value=6 which is smaller than mid+1 but greater than mid-1 which satisfies our query
Ex 3
arr3=[10, 11, 15, 16,17, 6, 8, 9]
mid_value=17 which is greater than mid+1 but greater than mid-1,
Ex 4
arr4=[11, 12, 0, 5, 6, 10] sum=17
output 2
a minimum element is the one whose previous value is greater than it, thats the unique thing we can find here.
All the values in the array is distinct and unique
now to check number of pairs which yields the sum for arr1=[11, 15, 6, 8, 9, 10]
when sum =16 number of pairs is 1
when sum =17 number of pairs is 2
'''
def minElementBinSearch(a,r):
    left=0
    right=r
    mid=left+(right-left)//2
    if a[mid-1]>a[mid]:
        min=a[mid]
        return min
    elif a[mid+1]<a[mid]:
        min=a[mid+1]
        return min
    else:
        right=mid-1
        return minElementBinSearch(arr,right)
def NoOfPairs(L,R,a,s):
    counter=0
    while L!=R:
        if a[L]+a[R]==s:
            counter+=1
            # The below condition is
            # required to be checked,
            # otherwise l and r will
            # cross each other and
            # loop will never terminate.
            R-=1
            if R<0:
                R=(n+R)%n
            if L==R:
                break
            L+=1
            if L==n:
                L=L-n
        elif a[L]+a[R]>s:
            R-=1
            if R<0:
                R=(n+R)%n
        else:
            L+=1
            if L==n:
                L=L-n
    return counter
n=int(input('enter the size of the array'))
arr=list(map(int,input().split(' ')[:n]))#slicing method it takes only up to n even if user enters more than N numbers
sum=17
L=minElementBinSearch(arr,n)
print(L)
L_index=arr.index(L)
R=arr[L_index-1]
R_index=L_index-1
K=NoOfPairs(L_index,R_index,arr,sum)
#now we run a loop till L meets R in a rotational manner

if K>0:
    print('Number of pairs for the sum {} is {}'.format(sum,K))
else:
    print('No pairs for the sum {} exists in the array'.format(sum))

'''
the code inside the while loop can be be replaced with this one, the above logic is used
for the ease of explanation
        while (l != r): 
            if arr[l] + arr[r] == x: 
                cnt += 1
                  
                # This condition is  
                # required to be checked,  
                # otherwise l and r will  
                # cross each other and  
                # loop will never terminate. 
                if l == (r - 1 + n) % n: 
                    return cnt 
                  
                l = (l + 1) % n 
                r = (r - 1 + n) % n 
              
            # If current pair sum  
            # is less, move to  
            # the higher sum side. 
            elif arr[l] + arr[r] < x: 
                l = (l + 1) % n 
              
            # If current pair sum  
            # is greater, move to  
            # the lower sum side. 
            else: 
                r = (n + r - 1) % n 
          
        return cnt 
'''
#do let me know the time and space complexity of the above program
