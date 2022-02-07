# OOP Multiple inheritance Program

class Father:
    father_name = "Shiva"

    def father(self):
        print("Father_Name:", self.father_name)


class Mother:
    mother_name = "Gora"

    def mother(self):
        print("Mother_Name:", self.mother_name)


class Son(Father, Mother):
    def parent(self):
        print("Father name:", self.father_name)
        print("Father name:", self.mother_name)


obj = Son()
obj.father()
obj.mother()
obj.parent()
