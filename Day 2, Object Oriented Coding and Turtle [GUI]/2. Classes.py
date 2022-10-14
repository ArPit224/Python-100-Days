
#TODO: Complete classes stuff https://docs.python.org/3/tutorial/classes.html

def scopes():
    
    """
    Namespace Scope
    """
    
    def localScope():
        """
        local scope only exists within the block of code
        """
        scopeTest = "local scope"
        
    def nonLocalScope():
        
        #nonlocal scopeTest
        scopeTest = "non local scope"
        
    def globalScope():
        scopetest = "global scope"
        
    
            