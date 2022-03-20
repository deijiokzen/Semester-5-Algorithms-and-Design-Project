import tkinter as tk
from tkinter import *
from MST_PRIM import *
from MST_KRUSKAL import *
from DJIKSTRA import *
from FloydWarshall import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from BELLMANFORD import *
class Keep(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        windowWidth = 800
        windowHeight = 600

        # Info for centering the window in the screen
        offsetLeft = int((self.winfo_screenwidth() - windowWidth) / 2)
        offsetTop = int((self.winfo_screenheight() - windowHeight) / 2)

        # Positions the window in the center of the screen
        self.geometry('{}x{}+{}+{}'.format(windowWidth, windowHeight, offsetLeft, offsetTop))
        self.config(bg='#0f4b6e')

        self.shared_data ={
            "filename": tk.StringVar(),

        }

        self.frames = {
            'StartPage': StartPage(self, self),
            'PageOne': PageOne(self, self),
            'PageTwo': PageTwo(self, self),
            'PageThree': PageThree(self, self),
            'PageFour':PageFour(self,self),
            'PageFive': PageFive(self, self),
            'PageSix': PageSix(self, self)


        }

        self.current_frame = None
        self.show_frame('StartPage')

    def show_frame(self, name):
        if self.current_frame:
            self.current_frame.forget()
        self.current_frame = self.frames[name]
        self.current_frame.pack()

        self.current_frame.update_widgets() # <-- update data in widgets


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.label = tk.Label(self, text="Enter File Name Here:")  # <-- create empty label
        self.label.pack()

        self.entry1 = tk.Entry(self, textvariable=self.controller.shared_data["filename"])
        self.entry1.pack()
        button = tk.Button(self, text="Submit", command=lambda: controller.show_frame("PageOne"))
        button.pack()


        frame1 = tk.Frame(self, width=1000, height=1000, background="bisque")


        frame1.pack(side="bottom",fill=None, expand=False)



    def update_widgets(self):

        pass

class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        frame1 = tk.Frame(self, width=1000, height=100, background='#0f4b6e')

        frame1.pack(side="top", fill=None, expand=False)
        frame1.pack_propagate(False)
        self.label1 = tk.Label(frame1, text="Welcome To Algorithms With Saud Ahmed Abbasi!",bg='#0f4b6e',
    fg='white',font=("Arial", 25))  # <-- create empty label
        self.label1.pack()
        self.label = tk.Label(frame1, text="",bg='#0f4b6e',
    fg='white',font=("Arial", 10)) # <-- create empty label
        self.label.pack(pady=20)



        button = tk.Button(self, text="Primm's Algorithm", command=lambda: controller.show_frame("PageTwo"))
        button.pack(pady=2)


        button2 = tk.Button(self, text="Kruskal's Algorithm" , command=lambda: controller.show_frame("PageThree"))
        button2.pack(pady=2)

        button3 = tk.Button(self, text="Djikstra's Algorithm", command=lambda: controller.show_frame("PageFour"))
        button3.pack(pady=2)

        button4 = tk.Button(self, text="Floyd Warshall", command=lambda: controller.show_frame("PageFive"))
        button4.pack(pady=2)

        button5 = tk.Button(self, text="Bellman Ford", command=lambda: controller.show_frame("PageSix"))
        button5.pack(pady=2)


        self.labelOG = tk.Label(self, text="Original Graph !",bg='black',
    fg='white')  # <-- create empty label
        self.labelOG.pack()
    def update_widgets(self):

        self.label["text"] = "Welcome, your input file is : {}".format(self.controller.shared_data["filename"].get()) # <-- update text in label
        getglobaldata(self.controller.shared_data["filename"].get())

        f = Figure(figsize=(9, 9), dpi=150)
        a = f.add_subplot(111)
        a.plot()

        pos = nx.get_node_attributes(G, 'pos')

        nx.draw(G, pos, with_labels=1, arrows=True, node_color='brown', ax=a)

        canvas = FigureCanvasTkAgg(f, self)
        # canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)




class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.label1 = tk.Label(self, text="Primm's MST Reduction!")  # <-- create empty label
        self.label1.pack()

        button = tk.Button(self, text="Back to Previous Page", command=lambda: controller.show_frame("PageOne"))
        button.pack()




    def update_widgets(self):
        #print(self.controller.shared_data["filename"].get())
        GlobalData=getglobaldata(self.controller.shared_data["filename"].get())
        prim = PrimmGraph(GlobalData[2], GlobalData[0])
        edges = prim.primMST()

        self.label2 = tk.Label(self, text="Reduction Cost Is: {}".format(edges[0]))
        self.label2.pack()


        self.drawgraph(edges[1])

    def drawgraph(self, edges):
            f = Figure(figsize=(9, 9), dpi=150)
            a = f.add_subplot(111)
            a.plot()

            pos = nx.get_node_attributes(G, 'pos')

            nx.draw(G, pos, with_labels=1, arrows=True, node_color='brown', ax=a)

            canvas = FigureCanvasTkAgg(f, self)
            # canvas.show()
            canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

            toolbar = NavigationToolbar2Tk(canvas, self)
            toolbar.update()
            canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
            returngraphtooriginal(edges)

class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.label1 = tk.Label(self, text="Kruskal's MST Reduction!")  # <-- create empty label
        self.label1.pack()

        button = tk.Button(self, text="Back to Previous Page", command=lambda: controller.show_frame("PageOne"))
        button.pack()





    def update_widgets(self):
        print(self.controller.shared_data["filename"].get())
        GlobalData=getglobaldata(self.controller.shared_data["filename"].get())
        g = KruskalGraph(GlobalData[0])
        g.list_edge_add(GlobalData[2])
        edges=g.kruskal()

        self.label2 = tk.Label(self, text="Reduction Cost Is: {}".format(edges[0]))
        self.label2.pack()

        self.drawgraph(edges[1])

    def drawgraph(self, edges):
            f = Figure(figsize=(9, 9), dpi=150)
            a = f.add_subplot(111)
            a.plot()
            pos = nx.get_node_attributes(G, 'pos')
            nx.draw(G, pos, with_labels=1, arrows=True, node_color='brown', ax=a)

            canvas = FigureCanvasTkAgg(f, self)
            # canvas.show()
            canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

            toolbar = NavigationToolbar2Tk(canvas, self)
            toolbar.update()
            canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
            returngraphtooriginal(edges)
class PageFour(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.label = tk.Label(self, text="Djikstra All Paths:")  # <-- create empty label
        button = tk.Button(self, text="Back to Previous Page", command=lambda: controller.show_frame("PageOne"))
        button.pack()
        self.i =0
    def update_widgets(self):
        if (self.i < 1):
            self.i += 1
            g = Graph()
            GlobalData = getglobaldata(self.controller.shared_data["filename"].get())
            x = g.dijkstra(GlobalData[3], GlobalData[1])
            # print(x)
            # self.label1 = tk.Label(self, text=x)  # <-- create empty label
            # self.label1.pack()
            v = Scrollbar(self)

            # attach Scrollbar to root window on
            # the side
            v.pack(side=RIGHT, fill=Y)
            t = Text(self, wrap=NONE,
                     yscrollcommand=v.set)
            t.insert(END, x)
            t.config(state=NORMAL)
            t.pack(side=BOTTOM, fill=X)
            v.config(command=t.yview)
class PageFive(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.label = tk.Label(self, text="Floyd Warshall:")  # <-- create empty label
        button = tk.Button(self, text="Back to Previous Page", command=lambda: controller.show_frame("PageOne"))
        button.pack()
        self.i =0
    def update_widgets(self):

        if (self.i < 1):
            self.i += 1
            GlobalData = getglobaldata(self.controller.shared_data["filename"].get())
            x = floyd(GlobalData[3], GlobalData[0])
            # print(x)
            # self.label1 = tk.Label(self, text=x)  # <-- create empty label
            # self.label1.pack()
            v = Scrollbar(self)

            # attach Scrollbar to root window on
            # the side
            h = Scrollbar(self, orient='horizontal')
            h.pack(side=BOTTOM, fill=X)
            v.pack(side=RIGHT, fill=Y)
            t = Text(self, wrap=NONE, xscrollcommand=h.set,
                     yscrollcommand=v.set)
            t.insert(END, x)
            t.config(state=NORMAL)
            t.pack(side=BOTTOM, fill=X)
            h.config(command=t.xview)
            v.config(command=t.yview)

class PageSix(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.label = tk.Label(self, text="BellmanFord:")  # <-- create empty label
        button = tk.Button(self, text="Back to Previous Page", command=lambda: controller.show_frame("PageOne"))
        button.pack()
        self.i=0
    def update_widgets(self):
        if (self.i < 1):
            self.i+=1
            GlobalData = getglobaldata(self.controller.shared_data["filename"].get())
            g = BellmanGraph(GlobalData[0])
            g.list_edge_add(GlobalData[3])

            x = g.BellmanFord(GlobalData[1])
            print(x)
            # print(x)
            # self.label1 = tk.Label(self, text=x)  # <-- create empty label
            # self.label1.pack()
            v = Scrollbar(self)

            # attach Scrollbar to root window on
            # the side
            h = Scrollbar(self, orient='horizontal')
            h.pack(side=BOTTOM, fill=X)
            v.pack(side=RIGHT, fill=Y)
            t = Text(self, wrap=NONE, xscrollcommand=h.set,
                     yscrollcommand=v.set)
            t.insert(END, x)
            t.config(state=NORMAL)
            t.pack(side=BOTTOM, fill=X)
            h.config(command=t.xview)
            v.config(command=t.yview)



if __name__ == "__main__":
    keep = Keep()
    keep.mainloop()