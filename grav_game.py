"""Gravity game"""
import tkinter as tk


class Gui:
    """Object that contains the GUI for the game, used to launch the game"""
    def __init__(self):
        """Initialise user interface/ GUI related variables"""
        self.window = tk.Tk()
        self.window.title("grav test")
        self.window.geometry("850x500")
        self.window.configure(bg="gray")
        self.game = Game(self)
        self.game.start()


class Game:
    """Object that contains the game and all game related variables"""
    def __init__(self, gui):
        """Initialse game related variables"""
        self.gui = gui

        # Setup canvas
        self.canvas = tk.Canvas(self.gui.window, width=600, height=400, bg="lightblue")
        self.canvas.grid(column=1, row=1)

        # setup basic game objects
        self.square = self.canvas.create_rectangle(10, 10, 20, 20, fill="pink")
        self.endpad = self.canvas.create_rectangle(580, 110, 590, 120, fill="gold")
        self.game_vars = {"level": 0, "left": 0, "right": 0}

        self.cornerofblock = 40
        self.topoffblock = 100
        self.bottomoffblock = self.topoffblock + 10
        self.xvelocity = 10
        self.yvelocity = 5
        self.dashcooldown = 0
        self.movecooldown = 0
        self.dpadpos = 0
        self.platform_list = []
        self.jpad_list = []
        self.dashpad_list = []
        self.square = None

    def bind_keys(self):
        """Bind all the keys required for the game"""
        self.gui.window.bind("<k>", self.dev_cheat)
        self.gui.window.bind("i", self.reset)
        self.gui.window.bind("<d>", right)
        self.gui.window.bind("<a>", left)
        self.gui.window.bind("<s>", self.jump)
        self.gui.window.bind("<w>", self.jump)
        self.gui.window.bind("<space>", self.jump)
        self.gui.window.bind("<e>", self.dash)
        self.gui.window.bind("<q>", self.backdash)
        self.gui.window.bind("<u>", self.do_dashpad)


    def do_dashpad(event=None):
        global left, right
        if left == 1:
            canvas.after(30, dashpad_left)
            canvas.after(60, dashpad_left)
            canvas.after(90, dashpad_left)
            canvas.after(120, dashpad_left)
            canvas.after(150, dashpad_left)
            canvas.after(180, dashpad_left)
            canvas.after(210, dashpad_left)
            canvas.after(240, dashpad_left)
            canvas.after(270, dashpad_left)
            canvas.after(300, dashpad_left)
            canvas.after(330, dashpad_left)
            canvas.after(360, dashpad_left)
        if right == 1:
            canvas.after(30, dashpad_right)
            canvas.after(60, dashpad_right)
            canvas.after(90, dashpad_right)
            canvas.after(120, dashpad_right)
            canvas.after(150, dashpad_right)
            canvas.after(180, dashpad_right)
            canvas.after(210, dashpad_right)
            canvas.after(240, dashpad_right)
            canvas.after(270, dashpad_right)
            canvas.after(300, dashpad_right)
            canvas.after(330, dashpad_right)
            canvas.after(360, dashpad_right)
    def dashpad_right(event=None):
        xvelocity = 10
        canvas.move(square, xvelocity, 0)
    def dashpad_left(event=None):
        xvelocity = -10
        canvas.move(square, xvelocity, 0)
    def death(event=None):
        canvas.coords(square, 10, 10, 20, 20)
        dashcooldown = 0
    def jpad_up(event=None):
        yvelocity = -20
        canvas.move(square, 0, yvelocity, )
    def grav(event=None):
        canvas.move(square, 0, yvelocity, )

    def end(event=None):
        exit()


    def start(self, event=None):
        global square, yvelocity, square_pos, platform_pos, dashcooldown, level, endpad, movecooldown, right, left

        if level == 0:
            level = 1
            levels()
        yvelocity = 5
        square_pos = canvas.coords(square)
        if square == None:
            print("square does not exist - exiting the loop")
            return
        for platform in platform_list:
            platform_pos = canvas.coords(platform)
    #        if platform_pos[3] >= platform_pos[1] - 1:
    #            yvelocity = 0

            if (square_pos[0] < platform_pos[2] - 1 and square_pos[3] >= platform_pos[1]
                and square_pos[2] > platform_pos[0] and square_pos[3] <= platform_pos[1]):
                yvelocity = 0

            if (square_pos[1] >= platform_pos[1] and square_pos[1] <= platform_pos[1] and
                square_pos[0] < platform_pos[2] - 1 and square_pos[2] > platform_pos[0]):
                canvas.coords(square, square_pos[0], platform_pos[1] - 10, square_pos[2], platform_pos[1])
                yvelocity = 0

        for jpad in jpad_list:
            jpad_pos = canvas.coords(jpad)
            if (square_pos[0] < jpad_pos[2] - 1 and square_pos[3] >= jpad_pos[1]
                and square_pos[2] > jpad_pos[0] and square_pos[3] <= jpad_pos[1]):
                    canvas.after(0, jpad_up)
                    canvas.after(20, jpad_up)
                    canvas.after(40, jpad_up)
                    canvas.after(70, jpad_up)
                    canvas.after(100, jpad_up)
        for dashpad in dashpad_list:
            dashpad_pos = canvas.coords(dashpad)
            if (square_pos[0] < dashpad_pos[2] - 1 and square_pos[3] >= dashpad_pos[1]
                and square_pos[2] > dashpad_pos[0] and square_pos[3] <= dashpad_pos[1]):
                do_dashpad()

        #end of level
        end_pos = canvas.coords(endpad)
        if (square_pos[0] < end_pos[2] - 1 and square_pos[3] >= end_pos[1]
                and square_pos[2] > end_pos[0] and square_pos[3] <= end_pos[1]):
            dashcooldown = 0
            print(level)
            level += 1
            canvas.coords(square, 10, 10, 20, 20)
            print(level)
            canvas.after(0, levels)
        if square_pos[2] <= 0:
            canvas.coords(square, -80, -80, -70, -70)
            #death
        if square_pos[3] >= 350:
            death()
        if square_pos[3] <= 0:
            canvas.coords(square, 10, 10, 20, 20)
        canvas.after(5, func=start)
        dashcooldown -= 1
        movecooldown -= 1
        if dashcooldown >= 1:
            canvas.itemconfig(square, fill='white')
        else:
            canvas.itemconfig(square, fill='pink')
        grav()

    def right(event=None):
        global movecooldown, left, right
        left = 0
        right = 1
        if movecooldown <= 0:
            movecooldown = 2
            canvas.move(square, xvelocity, 0)
    #    square_pos = canvas.coords(square)
    #    for platform in platform_list:
    #        platform_pos = canvas.coords(platform)
    #        if square_pos[0] == platform_pos[2] - 1 and square_pos[3] >= platform_pos[1]:
    #            return

    def left(event=None):
        global movecooldown, left, right
        left = 1
        right = 0
        if movecooldown <= 0:
            movecooldown = 2
            canvas.move(square, -xvelocity, 0)
    #def rightspace(event=None):
    #    global square,yvelocity,canvas
    #    if yvelocity != 0:
    #        return
    #    yvelocity = 30
    #    canvas.move(square,xvelocity,-yvelocity)
    #    yvelocity = 5

    def jump(self, event=None):
        if yvelocity != 0:
            return
        # loop to do something multiple times,
        # range function will call function with number "i" starting with 30, till it gets to 180
        # it will do steps of "30" between these numbers. try print(i) to see what is printed
        for i in range(30, 180, 30):
            self.canvas.after(i, self.jump_move)

    def jump_move(self, event=None):
        self.yvelocity = 10
        self.canvas.move(self.square, 0, -self.yvelocity)

    def dash(self, event=None):
        if self.dashcooldown <= 0:
            self.dashcooldown = 20
            for i in range(30, 120, 30):
                self.canvas.after(i, self.dash_move)

    def dash_move(self, event=None):
        xvelocity = 10
        self.canvas.move(self.square, self.xvelocity, 0)

    def backdash(self, event=None):
        if self.dashcooldown <= 0:
            self.dashcooldown = 20
            for i in range(30, 120, 30):
                self.canvas.after(i, self.backdash_move)

    def backdash_move(event=None):
        xvelocity = -10
        self.canvas.move(self.square, self.xvelocity, 0)

    def dev_cheat(self, event=None):
        """dev cheat, remove when decently done"""
        self.canvas.coords(self.square, 580, 90, 590, 100)

    def reset(self, event=None):
        global level, dashcooldown
        dashcooldown = 0
        print(level)
        level = 0
        self.canvas.coords(self.square, 10, 10, 20, 20)
        print(level)
        levels()
