 def application(environ, start_response):
     # Guardo la salida que devolveré como respuesta
     respuesta = "<html> <head> <title>Mi primera pagina web </title> </head> <body style=\"background-color:00BB2D;\"> <h1 align=\"center\" >Mi Primera pagina web </h1> <hr> <p>Pagina de prueba HTML.</p> </body> </html>"
     # Se genera una respuesta al navegador 
     start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])
     return respuesta