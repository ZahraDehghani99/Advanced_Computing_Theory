import math

def calculate_left_side(n):
    x = (n & (~(n - 1)))
    return int(math.log10(x) /
            math.log10(2))  


def calculate_right_side(n):
    power_of_2 = calculate_left_side(n)
    m = ((n//(2**power_of_2)) - 1)//2
    return m


def decode_pair_number(n):
    '''This function get the code of pair number as an input and then decode it based on
    following formula : 2^x(2y+1) - 1'''
    left_side = calculate_left_side(n)
    right_side = calculate_right_side(n)
    return left_side, right_side


def create_var_lst(c):
    var_lst = ["Y"]
    for i in range(math.floor((c+1)/2)):
        var_lst.extend([f"X{i+1}", f"Z{i+1}"])
    return var_lst    


def decode_instruction(code):
    '''find a, b and c from instruction code.'''
    code = code + 1
    a, b_c = decode_pair_number(code)
    b_c = b_c + 1
    b, c = decode_pair_number(b_c) 
    return a, b, c


def create_var_lst_of_program(code_list):
    '''find all of the variables in program '''
    inst_var_indx = []
    for code in code_list:
        _, _, c = decode_instruction(code)
        inst_var_indx.append(c)
    max_var_indx = max(inst_var_indx)
    var_lst = create_var_lst(max_var_indx)
    return var_lst


def initial_values(var_lst, input_vairiables):
    '''create a dictionary based on the the variable lists and input values before run the program.'''
    var_value_dict = {}
    for var in var_lst:
        var_value_dict[var] = 0
    for i in range(len(input_vairiables)):
        var_value_dict[var_lst[2*i + 1]] = input_vairiables[i]   
    return var_value_dict     


def find_var_used_lst(code_list):
    '''find used variables in program and sort them based on output format.'''
    inst_var_indx = []
    for code in code_list:
        _, _, c = decode_instruction(code)
        inst_var_indx.append(c)

    input_var = []
    local_var = []
    used_var = []

    for c in inst_var_indx:
        if c != 0 and c%2 == 0:
            local_var.append(c)

        elif c%2 != 0:
            input_var.append(c)  

    max_local_var = max(local_var, default = 0)  
    max_input_var = max(input_var, default = 0)      

    for i in range(math.ceil(max_input_var/2)):
        used_var.append(f"X{i+1}")
    for i in range(max_local_var//2):
        used_var.append(f"Z{i+1}")  
    used_var.append("Y")  
    return used_var      


def output_format(k, var_values_dict, used_var):
    output = [k]
    for i in used_var:
        output.append(var_values_dict[i])
    output_string = ""
    for i in output:
        output_string += str(i) + " "    
    return output_string    


def is_prime(k):
    # Corner cases
    if (k <= 1):
        return 0
    if (k == 2 or k == 3):
        return 1
    # below 5 there is only two prime numbers 2 and 3
    if (k % 2 == 0 or k % 3 == 0):
        return 0
  # Using concept of prime number can be represented in form of (6*k + 1) or(6*k - 1)
    for i in range(5, 1 + int(k ** 0.5), 6):
        if (k % i == 0 or k % (i + 2) == 0):
            return 0
    return 1
 

def nth_prime(n):
    '''function which gives prime at position n'''
    i = 2
    while(n > 0):
        # each time if a prime number found decrease n
        if(is_prime(i)):
            n -= 1
        i += 1  # increase the integer to go ahead
    i -= 1  # since decrement of k is being done before
    # Increment of i , so i should be decreased by 1
    return i   


def prime_factorization(n, p):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac.count(p) 


def decode_state(S, var_values_dict, var_lst):
    '''get the coded state, dictionary of variables and list of variables and decode the state and change the value of the variables in dictionary.'''
    for i, var in enumerate(var_lst):
        var_values_dict[var] = prime_factorization(S, nth_prime(i+1))
    return var_values_dict  


def universal_program(instruction_codes, input_vairiables):
    var_lst = create_var_lst_of_program(instruction_codes)
    used_var_lst = find_var_used_lst(instruction_codes)
    var_values_dict = initial_values(var_lst, input_vairiables)
    input_vars_count = (len(var_lst) - 1)//2 # count of input variables
    Z = instruction_codes
    S = 1 # state code
    for i in range(0, input_vars_count):
        temp = nth_prime(2*i + 2) ** var_values_dict[var_lst[2*i + 1]]
        S = S * temp
    K = 1

    while K != len(Z) + 1: 
        print(output_format(K, decode_state(S, var_values_dict, var_lst), used_var_lst))
        U = calculate_right_side(Z[K-1] + 1) # <b, c> 
        c = calculate_right_side(U + 1)
        P = nth_prime(calculate_right_side(U + 1) + 1)
        b = calculate_left_side(U + 1)

        if b == 0:
                K += 1
        elif b == 1:
            S = S * P
            K += 1
        elif S%P != 0:
            K += 1    
        elif b == 2:
            S = S//P 
            K += 1
        else:
            K = -1
            for i in range(0, len(Z)):
                if calculate_left_side(Z[i] + 1) + 2 == b:
                    K = i + 1
            if K == -1:
                K = len(Z) + 1



if __name__=='__main__':
    instruction_codes = list(map(int, input().split()))
    input_vairiables = list(map(int, input().split()))   
    universal_program(instruction_codes, input_vairiables)


             