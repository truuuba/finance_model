import customtkinter as CTk
from win_choice_table import *
import re
from tkinter import messagebox as mb

CTk.set_appearance_mode("dark")
CTk.set_default_color_theme("green")

class MyCheckBoxFrame(CTk.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master, width=1100, height=500)
        self.ttle1 = CTk.CTkLabel(master=self, text="Статья расходов")
        self.ttle1.grid(row=0, column=0, padx=(5,5), pady=(5,5))
        self.ttle2 = CTk.CTkLabel(master=self, text="Планируемый расход в месяц")
        self.ttle2.grid(row=0, column=1, padx=(5,5), pady=(5,5))
        counter = 1
        for el in r:
            self.nazv = CTk.CTkLabel(master=self, text=el)
            self.nazv.grid(row=counter, column=0, padx=(5,5), pady=(5,5))
            self.st_r = CTk.CTkEntry(master=self)
            self.st_r.grid(row=counter, column=1, padx=(5,5), pady=(5,5))
            counter += 1
            self.trati.append(self.st_r)
        
                
class win_bdr(CTk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1200x700")
        self.title("ФМ Калькулятор")
        self.resizable(True, True)
        self.protocol('WM_DELETE_WINDOW', self._done)

        #массив с двнными по затратам
        self.trati = []
        #сюда вытащить массив для данных по продолжительности в месяцах ОБЯЗАТЕЛЬНО!!!
        self.prodolj = []

        self.t = CTk.CTkLabel(master=self, text="Создание БДР")
        self.t.grid(row=0, column=0, padx=(5,5), pady=(5,5))
        self.scroll_frame = MyCheckBoxFrame(self)
        self.scroll_frame.grid(row=1, column=0, padx=(5,5), pady=(5,5))
        self.new_win = CTk.CTkButton(master=self, text="Готово", command=self.open_win_choice_table)
        self.new_win.grid(row=2, column=0, padx=(5,5), pady=(5,5))

    def _done(self):
        self.destroy()
        os.system('main.py')
        sys.exit(0)

    def open_win_choice_table(self):
        prov = True
        for el in self.trati:
            match_zav = re.match(r'^[0-9]+$', el.get())
            if not match_zav:
                prov = False
                mb.showerror('Ошибка!', 'Были неверно записаны данные')
                break
        if prov:
            #Добавление данных в БДР
            self.withdraw()
            f = win_choice_table()
            f.mainloop()