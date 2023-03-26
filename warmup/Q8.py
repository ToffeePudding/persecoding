original = [10, 10, 10, 10, 10]
for i in range(5):
    sweet = int(input())
    next_friend = (i + 1) % 5
    original[next_friend] += sweet
    original[i] -= sweet

max_sweets = max(original)
print(max_sweets)
