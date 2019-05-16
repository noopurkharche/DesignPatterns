# Singleton Pattern in Python

class Singleton:
    # __ for name mangling to avoid naming collision
    __instance = None 
    
    # static access method returns the instance
    def getinstance():
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance
    
    # constructor
    def __init__(self):
        # if instance already there raise Exception as it is singleton class
        if Singleton.__instance != None:
            raise Exception("This is a Singleton Class")
        else:
            Singleton.__instance = self
# create instance
s = Singleton()
print(s)

s = Singleton.getinstance()
print(s)