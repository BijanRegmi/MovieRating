import tkinter as tk
from tkinter import ttk
from urllib.request import urlopen
from io import BytesIO
from PIL import Image,ImageTk
import apiconnection as api
from scrollwindow import *

def main(window):
    root = tk.Frame(window)
    root.pack()

    input_frame = tk.LabelFrame(root, text = "Search", width = 580, padx = 10, pady = 10)
    input_frame.grid(row = 0, column = 0, pady = 10, sticky = "nesw")
    
    tk.Label(input_frame, text = "Title*").grid(row = 0, column = 0)
    title_field = tk.Entry(input_frame, width = 50)
    title_field.grid(row = 0, column = 1, columnspan = 6, pady = 10, padx = 10)

    year = tk.StringVar()
    tk.Label(input_frame, text = "Year").grid(row = 1, column = 0, padx = 10, pady = 10)
    year_field = ttk.Combobox(input_frame, width = 10, values = tuple(range(1970,2020)), textvariable = year)
    year_field.grid(row = 1, column = 1, padx = 10, pady = 10)

    plot = tk.StringVar()
    tk.Label(input_frame, text = "Plot").grid(row  = 1, column = 2, padx = 10, pady = 10)
    plot_field = ttk.Combobox(input_frame, values = ("Short", "Full"), width = 5, textvariable = plot)
    plot_field.grid(row = 1, column = 3, padx = 10, pady = 10)

    category = tk.StringVar()
    tk.Label(input_frame, text = "Category").grid(row = 1, column = 4, padx = 10, pady = 10)
    category_field = ttk.Combobox(input_frame, values = ("Movie", "Series", "Episode"), width = 6, textvariable = category)
    category_field.grid(row = 1, column = 5, padx = 10, pady = 10)

    tk.Label(input_frame,text = "Fields with * must be provided", fg = "green", font = ("Helvetica",8)).grid(row = 2, column = 0, columnspan = 5, sticky = "sw")
    search = tk.Button(input_frame, text = "Search", command = lambda: output(root))
    search.grid(row = 2, column = 5)


def output(root):
    output_frame = tk.LabelFrame(root, text = "RESULT", width = 400, height = 400, padx = 10, pady = 10)
    output_frame.grid(row = 1, column = 0, pady = 10)
    
    childs = (root.winfo_children())[0].winfo_children()
    title_box, year_box, plot_box, category_box = childs[1], childs[3], childs[5], childs[7]
    
    # Returns data fetched by the api
    ret = api.movie_data(title = title_box.get(), plot = plot_box.get(), category = category_box.get(), year = year_box.get())
    
    OPTIONS = ['Title', 'Year', 'Rated', 'Released', 'Runtime', 'Genre', 'Director', 'Writer', 'Actors', 'Plot', 'Language', 'Country', 'Awards', 'Metascore', 'imdbRating', 'imdbVotes', 'imdbID', 'Type', 'DVD', 'BoxOffice', 'Production']
    
    if ret["Response"] == "True":
        win = scrollwindow(output_frame, width = 465)
        frame = win.scrollframe

        for x in OPTIONS:
            tk.Label(frame, text = x + " : " + str(ret.get(x)), width = 60, wraplength = 400).pack(expand = True, anchor = "w", pady = 2)
        
        URL = urlopen(ret["Poster"])
        raw = URL.read()
        URL.close()

        #converting raw data to bytes
        byte = BytesIO(raw)

        #opening image from the bytes
        image = Image.open(byte).resize((200,200))

        #tkinter compatible image
        photo = ImageTk.PhotoImage(image)
        
        image_frame = tk.LabelFrame(root, text = "Poster", pady = 10, padx = 10)
        image_frame.grid(row = 2, column = 0, pady = 10)

        label = tk.Label(image_frame, image = photo)
        #without this re-assignment photo didn't load
        label.image = photo
        label.pack()
    else:
        tk.Label(output_frame, text = "OOPS! Something Went Wrong\nTry checking these options\n\nMake sure you have active internet connection.\nMake sure title is provided", width = 55).pack(anchor = "w", pady = 5)
    
    
    
if __name__ == "__main__":
    window = tk.Tk()
    window.geometry("600x780")
    main(window)
    window.mainloop()