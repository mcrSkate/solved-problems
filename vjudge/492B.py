def maxDiff(arr):
    diff = 0
    for i in range(len(arr)-1):
        if arr[i+1] - arr[i] > diff:
            diff = arr[i+1] - arr[i]
    return diff

parameters = list(map(int, input().split(" ")))
arr = list(map(int, input().split(" ")))
arr.sort()
print(max(max(arr[0], maxDiff(arr)/2), parameters[1]-arr.pop()))