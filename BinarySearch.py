def binarysearch(arr,lo,hi,k):
  while lo<=hi:
    mid=(hi-lo)//2
    if arr[mid]==k:
      return mid
    elif arr[mid]<mid:
      return binarysearch(arr,mid+1,hi,k)
    else:
      return binarysearch(arr,lo,mid-1,k)
  return -1

