class request:
    def __init__(self, request):
        
        self.data = request.split(' ')
        self.reqdata = self.data[1]
        self.reqdataargs = self.reqdata.split('/')
        
    
    def __len__(self):
        """Return the length or number of request arguments"""
        return len(self.reqdataargs)-1    
        
    @property
    def args(self):
        if self.__len__ == 2:
            sta = self.reqdataargs[2]
            orid = ""
            return {'sta':[sta], 'orid':[orid]}
        if self.__len__ == 3:  
            sta = self.reqdataargs[2]      
            orid = self.reqdataargs[3]
            return {'sta':[sta], 'orid':[orid]}
        else:
            raise ValueError(" the number of arguments overflows")
            
    
    @args.setter
    def args(self,*args):
        if len(args) == 1:
            sta = args[0]
            orid = ""
            return {'sta':[sta], 'orid':[orid]}
        if len(args) == 2:
            sta = args[0]    
            orid = args[1]   
            return {'sta':[sta], 'orid':[orid]}
        else:
            raise ValueError("the number of arguments overflows")         
            
        
        
    @property
    def path(self):
        
        return '/'+self.reqdataargs[1]
        
    @path.setter
    def path(self, value):
        self.path = value
        return path    
        
    @property
    def postpath(self):
        return [reqdataargs[1]]           
    
