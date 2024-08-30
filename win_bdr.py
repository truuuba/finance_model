import customtkinter as CTk
import re
from tkinter import messagebox as mb
from make_bdr_exe import *

CTk.set_appearance_mode("dark")
CTk.set_default_color_theme("green")

#массив с вводимыми данными
trati = []
idishniki = []

class MyCheckBoxFrame(CTk.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master, width=1100, height=500, orientation="vertical")
        id_proekt = arr[0]
        params_r = sql.take_stat(id_pr=id_proekt, param="Расходы")
        
        counter = 0
        #Добавляем данные по БД
        for el in params_r:
            self.rash = CTk.CTkLabel(master=self, text=("Расходы на " + el.nazv))
            self.rash.grid(row=counter, column=0, padx=(5,5), pady=(5,5))
            counter += 1
            dannie = sql.take_data_bdr(el.id_)
            for i in range(len(dannie)):
                self.dat_rash = CTk.CTkLabel(master=self, text=(dannie[i].mnt + " " + str(dannie[i].yr) + " года"))
                self.dat_rash.grid(row=counter, column=0, padx=(5,5), pady=(5,5))
                self.st_rash = CTk.CTkEntry(master=self)
                self.st_rash.grid(row=counter, column=1, padx=(5,5), pady=(5,5))
                counter += 1
                trati.append(self.st_rash)
                idishniki.append(dannie[i].id_)

class win_bdr(CTk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1200x700")
        self.title("ФМ Калькулятор")
        self.resizable(True, True)
        self.protocol('WM_DELETE_WINDOW', self._done)

        self.t = CTk.CTkLabel(master=self, text="Создание БДР")
        self.t.grid(row=0, column=0, padx=(5,5), pady=(5,5))
        self.scroll_frame = MyCheckBoxFrame(self)
        self.scroll_frame.grid(row=1, column=0, padx=(5,5), pady=(5,5))
        self.new_win = CTk.CTkButton(master=self, text="Обновить данные", command=self.create_bdr_table)
        self.new_win.grid(row=2, column=0, padx=(5,5), pady=(5,5))

        #Решаем вопрос с наличием данных в БДР
        id_proekt = arr[0]
        params_r = sql.take_stat(id_pr=id_proekt, param="Расходы")
        trt = []
        for i in range(len(params_r)):
            arr2 = sql.take_bdr_r_id(params_r[i].id_)
            for el in arr2:
                trt.append(sql.take_data_bdr_r(el))

        #Проверяем наличие данные в БДР
        prov = True
        for el in trt:
            if el is None:
                prov = False
        
        if prov:
            self.button_ready = CTk.CTkButton(master=self, text="Данные уже внесены")
            self.button_ready.grid(row=3, column=0, padx=(5,5), pady=(5,5))

    def _done(self):
        self.destroy()

    def create_bdr_table(self):
        prov = True
        for el in trati:
            match_zav = re.match(r'^[0-9]+$', el.get())
            if not match_zav:
                prov = False
                mb.showerror('Ошибка!', 'Были неверно записаны данные')
                break
        if prov:
            #Добавление данных в БДР
            for i in range(len(trati)):
                sql.update_bdr(id_=idishniki[i], trt=trati[i].get())
            mb.showinfo("Отлично!", "Данные внесены")
            
arr = []
