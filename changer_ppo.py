import customtkinter as CTk
from connect_db import sql
from tkinter import messagebox as mb
import re
import sys
import os

CTk.set_appearance_mode("dark")
CTk.set_default_color_theme("green")

entry_price = []
entry_ploshad = []
entry_kv = []

class Dohod_PPO(CTk.CTkScrollableFrame):
    def __init__(self, master, arr):
        super().__init__(master, width=500, height=500)
        cnt = 0
        for i in range(len(arr)):
            self.zagolovok = CTk.CTkLabel(master=self, text=arr[i].nazv, fg_color="#3A5A40")
            self.zagolovok.grid(row=cnt, column=0, padx=(5,5), pady=(5,5))
            cnt += 1
            self.price = CTk.CTkLabel(master=self, text="Цена за квадратный метр, в рублях")
            self.price.grid(row=cnt, column=0, padx=(5,5), pady=(5,5))
            cnt += 1
            self.pr = CTk.CTkEntry(master=self)
            self.pr.grid(row=cnt, column=0, padx=(5,5), pady=(5,5))
            entry_price.append(self.pr)
            cnt += 1
            self.ploshad = CTk.CTkLabel(master=self, text="Продаваемая площадь в кв.м.")
            self.ploshad.grid(row=cnt, column=0, padx=(5,5), pady=(5,5))
            cnt += 1
            self.pl = CTk.CTkEntry(master=self)
            self.pl.grid(row=cnt, column=0, padx=(5,5), pady=(5,5))
            entry_ploshad.append(self.pl)
            cnt += 1
            self.cnt_kavartir = CTk.CTkLabel(master=self, text="Количество квартир/помещений")
            self.cnt_kavartir.grid(row=cnt, column=0, padx=(5,5), pady=(5,5))
            cnt += 1
            self.cnt_kv = CTk.CTkEntry(master=self)
            self.cnt_kv.grid(row=cnt, column=0, padx=(5,5), pady=(5,5))
            entry_kv.append(self.cnt_kv)
            cnt += 1

class win_change_ppo(CTk.CTk):
    def __init__(self, id_proekt):
        super().__init__() 
        self.geometry("1200x700")
        self.title("ФМ Калькулятор")
        self.resizable(True, True)

        self.params_st = sql.take_stat(id_pr=id_proekt, param="Доходы")
        self.params_d = []
        for i in range(len(self.params_st)):
            a = sql.take_ppo(self.params_st[i].id_)
            for el in a:
                self.params_d.append(el)

        self.ttle = CTk.CTkLabel(master=self, text="Обновите данные ППО")
        self.ttle.grid(row=0, column=0, padx=(5,5), pady=(5,5))

        self.win_ppo = Dohod_PPO(master=self, arr=self.params_st)
        self.win_ppo.grid(row=1, column=0, padx=(5,5), pady=(5,5))

        self.btn_upd_ppo = CTk.CTkButton(master=self, text="Обновить", command=self.update_ppo)
        self.btn_upd_ppo.grid(row=2, column=0, padx=(5,5), pady=(5,5))

    def update_ppo(self):
        prov = True
        for i in range(len(self.params_d)):
            match_price = re.match(r'^[0-9]+$', entry_price[i].get())
            match_ploshad = re.match(r'^[0-9]+$', entry_ploshad[i].get())
            match_kv = re.match(r'^[0-9]+$', entry_kv[i].get())
            if not (match_price):
                mb.showerror('Ошибка!', 'Неверно записана стоимость за квадратный метр')
                prov = False
                break
            elif not (match_ploshad):
                mb.showerror('Ошибка!', 'Неверно записана продаваемая площадь')
                prov = False
                break
            elif not (match_kv):
                mb.showerror('Ошибка!', 'Неверно записано количество квартир/помещений')
                prov = False
                break

        if prov:
            for i in range(len(self.params_d)):
                sql.update_ppo(self.params_d[i].id_, entry_ploshad[i].get(), entry_price[i].get(), entry_kv[i].get())

            result = mb.askyesno(title="Подтверждение изменений", message="При изменении будут удалены текущие данные ППО, вы хотите продолжить?")
            if result:
                mb.showinfo('Отлично!', 'Вы успешно обновили данные, для дальнешей работы запустите приложение заново')
                self.destroy()
                os.system('main.py')
                sys.exit(0)