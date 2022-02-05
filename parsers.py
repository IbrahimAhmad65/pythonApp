import os

class Parser:
    def __init__(self,pathToData):
        self.path = pathToData
        self.open = False
    def safeOpen(self):
        if not self.open:
            self.File = open(self.path, "r+")
            self.open = True
        return True

    def getDataFromFile(self):
        return self.File.read()

    def parse(self,str,delimiter):
        out = []
        for line in str.split("\n"):
            if(line != ""):
                dataLine = []
            indices = line.split(delimiter)
            indicesTester = line.split(delimiter)
            temp = ""
            found = True
            if(line != ""):
                while len(indices) != 0:
                    #print(indicesTester)
                    indicesTester[0] = indicesTester[0].strip()
                    if (((indicesTester[0][0] == "\"" 
                        and indicesTester[0][-1] == "\"") 
                        or indicesTester[0][0] != "\"") and found):
                        

                        dataLine.append(indices[0].strip())
                        indices.remove(indices[0])
                        indicesTester.remove(indicesTester[0])
                    else:
                        temp += indices[0]
                        if(indicesTester[0][-1] != "\""):
                            found = False
                            temp += delimiter
                        else:
                            found = True
                            dataLine.append(temp.strip())
                        indices.remove(indices[0])
                        indicesTester.remove(indicesTester[0])
            if(line != ""):
                out.append(dataLine)
        return out

    def addData(self, str):
        self.File.close()
        self.File = open(self.path, "a")
        #self.File.seek(0,2)
        #self.File.write("\n")
        self.File.write(str)
        self.File.write("\n")
        self.File.write(str)
        self.File.close()
        self.safeOpen()
    
    def close(self):
        self.File.close()

    def test(self):
        self.safeOpen()
        str = self.getDataFromFile()
        print(self.parse(str,","))
        self.addData("hola")
        self.close()


