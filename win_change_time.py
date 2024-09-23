import customtkinter as CTk
from connect_db import sql
from tkinter import messagebox as mb
import re
import sys
import os

CTk.set_appearance_mode("dark")
CTk.set_default_color_theme("green")

class win_change_time(CTk.CTk):
    def __init__(self, id_pr):
        super().__init__() 
        self.geometry("1200x700")
        self.title("ФМ Калькулятор")
        self.resizable(True, True)
        self.id_proekt = id_pr

        self.ttle = CTk.CTkLabel(master=self, text="Введите новые данные времени работ")
        self.ttle.grid(row=0, column=1, padx=(5,5), pady=(5,5))

        self.m = CTk.CTkLabel(master=self, text="Месяц начала работ")
        self.m.grid(row=1, column=0, padx=(5,5), pady=(5,5))
        self.mount = CTk.CTkComboBox(master=self, values=["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"])
        self.mount.grid(row=2, column=0, padx=(5,5), pady=(5,5))
        
        self.year_work = CTk.CTkLabel(master=self, text="Год начала работ")
        self.year_work.grid(row=3, column=0, padx=(5,5), pady=(5,5))
        self.y_pr = CTk.CTkEntry(master=self)
        self.y_pr.grid(row=4, column=0, padx=(5,5), pady=(5,5))

        self.start_pr = CTk.CTkLabel(master=self, text="Старт продаж")
        self.start_pr.grid(row=1, column=2, padx=(5,5), pady=(5,5))
        self.start_pr = CTk.CTkComboBox(master=self, values=["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"])
        self.start_pr.grid(row=2, column=2, padx=(5,5), pady=(5,5))
        
        self.year_work = CTk.CTkLabel(master=self, text="Год начала продаж")
        self.year_work.grid(row=3, column=2, padx=(5,5), pady=(5,5))
        self.y_w = CTk.CTkEntry(master=self)
        self.y_w.grid(row=4, column=2, padx=(5,5), pady=(5,5))

        self.btn_upd = CTk.CTkButton(master=self, text="Изменить", command=self.change_time)
        self.btn_upd.grid(row=5, column=0, padx=(5,5), pady=(5,5))
    
    def change_time(self):
        mounth_w = self.mount.get()
        mounth_pr = self.start_pr.get()
        year_w = self.y_pr.get()
        year_pr = self.y_w.get()

        match_year_w = re.match(r'^\d+$', year_w)
        match_year_pr = re.match(r'^\d+$', year_pr)

        if not(match_year_w):
            mb.showerror('Ошибка', 'Неправильно введен год начала работ')
        elif not(match_year_pr):
            mb.showerror('Ошибка', 'Неправильно введен год начала продаж')
        else:
            result = mb.askyesno(title="Подтверждение изменений", message="При изменении данные будут невозвратны, вы хотите продолжить?")

            if result:
                sql.update_time(id_=self.id_proekt, m_w=mounth_w, yr_w=year_w, m_pr=mounth_pr, y_pr=year_pr)
                mb.showinfo('Отлично!', 'Вы успешно обновили данные, для дальнешей работы запустите приложение заново')
                self.destroy()
                os.system('main.py')
                sys.exit(0)