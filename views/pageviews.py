import jinja2
import os

JINJA_ENVIRONMENT = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions = ['jinja2.ext.autoescape'],
    autoescape = True
)


def viewHome():
    myfile = "static/index.html"
    try:
        file = open(myfile, 'rb') # open file , r => read
        response = file.read()
        file.close()
        
        header = 'HTTP/1.1 200 Ok\n'
        if (myfile.endswith(".jpg")):
            mimetype = "image/jpg"
        elif(myfile.endswith(".png")):
            mimetype ="image/png"
        elif (myfile.endswith(".css")):
            mimetype  ="text/css"
        else:
            mimetype = "text/html"
            header += 'Content-Type: '+ str(mimetype)+'\n\n'
    except Exception as e:
        header = 'HTTP/1.1 404 Not Found\n\n'
        response = 'static/404.html'.encode('utf-8')
    final_response = header.encode('utf-8')
    final_response += response
    return final_response
    
def loginView():
    myfile = "static/index.html"
    try:
        file = open(myfile, 'rb') # open file , r => read
        response = file.read()
        file.close()
        
        header = 'HTTP/1.1 200 Ok\n'
        if (myfile.endswith(".jpg")):
            mimetype = "image/jpg"
        elif(myfile.endswith(".png")):
            mimetype ="image/png"
        elif (myfile.endswith(".css")):
            mimetype  ="text/css"
        else:
            mimetype = "text/html"
            header += 'Content-Type: '+ str(mimetype)+'\n\n'
    except Exception as e:
        header = 'HTTP/1.1 404 Not Found\n\n'
        response = 'static/404.html'.encode('utf-8')
    final_response = header.encode('utf-8')
    final_response += response
    return final_response
    
def registrationView():
    myfile = "static/register.html"
    try:
        file = open(myfile, 'rb') # open file , r => read
        response = file.read()
        file.close()
        
        header = 'HTTP/1.1 200 Ok\n'
        if (myfile.endswith(".jpg")):
            mimetype = "image/jpg"
        elif(myfile.endswith(".png")):
            mimetype ="image/png"
        elif (myfile.endswith(".css")):
            mimetype  ="text/css"
        else:
            mimetype = "text/html"
            header += 'Content-Type: '+ str(mimetype)+'\n\n'
    except Exception as e:
        header = 'HTTP/1.1 404 Not Found\n\n'
        response = 'static/404.html'.encode('utf-8')
    final_response = header.encode('utf-8')
    final_response += response
    return final_response    

def urlRewriteView():
    myfile = "static/urlRewrite.html"
    try:
        file = open(myfile, 'rb') # open file , r => read
        response = file.read()
        file.close()
        
        header = 'HTTP/1.1 200 Ok\n'
        if (myfile.endswith(".jpg")):
            mimetype = "image/jpg"
        elif(myfile.endswith(".png")):
            mimetype ="image/png"
        elif (myfile.endswith(".css")):
            mimetype  ="text/css"
        else:
            mimetype = "text/html"
            header += 'Content-Type: '+ str(mimetype)+'\n\n'
    except Exception as e:
        header = 'HTTP/1.1 404 Not Found\n\n'
        response = 'static/404.html'.encode('utf-8')
    final_response = header.encode('utf-8')
    final_response += response
    return final_response     
    
    
def dynamicView():

    template_values = {
        'user':'mike okoth',
        'email':'mikeokoth4040@gmail.com',
        'url' :'https://github.com/myk4040okothogodo'
    
    }
    template = JINJA_ENVIRONMENT.get_template('dynamic.html')
    myfile = "static/error.html"
    try:
        file = open(myfile, 'w+') # open file , r => read
        response = file.write(template.render(template_values))
        file.close()
        
        header = 'HTTP/1.1 200 Ok\n'
        mimetype = "text/html"
        header += 'Content-Type: '+ str(mimetype)+'\n\n'
    except Exception as e:
        header = 'HTTP/1.1 404 Not Found\n\n'
        response = 'static/404.html'.encode('utf-8')
    final_response = header.encode('utf-8')
    final_response += response
    return final_response        
        
def errorView():
    myfile = "static/error.html"
    try:
        file = open(myfile, 'rb') # open file , r => read
        response = file.read()
        file.close()
        
        header = 'HTTP/1.1 200 Ok\n'
        if (myfile.endswith(".jpg")):
            mimetype = "image/jpg"
        elif(myfile.endswith(".png")):
            mimetype ="image/png"
        elif (myfile.endswith(".css")):
            mimetype  ="text/css"
        else:
            mimetype = "text/html"
            header += 'Content-Type: '+ str(mimetype)+'\n\n'
    except Exception as e:
        header = 'HTTP/1.1 404 Not Found\n\n'
        response = 'static/404.html'.encode('utf-8')
    final_response = header.encode('utf-8')
    final_response += response
    return final_response        
                                
                                       
