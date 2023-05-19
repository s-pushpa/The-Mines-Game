from tkinter import Button

class Cell:
    def __int__(self, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object = None

    def create_btn_object(self, location):
        btn = Button ( location, text='Text')
        # defining the events/actions for the button
        btn.bind('<Button-1>', self.left_click_actions)    # <Button-1> is for left click and <Button-3> is for the right click
        btn.bind('<Button-3>', self.right_click_actions)
        self.cell_btn_object = btn

    def left_click_actions(self, event):
        print(event)
        print("Left clicked")

    def right_click_actions(self, event):
        print(event)
        print("Right clicked")