# coding: utf-8
import tkinter as tk
# import os
# import subprocess

class Screen:
    def onDragged(self, e):
        w = self.size // 30
        self.canvas.create_oval(e.x - w, e.y - w, e.x + w, e.y + w,
                                fill = "white", outline = "white")
        
    def Clear(self):
        self.canvas.create_rectangle(0, 0, self.size, self.size, fill = "black")

    def Save(self):
        print("Saved")
        self.canvas.postscript(file = "tmp.ps", colormode="color")
        # process = subprocess.Popen(["ps2pdf", "tmp.ps", "result.pdf"], shell=True)
        # process.wait() 

    def __init__(self):
        self.size = 300
        self.window = tk.Tk()
        self.canvas = tk.Canvas(self.window, bg = "black",
                                width = self.size, height = self.size)
        self.canvas.pack()
        self.canvas.create_rectangle(0, 0, self.size, self.size, fill = "black")
        
        self.quitButton = tk.Button(self.window,
                                    text = "Quit",
                                    command = self.window.quit)        
        self.quitButton.pack(side = tk.RIGHT)
        
        self.clearButton = tk.Button(self.window,
                                     text = "Clear",
                                     command = self.Clear)        
        self.clearButton.pack(side = tk.RIGHT)

        self.saveButton = tk.Button(self.window,
                                    text = "Save",
                                    command = self.Save)        
        self.saveButton.pack(side = tk.RIGHT)
        
        self.canvas.bind("<B1-Motion>", self.onDragged)

        self.window.mainloop()

Screen()
