import math

def calculate_left_side(n):
    '''calculate the largest number (e.g. x) that n is divisible by 2^x'''
    x = (n & (~(n - 1)))
    return int(math.log10(x) / math.log10(2))  

def calculate_right_side(n):
    '''calculate another side of code based on the value of left side'''
    power_of_2 = calculate_left_side(n)
    m = ((n//(2**power_of_2)) - 1)//2
    return m

def decode_pair_number(n):
    '''This function get the code of pair number (n = <x, y>) as an input and then decode it based on the
    following formula : <x, y> = 2^x(2y+1) - 1'''
    n = n + 1
    left_side = calculate_left_side(n)
    right_side = calculate_right_side(n)
    return left_side, right_side

def create_var_lst(c):
    '''create list of variables in the instruction based on the value of c in the instruction code (#(I) = <a, <b, c>>)'''
    var_lst = ["Y"]
    for i in range(math.floor((c+1)/2)):
        var_lst.extend([f"X{i+1}", f"Z{i+1}"])
    return var_lst    

def create_label_lst(a):
    '''create list of labels in the instruction based on the value of a in the instruction code (#(I) = <a, <b, c>>)'''
    label_lst = []
    for i in range(math.ceil((a + 1)/5)):
        label_lst.extend([f"A{i+1}", f"B{i+1}", f"C{i+1}", f"D{i+1}", f"E{i+1}"])
    return label_lst  

def generate_instruction(a, b, c):
    var_lst = create_var_lst(c)
    label_lst = create_label_lst(a)
    instruction_lst = ["V <- V", "V <- V + 1", "V <- V - 1", "IF V != 0 GOTO L"]
    var = var_lst[c] # varibale used in our instruction
    
    # decode instruction
    if b == 0:
        inst = instruction_lst[b].replace("V", var)
    elif b == 1:
        inst = instruction_lst[b].replace("V", var)
    elif b == 2:
        inst = instruction_lst[b].replace("V", var)    
    else:
        inst = instruction_lst[3].replace("V", var)     
        inst = inst.replace("L", label_lst[b - 3])  
    
    # decode lable of the instruction
    if a != 0:
        inst = f"[{label_lst[a - 1]}]" + " " + inst

    return inst           

def decode(code):
    '''This function gets the code of the instruction as an input and decodes it to the instruction in language S.'''
    a, b_c = decode_pair_number(code)
    b, c = decode_pair_number(b_c) 
    inst = generate_instruction(a, b, c)
    return inst

 
if __name__=='__main__':
    input = list(map(int, input().split()))
    for i in input:
        print(decode(i))