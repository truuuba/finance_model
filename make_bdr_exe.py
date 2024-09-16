import sys
import os
import pandas as pd
from connect_db import sql
from transliterate import translit

def create_empty_excel(filename: str, columns, dt):
    df = pd.DataFrame(columns=columns, data=dt)

    if not os.path.exists('excel_files'):
        os.makedirs('excel_files')

    filepath = os.path.join('excel_files', filename)
    excel_writer = pd.ExcelWriter(filepath, engine='xlsxwriter')
    
    df.to_excel(excel_writer, index=False, sheet_name='БДР', freeze_panes=(1, 0))
    
    # Получаем workbook и worksheet для добавления форматирования
    workbook = excel_writer.book
    worksheet = excel_writer.sheets['БДР']

    # Создаем несколько форматов для цветовой заливки строк
    format1 = workbook.add_format({'bg_color': '#E6DCCA'})                # Для параметра доходов
    format2 = workbook.add_format({'bg_color': '#B7B7A4', 'bold': True})  # Для общих параметров доходов
    format3 = workbook.add_format({'bg_color': '#FFE8D6'})                # Для параметра расходов
    format4 = workbook.add_format({'bg_color': '#D4AC94', 'bold': True})  # Для общих параметров расходов
    format5 = workbook.add_format({'bg_color': '#CB997E', 'bold': True})  # Для прибыли

    # Применяем условное форматирование для всего диапазона данных, начиная с первой строки и второго столбца
    for row in range(1, len(df) + 1):
        first_col_value = df.iloc[row-1, 0]

        # Применяем разные форматы в зависимости от значения первого столбца
        if "Доходы" in first_col_value:
            cell_format = format1
        elif "доходы" in first_col_value:
            cell_format = format2
        elif "Все расходы" in first_col_value:
            cell_format = format4
        elif "Прибыль" in first_col_value:
            cell_format = format5
        else:
            cell_format = format3

        # Применяем формат только к ячейкам, содержащим данные
        for col in range(len(columns)):
            worksheet.write(row, col, df.iloc[row-1, col], cell_format)
    
    # Применяем сетку по всей таблице (по умолчанию)
    border_format = workbook.add_format({'border': 1})  # Формат с границей вокруг ячеек

    # Определяем диапазон ячеек для применения сетки
    worksheet.conditional_format(0, 0, len(df), len(columns) - 1, {'type': 'no_blanks', 'format': border_format})
    worksheet.conditional_format(0, 0, len(df), len(columns) - 1, {'type': 'blanks', 'format': border_format})
    
    excel_writer._save()

    return filepath

def create_tabel_bdr(id_pr):
    n_t = sql.take_nazv(id_pr)
    n_t = del_probel_nazv(n_t)
    name_table = translit(n_t, language_code='ru', reversed=True)

    mount_w = del_probel_nazv(sql.take_mnth_st_w(id_pr))
    mount_pr = del_probel_nazv(sql.take_mount_pr(id_pr))
    dl = sql.take_dlit_project(id_pr)
    year_w = sql.take_yr_st_w(id_pr)
    year_prod = sql.take_year_prod(id_pr)

    columns = make_first_list(mnt_w=mount_w, mnt_prod=mount_pr, yr_w=year_w, yr_prod=year_prod, dlit=dl)
    dannie_d = sql.take_stat(id_pr=id_pr, param="Доходы")
    dannie_r = sql.take_stat(id_pr=id_pr, param="Расходы")

    #Собираем данные для БДР
    bdr_d = []
    bdr_r = []
    for el in dannie_d:
        tmp = sql.take_data_bdr_dohodi(el.id_)
        for i in range(len(tmp)):
            bdr_d.append(tmp[i])
    for el in dannie_r:
        tmp = sql.take_data_bdr_rashodi(el.id_)
        for i in range(len(tmp)):
            bdr_r.append(tmp[i])
            print(tmp[i].id_st, tmp[i].mnt, tmp[i].yr, tmp[i].trt)

    #Считаем БДР
    dt = count_bdr(columns, dannie_d, dannie_r, bdr_d, bdr_r)

    for i in range(len(dt)):
        print(dt[i])

    filepath = create_empty_excel(filename=('bdr_' + name_table + '.xlsx'), columns=columns, dt=dt)

def del_probel_nazv(nm):
    n = len(nm)
    for j in range(n-1, 0, -1):
        if nm[j] == " ":
            nm = nm[:-1]
        else:
            return nm
        
