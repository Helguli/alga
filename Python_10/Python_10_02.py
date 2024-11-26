import os
def Fuggveny():
    def f():
        print("Ez a mondat egy függvény által létrehozott függvényből van.")
    return f

os.system('cls')
ujFuggveny=Fuggveny()
ujFuggveny()
    
Fuggveny()()   # ez ugyanazt eredményezi

