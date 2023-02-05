import os
directory = os.listdir("/home/salamanca/Descargas")

for fichero in directory:
    is_folder = os.path.exists(fichero)
    print("fichero : {0} es una carpeta : {1}".format(fichero,is_folder))
    if is_folder:
        print("Es una carpeta")
        for i in fichero:
            print(fichero.title())
    print(fichero.title())