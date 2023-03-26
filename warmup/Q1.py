amounts = []
for i in range(5):
    amounts.append(int(input()))
lost = int(input())

removed = amounts.pop(lost - 1)
total = sum(amounts)

print('${}'.format(total))
