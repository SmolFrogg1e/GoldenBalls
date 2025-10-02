import turtle
import p05
'''
class MozgoPont(turtle.Turtle):
    def __init__(self, szin, x, y, sebesseg):
        super().__init__()
        self.shape("circle")
        self.color(szin)
        self.penup()
        self.speed(5)
        self.goto(x,y)
        self.sebesseg = sebesseg

    def inditas(self):
        self.forward(self.sebesseg)
'''


ablak = turtle.Screen()
ablak.title("pontverseny")
ablak.bgcolor("black")

def inditas():
    turtle.forward(10)

def kilepes():
    ablak.bye()

pont1 = p05.MozgoPont("cyan", -200, 0, 15)
pont2 = p05.MozgoPont("magenta", -200, 50, 10)
pont3 = p05.MozgoPont("yellow", -200, 100, 20)

ablak.listen()

ablak.onkey(kilepes, "Escape")
ablak.onkey(pont1.inditas, "d")
ablak.onkey(pont2.inditas, "k")
ablak.onkey(pont3.inditas, "l")

turtle.mainloop()