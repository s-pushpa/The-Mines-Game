# defining cells, their actions/events (nature), numbers, height width,
# basically the file cell.py contain all the information about cells being used in the game

from tkinter import Button
import random
import settings


import settings


class Cell:
    all = []
    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object = None
        self.x = x
        self.y = y

        # append the object to the cell.all list
        Cell.all.append(self)

    def create_btn_object(self, location):
        btn = Button ( location,  width=12, height=4, text=f"{self.x},{self.y}")
      # btn = Button( location, width=12, height=4,)
        # defining the events/actions for the button
        btn.bind('<Button-1>', self.left_click_actions)    # <Button-1> is for left click and <Button-3> is for the right click
        btn.bind('<Button-3>', self.right_click_actions)
        self.cell_btn_object = btn

    # functions for events
    def left_click_actions(self, event):
        # print(event)
        # print("Left clicked")
        if self.is_mine:
            self.show_mine()
        else:
            self.show_cell()
    # function for return the cell object based on the value of x, y
    def get_cell_by_axis(self, x,y):
        for cell in Cell.all:
           if cell.x == x and cell.y == y:
               return cell


    def show_cell(self):
       # print(self.get_cell_by_axis(0,0))
        surrounded_cell = [
            self.get_cell_by_axis(self.x-1, self.y-1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y+1),
            self.get_cell_by_axis(self.x, self.y-1),
            self.get_cell_by_axis(self.x+1, self.y-1),
            self.get_cell_by_axis(self.x+1, self.y),
            self.get_cell_by_axis(self.x+1, self.y+1),
            self.get_cell_by_axis(self.x, self.y+1),

        ]
    # function for game interruption and display a message
    def show_mine(self):
        self.cell_btn_object.configure(bg='red')


    def right_click_actions(self, event):
        print(event)
        print("Right clicked")

    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(Cell.all, settings.MINES_COUNT)
        for picked_cells in picked_cells:
            picked_cells.is_mine = True

    # function will display the cells with their coordinates
    def __repr__(self):
        return f"Cell({self.x},{self.y})"