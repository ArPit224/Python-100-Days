class SuperClass:
    
    def __init__(self):
        self.supVar = 12
        
    def SupMethod(self):
        print("This is super.")
        
class SubClass(SuperClass):
    
    def __init__(self):
        super().__init__()
        
    def SubMethod(self):
        
        super().SupMethod()
        print("This is Sub")
        
        
inheritClass = SubClass()

inheritClass.SubMethod()