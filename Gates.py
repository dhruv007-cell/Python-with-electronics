#!/usr/bin/env python
# coding: utf-8

# In[1]:


def sub(Q):
    Q1 = Q.replace("OR","Gates.OR")
    Q2 = Q1.replace("AND","Gates.AND")
    Q3 = Q2.replace("NOT","Gates.NOT")
    Q4 = Q3.replace("NND","Gates.NAND")
    Q5 = Q4.replace("NR","Gates.NOR")
    Q6 = Q5.replace("XR","Gates.XOR")
    Q7 = Q6.replace("XNR","Gates.XNOR")
    return Q7



def OR(A, B):
    if A == 0 and B == 0:
        return 0
    else:
        return 1
    
def AND(A, B):
    if A == 0 or B == 0:
        return 0
    else:
        return 1
    
    
def NOT(A):
    if A == 0:
        return 1
    else:
        return 0
    
def NAND(A, B):
    if A == 0 or B == 0:
        return 1
    else:
        return 0
    
def NOR(A, B):
    if A == 1 or B == 1:
        return 0
    else:
        return 1
    
def XOR(A, B):
    if A == B:
        return 0
    else:
        return 1
    
def XNOR(A, B):
    if A == B:
        return 1
    else:
        return 0


# In[ ]:




