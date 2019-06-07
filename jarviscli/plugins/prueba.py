### Aca estara la interaccion con el usuario y la llamada a la clase APIrest
import stack.stackApi
from plugin import plugin, complete, require , alias

@require(network=True)
@alias("Stack","stackoverflow","Stackoverflow")

@plugin("stack")
def funtion(jarvis,s):
    api = stack.stackApi.APIrest()
    jarvis.say(api.coneccion)
    #jarvis.say("funcion de stackoverflow")
