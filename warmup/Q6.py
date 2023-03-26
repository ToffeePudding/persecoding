sum = 0
count = 0 
while True:
  number =int (input())
  if number>100:
    count += 1
  elif number<0:
    break
  else:
    sum += number
print(sum)
print(count)
