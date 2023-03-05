a = input()

b=0
c=0
d=0

for e in a:
  if e == "I":
    b += 1
  elif e == "M":
    c += 1
  elif e == "C":
    d += 1
    
if b<2:
  print("I")
elif c<1:
  print("M")
elif d<3:
  print("C")
else:
  print("W")
     
