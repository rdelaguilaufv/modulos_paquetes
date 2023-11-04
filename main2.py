from mipackage.misclases import Conexion, Pool
from module import hola_mundo

if __name__=='__main__':
    pool = Pool ('urldb')
    hola_mundo('mi modulo '+pool.devolver_conexion())
