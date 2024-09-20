import customtkinter as CTk
from connect_db import sql
from tkinter import messagebox as mb
import re
import sys
import os

CTk.set_appearance_mode("dark")
CTk.set_default_color_theme("green")

entr_prod = []
entr_zavis = []

class Work_GPR(CTk.CTkScrollableFrame):
    def __init__(self, master, p_r):
        super().__init__(master, width=800, height=500)
        self.w = CTk.CTkLabel(master=self, text="Параметры работ")
        self.w.grid(row=0, column=0, padx=(5,5), pady=(5,5))
        self.pr = CTk.CTkLabel(master=self, text="Продолжительность работ в месяцах")
        self.pr.grid(row=0, column=1, padx=(5,5), pady=(5,5))
        self.zav = CTk.CTkLabel(master=self, text="Зависимости от процессов")
        self.zav.grid(row=0, column=2, padx=(5,5), pady=(5,5))
        
        n = len(p_r)
        for i in range(n):
            self.work = CTk.CTkLabel(master=self, text=str(i+1)+". "+p_r[i])
            self.work.grid(row=i+1, column=0, padx=(5,5), pady=(5,5))
            self.prodolj = CTk.CTkEntry(master=self)
            self.prodolj.grid(row=i+1, column=1, padx=(5,5), pady=(5,5))
            entr_prod.append(self.prodolj)
            self.zavis = CTk.CTkEntry(master=self)
            self.zavis.grid(row=i+1, column=2, padx=(5,5), pady=(5,5))
            entr_zavis.append(self.zavis)

class win_change_gpo(CTk.CTk):
    def __init__(self):
        super().__init__() 
        self.geometry("1200x700")
        self.title("ФМ Калькулятор")
        self.resizable(True, True)

        self.ttle = CTk.CTkLabel(master=self, text="Вставьте новые данные для данных ГПР")
        self.ttle.grid(row=0, column=0, padx=(5,5), pady=(5,5))

        self.params_r = sql.take_stat(id_pr=self.id_proekt, param="Расходы")
        self.win_gpo = Work_GPR(self, p_r=self.params_r)
        self.win_gpo.grid(row=1, column=0, padx=(5,5), pady=(5,5))
        self.btn_upd = CTk.CTkButton(master=self, text="Применить изменения")
        self.btn_upd.grid(row=2, column=0, padx=(5,5), pady=(5,5))

    def update_gpr(self):
        #Проверка вводимых данных ГПР
        zavisim = []
        prod = []
        prov_GPR = True #Проверка на ввод данных 
        for i in range(len(self.params_r)):
            #Проверка данных для зависимостей процессов
            match_zav = re.match(r'^[\d\s]*$', entr_zavis[i].get())
            if not(match_zav):
                prov_GPR = False
                mb.showerror('Ошибка!', 'Были неверно записаны зависимости')
                break
            elif entr_zavis[i].get() != "":
                zavisim.append(entr_zavis[i].get())
            else:
                zavisim.append("0")
            
            #Проверка данных для продолжительности процессов
            match_prod = re.match(r'^\d+$', entr_prod[i].get())
            if not(match_prod):
                prov_GPR = False
                mb.showerror('Ошибка!', 'Были неверно записаны продолжительности процессов')
                break
            else:
                prod.append(entr_prod[i].get())
        
        if prov_GPR:
            for i, el in enumerate(self.params_r):
                sql.input_gpr(id_st=el.id_, prod=prod[i], zav=zavisim[i])
            mb.showinfo('Отлично!', 'Вы успешно обновили данные, для дальнешей работы запустите приложение заново')
            self.destroy()
            os.system('main.py')
            sys.exit(0)