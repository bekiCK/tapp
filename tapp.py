import curses as cr
from Text import *
from threading import Thread

class tapp:
    def __init__(self) -> None:
        self.win = cr.initscr()
        self.maxY,self.maxX = self.win.getmaxyx()
        self.alive = True
        self.func = True
        self.elements=[]
        self.events={}

        cr.cbreak()
        cr.noecho()
        cr.curs_set(0)
        cr.start_color()
        self.win.refresh()

    def add(self,element):
        self.elements.append(element)

    def __draw(self):
        while self.alive and self.func:
            self.win.erase()
            for element in self.elements:
                element.draw()
            self.win.refresh()

    def onkey(self,key,func):
        self.events[key] = func

    def __listenkey(self):
        while self.alive and self.func:
            k = self.win.getkey()
            try:
                self.events[k]()
            except:
                pass
    
    def start(self):
        Thread(target=self.__draw).start()
        Thread(target=self.__listenkey).start()
        return self
    
    def stop(self):
        self.alive = False
        cr.nocbreak()
        cr.echo()
        cr.curs_set(1)
        cr.endwin()
