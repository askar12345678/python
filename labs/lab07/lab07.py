import random
from abc import ABC, abstractmethod
    
class Nucleic_Acid(ABC):
    @abstractmethod
    def __init__(self, s: str):
        pass
    
    @abstractmethod
    def __str__(self) -> str:
        pass
    
    @abstractmethod
    def __repr__(self) -> str:
        pass
    
    @abstractmethod
    def __getitem__(self, item):
        pass
    
    @abstractmethod
    def __add__(self, other):
        pass
    
    @abstractmethod
    def __mul__(self, other):
        pass

    @abstractmethod
    def comp_chain(self, s1):
        pass
    
    @abstractmethod
    def __eq__(self, other):
        pass
    
class DNA(Nucleic_Acid):
    def __init__(self, s: str):
        
        for letter in s:
            if letter == "A" or letter == "T" or letter == "G" or letter == "C":
                self.coding_chain = s
            else:
                raise ValueError
        self.noncoding_chain =  self.comp_chain(s)
    
    def comp_chain(self, s1):
        s2 = ""
        for letter in s1:
            if letter == "A":
                s2 = s2 + "T"
            if letter == "T":
                s2 = s2 + "A"
            if letter == "G":
                s2 = s2 + "C"
            if letter == "C":
                s2 = s2 + "G"
        return s2
    
    def __str__(self) -> str:
        return f'''{self.coding_chain}
{self.noncoding_chain}'''
    
    def __repr__(self) -> str:
        return f' DNA("{self.coding_chain}") '
    
    def __getitem__(self, item):
        return f'''{self.coding_chain[item]}
{self.noncoding_chain[item]}'''
    
    def __add__(self, other):
        return[self.coding_chain + other.coding_chain , self.noncoding_chain + other.noncoding_chain]
    
    def __mul__(self, other):
        l1 = min(len(self.coding_chain), len(other.coding_chain))
        l2 = max(len(self.coding_chain), len(other.coding_chain))
        res_cod = ""
        for i in range(0, l1):
            res_cod = res_cod + random.choice(self.coding_chain[i] + other.coding_chain[i])
        if l1 != l2:
            if l2 == len(self.coding_chain):
                for i in range(l1, l2):
                    res_cod = res_cod + self.coding_chain[i]
            else:
                for i in range(l1, l2):
                    res_cod = res_cod + other.coding_chain[i]
        return DNA(res_cod)
    
    def __eq__(self: DNA, other: DNA):
        return self.coding_chain == other.coding_chain
    

class RNA(Nucleic_Acid):
    def __init__(self, s: str):
        
        for letter in s:
            if letter == "A" or letter == "U" or letter == "G" or letter == "C":
                self.chain = s
            else:
                raise ValueError
                
    def __str__(self) -> str:
        return f'{self.chain}'
    
    def __repr__(self) -> str:
        return f' RNA("{self.chain}") '            
                
    def __getitem__(self, item):
        return f'{self.chain[item]}'
    
    def comp_chain(self, s1) -> DNA:
        s2 = ""
        for letter in s1:
            if letter == "A":
                s2 = s2 + "T"
            if letter == "U":
                s2 = s2 + "A"
            if letter == "G":
                s2 = s2 + "C"
            if letter == "C":
                s2 = s2 + "G"
        return DNA(s2)
    
    def __add__(self, other):
        return self.chain + other.chain
    
    def __mul__(self, other):
        l1 = min(len(self.chain), len(other.chain))
        l2 = max(len(self.chain), len(other.chain))
        res_ch = ""
        for i in range(0, l1):
            res_ch = res_ch + random.choice(self.chain[i] + other.chain[i])
        if l1 != l2:
            if l2 == len(self.chain):
                for i in range(l1, l2):
                    res_ch = res_ch + self.chain[i]
            else:
                for i in range(l1, l2):
                    res_ch = res_ch + other.chain[i]
        return RNA(res_ch)
    
    def __eq__(self: RNA, other: RNA):
        return self.chain== other.chain
    
dna1 = DNA("AATGCTC")
dna2 = DNA("AAGCTGGTATAAAA")
rna1 = RNA("UUACGUUAAUUACCCCCCCCUUUUUU")
rna2 = RNA("CCGAAUUCGAUGG")
rna3 = RNA("CCGAAUUCGAUGG")
print(dna1 + dna2)
print(rna2 + rna1)
print(rna1.comp_chain(rna1.chain))
print(dna1 == dna2)
rna3 == rna2