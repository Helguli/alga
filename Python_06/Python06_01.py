class Node:                  # Csomópont osztály
    def __init__(self,data): # ez a speciális metódus a konstruktor
        self.data=data       # a self paraméter az osztály aktuális példányára való hivatkozás
        self.next=None       # a csomóponthoz tartozó adatot a data adattag tartalmazza
                             # a next adattag a következő csomópont címét tartalmazza, kezdetben
                             # "nem mutat sehova"
    def __str__(self):
        return str(self.data) # a csomópont sztringreprezentációja csak az adatrész
                              # sztringreprezentációja

class LinkedList:           # LáncoltLista osztály
    def __init__(self):     # konstruktor
        self.head=None      # a lista kezdetben üres, a fej "nem mutat sehova"

    def insertAtBeginning(self,data):   # ElejéreBeszúr művelet

    def insertAtEnd(self,data):     # VégéreBeszúr művelet

    def insertAtPosition(self,data,n): # HelyreBeszúr művelet: az n. pozícióra szúrja be az elemet

    def removeLastNode(self):          # UtolsótTöröl művelet

    def removeFirstNode(self):

    def insertAtPosition(self,data,n): # HelyreBeszúr művelet: az n. pozícióra szúrja be az elemet

    def printList(self):       # Bejár művelet; az összes adat kiírása
