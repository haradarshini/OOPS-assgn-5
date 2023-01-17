class point:
    def __init__(self, x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def sqSum(self):
        result = self.x**2 + self.y**2 + self.z**2
        return result
a = point(1,2,3)
print(a.sqSum())