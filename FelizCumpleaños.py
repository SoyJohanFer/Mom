import time
import platform
import os

one = "Bien" or "BIEN"
one1 = "mal" or "Mal"

contador = 1
rojo = '\033[31m'
normal = '\033[39m'

def limpiar_pantalla():
    time.sleep(1)

    if platform.system() == 'Windows':
        os.system('cls')

    else:
        os.system('clear')

if __name__ == '__main__':
    limpiar_pantalla()

time.sleep(1)
print ("----------La mujer sabia une a su familia.----------")
print ("                Proverbios 14:1                     ")
print ("")
print ("")
print ("")
print ("")
print ("")
time.sleep(2)
print ("Hola ma ¿Como estas? :3")
time.sleep(1)
print ("")
print ("1. Bien <3")
time.sleep(1)
print ("2. Mal :(")
print ("")
time.sleep(1)

while contador <= 3:

    respuesta = input("Respuesta: ")

    if (respuesta == "Bien"):

        contador = 4
        print ("Me alegro ma :3")
        time.sleep(2)
        os.system('cls')
        print ("----------Mujer ejemplar no es fácil hallarla; ¡vale más que las piedras preciosas!----------")
        print ("                                      Proverbios 31:10                                       ")
        print ("")
        print ("")
        print ("")
        print ("")
        print ("")
        time.sleep(2)
        print("Ma el día de hoy te quiero decir y quiero que te des cuenta que eres la mejor ama del mundo, eres la persona que me comprende, eres la persona que me apoya en todo lo que yo quiero, el dia de hoy quiero que la pases muy bien porque como una persona como tu se merece el cielo y la tierra, perdón si no soy el mejor hijo o no soy lo que tu quieres que yo sea, pero quiero que sepas que tu eres mis alegrías y las fuerzas que tengo, gracias por hacerme darme cuenta en este mundo y prepararse para el futuro mío, gracias por todo lo que has hecho por mi y gracias por todo lo que hará en un futuro, eres una gran mamá y no quiero cambiarte por nada del mundo, quiero que sepas que te amo mucho y que hoy la pases muy feliz y que algun dia te haga sentir orgullosa de tenerme a mí como hijo, GRACIAS POR TODO Y FELIZ CUMPLEAÑOS MA <3")
        time.sleep(10)
        print ("Quisiera dedicarte estas frases:")
        print ("")
        time.sleep (1)
        print ("Muchas mujeres han realizado proezas, pero tú las superas a todas. (Proverbios 31:29)")
        print ("")
        time.sleep(2)
        print ("Por mí aumentarán tus días; muchos años de vida te serán añadidos. (Proverbios 9:11)")
        print ("")
        time.sleep(1)
        print ("Que te envíe ayuda desde el santuario; que desde Sión te dé su apoyo. Que se acuerde de todas tus ofrendas; que acepte tus holocaustos.")
        print ("Que te conceda lo que tu corazón desea; que haga que se cumplan todos tus planes. (Salmos 20:2-4)")
        print ("")
        print ("")

        quit() 

    if (respuesta == "Mal"):
        contador = 4
        print ("Y... eso por que ma :(")
        print ("")
        time.sleep(1)
        input("¿Por que?: ")
        print ("")
        print ("Te entiendo ma :(")
        time.sleep(1)
        os.system('cls')
        print ("Quería solamente desearte un feliz cumpleaños y que hoy la pases super bien, quería recordarte que eres la mejor mama del mundo y que te agradezco por siempre estar ahi para mi, te agradezco por todo lo que hace por mi, los esfuerzos, la paciencia, y perdón si no soy el mejor hijo del mundo o no soy como quiere que yo sea pero trato de ser lo mejor para ti y que estes orgullosa tanto tu como mi papa, gracias por todo y voy a tratar que hoy la pases muy bien y te sientas feliz")
        time.sleep(7)
        print ("")
        print ("Sus hijos se levantan y la felicitan; también su esposo la alaba: «Muchas mujeres han realizado proezas, pero tú las superas a todas».- Proverbios 31:28-29")
        time.sleep(3)
        print ("")
        print ("El Señor te bendiga y te guarde; el Señor te mire con agrado y te extienda su amor; el Señor te muestre su favor y te conceda la paz”.- Números 6:24-26")
        time.sleep(2)
        print ("Bueno ma... queria decirte eso, recuerda tambien que te amo mucho <3")
        time.sleep(1)
        exit
        quit()

    if (respuesta != "Bien" and "Mal"):
        print ("Esta opcion no es existente, intentelo de nuevo")
        contador = contador +1
    
    if  (contador == 3):
        print ("Le queda un ultimo intento")
        exit