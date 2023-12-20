class GrandFather:
    def __init__(self):
        self.name = " GrandFather"
        self._assets = 1000

class Father(GrandFather):
    def __init__(self):
        super().__init__()
        self.name = self.name + " Father"
        self._inharitedAssets = self._assets 
        self._purchasedAssets = 200
        self._totalAssets = self._inharitedAssets + self._purchasedAssets

class Child(Father):
    def __init__(self, name, assets):
        super().__init__()
        self.name = self.name + " " + name
        self.__inharitedAssets = self._totalAssets
        self.__purchasedAssets = assets
        self.totalAssets = self.__inharitedAssets + self.__purchasedAssets
    
    def displayData(self):
        print("Name: ", self.name)
        print("Assets: ", self._totalAssets)

obj = Child("Child",10000)
obj.displayData()