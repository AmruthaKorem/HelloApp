#method 1

n = int(input())
nums = list(map(int, input().split()))

freq = {}
for num in nums:
    freq[num] = freq.get(num, 0) + 1

count = 0
for value in freq.values():
    if value == 1:
        count += 1

print(count)



#method 2

freq = {}

# First loop: initialize all keys to 0
for num in nums:
    freq[num] = 0

# Second loop: count occurrences
for num in nums:
    freq[num] += 1

# Count numbers appearing once
count = 0
for key in freq:
    if freq[key] == 1:
        count += 1


