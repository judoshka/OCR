import pytesseract
from PIL import Image, ImageTk
from tkinter import filedialog as fd
from tkinter import messagebox
import tkinter as tk

class App(tk.Tk):
    def open(self):
        file_name = fd.askopenfilename()
        self.filename_entry.delete(0, tk.END)
        self.filename_entry.insert(0, file_name)
        # img = tk.PhotoImage(file=self.filename_entry.get())
        img = Image.open(self.filename_entry.get())
        tatras = ImageTk.PhotoImage(img)
        self.image.create_image(20, 20, anchor=tk.NW, image=tatras)

    def recognize(self):
        filename = self.filename_entry.get()
        messagebox.showinfo('Recognize', pytesseract.image_to_string(Image.open(filename)))

    def __init__(self):
        super().__init__()
        self.title = 'OCR Window'
        self.main_frame = tk.Frame(master=self, bd=2)
        self.filename_entry = tk.Entry(self.main_frame, bd=2, width=32)
        self.open_btn = tk.Button(self.main_frame, text='open', command=self.open)
        self.work_btn = tk.Button(self.main_frame, text='Do it', command=self.recognize)
        self.image = tk.Canvas(self, width=300, height=300)
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

        self.main_frame.grid(column=0, row=0, sticky="WESN")
        self.image.grid(column=0, row=1, sticky="WESN")
        self.filename_entry.grid(column=0, columnspan=2, row=0, sticky="WESN")
        self.open_btn.grid(column=2, row=0, sticky="WESN")
        self.work_btn.grid(column=3, row=0, sticky="WESN")


def main():
    app = App()
    app.mainloop()


if __name__ == '__main__':
    main()