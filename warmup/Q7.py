old=float(input())
percent=int(input())
if old<10:
  new=(old/100)*(100-percent)
  if new<1:
    print("${:.2f}".format(old))
  elif new>=1:
    print("${:.2f}".format(new))
elif old>=10:
  new=(old/100)*(100+percent)
  if new>100:
    print("${:.2f}".format(old))
  elif new<=100:
    print("${:.2f}".format(new))
