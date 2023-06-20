def LinearSearch(arr,n,k):

  for i in range(0, n):

       if (arr[i] == k):

            return i

  return -1

arr=[2,4,5,8,0]

k=5

n=len(arr)

res=LinearSearch(arr,n,k)

print(res)
