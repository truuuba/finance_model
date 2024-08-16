#Подготовка файлов для тестирования по ГПР
str1 = ['Ura', 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
str2 = ['Ya', 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
str3 = ['Zaeb', 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
str4 = ['Les', 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
str5 = ['Kent', 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
str6 = ['uMB', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
str7 = ['rel', 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
str8 = ['PUPPY', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]

gpr = []
gpr.append(str1)
gpr.append(str2)
gpr.append(str3)
gpr.append(str4)
gpr.append(str5)
gpr.append(str6)
gpr.append(str7)
gpr.append(str8)

mounth = 'Ноябрь'
year = 2024

import customtkinter as CTk
from CTkTable import *

#Добавляем функцию для поиска месяцев и годов
def make_first_list(mnth, cnt, yr):
    lst = ['Параметры расходов']
    counter = 0
    ind = 0
    mounthes = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
    for i in range(len(mounthes)):
        if mounthes[i] == mnth:
            ind = i
    while (counter < cnt):
        lst.append(mounthes[ind] + ' ' + str(yr))
        if ind == 11:
            ind = 0
            yr += 1
        else:
            ind += 1
        counter += 1     
    return lst

#ДОБАВИТЬ СКРОЛ ВПРАВО И ВЛЕВО
class MyTabFrame(CTk.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master, width=600, height=600, orientation='horizontal')

        self.lst = make_first_list(mounth, len(gpr[0]), year)
        self.tab_gpr = []
        self.tab_gpr.append(self.lst)
        for i in range(len(gpr)):
            self.tab_gpr.append(gpr[i])
        self.table = CTkTable(master=self, row=len(self.tab_gpr), column=len(self.tab_gpr[0]), values=self.tab_gpr)
        self.table.grid(row=0, column=0)


class win_table_gpr(CTk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("1200x700")
        self.title("ФМ Калькулятор")
        self.resizable(True, True)

        self.t = MyTabFrame(self)
        self.t.grid(row=0, column=0)




