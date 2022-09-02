from turtle import Turtle
FONT = ("Courier", 24, "normal")
FONT_GAME_UP = ("Courier", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.start_level=1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-270,250)
        self.write(F"LEVEL: {self.start_level}",False,"left",FONT)


    def level_2(self):
        self.start_level+=1
        self.update_scoreboard()

    def you_won(self):
        # self.color()
        self.goto(0,0)
        self.write("YOU WON 😎",False,"center",FONT_GAME_UP)

    def you_lose(self):
        self.goto(0, 0)
        self.write("GAME OVER 😥",False,"center",FONT_GAME_UP)
