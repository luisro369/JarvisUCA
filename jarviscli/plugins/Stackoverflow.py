##===============Model of how to access Stack class in the folder StackApi
## ACA TIENEN QUE ESTAR TODAS LAS VALIDACIONES DE TIPO DE ELEMENTOS A ENVIAR
import StackApi.Stack as Conexion
from plugin import plugin, complete, require, alias

@require(network=True)
@alias("Stack","stackoverflow","Stackoverflow")
@plugin("stack")

class stacko():
    """
    Ask any question in stackoverflow,
    the format is stack question,
    then you'll be prompt to a list of questions,
    acordin to your criteria, you'll then choose
    wich question you like by typing the number of it,
    and you can visualise the entire question thread with
    the answer.
    ---- Example:
         stack how to print in c
    """
    #===========================================================
    def __init__(self):
        self.stack = Conexion.Stack()
    #===========================================================
    def __call__(self, jarvis, s):
        k = s.split(' ',1)
        if len(k) == 1:
            jarvis.say("Steps to use stackoverflow in J.A.R.V.I.S:\n-stack your question here\n-then choose a question form the menu")
        else:
            self.ask(jarvis, s)
            try:
                s2 = int(input("PLEASE CHOOSE WHICH QUESTION YOU LIKE:  "))
                if s2 < len(self.stack.title):
                    self.answ(jarvis, s2)
                else:
                    jarvis.say("PLEASE CHOOSE ONLY A NUMBER FROM THE MENU!!!")
            except ValueError:
                jarvis.say("PLEASE CHOOSE A NUMBER!!!")
        #----------------ONCE THE OBJECT IS UTILIZED WE SHOULD ELIMINATE IT
        del self.stack
    #============================================================
    def ask(self, jarvis, s):
        self.stack = Conexion.Stack()
        List_of_questions = self.stack.ask(s)
        jarvis.say("HERE YOU CAN SEE ALL QUESTIONS RELATED TO YOUR SEARCH : ")
        for i in range(0,len(List_of_questions)):
            jarvis.say(str(i) + ": " + List_of_questions[i])
    #============================================================
    def answ(self,jarvis, s):
        List_of_answers = self.stack.getAnswer(int(s))
        jarvis.say("============================================ " + self.stack.title[int(s)].upper() + " =================================================================== \n")
        for i in range(0,len(List_of_answers)):
            jarvis.say(List_of_answers[i])
            if i+1 < len(List_of_answers):
                jarvis.say("============================================ANSWER " + str(i+1) + "============================================================= \n")
            else:
                jarvis.say("================================================================================================================== \n")
