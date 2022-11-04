class Residue:
    def __init__(self, num: int, mod: int):
        self.num = num % mod
        self.mod = mod
        
    def __str__(self) -> str:
        return f'{self.num} (mod {self.mod})'
    
    def __repr__(self) -> str:
        return f'Residue({self.num}, {self.mod})'
    
    def __eq__(self,other):
        if self.mod == other.mod:
            return self.num == other.num
        else:
            raise TypeError
    
    def __add__(self, other) -> 'Residue':
        if self.mod == other.mod:
            return Residue(self.num + other.num, self.mod)
        else:
            raise TypeError
    
    def __neg__(self):
        return Residue(-1 * self.num, self.mod)
    
    def __sub__(self, other) -> 'Residue':
        if self.mod == other.mod:
            return self + -other
        else:
            raise TypeError
    
    def __mul__(self, other) -> 'Residue':
        if self.mod == other.mod:
            return Residue(self.num * other.num, self.mod)
        else:
            raise TypeError
        
r1 = Residue(2, mod=3)
r2 = Residue(5, mod=3)

print(r1)        # 2 (mod 3)
print(r2)        # 2 (mod 3)
print(r1 == r2)  # True
print(r1 + r2)   # 1 (mod 3)
print(r1 - r2)   # 0 (mod 3)
print(r1 * r2)   # 1 (mod 3)
r1 - r2
