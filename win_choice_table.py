import customtkinter as CTk
from win_tab_gpr import *
import os
import sys

class win_choice_table(CTk.CTk):
    def __init__(self):
        super().__init__() 
        self.geometry("1200x700")
        self.title("ФМ Калькулятор")
        self.resizable(True, True)
        self.protocol('WM_DELETE_WINDOW', self._done)

        self.gpr = CTk.CTkLabel(master=self, text="Таблица графика проивзодственных работ")
        self.gpr.grid(row=0, column=0, padx=(5,5), pady=(5,5))
        self.gpr_ex = CTk.CTkButton(master=self, text="Создать таблицу ГПР в Excel")
        self.gpr_ex.grid(row=1, column=0, padx=(5,5), pady=(5,5))
        self.gpr_win = CTk.CTkButton(master=self, text="Открыть таблицу ГПР в приложении", command=self.open_window_tab_gpr)
        self.gpr_win.grid(row=2, column=0, padx=(5,5), pady=(5,5))

        self.ppo = CTk.CTkLabel(master=self, text="Таблица ППО")
        self.ppo.grid(row=3, column=0, padx=(5,5), pady=(5,5))
        self.ppo_ex = CTk.CTkButton(master=self, text="Создать таблицу ППО в Excel")
        self.ppo_ex.grid(row=4, column=0, padx=(5,5), pady=(5,5))
        self.ppo_win = CTk.CTkButton(master=self, text="Открыть таблицу ППО в приложении")
        self.ppo_win.grid(row=5, column=0, padx=(5,5), pady=(5,5))

        self.bdr = CTk.CTkLabel(master=self, text="Таблица БДР")
        self.bdr.grid(row=6, column=0, padx=(5,5), pady=(5,5))
        self.bdr_ex = CTk.CTkButton(master=self, text="Создать таблицу БДР в Excel")
        self.bdr_ex.grid(row=7, column=0, padx=(5,5), pady=(5,5))
        self.bdr_win = CTk.CTkButton(master=self, text="Открыть таблицу БДР в приложении")
        self.bdr_win.grid(row=8, column=0, padx=(5,5), pady=(5,5))

        self.bdds = CTk.CTkLabel(master=self, text="Таблица БДДС")
        self.bdds.grid(row=9, column=0, padx=(5,5), pady=(5,5))
        self.bdds_ex = CTk.CTkButton(master=self, text="Создать таблицу БДДС в Excel")
        self.bdds_ex.grid(row=10, column=0, padx=(5,5), pady=(5,5))
        self.bdds_win = CTk.CTkButton(master=self, text="Открыть таблицу БДДС в приложении")
        self.bdds_win.grid(row=11, column=0, padx=(5,5), pady=(5,5))
        self.bdds_upd = CTk.CTkButton(master=self, text="Добавить данные в таблицу БДДС в приложении")
        self.bdds_upd.grid(row=12, column=0, padx=(5,5), pady=(5,5))

        self.changer = CTk.CTkLabel(master=self, text="Добавить изменения в талицу")
        self.changer.grid(row=13, column=0, padx=(5,5), pady=(15,5))
        self.cnanger_check_box = CTk.CTkComboBox(master=self, values=["ГПР", "ППО", "БДР", "БДДС"])
        self.cnanger_check_box.grid(row=14, column=0, padx=(5,5), pady=(5,5))
        self.changer_but = CTk.CTkButton(master=self, text="Изменить")
        self.changer_but.grid(row=15, column=0, padx=(5,5), pady=(5,5))

        self.poyasn_t = CTk.CTkLabel(master=self, text="При создании нового файла не забывайте удалять старый!", text_color='#EB5E28')
        self.poyasn_t.grid(row=16, column=0, padx=(5,5), pady=(5,5))

    def open_window_tab_gpr(self):
        self.withdraw()
        d = win_table_gpr()
        d.mainloop()
    
    def _done(self):
        self.destroy()
        os.system('main.py')
        sys.exit(0)

r = []
