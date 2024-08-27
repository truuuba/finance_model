import os
import pandas as pd
from connect_db import sql
from transliterate import translit
import math

def create_tabel_ppo(id_pr):
    #Берем данные по названию проекта
    n_t = sql.take_nazv(id_pr)
    n_t = del_probel_nazv(n_t)
    name_table = translit(n_t, language_code='ru', reversed=True)

    #Вытаскиваем статьи доходов по айди проекта
    dannie = sql.take_stat(id_pr=id_pr, param="Доходы")
    t_ppo = []
    m = sql.take_mount_pr(id_pr)
    prod = sql.take_dlit_project(id_pr)
    sht_name = []

    #Вытаскиваем данные из ППО
    for i in range(len(dannie)):
        ploshad_kv_m = sql.take_data_gpo(id_st=dannie[i].id_, param="Prod_pl")
        st_kv_m = sql.take_data_gpo(id_st=dannie[i].id_, param="Stoim")    
        cnt_kvartir = sql.take_data_gpo(id_st=dannie[i].id_, param="Kv_cnt")
        sht_name.append(dannie[i].nazv)

        #Считаем ППО по каждой статье расходов
        t_ppo.append(cout_ppo(ploshad_kv_m, st_kv_m, prod, m, cnt_kvartir))

    filepath = create_empty_excel(columns=make_first_list(m, prod), filename=('ppo_' + name_table + '.xlsx'), data=t_ppo, sheet_name = sht_name)

#Создаем файлик для вноса данных 
def create_empty_excel(columns: list, data: list, filename: str, sheet_name):
    if not os.path.exists('excel_files'):
        os.makedirs('excel_files')
    
    filepath = os.path.join('excel_files', filename)
    with pd.ExcelWriter(filepath, engine='xlsxwriter') as excel_writer:
        for i in range(len(data)):
            df = pd.DataFrame(columns=columns, data=data[i])
            df.to_excel(excel_writer, index=False, sheet_name=sheet_name[i], freeze_panes=(1, 0))

    #excel_writer._save()
    return filepath

#Считаем ППО
def cout_ppo(ploshad, st_m, prod, mounth_start, cnt_kv):
    # Проценты
    pr_ipot = 0.45
    pr_rassr = 0.39
    pr_full = 0.16
    pr_rassr_vznos = 0.35
    sr_plat_rassr = 50

    virochka = ploshad * st_m
    sr_st_kv = math.ceil(virochka/cnt_kv)
    vir_per_m = float(virochka) * 0.01
    ddu = [0] * prod
    koefs = make_koef()
    ind_m = 0
    for i in range(len(koefs)):
        if koefs[i].mounth == mounth_start:
            ddu[0] = round(koefs[i].koef * vir_per_m)
            if i != 11:
                ind_m = i + 1

    proc_y = [round(100/math.ceil(prod/12), 2)] * math.ceil(prod/12)
    proc_y[0] += 100 - sum(proc_y)
    
    #Считаем продажи
    prod_years = []
    for i in range(len(proc_y)):
        prod_years.append(float(virochka) * (proc_y[i] / 100))

    prod_posl_m = prod_years[len(prod_years) - 1] * 0.005

    #Средние продажи
    sr_prod = []
    for i in range(len(prod_years)):
        if i == 0:
            sr_prod.append(round((prod_years[0] - vir_per_m) / 11))
        elif i == (len(prod_years) - 1):
            sr_prod.append(round((prod_years[len(prod_years) - 1] - prod_posl_m) / 11))
        else:
            sr_prod.append(round(prod_years[i] / 12))

    # Считаем ДДУ
    cnt = 0
    for i in range(1, prod):
        if i == (prod - 1):
            ddu[i] = round(koefs[ind_m].koef * prod_posl_m)
        else:
            ddu[i] = round(koefs[ind_m].koef * sr_prod[cnt])
        if (i / 11) == 0:
            cnt += 1
        if ind_m == 11:
            ind_m = 0
        else:
            ind_m += 1

    # Считаем денюжки и долги
    money = []
    dolg = []
    ddu_rassr = []
    for i in range(len(ddu)):
        money.append(round(ddu[i]*pr_ipot+ddu[i]*pr_full+ddu[i]*pr_rassr*pr_rassr_vznos))
        dolg.append(round(ddu[i]-money[i]))
        ddu_rassr.append(round(dolg[i]/(sr_st_kv * pr_rassr_vznos), 2))

    #Создаем таблицу для вычилений
    table_ppo = [0] * prod
    for i in range(prod):
        table_ppo[i] = [0] * prod

    cnt = 12
    for i in range(prod):
        summa = 0
        for j in range(1, prod):
            if j == cnt:
                table_ppo[i][j] = round(dolg[i] - summa, 3)
                break
            elif j > i:
                table_ppo[i][j] = round(ddu_rassr[i] * sr_plat_rassr, 3)
            summa += table_ppo[i][j]    
        if cnt < (prod - 1):
            cnt += 1
    
    #Ищем месяц, который нужен
    arr = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
    ind_m = 0
    for i in range(1, len(arr)):
        if arr[i] == mounth_start:
            ind_m = i

    #Создаем таблицу для экселя
    ppo = [0] * (prod + 2)
    for i in range(prod + 2):
        ppo[i] = [0] * (prod + 1)

    ppo[0][0] = '$'
    for j in range(1, prod+1):
        ppo[0][j] = money[j-1]

    for i in range(1, prod+2):
        if i == (prod+1):
            ppo[i][0] = 'Итого поступления $'
        else:
            ppo[i][0] = arr[ind_m]
        for j in range(1, prod+1):
            if i == (prod + 1):
                ppo[i][j] += money[j-1]
            else:
                ppo[i][j] = table_ppo[i-1][j-1]
                ppo[prod + 1][j] += table_ppo[i-1][j-1] 
        if ind_m == 11:
            ind_m = 0
        else:
            ind_m += 1

    # Вывод ППО для теста
    for i in range(len(ppo)):
        print(ppo[i])

    return ppo

#Класс для подсчета коэффициентов
class season_k:
    def __init__(self, mounth, koef, cnt):
        self.cnt = cnt + 1
        self.mounth = mounth
        self.koef = koef

#Подсчет коэффициентов
def make_koef():
    arr = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
    k = [0.89, 0.98, 1.01, 0.99, 0.93, 0.73, 0.76, 1.03, 1.07, 1.05, 1.28, 1.28]

    koefs =[]
    for i in range(len(arr)):
        s_k = season_k(mounth=arr[i], koef=k[i], cnt=i)
        koefs.append(s_k)

    return koefs

#Шапка таблицы
def make_first_list(m, pr):
    shapka = []
    shapka.append('')
    arr = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
    ind_m = 0
    for i in range(1, len(arr)):
        if m == arr[i]:
            ind_m = i
            break
    for i in range(pr):
        shapka.append(arr[ind_m])
        if ind_m == 11:
            ind_m = 0
        else:
            ind_m += 1
    return shapka

#Удаляем пробелы названия
def del_probel_nazv(nm):
    n = len(nm)
    for j in range(n-1, 0, -1):
        if nm[j] == " ":
            nm = nm[:-1]
        else:
            return nm

