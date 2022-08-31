class AlternateList_comp():
    def __init__(self):
        self.values = []
        self._set = True

    def add_item(self, value):
        if self._set:
            self.values.append(value)
            self._set = False
        else:
            self._set = True

    def add_collection(self, values):
        for value in values:
            self.add_item(value)


class AlternateList_inh(list):
    def __init__(self):
        super().__init__()
        self.set = True

    def add_item(self, value):
        if self.set:
            self.append(value)
            self.set = False
        else:
            self.set = True

    def add_collection(self, values):
        for value in values:
            self.add_item(value)


obj1_comp = AlternateList_comp()
obj2_comp = AlternateList_comp()
obj1_inh = AlternateList_inh()
obj2_inh = AlternateList_inh()
n = 21
for i in range(1, n):
    obj1_comp.add_item(i)
    obj1_inh.add_item(i)

obj2_comp.add_collection(list(range(1, n)))
obj2_inh.add_collection(list(range(1, n)))

print(obj1_comp.values)
print(obj2_comp.values)
print(obj1_inh)
print(obj2_inh)
