#!/usr/bin/env python
# coding: utf-8

# In[9]:


from typing import Callable
def author(author_name: str):
    def new_param(func: Callable):
        func._author = author_name
        return func
    return new_param
@author("Dany Longo")
def add2(num: int) -> int:
    return num + 2
print(add2._author)