#def backsuperjump(event=None):
#    global square,yvelocity,xvelocity,canvas
#    if yvelocity != 0:
#        return
#    yvelocity = 50
#    xvelocity = 30
#    canvas.move(square,-xvelocity,-yvelocity)
#    xvelocity = 10
#    yvelocity = 5


#button = tk.Button(window, text = "start", bg="white")
#button.grid(column=1,row=1,)
#button.bind("<Button-1>",start)
class LevelManager:
    """Defines a level in the game"""
    def __init__(self):
        """Initialise the variables relating to a level"""
        label_blank = tk.Label(window,  textvariable = "\n   \n ", bg="gray")
        label_blank.grid(column=1, row=0)
        label = tk.Label(window, text = "press s or w to jump, \ne to dash, \nq to backwards dash, \nd to go forwards \nand a to go back\n\nIf your player is white,\n you cannot dash.\n If your player is pink,\n you can.", bg="gray")
        label.grid(column=1, row=2)
        sun = canvas.create_rectangle(570, 10, 590, 30, fill="gold")
        floor = canvas.create_rectangle(0, 600, 800, 300, fill="orange", outline="red")
        label.grid(column=0, row=1, )

    def level_loader(self, i):
        """Given a certain level number i will load this level"""
        global platform_list, jpad_list, endpad_list, dashpad_list
        canvas.delete("level")
        if level == 1:
            platform1 = canvas.create_rectangle(0, topoffblock, cornerofblock, bottomoffblock,
                                                fill="gray",tag="level")
            platform2 = canvas.create_rectangle(100, 150, 60, 160, fill="gray", tag="level")
            platform3 = canvas.create_rectangle(140, 190, 180, 200, fill="gray", tag="level")
            platform4 = canvas.create_rectangle(250, 140, 200, 150, fill="gray", tag="level")
            platform5 = canvas.create_rectangle(260, 130, 250, 140, fill="gray", tag="level")
            platform6 = canvas.create_rectangle(270, 120, 260, 130, fill="gray", tag="level")
            platform7 = canvas.create_rectangle(280, 110, 270, 120, fill="gray", tag="level")
            platform8 = canvas.create_rectangle(310, 100, 280, 110, fill="gray", tag="level")
            platform9 = canvas.create_rectangle(340, 80, 370, 90, fill="gray", tag="level")
            platform10 = canvas.create_rectangle(370, 120, 380, 130, fill="gray", tag="level")
            platform11 = canvas.create_rectangle(430, 130, 420, 140, fill="gray", tag="level")
            platform12 = canvas.create_rectangle(450, 110, 440, 120, fill="gray", tag="level")
            platform13 = canvas.create_rectangle(480, 110, 800, 120, fill="gray", tag="level")

            jpad1 = canvas.create_rectangle(170, 190, 180, 200, fill="lightgreen", tag="level")
            jpad2 = canvas.create_rectangle(310, 100, 300, 110, fill="lightgreen", tag="level")

            platform_list = [platform1, platform2, platform3, platform4, platform5, platform6,
                             platform7, platform8, platform9, platform10, platform11, platform12,
                             platform13]
            dashpad_list = []
            jpad_list = [jpad1, jpad2]

        if level == 2:
            platform1 = canvas.create_rectangle(0, topoffblock, cornerofblock, bottomoffblock,
                                                fill="gray", tag="level")
            platform2 = canvas.create_rectangle(100, 100, 140, 110, fill="gray", tag="level")
            platform3 = canvas.create_rectangle(250, 290, 270, 300, fill="gray", tag="level")
            platform4 = canvas.create_rectangle(280, 290, 300, 300, fill="gray", tag="level")
            platform5 = canvas.create_rectangle(350, 260, 370, 270, fill="gray", tag="level")
            platform6 = canvas.create_rectangle(410, 230, 450, 240, fill="gray", tag="level")
            platform7 = canvas.create_rectangle(440, 170, 450, 180, fill="gray", tag="level")
            platform8 = canvas.create_rectangle(440, 110, 450, 120, fill="gray", tag="level")
            platform9 = canvas.create_rectangle(530, 110, 590, 120, fill="gray", tag="level")
            jpad1 = canvas.create_rectangle(360, 260, 370, 270, fill="lightgreen", tag="level")
            jpad2 = canvas.create_rectangle(440, 110, 450, 120, fill="lightgreen", tag="level")
            platform_list = [platform1, platform2, platform3, platform4, platform5, platform6, platform7, platform8, platform9]
            dashpad_list = []
            jpad_list = [jpad1, jpad2]
        if level == 3:
            platform1 = canvas.create_rectangle(0, topoffblock, cornerofblock, bottomoffblock, fill="gray", tag="level")
            platform2 = canvas.create_rectangle(110, 90, 150, 100, fill="gray", tag="level")
            dash_pad1 = canvas.create_rectangle(130, 90, 150, 100, fill="blue", tag="level")
            platform_list = [platform1, platform2]
            dashpad_list = [dash_pad1]
            jpad_list = []
        if level >= 4:
            platform1 = canvas.create_rectangle(0, topoffblock, cornerofblock, bottomoffblock, fill="gray", tag="level")
            platform_list = [platform1]
            dashpad_list = []
            jpad_list = []
        endpad = canvas.create_rectangle(580, 110, 590, 120, fill="gold")

if __name__ == "__main__":
    game_gui = Gui()
    input()


# Changes done by jake:
# Added a space after every comma, not necessary, but looks nicer.
# Added "dashpad_list" to global variables, this fixed the bug with dashpads not being checked
# renamed "dashpad" function to "do_dashpad" as it was clashing with "dashpad" object in list call
# changed keybind "<u>" to use "do_dashpad" as I assume these are connected, but I am unsure why
