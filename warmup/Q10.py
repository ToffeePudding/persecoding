list = [1,2.3,4,5,6,7,8,9]
x = int(input())
y = int(input())
n = int(input())
for i in range(n):
    top = list[:x]
    list = list[x:]
    
    bottom = list[-y:]
    list = list[:-y]
    
    new = top + bottom[::-1]
    list = new
    
print(list[0])
