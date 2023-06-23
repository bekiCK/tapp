from curses import newwin
from threading import Thread

class win:
    def __init__(self,parent,x,y,w,h,border=True):
        self.win = newwin(h,w,y,x)
        self.maxY,self.maxX = self.win.getmaxyx()
        self.parent = parent
        self.elements =[]
        if border:
            self.win.border()
        self.win.refresh()

    def add(self,elem):
        self.elements.append(elem)

    def __draw(self):
        while self.parent.alive:
            self.win.erase()
            for element in self.elements:
                element.draw()
            self.win.refresh()
    def start(self):
        Thread(target=self.__draw).start()
        return self
def Window(parent,x,y,w,h,border = True):
    return win(parent,x,y,w,h,border).start()
