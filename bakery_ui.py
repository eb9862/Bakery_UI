import tkinter
from tkinter import *


class BakeryView:
    def __init__(self, window):
        self.__init_window(window)

    def __init_window(self, window):
        window.title("빵집")
        window.geometry('400x200')
        label = Label(window, text='주문내역')
        label.pack()
        self.orderText = Text(window)
        self.orderText.pack()

    def add_order(self, orders):
        self.orderText.insert(0.0, orders + "\n")


class CustomerView:
    def __init__(self, name, window, bakery_view):
        self.name = name
        self.__init_window(window)
        self.bakeryView = bakery_view

    def __init_window(self, window):
        window.title("고객: " + self.name)
        window.geometry('350x200')

        self.sand = StringVar()
        label_1 = Label(window, text='샌드위치 (5000원)')
        label_1.place(x=0, y=0)
        input_entry_1 = Entry(window, width=5, textvariable=self.sand)
        input_entry_1.place(x=110, y=0)

        self.cake = StringVar()
        label_2 = Label(window, text='케이크 (20000원)')
        label_2.place(x=0, y=20)
        input_entry_2 = Entry(window, width=5, textvariable=self.cake)
        input_entry_2.place(x=110, y=20)

        btn = Button(window, text='주문하기', command=self.send_order)
        btn.place(x=10, y=50)

    def send_order(self):
        v1 = self.sand.get()
        v2 = self.cake.get()

        sand_check = True
        cake_check = True
        try:
            int(v1)
            if sand_check:
                if int(v1) <= 0:
                    sand_check = False
        except ValueError:
            sand_check = False
        try:
            int(v2)
            if cake_check:
                if int(v2) <= 0:
                    cake_check = False
        except ValueError:
            cake_check = False

        if (sand_check is False) & (cake_check is False):
            pass
        elif sand_check | cake_check:
            if sand_check:
                if cake_check:
                    order_text = '{0} : 샌드위치 (5000원) {1}개, 케이크 (20000원) {2}개'.format(self.name, v1, v2)
                    self.bakeryView.add_order(order_text)
                else:
                    order_text = order_text = '{0} : 샌드위치 (5000원) {1}개'.format(self.name, v1)
                    self.bakeryView.add_order(order_text)
            else:
                order_text = '{0} : 케이크 (20000원) {1}개'.format(self.name, v2)
                self.bakeryView.add_order(order_text)


if __name__ == '__main__':
    app = Tk()
    bakery = BakeryView(app)
    CustomerView('고객A', Toplevel(app), bakery)
    CustomerView('고객B', Toplevel(app), bakery)
    app.mainloop()
