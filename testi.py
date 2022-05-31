# import tkinter as tk

# class Page(tk.Frame):
#     def __init__(self, *args, **kwargs):
#         tk.Frame.__init__(self, *args, **kwargs)
#     def show(self):
#         self.lift()

# class Page1(Page):
#    def __init__(self, *args, **kwargs):
#        Page.__init__(self, *args, **kwargs)
#        label = tk.Label(self, text="This is page 1")
#        label.pack(side="top", fill="both", expand=True)

# class Page2(Page):
#    def __init__(self, *args, **kwargs):
#        Page.__init__(self, *args, **kwargs)
#        self.label = tk.Label(self, text="This is page 2")
#        self.label.pack(side="top", fill="both", expand=True)

# class Page3(Page):
#    def __init__(self, *args, **kwargs):
#        Page.__init__(self, *args, **kwargs)
#        label = tk.Label(self, text="This is page 3")
#        label.pack(side="top", fill="both", expand=True)

# class MainView(tk.Frame):
#     def __init__(self, *args, **kwargs):
#         tk.Frame.__init__(self, *args, **kwargs)
#         p1 = Page1(self)
#         p2 = Page2(self)
#         p3 = Page3(self)

#         buttonframe = tk.Frame(self)
#         container = tk.Frame(self)
#         buttonframe.pack(side="top", fill="x", expand=False)
#         container.pack(side="top", fill="both", expand=True)

#         p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
#         p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
#         p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

#         b1 = tk.Button(buttonframe, text="Page 1", command=p1.show)
#         b2 = tk.Button(buttonframe, text="Page 2", command=p2.show)
#         b3 = tk.Button(buttonframe, text="Page 3", command=p3.show)

#         b1.pack(side="left")
#         b2.pack(side="left")
#         b3.pack(side="left")

#         p1.show()


# root = tk.Tk()
# main = MainView(root)
# main.pack(side="top", fill="both", expand=True)
# root.wm_geometry("400x400")
# root.mainloop()
# import tkinter as tk
# from tkinter import ttk

# class MainApplication(tk.Tk):
#     def __init__(self):
#         super().__init__()

#         self.title("Example")
#         self.geometry('300x300')

#         self.notebook = ttk.Notebook(self)

#         self.Frame1 = Frame1(self.notebook)
#         self.Frame2 = Frame2(self.notebook)

#         self.notebook.add(self.Frame1, text='Frame1')
#         self.notebook.add(self.Frame2, text='Frame2')

#         self.notebook.pack()

# class Frame1(ttk.Frame):
#     def __init__(self, container):
#         super().__init__()

#         self.labelA = ttk.Label(self, text = "This is on Frame One")
#         self.labelA.grid(column=1, row=1)

# class Frame2(ttk.Frame):
#     def __init__(self, container):
#         super().__init__()

#         self.labelB = ttk.Label(self, text = "This is on Frame Two")
#         self.labelB.grid(column=1, row=1)

# if __name__ == '__main__':
#     app = MainApplication()
#     app.mainloop()
#Import the required libraries
import tkinter as tk  # python 3.x
# import Tkinter as tk # python 2.x

class Example(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        # valid percent substitutions (from the Tk entry man page)
        # note: you only have to register the ones you need; this
        # example registers them all for illustrative purposes
        #
        # %d = Type of action (1=insert, 0=delete, -1 for others)
        # %i = index of char string to be inserted/deleted, or -1
        # %P = value of the entry if the edit is allowed
        # %s = value of entry prior to editing
        # %S = the text string being inserted or deleted, if any
        # %v = the type of validation that is currently set
        # %V = the type of validation that triggered the callback
        #      (key, focusin, focusout, forced)
        # %W = the tk name of the widget

        vcmd = (self.register(self.onValidate),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        self.entry = tk.Entry(self, validate="key", validatecommand=vcmd)
        self.text = tk.Text(self, height=10, width=40)
        self.entry.pack(side="top", fill="x")
        self.text.pack(side="bottom", fill="both", expand=True)

    def onValidate(self, d, i, P, s, S, v, V, W):
        self.text.delete("1.0", "end")
        self.text.insert("end","OnValidate:\n")
        self.text.insert("end","d='%s'\n" % d)
        self.text.insert("end","i='%s'\n" % i)
        self.text.insert("end","P='%s'\n" % P)
        self.text.insert("end","s='%s'\n" % s)
        self.text.insert("end","S='%s'\n" % S)
        self.text.insert("end","v='%s'\n" % v)
        self.text.insert("end","V='%s'\n" % V)
        self.text.insert("end","W='%s'\n" % W)

        # Disallow anything but lowercase letters
        if S == S.lower():
            return True
        else:
            self.bell()
            return False

if __name__ == "__main__":
    root = tk.Tk()
    Example(root).pack(fill="both", expand=True)
    root.mainloop()