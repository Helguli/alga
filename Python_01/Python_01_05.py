a = '''Természetesen megadható
akár hosszabb szöveg is,
a python még ezt is szereti.
Dupla idézőjellel is működik és még sortöréseket is megtartja!'''

print(a)
print("18. karakter: ")  # 18. karakter kiírás
print("String részlet: ")  # írjuk ki az első sorból a mész stringrészletet
print("String részlet: ", a[-7:-3])  # negatív index, mi az eredmény?