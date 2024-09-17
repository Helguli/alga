print("While ciklus használata",end=":")
i = 1  # egyszerű while ciklus
while i < 4:
  print(i,end=",")
  i += 1

print("\nbreak utasítás használata",end=":")
i = 1  # break utasítással
while i < 4:
  print(i,end=",")
  if i == 2:
    break
  i += 1

print("\ncontinue utasítás használata",end=":")
i = 0 # continue utasítással
while i < 4:
  i += 1
  if i == 2:
    continue
  print(i,end=",")

print("\nelse utasítás használata",end=":")
i = 1 # else utasítással
while i < 4:
    print(i,end=",")
    i += 1
else:
    print("i már nem kisebb, mint 4")

