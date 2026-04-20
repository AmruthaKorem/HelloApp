n = int(input())
nums = list(map(int, input().split()))

count = 0

for i in range(1, n):
    if nums[i] > nums[i - 1]:
        count += 1

print(count)

