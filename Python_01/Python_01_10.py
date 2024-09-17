a = 10 # 'a' szám beolvasása a billentyűzetről
b = 20 # 'b' szám beolvasása a billentyűzetről

if b > a:
  print("Az összhasonlítás eredménye: ",b," nagyobb, mint ",a,)

else:
  print("Az összhasonlítás eredménye: ",a," nagyobb, mint ",b)

# rövid kiírás
print(a," nagyobb, mint ",b) if a > b else print("egyenlőek") if a == b else print(b," nagyobb, mint ",a)

