class Student:
    def __init__(self, nom, prenom, id_):
        self.__nom = nom
        self.__prenom = prenom
        self.__num_etudiants = id_
        self.__nbr_credits = 0
        self.__level = self.__studentEval()
    
    def setNom(self, nom):
        self.__nom = nom
    
    def setPrenom(self, prenom):
        self.__prenom = prenom
    
    def setNum_etudiants(self, num_etudiants):
        self.__num_etudiants = num_etudiants
    
    def getNom(self):
        print(f"L'étudiant se nomme {self.__nom}")
        return self.__nom
    
    def getPrenom(self):
        print(f"L'étudiant se prenomme {self.__prenom}")
        return self.__prenom
    
    def getNum_etudiants(self):
        print(f"Le numéro de l'étudiant est : {self.__num_etudiants}")
        return self.__num_etudiants
    
    def add_credits(self, credits):
        if credits > 0:
            self.__nbr_credits += credits
            self.__nbr_credits = self.__nbr_credits
            self.__level = self.__studentEval()
            return self.__nbr_credits
    
    def __studentEval(self):
        if self.__nbr_credits >= 90:
            return "Excellent"
        elif self.__nbr_credits >= 80:
            return "Très bien"
        elif self.__nbr_credits >= 70:
            return "Bien"
        elif self.__nbr_credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"
        
    def studentInfo(self):
        print(f"Nom : {self.__nom}\
              \nPrenom : {self.__prenom}\
              \nid : {self.__num_etudiants}\
              \nNiveau : {self.__level}")

John_doe = Student("Doe", "Jo", 150)
John_doe.getPrenom()
John_doe.getNom()
John_doe.getNum_etudiants()
John_doe.setPrenom("John")
John_doe.setNum_etudiants(145)
John_doe.add_credits(100)
John_doe.studentInfo()