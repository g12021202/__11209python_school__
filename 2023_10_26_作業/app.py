import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from threading import Timer
import datasource

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        try:
            data = datasource.download_air_data()
        except Exception as e:
            messagebox.showerror("錯誤",f'{e}\n將關閉應用程式\n請稍後再試')
            self.destroy()
        
t = None
def main():
    def on_closing():
        print("window關閉")
        t.cancel()
        window.destroy()
    
    def update_data()->None:
        datasource.update_sqlite_data()
        global t
        t = Timer(5000,update_data)
        t.start()

    window = Window()
    window.title('空氣品質監測站基本資料')
    window.geometry('600x300')
    window.resizable(height = False, width = False)
    update_data()
    window.protocol("WM_DELETE_WINDOW",on_closing)
    window.mainloop()

if __name__ == '__main__':
    main()