class Operation:
    def __init__(self):
        self.nombre1 = 1
        self.nombre2 = 2
    
    def addition(self):
        print(f"Le résultat de : {self.nombre1} + {self.nombre2} est : {self.nombre1 + self.nombre2}")

operation1 = Operation()
operation1.addition()