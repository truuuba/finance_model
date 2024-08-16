from win_bdr import *

CTk.set_appearance_mode("dark")
CTk.set_default_color_theme("green")

entry_price = []
entry_ploshad = []
entry_kv = []

class MyFrame(CTk.CTkScrollableFrame):
    def __init__(self, master, arr):
        super().__init__(master, width=1100, height=500)
        for i in range(len(arr)):
            cnt = 0
            self.zagolovok = CTk.CTkLabel(master=self, text=arr[i].nazv)
            self.zagolovok.grid(row=cnt, column=i, padx=(5,5), pady=(5,5))
            cnt += 1
            self.price = CTk.CTkLabel(master=self, text="Цена за квадратный метр, в рублях")
            self.price.grid(row=cnt, column=i, padx=(5,5), pady=(5,5))
            cnt += 1
            self.pr = CTk.CTkEntry(master=self)
            self.pr.grid(row=cnt, column=i, padx=(5,5), pady=(5,5))
            entry_price.append(self.pr)
            cnt += 1
            self.ploshad = CTk.CTkLabel(master=self, text="Продаваемая площадь в кв.м.")
            self.ploshad.grid(row=cnt, column=i, padx=(5,5), pady=(5,5))
            cnt += 1
            self.pl = CTk.CTkEntry(master=self)
            self.pl.grid(row=cnt, column=i, padx=(5,5), pady=(5,5))
            entry_ploshad.append(self.pl)
            cnt += 1
            self.cnt_kavartir = CTk.CTkLabel(master=self, text="Количество квартир/помещений")
            self.cnt_kavartir.grid(row=cnt, column=i, padx=(5,5), pady=(5,5))
            cnt += 1
            self.cnt_kv = CTk.CTkEntry(master=self)
            self.cnt_kv.grid(row=cnt, column=i, padx=(5,5), pady=(5,5))
            entry_kv.append(self.cnt_kv)

class win_ppo(CTk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1200x700")
        self.title("ФМ Калькулятор")
        self.resizable(True, True)
        self.protocol('WM_DELETE_WINDOW', self._done)

        self.t = CTk.CTkLabel(master=self, text="Создание ППО")
        self.t.grid(row=0, column=0, padx=(5,5), pady=(5,5))
        id_pr = arr[0]
        dannie = sql.take_stat(id_pr=id_pr, param="Доходы")
        
        self.my_frame = MyFrame(self, arr=dannie)
        self.my_frame.grid(row=1, column=0, padx=(5,5), pady=(5,5))

        self.new_but = CTk.CTkButton(master=self, text="Готово", command=self.open_win_bdr)
        self.new_but.grid(row=2, column=0, padx=(5,5), pady=(5,5))

    def _done(self):
        self.destroy()
        os.system('main.py')
        sys.exit(0)

    def open_win_bdr(self):
        prov = True
        for i in range(len(entry_price)):
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
            id_pr = arr[0]
            dannie = sql.take_stat(id_pr=id_pr, param="Доходы")
            for i in range(len(dannie)):
                sql.input_ppo(dannie[i].id_, entry_ploshad[i].get(), entry_price[i].get(), entry_kv[i].get())
            self.withdraw()
            e = win_bdr()
            e.mainloop()