def make_first_list(mnt_w, mnt_prod, yr_w, yr_prod, dlit):
    arr_time = ["", "Общая сумма"]

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
    
    #Условие для продаж перед строительством
    if prov_w:
        prov = mnt_w + " " + str(yr_w)
        tmp = mnt_prod + " " + str(yr_prod)
        mnt = mnt_prod
        yr = yr_prod
        while (prov != tmp):
            print(prov)
            print(tmp)
            arr_time.append(tmp)
            mnt = change_mnt(mnt)
            if mnt == 'Январь':
                yr += 1
            tmp = mnt + " " + str(yr)
        for i in range(dlit):
            arr_time.append(mnt + " " + yr)
            mnt = change_mnt(mnt)
            if mnt == 'Январь':
                yr += 1
            tmp = mnt + " " + str(yr)
    
    #Условие для строительства перед продажами
    if prov_prod:
        prov = mnt_prod + " " + str(yr_prod)
        tmp = mnt_w + " " + str(yr_w)
        mnt = mnt_w
        yr = yr_w
        while (prov != tmp):
            print(prov)
            print(tmp)
            arr_time.append(tmp)
            mnt = change_mnt(mnt)
            if mnt == 'Январь':
                yr += 1
            tmp = mnt + " " + str(yr)
        for i in range(dlit):
            arr_time.append(mnt + " " + str(yr))
            mnt = change_mnt(mnt)
            if mnt == 'Январь':
                yr += 1
            tmp = mnt + " " + str(yr)
    
    return arr_time

#Меняем месяца
def change_mnt(mounth):
    arr = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
    ind = 0
    for i in range(len(arr)):
        if arr[i] == mounth:
            ind = i
            break
    if ind == 11:
        return arr[0]
    else:
        return arr[ind+1]

def found_ind_mnt(mnt):
    arr = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
    for i in range(len(arr)):
        if arr[i] == mnt:
            return i

#считаем БДР
def count_bdr(columns, d_d, d_r, bdr_d, bdr_r):
    table_gpr = []

    #идем по каждой статье доходов
    for el in d_d:
        temp = [] #массив под бдр
        temp.append(el.nazv)
        temp.append(0)
        mas_el = [] #массив под статью дохода

        #вытаскиваем все записи по этой статье
        for elem in bdr_d:
            if elem.id_st == el.id_:
                mas_el.append(elem)

        summ = 0
        #проверяем наличие доходов в этом месяце
        for i in range(2, len(columns)):
            tr = 0
            for j in range(len(mas_el)):
                tp = mas_el[j].mnt + " " + str(mas_el[j].yr)
                if columns[i] == tp:
                    tr = float(mas_el[j].doh)
                    summ += tr
            temp.append(tr)
        
        temp[1] = summ
        table_gpr.append(temp)

    # Считаем сумму доходов
    n = len(columns)
    s_d = [0] * n
    s_d[0] = "Все доходы по месяцам"

    # Проходимся по таблице
    for i in range(len(d_d)):
        for j in range(2, len(columns)):
            s_d[j] += table_gpr[i][j]

    #Считаем общий доход по всем статьям
    summ = 0
    for i in range(2, len(s_d)):
        summ += s_d[i]
    s_d[1] = summ
    table_gpr.append(s_d)
    
    #идем по каждой статье расходов
    summ = 0
    rashod = [] #таблица под расходы
    for el in d_r:
        temp = [] #массив под бдр
        temp.append(el.nazv)
        temp.append(0)
        mas_el = [] #массив под статью расходов

        #вытаскиваем все записи по этой статье
        for elem in bdr_r:
            if elem.id_st == el.id_:
                mas_el.append(elem)

        #проверяем наличие расходов в этом месяце
        for i in range(2, len(columns)):
            tr = 0
            for j in range(len(mas_el)):
                tp = mas_el[j].mnt + " " + str(mas_el[j].yr)
                if columns[i] == tp:
                    tr = float(mas_el[j].trt)
                    summ += tr
            temp.append(tr)

        temp[1] = summ
        summ = 0    
        rashod.append(temp)        
        table_gpr.append(temp)
    
    s_r = [0] * n
    pribil = [0] * n
    s_r[0] = "Все расходы по месяцам"
    pribil[0] = "Прибыль"
    # Проходимся по таблице
    for i in range(len(d_r)):
        for j in range(2, len(columns)):
            s_r[j] += rashod[i][j]

    # Считаем прибыль
    for i in range(2, len(columns)):
        pribil[i] = s_d[i] - s_r[i]

    #Считаем общее значение по месяцам расходов и прибыли
    for i in range(2, len(s_r)):
        s_r[1] += s_r[i]
        pribil[1] += pribil[i]

    table_gpr.append(s_r)
    table_gpr.append(pribil)

    return table_gpr
