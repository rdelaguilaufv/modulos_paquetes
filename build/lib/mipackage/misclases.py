
    
class Conexion:
    def __init__(self,dburl):
        self._bd = 'sqlite://'+dburl
    
    def establecer_conexion(self):
        return 'conectado a '+self._bd
    
class Pool:
    def __init__(self, url):
        self._url = url
        
    def devolver_conexion(self):
        self._conexion = Conexion(self._url)
        return self._conexion.establecer_conexion()