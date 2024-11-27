class Queue:
    def __init__(self, length):
        self.RP = 0
        self.FP = 0
        self.arr = []
        self.length = length
        for i in range(self.length):
            self.arr.append(None)

    def push(self, val):
        if self.arr.count(None) == 0:
            return IndexError("list is full")
        else:
            self.RP = self.RP % self.length
            self.arr[self.RP] = val
            self.RP += 1
            return 0

    def pop(self):
        if self.RP == self.FP:
            return IndexError("list is already empty")
        else:
            temp = self.arr[self.FP]
            self.arr[self.FP] = None
            self.FP += 1
            self.FP = self.FP % self.length
            return temp

    def show(self):
        print(self.arr)
        
q1 = Queue(8)
print(q1.push(3))
print(q1.push(3))
print(q1.push(3))
print(q1.push(3))
print(q1.push(3))
print(q1.push(3))
print(q1.push(3))
q1.push(4)
q1.pop()
q1.pop()
q1.show()
q1.push(5)
q1.push(2)
q1.push(1)
q1.show()