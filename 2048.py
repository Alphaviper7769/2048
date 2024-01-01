import tkinter as tk
import colors as c

class Game(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.master.title("2048")
        
        self.main_grid = tk.Frame(
            self,bg=c.GAME_COLOR,bd=3,width=600,height=600
        )
        
        self.main_grid.grid(pady=(100,0))
        
    
    def make_GUI(self):
        
        self.grid