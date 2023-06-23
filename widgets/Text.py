
class Text:
    def __init__(self,text,parent: object,x=0,y=0):
        self.text=text
        self.parent=parent
        self.x = x 
        self.y = y 

        parent.add(self)
    def draw(self):
        self.parent.win.addstr(self.y,self.x,self.text)
