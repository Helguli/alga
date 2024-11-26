def Negyzet(x):
    return x*x

def NegyzetDekoralo(fuggveny):
    def Csomagolo(x):
        if x > 0:
            return fuggveny(x)
        else:
            return -fuggveny(x)
    return Csomagolo

dekoraltNegyzet= NegyzetDekoralo(Negyzet)
print(dekoraltNegyzet(10))
print(dekoraltNegyzet(-10))

