from views import pageviews

class router:
    def __init__(self, request):
        #self.string_list = request.split(' ') split request using space
        self.method = self.request[0]
        self.requesting_file = self.request[1]
        print("Client request: ",  self.requesting_file)
        self.myfile1 = self.requesting_file.split('?')[0]
        self.myfile = self.myfile1.lstrip('/')
        
    def routing(self):
        if self.method == "GET":
            if self.myfile == "":
                viewHome()
                
            elif self.myfile == "register":
                registrationView()
                
            elif self.myfile == "login":
                loginView()
            elif self.myfile =="data/rewrite" | "data/rewrite/route":
                urlRewriteView()  
            elif self.myfile == "dynamic":
                dynamicView()
            else:
                errorView()            
            
        # handle post method    
        if self.method == "POST":
            if self.myfile == "/new":
                pass   
            
                              
                         
                           
        
