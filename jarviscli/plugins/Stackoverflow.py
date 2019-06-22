##===============Model of how to access Stack class in the folder StackApi
## ACA TIENEN QUE ESTAR TODAS LAS VALIDACIONES DE TIPO DE ELEMENTOS A ENVIAR
import StackApi.Stack as Conexion
from plugin import plugin, complete, require, alias

@require(network=True)
@alias("Stack","stackoverflow","Stackoverflow")

@plugin("stack")

def nombre(jarvis,s):
    objeto = Conexion.Stack()
    jarvis.say(objeto.holi())

'''
List_of_questions = []
#----------object "stack" creation
stack = Conexion.Stack()
#-----------------Making question to "API-REST"
pregunta = input('bienvenido al asistente de preguntas por consola de Stackoverflow, porfavor ingrese su pregunta: \n')

List_of_questions = stack.ask(pregunta)
print("Aca se muestra la lista de preguntas, seleccione el numero de la pregunta: ")
for i in range(0,len(List_of_questions)):
    print(str(i) + ": " + List_of_questions[i])
#-----------------Choosing the best question and getting answer
respuesta = int(input('A cual de las preguntas anteriores desea acceder? : '))

#print(stack.getAnswer(respuesta))
List_of_answers = stack.getAnswer(respuesta)
print("============================================ORIGINAL QUESTION========================================================================== \n")
for i in range(0,len(List_of_answers)):
    print(List_of_answers[i])
    print("============================================ANSWER " + str(i+1) + "============================================================= \n")

#----------------ONCE THE OBJECT IS UTILIZED WE SHOULD ELIMINATE IT
del stack
'''
