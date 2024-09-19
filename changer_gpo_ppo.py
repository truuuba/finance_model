from connect_db import sql
import customtkinter as CTk

CTk.set_appearance_mode("dark")
CTk.set_default_color_theme("green")

entr_prod = []
entr_zavis = []

entry_price = []
entry_ploshad = []
entry_kv = []

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

class Dohod_PPO(CTk.CTkScrollableFrame):
    def __init__(self, master, arr):
        super().__init__(master, width=250, height=500)
        cnt = 0
        for i in range(len(arr)):
            self.zagolovok = CTk.CTkLabel(master=self, text=arr[i])
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

class win_change_gpo_ppo(CTk.CTk):
    def __init__(self, id_pr, arr_r, arr_d):
        super().__init__() 
        self.geometry("1200x700")
        self.title("ФМ Калькулятор")
        self.resizable(True, True)

        #Для ГПР
        self.ttle_gpr = CTk.CTkLabel(master=self, text="Данные для ГПР")
        self.ttle_gpr.grid(row=1, column=0, padx=(5,5), pady=(5,5))
        self.win_gpr = Work_GPR(master=self, p_r=arr_r)
        self.win_gpr.grid(row=2, column=0, padx=(5,5), pady=(5,5))

        #Для ППО
        self.ttle_ppo = CTk.CTkLabel(master=self, text="Данные для ППО")
        self.ttle_ppo.grid(row=1, column=2, padx=(5,5), pady=(5,5))
        self.win_ppo = Dohod_PPO(master=self, arr=arr_d)
        self.win_ppo.grid(row=2, column=2, padx=(5,5), pady=(5,5))

        self.btn_ready = CTk.CTkButton(master=self, text="Применить изменения для таблиц")
        self.btn_ready.grid(row=3, column=0, padx=(5,5), pady=(5,5))
