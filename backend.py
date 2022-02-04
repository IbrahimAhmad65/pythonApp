import os
from data import *
from parsers import *

class UserData:
    def __init__(self, userName):
        self.username = userName


class Backend:
    def __init__(self):
        self.parser = Parser("./files/randomData")
        self.parser.safeOpen()
        self.dataList = self.parser.parse(self.parser.getDataFromFile(),",")
        self.data = Data(self.dataList)
    
    def pullData(self):
        self.dataList = self.parser.parse(self.parser.getDataFromFile(),",") 
        self.data.setData(dataList)

    def pushData(self,str):
        self.parser.addData(str)
        
    def getData(self):
        return self.data

    def getParser(self):
        return self.parser;

    def tick(self,str):
        self.pushData(str)
        self.pullData()
        return self.getData()
