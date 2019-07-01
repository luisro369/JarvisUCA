##===============Model of how to access Stack class in the folder StackApi
## ACA TIENEN QUE ESTAR TODAS LAS VALIDACIONES DE TIPO DE ELEMENTOS A ENVIAR
import Stack as Conexion
from plugin import plugin, complete, require, alias

@require(network=True)
@alias("Stack","stackoverflow","Stackoverflow","STACK","STACKOVERFLOW")
@plugin("stack")

class stacko():
    """
    Ask any question in stackoverflow,
    the format is: stack question,
    then you'll be prompt to a list of questions
    acordin to your criteria, you'll then choose
    wich question you like by typing the number of it,
    and you can visualise the entire question thread with
    the answer.
    ---- Example:
         stack how to print in c
    """
    #===========================================================
    #--------Defining the class constructor with an argument(object): stack
    def __init__(self):
        self.stack = Conexion.Stack()
    #===========================================================
    #--------First method of the class it basicly works like a main
    def __call__(self, jarvis, s):
        k = s.split(' ',1)
        if len(k) == 1:#<----if the user doesn't put anything he will be prompt with the commands he can type
            jarvis.say("Steps to use stackoverflow in J.A.R.V.I.S:\n-stack your question here\n-then choose a question form the menu")
        else:#<-----If he types a question we call the method ask
            self.ask(jarvis, s)
            try:#-------Here we need two validations, one if the user put something that is not a number, and the other if a user
                #-------put a number that is not in the list
                s2 = int(input("PLEASE CHOOSE WHICH QUESTION YOU LIKE:  "))
                if s2 < len(self.stack.title):
                    self.answ(jarvis, s2)
                    #----------------ONCE THE OBJECT IS UTILIZED WE SHOULD ELIMINATE IT
                    self.stack.reset()#<---resets all variables(arguments)
                else:
                    jarvis.say("PLEASE CHOOSE ONLY A NUMBER FROM THE MENU!!!")

            except ValueError:
                jarvis.say("PLEASE CHOOSE A NUMBER!!!")
    #============================================================
    def ask(self, jarvis, s):
        List_of_questions = self.stack.ask(s)#<----the interaction with the API returns a list that we can iterate with, we save
        #------------------------------------------all the results in the atribute of the class Stack() on the API
        if List_of_questions:
            jarvis.say("HERE YOU CAN SEE ALL QUESTIONS RELATED TO YOUR SEARCH : ")
            for i in range(0,len(List_of_questions)):
                jarvis.say(str(i) + ": " + List_of_questions[i])
        else:
            jarvis.say("CHECK YOUR INTERNET CONEXION")
    #============================================================
    def answ(self,jarvis, s):
        List_of_answers = self.stack.getAnswer(s)#<----The API returns a list of all the questions, all we need to do is iterate
        j = len(List_of_answers)
        jarvis.say("TOTAL OF ANSWERS: "+str(j))
        s3 = int(input("HOW MANY ANSWERS SHOULD I SHOW YOU?: (0-"+str(j)+") "))
        if s3 < len(List_of_answers):
            jarvis.say("============================================ " + self.stack.title[int(s)].upper() + " =================================================================== \n")
            for i in range(0,s3):
                jarvis.say(List_of_answers[i])
                if i+1 < s3:
                    jarvis.say("============================================ANSWER " + str(i+1) + "============================================================= \n")
                else:
                    jarvis.say("================================================================================================================== \n")
        else:
            jarvis.say("PLEASE CHOOSE ONLY A NUMBER IN RANGE OF THE TOTAL OF ANSWERS")
