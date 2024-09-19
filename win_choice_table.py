import customtkinter as CTk
from make_gpr_exe import *
from make_ppo_exe import *
from win_bdr import *
from changer_stati import *

class win_choice_table(CTk.CTk):
    def __init__(self):
        super().__init__() 
        self.geometry("1200x700")
        self.title("ФМ Калькулятор")
        self.resizable(True, True)
        self.protocol('WM_DELETE_WINDOW', self._done)
        self.id_pr = arr[0]

        #ГПР
        self.gpr = CTk.CTkLabel(master=self, text="Таблица графика производственных работ")
        self.gpr.grid(row=0, column=0, padx=(5,5), pady=(5,5))
        self.gpr_ex = CTk.CTkButton(master=self, text="Создать таблицу ГПР в Excel", command=create_tabel_gpr(self.id_pr))
        self.gpr_ex.grid(row=1, column=0, padx=(5,5), pady=(5,5))

        #ППО
        self.ppo = CTk.CTkLabel(master=self, text="Таблица ППО")
        self.ppo.grid(row=2, column=0, padx=(5,5), pady=(5,5))
        self.ppo_ex = CTk.CTkButton(master=self, text="Создать таблицу ППО в Excel", command=create_tabel_ppo(self.id_pr))
        self.ppo_ex.grid(row=3, column=0, padx=(5,5), pady=(5,5))

        #БДР
        self.bdr = CTk.CTkLabel(master=self, text="Таблица БДР")
        self.bdr.grid(row=4, column=0, padx=(5,5), pady=(5,5))
        self.bdr_ex = CTk.CTkButton(master=self, text="Открыть таблицу БДР", command=self.open_win_bdr)
        self.bdr_ex.grid(row=5, column=0, padx=(5,5), pady=(5,5))

        #БДДС
        self.bdds = CTk.CTkLabel(master=self, text="Таблица БДДС")
        self.bdds.grid(row=6, column=0, padx=(5,5), pady=(5,5))
        self.bdds_ex = CTk.CTkButton(master=self, text="Создать таблицу БДДС в Excel")
        self.bdds_ex.grid(row=7, column=0, padx=(5,5), pady=(5,5))

        #Изменения в конкретных таблицах
        self.changer = CTk.CTkLabel(master=self, text="Добавить изменения в талицу")
        self.changer.grid(row=8, column=0, padx=(5,5), pady=(15,5))
        self.cnanger_check_box = CTk.CTkComboBox(master=self, values=["ГПР", "ППО", "БДДС"])
        self.cnanger_check_box.grid(row=9, column=0, padx=(5,5), pady=(5,5))
        self.changer_but = CTk.CTkButton(master=self, text="Изменить")
        self.changer_but.grid(row=10, column=0, padx=(5,5), pady=(5,5))

        #Изменения в статьях
        self.ch_st = CTk.CTkLabel(master=self, text="Изменить статьи доходов и расходов")
        self.ch_st.grid(row=11, column=0, padx=(5,5), pady=(5,5))
        self.change_stat = CTk.CTkButton(master=self, text="Изменить", command=self.open_win_changer_stati)
        self.change_stat.grid(row=12, column=0, padx=(5,5), pady=(5,5))

        #Изменить даты начала работ
        self.time_work = CTk.CTkLabel(master=self, text="Изменить даты продаж и строительства")
        self.time_work.grid(row=13, column=0, padx=(5,5), pady=(5,5))
        self.ch_t = CTk.CTkButton(master=self, text="Изменить")
        self.ch_t.grid(row=14, column=0, padx=(5,5), pady=(5,5))

        self.poyasn_t = CTk.CTkLabel(master=self, text="При изменении файла закрывайте его в Excel!", text_color='#EB5E28')
        self.poyasn_t.grid(row=15, column=0, padx=(5,5), pady=(5,5))
    
    def _done(self):
        self.destroy()
        os.system('main.py')
        sys.exit(0)

    def open_win_bdr(self):
        d = win_bdr()
        d.mainloop()    

    def open_win_changer_stati(self):
        c = win_change_stati(id_pr=self.id_pr)
        c.mainloop()


