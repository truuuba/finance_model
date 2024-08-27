from win_gpo import *

CTk.set_appearance_mode("dark")
CTk.set_default_color_theme("green")

checkboxes_r = []
checkboxes_d = []

class MyCheckBoxFrame(CTk.CTkFrame):
    def __init__(self, master, values):
        super().__init__(master)
        self.values = values
        for i, value in enumerate(self.values):
            checkbox = CTk.CTkCheckBox(self, text=value)
            checkbox.grid(row=i, column=0, padx=(5,5), pady=(5,5))
            checkboxes_d.append(checkbox)

class MyCheckBoxFrame2(CTk.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master, width=400, height=330)

        self.values = ["Формирование участка", "Проектные работы", "Изыскательные работы", "Технологическое присоединение", "Контроль и технический надзор", "Сдача объекта", "PR, реклама и маркетинговые исследования", "Управленческие расходы", "Страхование ответственности застройщика", "Расходы на содержание непроданных квартир", "Госпошлины за гос.регистрацию сделок с недвижимостью", "Налоги (кроме УСН и НСП)", "Услуги риэлторов", "Вознаграждение за брокеридж (для ТРЦ)", "Субсидирование ипотечной ставки", "Возврат ДС дольщикам", "Социальная инфраструктура", "Услуги банка (билинг)"]
        self.stat_rash_zakazch = CTk.CTkLabel(master=self, text="Статьи расходов заказчика:")
        self.stat_rash_zakazch.grid(row=0, column=0, padx=(0,0))
        for i, value in enumerate(self.values):
            checkbox = CTk.CTkCheckBox(self, text=value)
            checkbox.grid(row=i+1, column=0, padx=(5,5), pady=(10,10))
            checkboxes_r.append(checkbox)

        self.values = "Фундаменты", "Общестр-ные работы ниже отм.0", "Земляные работы", "Каркас ниже отм. 0.00" 
        self.stat_rash_CMP = CTk.CTkLabel(master=self, text="Расходы СМР (Подземная часть)")
        self.stat_rash_CMP.grid(row=20, column=0, padx=(5,5), pady=(5,5))
        for i, value in enumerate(self.values):
            checkbox = CTk.CTkCheckBox(self, text=value)
            checkbox.grid(row=i+21, column=0, padx=(5,5), pady=(5,5))
            checkboxes_r.append(checkbox)

        self.values = "Несущие конструкции", "Общестроительные работы выше отм.0", "Наружные стены и наружная отделка", "Заполнение оконных проемов", " Заполнение дверных проемов", "Металлоконструкции", "Кровля"    
        self.stat_rash_CMP = CTk.CTkLabel(master=self, text="Расходы СМР (Конструкции надземной части)")
        self.stat_rash_CMP.grid(row=25, column=0, padx=(5,5), pady=(5,5))
        for i, value in enumerate(self.values):
            checkbox = CTk.CTkCheckBox(self, text=value)
            checkbox.grid(row=i+26, column=0, padx=(5,5), pady=(5,5))
            checkboxes_r.append(checkbox)

        self.values = "Внутренние стены и перегородки", "Двери входные в квартиры, двери МОП", "Внутренние отделочные работы (предчистовая кв.)", "Внутренние отделочные работы чистовые (по квар.)"
        self.stat_rash_CMP = CTk.CTkLabel(master=self, text="Расходы СМР (Внутренние работы)")
        self.stat_rash_CMP.grid(row=33, column=0, padx=(5,5), pady=(5,5))
        for i, value in enumerate(self.values):
            checkbox = CTk.CTkCheckBox(self, text=value)
            checkbox.grid(row=i+34, column=0, padx=(5,5), pady=(5,5))
            checkboxes_r.append(checkbox)

        self.values = "Лифты, подъемники. Диспетчеризация. Пуско-н", "Специализированное транспортное оборудование", "Системы ВК", "Газоснабжение", "ИТП, узел учета тепловой энергии, АСКУЭ", "Система отопления", "Противопожарные системы", "Электрические сети и оборудование", "Внутренняя вентиляция и дымоудаление", "Кондиционирование"
        self.stat_rash_CMP = CTk.CTkLabel(master=self, text="Расходы СМР (Внутренние инженерные системы)")
        self.stat_rash_CMP.grid(row=38, column=0, padx=(5,5), pady=(5,5))
        for i, value in enumerate(self.values):
            checkbox = CTk.CTkCheckBox(self, text=value)
            checkbox.grid(row=i+39, column=0, padx=(5,5), pady=(5,5))
            checkboxes_r.append(checkbox)

        self.stat_rash_CMP = CTk.CTkLabel(master=self, text="Расходы СМР (Оборудование)")
        self.stat_rash_CMP.grid(row=49, column=0, padx=(5,5), pady=(5,5))
        checkbox = CTk.CTkCheckBox(self, text="Технологическое оборудование")
        checkbox.grid(row=50, column=0, padx=(5,5), pady=(5,5))
        checkboxes_r.append(checkbox)

        self.values = "Подготовка площадки строительства", "Благоустройство и озеленение", "Наружный водопровод и канализация", "Наружная ливневая канализация", "Наружные тепловые сети, ЦТП", "Наружные трубопроводы газоснабжения", "Наружные сети электроснабжения, трансформат", "Наружное освещение", "Наружные сети связи"
        self.stat_rash_CMP = CTk.CTkLabel(master=self, text="Расходы СМР (Внутренние инженерные системы)")
        self.stat_rash_CMP.grid(row=51, column=0, padx=(5,5), pady=(5,5))
        for i, value in enumerate(self.values):
            checkbox = CTk.CTkCheckBox(self, text=value)
            checkbox.grid(row=i+52, column=0, padx=(5,5), pady=(5,5))
            checkboxes_r.append(checkbox)

        self.values = "Реализация услуг по вывозу мусора", "Временные здания, сооружения (бытовой городок)", "Содержание строительной площадки", "Временный водопровод", "Временное освещение, элект-ие, КТП, ТП, ВРУ", "Временное ограждение, ворота", "Дороги временные", "Вертикальный транспорт", " Непредвиденные расходы по объекту"
        self.stat_rash_CMP = CTk.CTkLabel(master=self, text="Расходы СМР (Прочее)")
        self.stat_rash_CMP.grid(row=61, column=0, padx=(5,5), pady=(5,5))
        for i, value in enumerate(self.values):
            checkbox = CTk.CTkCheckBox(self, text=value)
            checkbox.grid(row=i+62, column=0, padx=(5,5), pady=(5,5))
            checkboxes_r.append(checkbox)

        self.stat_rash_CMP = CTk.CTkLabel(master=self, text="Финансовая деятельность")
        self.stat_rash_CMP.grid(row=71, column=0, padx=(5,5), pady=(5,5))
        checkbox = CTk.CTkCheckBox(self, text="% по кредитам и займам")
        checkbox.grid(row=72, column=0, padx=(5,5), pady=(5,5))
        checkboxes_r.append(checkbox)
        
        self.stat_rash_CMP = CTk.CTkLabel(master=self, text="Налог на прибыль")
        self.stat_rash_CMP.grid(row=73, column=0, padx=(5,5), pady=(5,5))
        checkbox = CTk.CTkCheckBox(self, text="Налог на прибыль")
        checkbox.grid(row=74, column=0, padx=(5,5), pady=(5,5))
        checkboxes_r.append(checkbox)
           
        self.values = "Заработная плата основных рабочих", "Заработная плата машинистов БК", "Заработная плата электриков"
        self.stat_rash_CMP = CTk.CTkLabel(master=self, text="Заработная плата")
        self.stat_rash_CMP.grid(row=75, column=0, padx=(5,5), pady=(5,5))
        for i, value in enumerate(self.values):
            checkbox = CTk.CTkCheckBox(self, text=value)
            checkbox.grid(row=i+76, column=0, padx=(5,5), pady=(5,5))
            checkboxes_r.append(checkbox)

        self.values = "Услуги башенного крана", "Услуги мачтового подъемника", "Услуги стропальщика"
        self.stat_rash_CMP = CTk.CTkLabel(master=self, text="Услуги грузоподъемных механизмов")
        self.stat_rash_CMP.grid(row=79, column=0, padx=(5,5), pady=(5,5))
        for i, value in enumerate(self.values):
            checkbox = CTk.CTkCheckBox(self, text=value)
            checkbox.grid(row=i+80, column=0, padx=(5,5), pady=(5,5))
            checkboxes_r.append(checkbox)

