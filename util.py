import itertools

class SmartSublist(object):

    def __init__(self, n, lower_bound, upper_bound=0, original_list=[]):

        self.n              = n        
        self.lower_bound    = lower_bound
        self.upper_bound    = lower_bound if upper_bound == 0 else upper_bound
        self.original_list  = original_list
    
    def get_sublists(self):
        
        sublists                      = []
        original_list_representatives = []
        
        if (len(self.original_list) == 0):
            original_list_representatives = range(self.n)
        else:
            original_list_representatives = self.original_list
        
        for i in range(self.lower_bound, self.upper_bound + 1):
            sublists = sublists + list(itertools.combinations(original_list_representatives,i))
        
        return sublists        