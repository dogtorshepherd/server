import json
import re

class Stack:

    def __init__(self):
        """
        Initializing Stack.
        """
        self.stack = []

    def isEmpty(self) -> bool:
        return True if len(self.stack) == 0 else False

    def length(self) -> int:
        return len(self.stack)

    def top(self) :
        return self.stack[-1]

    def push(self, x) -> None:
        self.x = x
        self.stack.append(x)

    def pop(self):
        return self.stack.pop()

class TagParser():

    def parseTag(self,data):
        result = data.replace("&","<")
        result = result.replace(";",">")
        return result

    def decode(self,data):
        result = data.replace("<", "&")
        result = result.replace(">", ";")
        return result

    def parse(self,data):
        stack = Stack()
        tagTemp = {}
        isTag = False
        isEndTag = False
        tagName = ""
        endTag = ""
        for i in data:
            if i == "<":
                isTag = True
                tagName = ""
            elif i == ">":
                isTag = False
                if isEndTag:
                    isEndTag = False
                    if endTag == stack.top():
                        popName = stack.pop()
                        component = Component()
                        component.setComponent(popName,data)
                        if popName in tagTemp:
                            tagTemp[popName] = component.getComponent()
                        if not stack.isEmpty():
                            if stack.top() in tagTemp:
                                tagTemp[stack.top()]['children'].append(tagTemp[popName])
                            else:
                                newComponent = Component()
                                newComponent.setComponent(stack.top,data)
                                tagTemp[stack.top()] = newComponent.getComponent()
                                tagTemp[stack.top()]['children'].append(tagTemp[popName])
                        print("POP : ",popName)

                if tagName != "":
                    stack.push(tagName)

            elif i == " ":
                isTag = False
            elif isTag and i == "/":
                endTag = ""
                isEndTag = True
            elif isEndTag:
                endTag += i
            elif isTag :
                tagName += i
        print("STACK: ",stack.__dict__)
        print("TAG COMPONENT: ", tagTemp)
        return {}

class Component:
    value = []
    def __init__(self):
        self.value = []

    def fill(self,var,word):
        if var == word:
            return True
        else:
            return False

    def setComponent(self,tag,data):
        self.data = data
        self.tag = tag
        index = 0
        stack = Stack()
        mem = []
        temp = ""
        tagName = ""
        endTag = ""
        tempText = ""
        parentName = ""
        isStart = False
        isTag = False
        isUseTemp = False
        isEndTag = False
        for i in data:
            if not isStart:
                if i == "<" and not isTag :
                    tagName = ""
                    isTag = True
                elif i == ">":
                    isTag = False
                    stack.push(tagName)
                    mem.append(tagName)
                    #print("Tag : ",tagName)
                    if tag == tagName:
                        isStart = True
                elif i == " ":
                    isTag = False
                elif i == "/":
                    isTag = False
                elif isTag:
                    tagName += i
            else:
                if i == "<":
                    isUseTemp = True
                    tempText += i
                elif i == ">":
                    #print("EndTag : ",endTag)
                    isUseTemp = False
                    tempText += i
                    if isEndTag:
                        isEndTag = False
                    if tag == endTag:
                        isStart = False
                        filtered = filter(lambda x: x == endTag, mem)
                        index = len(list(filtered))
                        if not stack.isEmpty():
                            stack.pop()
                            if not stack.isEmpty():
                                parentName = stack.top()
                        tagComp = {"tagName": tag, "data": temp, "attribute": self.getAttribute(), "parentName": parentName,"index":index ,"children": []}
                        self.value.append(tagComp)
                        temp = ""
                        index = 0
                    else:
                        temp += tempText

                        tempText = ""
                elif i == "/":
                    isEndTag = True
                    tempText += i
                    endTag = ""
                elif isUseTemp:
                    tempText += i
                    if isEndTag:
                        endTag += i
                else:
                    temp += i


        print(self.value)

    def getComponent(self):
        return self.value

    def getAttribute(self):
        result = []
        isTag = False
        isAttr = False
        isValue = False
        data = self.data
        tag = self.tag
        tagName = ""
        attrName = ""
        attrValue = ""
        for i in data:
            if i == "<":
                isTag =True
                tagName = ""
            elif i == ">":
                isTag = False
                isAttr = False
                if tag == tagName:
                    if attrName != "":
                        result.append({"name": attrName, "value": attrValue})
                attrName = ""
                attrValue = ""
            elif i == "=":
                isValue = True
                attrValue = ""
            elif isValue:
                if i != "\"" and i != "\'":
                    attrValue += i
                if attrValue != "" and (i == "\"" or i == "\'"):
                    isValue = False
            elif i == " " and tag == tagName:
                isAttr = True
                isValue = False
                if tag == tagName:
                    if attrName != "":
                        result.append({"name": attrName, "value": attrValue})
                attrName = ""
                attrValue = ""
            elif isTag and isAttr:
                attrName += i
            elif isTag:
                tagName += i

        return result




# tag = "<Tag1 htmlTest=\"xxxx\">" \
#       "<Tag2>Test1Value</Tag2>" \
#       "<Tag2 tttt>xxxffff<data>444444</data></Tag2>" \
#       "<Tag3><data>5555</data><data>6666</data></Tag3>" \
#       "</Tag1>"
# # tagParser = TagParser()
# # decode = tagParser.parse(tag)
# # print("DECODE : ",decode)
#
# component = Component()
# component.setComponent("data",tag)
# print("Attr : ====>",component.getAttribute())
# print("TAG : ====>",component.getComponent())

