input = list(map(int, input().split()))

import math
def calculat_left_side(n):
    x = (n & (~(n - 1)))
    return int(math.log10(x) /
            math.log10(2))  

def calculat_right_side(n):
    power_of_2 = calculat_left_side(n)
    m = ((n//(2**power_of_2)) - 1)//2
    return m

def decode_pair_number(n):
    '''This function get the code of pair number as an input and then decode it based on
    following formula : 2^x(2y+1) - 1'''
    left_side = calculat_left_side(n)
    right_side = calculat_right_side(n)
    return left_side, right_side

def create_var_lst(c):
    var_lst = ["Y"]
    for i in range(math.floor((c+1)/2)):
        var_lst.extend([f"X{i+1}", f"Z{i+1}"])
    return var_lst    

def create_label_lst(a):
    label_lst = []
    for i in range(math.ceil((a + 1)/5)):
        label_lst.extend([f"A{i+1}", f"B{i+1}", f"C{i+1}", f"D{i+1}", f"E{i+1}"])
    return label_lst  

def generate_instruction(a, b, c):
    var_lst = create_var_lst(c)
    label_lst = create_label_lst(a)
    instruction_lst = ["V <- V", "V <- V + 1", "V <- V + 1", "IF V != 0 GOTO L"]
    var = var_lst[c]

    if b == 0:
        inst = instruction_lst[b].replace("V", var)
    elif b == 1:
        inst = instruction_lst[b].replace("V", var)
    elif b == 2:
        inst = instruction_lst[b].replace("V", var)    
    else:
        inst = instruction_lst[3].replace("V", var)     
        inst = inst.replace("L", label_lst[b - 3])  

    if a != 0:
        inst = f"[{label_lst[a - 1]}]" + " " + inst

    return inst           