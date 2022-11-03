def funDef(a, b, c):
    
    '''
    Basic hard coded Function
    '''
    
    return a + b + c

def funDefDefault(a = 1, b = 2, c = 3):
    
    '''
    This function uses default value
    '''
    
    return (a + b + c)

def funArgs(*args):
    
    '''
    This function uses args
    A tuple
    '''
    
    output = 0
    
    for n in args:
        
        output += n
        
    return output


def funKwargs(**kwargs):
        
        '''
        This function uses Kwargs (Key words argument)
        A dict
        First: will be printed first
        Second: will be printed second
        '''
        
        return (kwargs["first"], kwargs["second"])
        
print(funDef(1, 2, 3))
print(funDefDefault(1, 2, 3))
print(funArgs(1, 2, 3))
print(funKwargs(second = "32", first = 12))