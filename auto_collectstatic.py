import os

correr = True
for x in range(0, 200):
    respuesta = os.system("python manage.py collectstatic --noinput")
    print respuesta
    if not str(respuesta) == "256":
        print "RESPUESTA NO FUE 256, OJALA HAYA FUNCIONADO"
        break

    print "respuesta: %s" % respuesta
