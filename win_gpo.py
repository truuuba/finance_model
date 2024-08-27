from win_ppo import *

CTk.set_appearance_mode("dark")
CTk.set_default_color_theme("green")

entry_prod = []
entry_zavis = []

class MyCheckBoxFrame(CTk.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master, width=1100, height=500)
        self.w = CTk.CTkLabel(master=self, text="Параметры работ")
        self.w.grid(row=0, column=0, padx=(5,5), pady=(5,5))
        self.pr = CTk.CTkLabel(master=self, text="Продолжительность работ в месяцах")
        self.pr.grid(row=0, column=1, padx=(5,5), pady=(5,5))
        self.zav = CTk.CTkLabel(master=self, text="Зависимости от процессов (пишите номера процессов через пробел)")
        self.zav.grid(row=0, column=2, padx=(5,5), pady=(5,5))
        id_proekt = arr[0]
        params_r = sql.take_stat(id_pr=id_proekt, param="Расходы")
        n = len(params_r)
        for i in range(n):
            self.work = CTk.CTkLabel(master=self, text=str(i+1)+". "+params_r[i].nazv)
            self.work.grid(row=i+1, column=0, padx=(5,5), pady=(5,5))
            self.prodolj = CTk.CTkEntry(master=self)
            self.prodolj.grid(row=i+1, column=1, padx=(5,5), pady=(5,5))
            entry_prod.append(self.prodolj)
            self.zavis = CTk.CTkEntry(master=self)
            self.zavis.grid(row=i+1, column=2, padx=(5,5), pady=(5,5))
            entry_zavis.append(self.zavis)

class win_gpo(CTk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1200x700")
        self.title("ФМ Калькулятор")
        self.resizable(True, True)
        self.protocol('WM_DELETE_WINDOW', self._done)

        self.make_gpr = CTk.CTkLabel(master=self, text="Создание ГПР")
        self.make_gpr.grid(row=0, column=0, padx=(5,5), pady=(5,5))

        self.check_box_frame = MyCheckBoxFrame(self)
        self.check_box_frame.grid(row=1, column=0, padx=(5,5), pady=(5,5))
        self.but_new_win = CTk.CTkButton(master=self, text="Готово", command=self.open_win_ppo)
        self.but_new_win.grid(row=2, column=0, padx=(5,5), pady=(5,5))

    def open_win_ppo(self):
        zavisim = []
        prod = []
        id_proekt = arr[0]
        params_r = sql.take_stat(id_pr=id_proekt, param="Расходы")
        prov = True #Проверка на ввод данных 
        for i in range(len(params_r)):
            #Проверка данных для зависимостей процессов
            match_zav = re.match(r'^[\d\s]*$', entry_zavis[i].get())
            if not(match_zav):
                prov = False
                mb.showerror('Ошибка!', 'Были неверно записаны зависимости')
                break
            elif entry_zavis[i].get() != "":
                zavisim.append(entry_zavis[i].get())
            else:
                zavisim.append("0")
            
            #Проверка данных для продолжительности процессов
            match_prod = re.match(r'^\d+$', entry_prod[i].get())
            if not(match_prod):
                prov = False
                mb.showerror('Ошибка!', 'Были неверно записаны продолжительности процессов')
                break
            else:
                prod.append(entry_prod[i].get())

        #Добавление данных в таблицу ГПР   
        if prov:     
            for i in range(len(params_r)):
                sql.input_gpr(id_st=params_r[i].id_, prod=prod[i], zav=zavisim[i])
            self.withdraw()
            c = win_ppo()
            c.mainloop()

    def _done(self):
        self.destroy()
        os.system('main.py')
        sys.exit(0)
