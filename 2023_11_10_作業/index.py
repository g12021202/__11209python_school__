import datasource 
import psycopg2
import password as pw
import tkinter as tk
from tkinter import ttk
from threading import Timer

class Window(tk.Tk):
    pass


def main():
    def update_data(w:Window)->None:
        datasource.update_render_data()
        #-----------更新treeView資料---------------
        #lastest_data = datasource.lastest_datetime_data()
        #w.youbikeTreeView.update_content(lastest_data)

        # w.after(10*60*1000, update_data,w)  #每隔10分鐘
        t = Timer(60*60, update_data,args=(window,))

    window = Window()
    window.title('空氣品質監測站基本資料')
    window.geometry('600x300')
    window.resizable(width=False,height=False)
    # window.after(1000, update_data, window)
    t = Timer(1, update_data, args=(window,))
    t.start()
    window.mainloop()
    

if __name__ == "__main__":
    main()