class win_new_project(CTk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1200x700")
        self.title("ФМ Калькулятор")
        self.resizable(True, True)
        self.protocol('WM_DELETE_WINDOW', self._done)

        self.m = CTk.CTkLabel(master=self, text="Месяц начала работ")
        self.m.grid(row=2, column=0, padx=(5,5), pady=(5,5))
        self.mount = CTk.CTkComboBox(master=self, values=["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"])
        self.mount.grid(row=3, column=0, padx=(5,5), pady=(5,5))
        
        self.year_work = CTk.CTkLabel(master=self, text="Год начала работ")
        self.year_work.grid(row=4, column=0, padx=(5,5), pady=(5,5))
        self.y_pr = CTk.CTkEntry(master=self)
        self.y_pr.grid(row=5, column=0, padx=(5,5), pady=(5,5))

        self.start_pr = CTk.CTkLabel(master=self, text="Старт продаж")
        self.start_pr.grid(row=2, column=2, padx=(5,5), pady=(5,5))
        self.start_pr = CTk.CTkComboBox(master=self, values=["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"])
        self.start_pr.grid(row=3, column=2, padx=(5,5), pady=(5,5))
        
        self.year_work = CTk.CTkLabel(master=self, text="Год начала продаж")
        self.year_work.grid(row=4, column=2, padx=(5,5), pady=(5,5))
        self.y_w = CTk.CTkEntry(master=self)
        self.y_w.grid(row=5, column=2, padx=(5,5), pady=(5,5))

        self.nazvanie_proekta = CTk.CTkLabel(master=self, text='Введите название проекта')
        self.nazvanie_proekta.grid(row=0, column=1, padx=(5,5), pady=(5,5))
        self.n_p = CTk.CTkEntry(master=self)
        self.n_p.grid(row=1, column=1, padx=(5,5), pady=(5,5))

        self.stat_doh = CTk.CTkLabel(master=self, text="Выберите необходимые статьи доходов")
        self.stat_doh.grid(row=6, column=2, padx=(0,0))
        self.check_box_frame = MyCheckBoxFrame(self, values=["Доходы от жилых", "Доходы от нежилых"])
        self.check_box_frame.grid(row=7, column=2)

        self.stat_rash = CTk.CTkLabel(master=self, text="Выберите необходимые статьи расходов")
        self.stat_rash.grid(row=6, column=0, padx=(30,30), pady=(5,5), sticky="sew")        
        self.check_box_frame2 = MyCheckBoxFrame2(self)
        self.check_box_frame2.grid(row=7, column=0, padx=(30,30), sticky="sew")

        self.next_win = CTk.CTkButton(master=self, text="Все параметры выбраны", command=self.open_win_gpo)
        self.next_win.grid(row=8, column=1)

    def open_win_gpo(self):
        parametrs_d = [] 
        parametrs_r = []
        mounth_w = self.mount.get()
        mounth_pr = self.start_pr.get()
        year_w = self.y_pr.get()
        year_pr = self.y_w.get()
        nazv = self.n_p.get()
        nazv_ = combobox2[0].get()

        match_year_w = re.match(r'^\d+$', year_w)
        match_year_pr = re.match(r'^\d+$', year_pr)
        match_nazv = re.match(r'^[А-Яа-яЁё0-9]+$', nazv)

        if not(match_year_w):
            mb.showerror('Ошибка', 'Неправильно введен год начала работ')
        elif not(match_year_pr):
            mb.showerror('Ошибка', 'Неправильно введен год начала продаж')
        elif not(match_nazv):
            mb.showerror('Ошибка', 'Неправильно введено название проекта')
        elif (len(checkboxes_r) != 0):
            for el in checkboxes_r:
                if el.get():
                    parametrs_r.append(el.cget("text"))
            for el in checkboxes_d:
                if el.get():
                    parametrs_d.append(el.cget("text"))
            if (len(parametrs_r) == 0) or (len(parametrs_d) == 0):
                mb.showerror('Ошибка', 'Не выбраны статьи доходов и расходов')
            else:
                arr_nazv = sql.take_nazv_projects(nazv_comp=nazv_)
                prov = True
                for el in arr_nazv:
                    if nazv == el:
                        prov = False
                        mb.showerror('Ошибка', 'Название уже занято')
                        break
                if prov:
                    id_pr = sql.input_project(nazv_comp=nazv_, nazv=nazv, mount_w=mounth_w, yr_w=year_w, mount_pr=mounth_pr, yr_pr=year_pr)
                    arr.append(id_pr)
                    for el in parametrs_r:
                        sql.input_stati(id_pr=id_pr, nazv=el, param="Расходы")
                    for el in parametrs_d:
                        sql.input_stati(id_pr=id_pr, nazv=el, param="Доходы")
                    
                    self.withdraw()
                    d = win_gpo()
                    d.mainloop()
        
    def _done(self):
        self.destroy()
        os.system('main.py')
        sys.exit(0)
      
combobox2 = []  #ИНФОРМАЦИЯ О ПРОЕКТЕ

#Пизда какая-то дай бог здоровья челу с сайтика https://xn--80aanbzjgivicdg0b3l.xn--p1ai/customtkinter


