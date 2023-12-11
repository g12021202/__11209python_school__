import yfinance as yf

data = yf.download("2330.TW", start = '2023-01-01')
data.to_csv('台積電.csv')

#1, Imports the tkinter module.
import tkinter as tk
from tkinter import ttk
import csv
from tkinter.messagebox import showinfo

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title("台積電股價")
        self.treeView = ttk.Treeview(self, columns=('#1','#2','#3', '#4', '#5', '#6', '#7'),show='headings')
        self.treeView.heading('#1',text='Data')
        self.treeView.heading('#2', text='Open')
        self.treeView.heading('#3', text='High')
        self.treeView.heading('#4', text='Low')
        self.treeView.heading('#5', text='Adj')
        self.treeView.heading('#6', text='Close')
        self.treeView.heading('#7', text='Volume')
        self.treeView.grid(row=0, column=0, sticky='nsew')
        self.treeView.bind("<<TreeviewSelect>>",self.item_selected)

        for _ in range(10):
            for data in self.datas[1:]:
                self.treeView.insert('',tk.END, values = data)
        
        # Create a Scrollbar
        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.treeview.yview)
        # Configure the Treeview to use the scrollbar
        self.treeView.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0,column=1,sticky='ns')

        def item_selected(self,event):
            item = self.treeView.item(self.treeView.selection()[0])
            record = item['values']
            showinfo(title='選取資訊',message=','.join(record))

class ShowDialog:
    def closeWindow(self):
        self.subWindow.destroy()

    def __init__(self,root,message,options):
        self.subWindow = tk.Toplevel(root)
        self.subWindow.geometry('300x300')
        self.subWindow.transient()
        tk.Label(self.subWindow, text=message).pack()
        for item in options:
            ttk.Button(self.subWindow, text=item, command=self.closeWindow).pack()
        self.subWindow().mainloop()

def read_csv(fileName):
    try:
        fileObject = open(fileName, 'r', encoding='utf8')
    except Exception as e:
        print("讀取錯誤")
        fileObject.close()
        return None


def main():
    window = Window()
    s = ttk.Style()
    window.mainloop()
        
if __name__ == "__main__":
    main()