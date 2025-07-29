class Vault:
    def __init__(self, vang=0, bac=0, dong=0):
        self.vang = vang
        self.bac = bac
        self.dong = dong

    def __str__(self):
        return f"{self.vang} vang, {self.bac} bac, {self.dong} dong"

#use __add__ to add other similar variable (2 different Vault)
# without having to write code to add many vaults( can just use 'other')
    def __add__(self, other):
        vang = self.vang + other.vang
        bac = self.bac + other.bac
        dong = self.dong + other.dong
        # then return new function with new added variebles
        return Vault(vang, bac, dong)

Harry = Vault(10,5,2)
print(Harry)
Vu = Vault(2,3,5)
print(Vu)
total = Harry + Vu
print(total)
