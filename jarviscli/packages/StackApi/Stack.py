#===Class for stackoverflow.com Consumption
import requests
from bs4 import BeautifulSoup

class Stack():
    #-------Atributes
    def __init__(self):
        self.URL_BASE = "https://stackoverflow.com"
        self.Title_link = []
        self.title = []
    #======================Method 1 ASKING IN STACKOVERFLOW================================
    def ask(self,question):
        try:
            res = requests.get(self.URL_BASE + "/search?q=" + question)
            soup = BeautifulSoup(res.text,"html.parser")
            question_summary = soup.findAll("div",{"class": "question-summary search-result"})
            #title = []
            for question in question_summary:
                self.title.append(question.h3.a["title"])
                self.Title_link.append(question.h3.a["href"])
            return self.title
        except Exception as e:
            return None
    #======================Method 2 GETTING THE ANSWER=====================================
    def getAnswer(self,response):   
        try:
            res = requests.get(self.URL_BASE + self.Title_link[response])
            soup = BeautifulSoup(res.text,"html.parser")
            answer_summary = soup.findAll("div",{"class": "post-text"})#<---es würde nur "find", wenn du nur die erste frage willst
            #=================BURGO'S CODE HERE===========================
            algo = []
            for answer in answer_summary:
                algo.append(answer.text)
            return algo
        except Exception as e:
            return e
    #============================Method 3 OBJECT DESTRUCTOR==============
    def holi(self):
        saludo = "holi desde la api, mis metodos son: ask(pregunta)<--tipo de dato str, getAnswer(seleccion_pregunta)<---tipo de dato int"
        return saludo

    def reset(self):
        self.Title_link = []
        self.title = []
