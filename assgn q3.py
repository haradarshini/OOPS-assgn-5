class student:
    def set_name(self, name):
        self.__name = name
    def get_name(self):
        return self.__name
        
a = student()
a.set_name("lipsa")
print(a.get_name())
    
    