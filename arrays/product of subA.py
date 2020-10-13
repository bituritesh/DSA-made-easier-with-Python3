'''Input : arr[] = {10, 3, 7}
Output : 30870
Here, subarrays are [10], [10, 3], [10, 3, 7], [3], [3, 7], [7]
Prodcuts are 10, 30, 210, 3, 21, 7
Product of all Subarrays = 27783000 '''

import array
arr = array.array('i', [1,2,3])

res=1
for i in range(0,len(arr)):
    prod =1
    for j in range(i,len(arr)):
        prod = prod * arr[j]
        res = res * prod
print(res)
