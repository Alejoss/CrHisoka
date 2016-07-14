import os

counter = 0
for f in os.listdir("."):
    counter += 1
    filename, extencion = os.path.splitext(f)
    if extencion is not ".py":
        nuevo_nombre = str(counter) + extencion
        os.rename(f, nuevo_nombre)
