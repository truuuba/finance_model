from win_new_project import *
from win_choice_table import *

CTk.set_appearance_mode("dark")
CTk.set_default_color_theme("green")

class win_choice_project(CTk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1200x700")
        self.title("ФМ Калькулятор")
        self.resizable(True, True)
        self.protocol('WM_DELETE_WINDOW', self._done)

        self.ch_lab = CTk.CTkLabel(master=self, text="Выберите проект или создайте новый")
        self.ch_lab.grid(row=0, column=0, padx=(0,0))

        self.old_pr_lab = CTk.CTkLabel(master=self, text="Текущие проекты")
        self.old_pr_lab.grid(row=3, column=0, padx=(0,0))
        arr = self.make_arr_nazv_pr()
        self.old_pr = CTk.CTkComboBox(master=self, values=arr)                                                  
        self.old_pr.grid(row=4, column=0, padx=(0,0))
        
        self.old_pr_but = CTk.CTkButton(master=self, text="Перейти к проекту", command=self.open_win_choice_t)
        self.old_pr_but.grid(row=5, column=0, padx=(20,20), pady=(20,20))

        self.new_pr = CTk.CTkLabel(master=self, text="Создайте новый проект")
        self.new_pr.grid(row=7, column=0, padx=(0,0))
        self.new_pr_but = CTk.CTkButton(master=self, text="Создать", command=self.open_win_new_project)
        self.new_pr_but.grid(row=8, column=0, padx=(0,0))

    def _done(self):
        self.destroy()
        os.system('main.py')
        sys.exit(0)

    def make_arr_nazv_pr(self):
        arr = sql.take_project(combobox2[0].get())
        if len(arr) >= 1:
            return arr
        else:
            arr = ['Проекты отсутствуют']
            return arr

    def open_win_new_project(self):
        self.withdraw()
        c = win_new_project()
        c.mainloop()

    def open_win_choice_t(self):
        if not(self.old_pr.get() == 'Проекты отсутствуют'):
            id_pr = sql.take_id_nazv_project(nazv_comp=combobox2[0].get(), nazv_pr=self.old_pr.get())
            arr.append(id_pr)

            self.withdraw()
            h = win_choice_table()
            h.mainloop()
        else:
            mb.showerror('Ошибка!', 'Проекты не найдены')
 
