

def rewrite_url(reqobj):
    if reqobj.path == '/data':
        if len(reqobj) == 2:
            reqobj.args[sta] = 'rewrite'
            new_url = reqobj.path+'/'+reqobj.args[sta]
            reqobj.data[1] = new_url
            return reqobj.data
        
        elif len(reqobj) == 3  & reqobj.args[sta]=='rewrite':
            reqobj.args[orid] = 'route'
            new_url = reqobj.path+'/'+reqobj.args[sta]+'/'+reqobj.args[orid] 
            reqobj.data[1] = new_url
            return reqobj.data
            
            
        elif len(reqobj) == 3 & reqobj.args[sta] != 'rewrite':
            reqobj.args[orid] = 'route'
            reqobj.args[sta] = 'rewrite'
            new_url = reqobj.path+'/'+ reqobj.args[sta] +'/'+reqobj.args[orid]
            reqobj.data[1] = new_url
            return reqobj.data
              
        else:
            reqobj.args[sta] = 'rewrite'
            reqobj.args[orid] = 'route'
            new_url = reqobj.path+'/'+ reqobj.args[sta]+'/'+reqobj.args[orid]  
            reqobj.data[1] = new_url 
            return reqobj.data
    else:
        return reqobj.data       
             
            
        
