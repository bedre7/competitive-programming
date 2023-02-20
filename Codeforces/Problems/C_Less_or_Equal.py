def solve():
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    nums.sort()

    if k == 0:  
        return 1 if nums[0] > 1 else -1
        
    if k == n:  return nums[-1]

    if nums[k] <= nums[k - 1]:
        return -1
    else:
        return nums[k - 1]

if __name__ == '__main__':
    print(solve())