class Text:
    def __init__(self,parent,x,y,text):
        self.text=text
        self.parent=parent
        self.x = x 
        self.y = y 

        parent.add(self)
    def draw(self):
        self.parent.win.addstr(self.y,self.x,self.text)
