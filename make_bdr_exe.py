import sys
import os
import pandas as pd
from connect_db import sql
from transliterate import translit

def create_empty_excel(filename: str):
    df = pd.DataFrame(columns=columns, data=dt)

    if not os.path.exists('excel_files'):
        os.makedirs('excel_files')

    filepath = os.path.join('excel_files', filename)
    excel_writer = pd.ExcelWriter(filepath, engine='xlsxwriter')
    
    df.to_excel(excel_writer, index=False, sheet_name='БДР', freeze_panes=(1, 0))
    excel_writer._save()

    return filepath

def create_tabel_bdr(id_pr):
    n_t = sql.take_nazv(id_pr)
    n_t = del_probel_nazv(n_t)
    name_table = translit(n_t, language_code='ru', reversed=True)

    #Не забыть удалить пробелы после месяцев
    columns=make_first_list(mounth_w, dlit, year_w)
    dt = count_bdr_rashodi(gpr, trati)

    filepath = create_empty_excel(filename=('bdr_' + name_table + '.xlsx'))

def del_probel_nazv(nm):
    n = len(nm)
    for j in range(n-1, 0, -1):
        if nm[j] == " ":
            nm = nm[:-1]
        else:
            return nm
        
def make_first_list(mnt_w, mnt_prod, yr_w, yr_prod):
    arr_time = []
    mnt = ''
    yr = 0

    #Проверка на то, что раньше
    prov_w = False
    prov_prod = False
    if yr_w > yr_prod:
        prov_w = True
    elif yr_w < yr_prod:
        prov_prod = True
    else:
        ind_mnt_w = found_ind_mnt(mnt_w)
        ind_mnt_prod = found_ind_mnt(mnt_prod)
        if ind_mnt_prod > ind_mnt_w:
            #Проверка продажи
            prov_prod = True
        else:
            #Проверка строительства
            prov_w = True

def found_ind_mnt(mnt):
    arr = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
    for i in range(len(arr)):
        if arr[i] == mnt:
            return i