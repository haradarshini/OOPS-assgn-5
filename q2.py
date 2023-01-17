class calculator:
    def __init__(self,n1,n2):
        self.n1 = n1
        self.n2 = n2
    def add (self):
        return self.n1 + self.n2
    def substract(self):
        return self.n2 - self.n1
    def multiply(self):
        return self. n1 * self.n2
    def divide (self):
        return self.n2 / self.n1
     
object = calculator(10,94)
print(object.add())
print(object.substract())
print(object.multiply())
print(object.divide())