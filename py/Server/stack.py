class Stack:
    def __init__(self):
        self.items =[]

    def isNull(self):
        return self.items ==[]

    def add(self,item):
        self.items.append(item)

    def get(self):
        return self.items.pop(0)

    def insp(self):
        return self.items[len(self.items)-1]

    def length(self):
        return len(self.items)

    def toString(self):
        string=""
        for i in range(len(self.items)):
            string+=self.items[i]
        return string
