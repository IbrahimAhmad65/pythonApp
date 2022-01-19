class Data:
    def __init__(self, startingArray):
        self.dict = {
                "Category" : 0,
                "Month" : 1,
                "Day" : 2,
                "RepeatType" : 3,
                "Time" : 4,
        }
        
        self.list = ["Category","Month", "Day", "RepeatMonth", "Time"]
        self.data = startingArray

    def setData(self, array):
        self.data = array

    def getData(self):
        return self.data

    def getDataIndex(self, index):
        return self.data[index]

    def getDataLen(self):
        return len(self.data)

    def getDataIndexIdentifier(self, index, identifier):
        return self.data[index][identifier]

    def getAllDataIdentifier(self, identifier):
        array = {}
        for i in self.data:
            array.append(i[identifier])
        return array

    def getAllDataIDList(self, idList):
        out = {}
        for i in self.data:
            temp = {}
            for j in idList:
                temp.append(i[j])
            out.append(temp)
        return out

    def getDataFiltered(self, filter, filterType, dataType):
#        print("Filter ", filter)
        array = []
        for i in self.data:
#            print("Left Side of boolean check",i[self.dict[filterType]],int(i[self.dict[filterType]]) == filter)
            if(int(i[self.dict[filterType]]) == filter):
                array.append(int(i[self.dict[dataType]]))
#            print("array after appending",array)
        return array
