import os
import pandas as pd
from connect_db import sql

class data_gpo:
    def __init__(self, gpo, critic, dlit):
        self.critic = critic
        self.gpo = gpo
        self.dlit = dlit

#Не забыть добавить в project продолжительность строительных работ

def create_tabel_gpr(id_pr):
    #Заготовка меняемой таблицы
    gpo = []
    critical = []
    dlitel = 0
    datas = data_gpo(gpo=gpo, critic=critical, dlit=dlitel)
    
    '''
    name_rash = ["Ura", "Ya", "Zaeb", "Les", "Kent", "uMB", "rel", "PUPPY"]
    zavisim = ["0", "3", "1", "0", "0", "5 8", "0", "1 2 4"]
    prod = ["2", "2", "1", "17", "2", "1", "9", "10"]
    '''

    #Сначала по таблице Статы через айди проекта вытащить статьи расходов - в name_rash записываем названия и в другой массив фиксируем айдишники
    #Далее по таблице ГПР проходимся через айдишники статей и вытаскиваем зависимости и продолжительность

    #считаем данные по ГПР
    count_gpo(datas, name_rash, zavisim, prod)

    filepath = create_empty_excel(columns=make_first_list(mounth, datas.dlit, year),
                                  filename=('gpr_' + name_table + '.xlsx'))