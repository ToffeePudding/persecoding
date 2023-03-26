a = int(input())
b = (a//8)
c = (a%8)
if c <=4 and c!=0:
    print(8+8*b)
elif c == 0:
  	print(a)
else: 
    print((b+1)*8)
#doesnt work for T1, idk why but i give up
