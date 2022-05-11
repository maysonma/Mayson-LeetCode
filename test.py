def shortest_window_sort(arr):
  # TODO: Write your code here
  if len(arr) <= 1:
    return 0
  l = 0
  r = len(arr) - 1
  while l < r:
    if arr[l] <= arr[l+1] and arr[l+1] <= arr[r]:
      l += 1
    elif arr[r] >= arr[r-1] and arr[r-1] >= arr[l]:
      r -= 1
    else:
      break


  for i in range(l+1, r):
    while l >= 0 and arr[l] > arr[i]:
      l -= 1
    while r < len(arr) and arr[r] < arr[i]:
      r += 1

  return r - l

if __name__ == "__main__":
  ans = shortest_window_sort([1, 2, 5, 3, 7, 10, 9, 12])
  print(ans)