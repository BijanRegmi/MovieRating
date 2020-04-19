import tkinter as tk

class scrollwindow:
    def __init__(self,parent,**kwargs):
        canvas = tk.Canvas(parent, bg = "grey", **kwargs)
        scrollbar = tk.Scrollbar(parent, orient = "vertical", command = canvas.yview)
        self.scrollframe = tk.Frame(canvas, **kwargs)

        self.scrollframe.bind("<Configure>",lambda x: canvas.configure(scrollregion = canvas.bbox("all")))
        canvas.create_window((0,0), window = self.scrollframe, anchor = "nw")
        canvas.configure(yscrollcommand = scrollbar.set)
        
        canvas.pack(side = "left", fill = "both")
        scrollbar.pack(side = "right", fill = "y")