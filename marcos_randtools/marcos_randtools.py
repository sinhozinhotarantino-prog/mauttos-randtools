__author__ = "Marcos Valério Battisti - Math Educator & Computer Engineering Student"
__version__ = "1.0.0"
__description__ = "Advanced random number list generation library."

import random

def randlist(size, max_val, allow_duplicates=False, use_floats=False):
    """
    Generates a list of random numbers with advanced configurations.
    
    Created by: Marcos Valério Battisti - Math Educator & Computer Engineering Student
    
    Parameters:
    -----------
    size : int
        The number of random elements to be generated in the list.
    max_val : int or float
        The maximum allowed value for the random selection.
    allow_duplicates : bool, optional (default is False)
        If True, allows repeated numbers to appear in the list.
        If False, ensures that all numbers are unique.
    use_floats : bool, optional (default is False)
        If True, generates real numbers (floating-point with decimals).
        If False, generates only integers.
        
    Returns:
    --------
    list
        A list containing the generated random numbers.
    """
    result_list = [] 
    
    # Mathematical Security Validation
    if not allow_duplicates and not use_floats and size > max_val:
        raise ValueError(f"Impossible to generate {size} unique integers within a limit of {max_val}.")
    
    # PATH 1: Free Generation (Allows Duplicates)
    if allow_duplicates:
        for _ in range(size):
            num = random.uniform(1, max_val) if use_floats else random.randint(1, max_val)
            result_list.append(num)
            
    # PATH 2: Exclusive Generation (Unique Numbers Only)
    else:
        while len(result_list) < size:
            num = random.uniform(1, max_val) if use_floats else random.randint(1, max_val)
            if num not in result_list:
                result_list.append(num)
                
    return result_list

