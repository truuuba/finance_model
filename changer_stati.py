from connect_db import sql
import customtkinter as CTk

CTk.set_appearance_mode("dark")
CTk.set_default_color_theme("green")

rashodi_check = []
dohodi_check = []

class Frame_Dohodov(CTk.CTkFrame):
    def __init__(self, master, values):
        super().__init__(master)
        self.values = values
        for i, value in enumerate(self.values):
            checkbox = CTk.CTkCheckBox(self, text=value)
            checkbox.grid(row=i, column=0, padx=(5,5), pady=(5,5))
            dohodi_check.append(checkbox)

class Frame_Rashodov(CTk.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master, width=400, height=330)

        self.values = ["Формирование участка", "Проектные работы", "Изыскательные работы", "Технологическое присоединение", "Контроль и технический надзор", "Сдача объекта", "PR, реклама и маркетинговые исследования", "Управленческие расходы", "Страхование ответственности застройщика", "Расходы на содержание непроданных квартир", "Госпошлины за гос.регистрацию сделок с недвижимостью", "Налоги (кроме УСН и НСП)", "Услуги риэлторов", "Вознаграждение за брокеридж (для ТРЦ)", "Субсидирование ипотечной ставки", "Возврат ДС дольщикам", "Социальная инфраструктура", "Услуги банка (билинг)"]
        self.stat_rash_zakazch = CTk.CTkLabel(master=self, text="Статьи расходов заказчика:")
        self.stat_rash_zakazch.grid(row=0, column=0, padx=(0,0))
        for i, value in enumerate(self.values):
            checkbox = CTk.CTkCheckBox(self, text=value)
            checkbox.grid(row=i+1, column=0, padx=(5,5), pady=(10,10))
            rashodi_check.append(checkbox)

        self.values = "Фундаменты", "Общестр-ные работы ниже отм.0", "Земляные работы", "Каркас ниже отм. 0.00" 
        self.stat_rash_CMP = CTk.CTkLabel(master=self, text="Расходы СМР (Подземная часть)")
        self.stat_rash_CMP.grid(row=20, column=0, padx=(5,5), pady=(5,5))
        for i, value in enumerate(self.values):
            checkbox = CTk.CTkCheckBox(self, text=value)
            checkbox.grid(row=i+21, column=0, padx=(5,5), pady=(5,5))
            rashodi_check.append(checkbox)

        self.values = "Несущие конструкции", "Общестроительные работы выше отм.0", "Наружные стены и наружная отделка", "Заполнение оконных проемов", " Заполнение дверных проемов", "Металлоконструкции", "Кровля"    
        self.stat_rash_CMP = CTk.CTkLabel(master=self, text="Расходы СМР (Конструкции надземной части)")
        self.stat_rash_CMP.grid(row=25, column=0, padx=(5,5), pady=(5,5))
        for i, value in enumerate(self.values):
            checkbox = CTk.CTkCheckBox(self, text=value)
            checkbox.grid(row=i+26, column=0, padx=(5,5), pady=(5,5))
            rashodi_check.append(checkbox)

        self.values = "Внутренние стены и перегородки", "Двери входные в квартиры, двери МОП", "Внутренние отделочные работы (предчистовая кв.)", "Внутренние отделочные работы чистовые (по квар.)"
        self.stat_rash_CMP = CTk.CTkLabel(master=self, text="Расходы СМР (Внутренние работы)")
        self.stat_rash_CMP.grid(row=33, column=0, padx=(5,5), pady=(5,5))
        for i, value in enumerate(self.values):
            checkbox = CTk.CTkCheckBox(self, text=value)
            checkbox.grid(row=i+34, column=0, padx=(5,5), pady=(5,5))
            rashodi_check.append(checkbox)

        self.values = "Лифты, подъемники. Диспетчеризация. Пуско-н", "Специализированное транспортное оборудование", "Системы ВК", "Газоснабжение", "ИТП, узел учета тепловой энергии, АСКУЭ", "Система отопления", "Противопожарные системы", "Электрические сети и оборудование", "Внутренняя вентиляция и дымоудаление", "Кондиционирование"
        self.stat_rash_CMP = CTk.CTkLabel(master=self, text="Расходы СМР (Внутренние инженерные системы)")
        self.stat_rash_CMP.grid(row=38, column=0, padx=(5,5), pady=(5,5))
        for i, value in enumerate(self.values):
            checkbox = CTk.CTkCheckBox(self, text=value)
            checkbox.grid(row=i+39, column=0, padx=(5,5), pady=(5,5))
            rashodi_check.append(checkbox)

        self.stat_rash_CMP = CTk.CTkLabel(master=self, text="Расходы СМР (Оборудование)")
        self.stat_rash_CMP.grid(row=49, column=0, padx=(5,5), pady=(5,5))
        checkbox = CTk.CTkCheckBox(self, text="Технологическое оборудование")
        checkbox.grid(row=50, column=0, padx=(5,5), pady=(5,5))
        rashodi_check.append(checkbox)

        self.values = "Подготовка площадки строительства", "Благоустройство и озеленение", "Наружный водопровод и канализация", "Наружная ливневая канализация", "Наружные тепловые сети, ЦТП", "Наружные трубопроводы газоснабжения", "Наружные сети электроснабжения, трансформат", "Наружное освещение", "Наружные сети связи"
        self.stat_rash_CMP = CTk.CTkLabel(master=self, text="Расходы СМР (Внутренние инженерные системы)")
        self.stat_rash_CMP.grid(row=51, column=0, padx=(5,5), pady=(5,5))
        for i, value in enumerate(self.values):
            checkbox = CTk.CTkCheckBox(self, text=value)
            checkbox.grid(row=i+52, column=0, padx=(5,5), pady=(5,5))
            rashodi_check.append(checkbox)

        self.values = "Реализация услуг по вывозу мусора", "Временные здания, сооружения (бытовой городок)", "Содержание строительной площадки", "Временный водопровод", "Временное освещение, элект-ие, КТП, ТП, ВРУ", "Временное ограждение, ворота", "Дороги временные", "Вертикальный транспорт", " Непредвиденные расходы по объекту"
        self.stat_rash_CMP = CTk.CTkLabel(master=self, text="Расходы СМР (Прочее)")
        self.stat_rash_CMP.grid(row=61, column=0, padx=(5,5), pady=(5,5))
        for i, value in enumerate(self.values):
            checkbox = CTk.CTkCheckBox(self, text=value)
            checkbox.grid(row=i+62, column=0, padx=(5,5), pady=(5,5))
            rashodi_check.append(checkbox)

        self.stat_rash_CMP = CTk.CTkLabel(master=self, text="Финансовая деятельность")
        self.stat_rash_CMP.grid(row=71, column=0, padx=(5,5), pady=(5,5))
        checkbox = CTk.CTkCheckBox(self, text="% по кредитам и займам")
        checkbox.grid(row=72, column=0, padx=(5,5), pady=(5,5))
        rashodi_check.append(checkbox)
        
        self.stat_rash_CMP = CTk.CTkLabel(master=self, text="Налог на прибыль")
        self.stat_rash_CMP.grid(row=73, column=0, padx=(5,5), pady=(5,5))
        checkbox = CTk.CTkCheckBox(self, text="Налог на прибыль")
        checkbox.grid(row=74, column=0, padx=(5,5), pady=(5,5))
        rashodi_check.append(checkbox)
           
        self.values = "Заработная плата основных рабочих", "Заработная плата машинистов БК", "Заработная плата электриков"
        self.stat_rash_CMP = CTk.CTkLabel(master=self, text="Заработная плата")
        self.stat_rash_CMP.grid(row=75, column=0, padx=(5,5), pady=(5,5))
        for i, value in enumerate(self.values):
            checkbox = CTk.CTkCheckBox(self, text=value)
            checkbox.grid(row=i+76, column=0, padx=(5,5), pady=(5,5))
            rashodi_check.append(checkbox)

        self.values = "Услуги башенного крана", "Услуги мачтового подъемника", "Услуги стропальщика"
        self.stat_rash_CMP = CTk.CTkLabel(master=self, text="Услуги грузоподъемных механизмов")
        self.stat_rash_CMP.grid(row=79, column=0, padx=(5,5), pady=(5,5))
        for i, value in enumerate(self.values):
            checkbox = CTk.CTkCheckBox(self, text=value)
            checkbox.grid(row=i+80, column=0, padx=(5,5), pady=(5,5))
            rashodi_check.append(checkbox)

class win_change_stati(CTk.CTk):
    def __init__(self):
        super().__init__() 
        self.geometry("1200x700")
        self.title("ФМ Калькулятор")
        self.resizable(True, True)

        self.ttle = CTk.CTkLabel(master=self, text="Выберите статьи, которые хотите использовать")
        self.ttle.grid(row=0, column=1, padx=(5,5), pady=(5,5))

        self.stat_doh = CTk.CTkLabel(master=self, text="Выберите необходимые статьи доходов")
        self.stat_doh.grid(row=1, column=2, padx=(0,0))
        self.check_box_frame = Frame_Dohodov(self, values=["Доходы от жилых", "Доходы от нежилых"])
        self.check_box_frame.grid(row=2, column=2)

        self.stat_rash = CTk.CTkLabel(master=self, text="Выберите необходимые статьи расходов")
        self.stat_rash.grid(row=1, column=0, padx=(30,30), pady=(5,5), sticky="sew")        
        self.check_box_frame2 = Frame_Rashodov(self)
        self.check_box_frame2.grid(row=2, column=0, padx=(30,30), sticky="sew")

        self.but_update = CTk.CTkButton(master=self, text="Обновить данные")
        self.but_update.grid(row=3, column=1, padx=(5,5), pady=(5,5))



