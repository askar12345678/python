#!/usr/bin/env python
# coding: utf-8

# In[108]:


class Residue:
    def __init__(self, num: int, mod: int):
        self.num = num % mod
        self.mod = mod
        
    def __str__(self) -> str:
        return f'{self.num} (mod {self.mod})'
    
    def __repr__(self) -> str:
        return f'{self.num} (mod {self.mod})'
    
    def __eq__(self,other):
        if self.mod == other.mod:
            if self.num == other.num:
                return True
            else:
                return False
        else:
            raise TypeError
    
    def __add__(self, other) -> 'Residue':
        if self.mod == other.mod:
            return Residue(self.num + other.num, self.mod)
        else:
            raise TypeError
            
    def __sub__(self, other) -> 'Residue':
        if self.mod == other.mod:
            return self + Residue(-1 * other.num, other.mod)
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
print(r1 * r2)

