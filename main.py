from win_choice_project import *
from win_for_ad import *

CTk.set_appearance_mode("dark")
CTk.set_default_color_theme("green")

class App(CTk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("1200x700")
        self.title("ФМ Калькулятор")
        self.resizable(True, True)

        self.tit = CTk.CTkLabel(master=self, text="Добро пожаловать")
        self.tit.grid(row=0, column=1, padx=(0,0))

        self.n_lab = CTk.CTkLabel(master=self, text="Название вашей компании")
        self.n_lab.grid(row=1, column=1, padx=(0,0))
        
        arr = sql.take_nazv_comp()
        self.nazv_comagne = CTk.CTkComboBox(master=self, values=arr)
        self.nazv_comagne.grid(row=2,column=1)
        combobox.append(self.nazv_comagne)
        combobox2.append(self.nazv_comagne)

        self.l_lab = CTk.CTkLabel(master=self, text="Логин")
        self.l_lab.grid(row=3, column=1, padx=(0,0))
        self.login = CTk.CTkEntry(master=self)
        self.login.grid(row=4,column=1)
 
        self.p_lab = CTk.CTkLabel(master=self, text="Пароль")
        self.p_lab.grid(row=5, column=1, padx=(0,0))
        self.passw = CTk.CTkEntry(master=self, show="*")
        self.passw.grid(row=6,column=1)

        self.auth = CTk.CTkButton(master=self, text="Авторизация", command=self.open_authoris)
        self.auth.grid(row=7, column=1, pady=(20, 20))
        self.ad = CTk.CTkButton(master=self, text="Войти как администратор", command=self.open_adminka)
        self.ad.grid(row=7, column=2, pady=(40, 40), padx=(20,20))

    def open_authoris(self):
        #считать данные по компаниям
        nazv = combobox[0].get()
        l_p = sql.take_log_pas_empl(nazv)
        prov = True
        for i in range(len(l_p)):
            if (l_p[i][0] == self.login.get()) and (l_p[i][1] == self.passw.get()):
                self.withdraw()
                b = win_choice_project()
                b.mainloop()
                prov = False
        if prov:
            mb.showerror("Ошибка!", "Введены неправильные данные логина и пароля, либо неправильно выбрана компания")

    def open_adminka(self):
        #считать данные по компаниям
        nazv = combobox[0].get()
        l_p = sql.take_log_pass_adm(nazv)
        prov = True
        for i in range(len(l_p)):
            if (l_p[i][0] == self.login.get()) and (l_p[i][1] == self.passw.get()):
                l = win_for_ad()
                l.mainloop()
                prov = False
        if prov:
            mb.showerror("Ошибка!", "Введены неправильные данные логина и пароля, либо неправильно выбрана компания")

if __name__ == "__main__":
    app = App()
    app.mainloop()
    
