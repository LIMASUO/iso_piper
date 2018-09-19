from tkinter import *
import isoplane

BUTTON_PANEL_WIDTH = 130


def test_function():
    print("foo")


class ButtonWrapper(Button):

    def __init__(self, name, func, height, parent_container):
        Button.__init__(self)
        self.container = Frame(parent_container, padx=5, pady=5, width=BUTTON_PANEL_WIDTH)
        self.button_object = Button(self.container, text=name, height=height)
        self.button_object.configure(command=lambda: func())
        self.button_object.pack(fill=X, expand=YES)
        self.container.pack(side=TOP, fill=X)


class ButtonsPanel:

    def __init__(self):
        self.main_frame = Frame(bd=3, relief=GROOVE)
        right_margin = Frame(width=5)
        right_margin.pack(side=RIGHT)
        width_controller = Frame(self.main_frame, width=BUTTON_PANEL_WIDTH)
        width_controller.pack()
        self.main_frame.pack(side=LEFT, fill=Y)

    def get_frame(self):
        return self.main_frame


class MessageBox(Label):
    def __init__(self):
        Label.__init__(self)


class DynamicCanvas(Canvas):

    def canvas_manager(self):
        # self.canvas_frame.bind("<Configure>", self.on_resize)
        self.canvas.pack(fill=BOTH, expand=YES)
        self.canvas_frame.pack(side=RIGHT, fill=BOTH, expand=YES)

    def on_resize(self, event):
        parent_width = self.parent.root.winfo_width()
        self.canvas_frame.config(width=parent_width-BUTTON_PANEL_WIDTH)

    def __init__(self, parent=None):
        Canvas.__init__(self)
        self.parent = parent
        self.canvas_frame = Frame()
        self.canvas = Canvas(self.canvas_frame, background='black')
        self.canvas_manager()


class CommandInput(Entry):
    def __init__(self, parent=None):
        Entry.__init__(self)
        self.parent = parent
        self.entry_container = Frame()
        self.separator = Frame(self.entry_container, height=10)
        self.separator.pack()
        self.entry = Entry(self.entry_container, font='System, 11', bg='silver')
        self.entry.pack(fill=BOTH, expand=YES)
        self.entry.focus()
        self.entry_container.pack(side=BOTTOM, fill=X)


class MainWindow:

    def core_margins(self):
        top_margin = Frame(height=self.margin_size)
        top_margin.pack(side=TOP)
        bottom_margin = Frame(height=self.margin_size)
        bottom_margin.pack(side=BOTTOM)
        right_margin = Frame(width=self.margin_size)
        right_margin.pack(side=RIGHT)
        left_margin = Frame(width=self.margin_size)
        left_margin.pack(side=LEFT)

    def __init__(self):
        self.margin_size = 10
        self.root = Tk()
        self.root.geometry('800x580')
        self.root.title("Piping Isometrics Generator")
        self.core_margins()
        self.entry = CommandInput(self)
        self.canvas = DynamicCanvas(self)
        isoplane.draw_isoplane(self.canvas.canvas)
        self.panel = ButtonsPanel()
        self.test_button1 = ButtonWrapper("Toggle Isoplane", test_function, 1, self.panel.get_frame())
        self.test_button2 = ButtonWrapper("Create Elbow", test_function, 1, self.panel.get_frame())


def main():
    app = MainWindow()
    app.root.mainloop()


if __name__ == '__main__':
    main()

