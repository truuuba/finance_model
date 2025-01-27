import os
import pandas as pd
from connect_db import sql
from transliterate import translit

class data_gpo:
    def __init__(self, gpo, critic, dlit):
        self.critic = critic
        self.gpo = gpo
        self.dlit = dlit

#Заготовка меняемой таблицы
gpo = []
critical = []
dlitel = 0
datas = data_gpo(gpo=gpo, critic=critical, dlit=dlitel)

def create_tabel_gpr(id_pr, prov_create):    
    #Сначала по таблице Статы через айди проекта вытащить статьи расходов - в name_rash записываем названия и в другой массив фиксируем айдишники
    #Далее по таблице ГПР проходимся через айдишники статей и вытаскиваем зависимости и продолжительность
    dannie = sql.take_stat(id_pr=id_pr, param="Расходы")
    mounth = del_probel_nazv(sql.take_mnth_st_w(id_pr))
    year = sql.take_yr_st_w(id_pr)

    n_t = sql.take_nazv(id_pr)
    n_t = del_probel_nazv(n_t)
    name_table = translit(n_t, language_code='ru', reversed=True) 

    name_rash = []
    zavisim = []
    prod = []
    for i in range(len(dannie)):
        name_rash.append(dannie[i].nazv)
        el = sql.take_gpr_zavisim(dannie[i].id_)
        zavisim.append(el)
        print(el)
        el2 = sql.take_gpr_prod(dannie[i].id_)
        prod.append(el2)
        print(el2)

    #считаем данные по ГПР
    count_gpo(datas, name_rash, zavisim, prod)

    #Добавляем данные в БДР
    for i in range(0, len(datas.gpo)):
        mnt = mounth #Месяц начала работ
        yr = year #Год начала работ
        per = datas.gpo[i][0]
        ind_st = 0
        #поиск айдишника
        for el in dannie:
            if el.nazv == per:
                ind_st = el.id_
        arr = sql.take_data_bdr(ind_st)
        if len(arr) == 0:                                                            #ПРОВЕРКА БЛЯТЬ НА ВОНЮЧИЕ ЗАПИСИ В НАЛИЧИИ
            for j in range(1, datas.dlit + 1):
                #Проверка на наличие работ в этом месяце
                if datas.gpo[i][j] == 1:
                    sql.input_BDR(id_st=ind_st, mnt=mnt, yr=yr)
                mnt = change_mounth(mnt)
                if mnt == 'Январь':
                    yr += 1   
        else:
            n = len(arr)
            cnt = 0
            while (cnt < n):
                yr = year #Год начала работ
                for j in range(1, datas.dlit + 1):
                    #Проверка на наличие работ в этом месяце
                    if datas.gpo[i][j] == 1:
                        sql.update_bdr2(id_= arr[cnt].id_, mnt=mnt, yr=yr)     
                        cnt += 1
                    mnt = change_mounth(mnt)
                    if mnt == 'Январь':
                        yr += 1            

    #Добавляем продолжительность в базу
    sql.input_prod_project(id_pr=id_pr, prod=datas.dlit)

    if prov_create:
        filepath = create_empty_excel(columns=make_first_list(mounth, datas.dlit, year),
                                  filename=('gpr_' + name_table + '.xlsx'))

#Меняем месяца
def change_mounth(mounth):
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

# Функция для подсветки ячеек
def highlight_cells(val):
    color = '#FFFCF2'
    for crit in datas.critic:
        if val == crit:
            color = '#EB5E28'
            break
    if val == 1:
        color = '#CCC5B9'
    return f'background-color: {color}'

#Создаем файлик для вноса данных 
def create_empty_excel(columns: list, filename: str, sheet_name: str = 'Таблица ГПР'):
    df = pd.DataFrame(columns=columns, data=datas.gpo)

    if not os.path.exists('excel_files'):
        os.makedirs('excel_files')

    filepath = os.path.join('excel_files', filename)
    excel_writer = pd.ExcelWriter(filepath, engine='xlsxwriter')
    df.to_excel(excel_writer, index=False, sheet_name=sheet_name, freeze_panes=(1, 0))
    # Сохраняем DataFrame в Excel с применением стиля
    df.style.applymap(highlight_cells).to_excel(excel_writer, index=False, sheet_name=sheet_name)

    excel_writer._save()

    return filepath

def insertion_sort(unsorted, nazv, zav, prod, ind, ish):
    """ сортировка вставками """
    n = len(unsorted)
    # итерация по неотсортированным массивам
    for i in range(1, n):
        # получаем значение элемента
        val = unsorted[i]

        val_n = nazv[i]
        val_z = zav[i]
        val_pr = prod[i]
        val_ind = ind[i]
        val_ish = ish[i]
        # записываем в hole индекс i
        hole = i
        # проходим по массиву в обратную сторону, пока не найдём элемент больше текущего
        while hole > 0 and unsorted[hole - 1] > val:
            # переставляем элементы местами , чтобы получить правильную позицию
            unsorted[hole] = unsorted[hole - 1]

            nazv[hole] = nazv[hole - 1]
            zav[hole] = zav[hole - 1]
            prod[hole] = prod[hole - 1]
            ind[hole] = ind[hole - 1]
            ish[hole] = ish[hole - 1]
            # делаем шаг назад
            hole -= 1
        # вставляем значение на верную позицию
        unsorted[hole] = val

        nazv[hole] = val_n
        zav[hole] = val_z
        prod[hole] = val_pr
        ind[hole] = val_ind
        ish[hole] = val_ish

def count_gpo(data_gpr, name_rash, zavisim, prod):
    del_probeli_zavisim(zavisim)
    print(name_rash)
    print(zavisim)
    print(prod)

    numbers = []
    #Подготовка всех переменнных
    dl = len(name_rash)
    for i in range(dl):
        numbers.append(i+1)
    ish_isha = []
    rasch_nazv = []
    rasch_zav = []
    rasch_prod = []
    numb = []
    dlina = []

    # Добавление всех параметров, которые идут от нулевого события

    indexes = []
    for j in range(dl):
        if zavisim[j] == "0":
            #Двигаем данные в новые массивы данные
            rasch_zav.append(zavisim[j])
            rasch_nazv.append(name_rash[j])
            rasch_prod.append(prod[j])
            numb.append(numbers[j])
            dlina.append(int(prod[j]))
            ish_isha.append(0)
            indexes.append(j)

    #Удаляем данные из оригинального массива
    for i in range(len(indexes)):
        name_rash.pop(indexes[i])
        zavisim.pop(indexes[i])
        prod.pop(indexes[i])
        numbers.pop(indexes[i])
        for j in range(len(indexes)):
            indexes[j] -= 1
    indexes.clear()

    # Делаем прямую проходку для поиска продолжительности процесов

    while len(rasch_nazv) < dl:
        indexes = []
        for i in range(len(name_rash)):
            prov = True
            z = zavisim[i].split()
            max_dl = []
            num = []
            for l in range(len(z)):
                if not(int(z[l]) in numb):
                    prov = False
            if prov:
                for el in z:
                    for j in range(len(rasch_nazv)):
                        if int(el) == numb[j]:
                            num.append(numb[j])
                            max_dl.append(int(dlina[j])+int(prod[i]))
                maxim = max_dl[0]
                m_num = num[0]
                for j in range(len(num)-1):
                    if maxim < max_dl[j+1]:
                        maxim = max_dl[j+1]
                        m_num = num[j+1]
                ish_isha.append(m_num)
                dlina.append(maxim)
                indexes.append(i)
                rasch_nazv.append(name_rash[i])
                rasch_zav.append(zavisim[i])
                rasch_prod.append(prod[i])
                numb.append(numbers[i])
            z.clear()
            max_dl.clear()
            num.clear
        for el in indexes:
            name_rash.pop(el)
            zavisim.pop(el)
            prod.pop(el)
            numbers.pop(el)
            for j in range(len(indexes)):
                indexes[j] -= 1
        indexes.clear()

    #cортировка
    for i in range(len(dlina)):
        dlina[i] = int(dlina[i])

    insertion_sort(dlina, rasch_nazv, rasch_zav, rasch_prod, numb, ish_isha)

    #Добавляем значение КОН - конец всех процессов
    vse_zav = []
    st = ""
    for i in range(len(rasch_nazv)):
        z = rasch_zav[i].split()
        for el in z:
            if not(el in vse_zav):
                vse_zav.append(el)
    for i in range(len(rasch_nazv)):
        if not(str(numb[i]) in vse_zav):
            st += str(numb[i]) + " "
            
    rasch_nazv.append("КОН")
    rasch_zav.append(st)
    rasch_prod.append(0)
    numb.append(len(rasch_nazv))
    ish_isha.append(numb[-2])
    dlina.append(dlina[-1])

    #Начинаем обратный проход

    dl_obr = []
    nazv_obr = []
    zav_obr = []
    prod_obr = []
    numb_obr = []
    ish_isha_obr = []
    dlina_obr = []

    provereno = []
    for i in range(dl+1):
        provereno.append(False)

    dl_obr.append(dlina[-1])
    nazv_obr.append(rasch_nazv[-1])
    zav_obr.append(rasch_zav[-1])
    prod_obr.append(rasch_prod[-1])
    numb_obr.append(numb[-1])
    ish_isha_obr.append(ish_isha[-1])
    dlina_obr.append(dlina[-1])

    n = len(rasch_nazv)
    rasch_nazv.pop(n-1)
    rasch_zav.pop(n-1)
    rasch_prod.pop(n-1)
    numb.pop(n-1)
    ish_isha.pop(n-1)
    dlina.pop(n-1)

    while len(nazv_obr) < (dl + 1):
        cnt = 0
        while(cnt < len(nazv_obr)):
            z = zav_obr[cnt].split()
            if not provereno[cnt]:
                for el in z:
                    if el != '0':
                        prov = True
                        # Туть проверяем на то возможны ли вообще другие вычисления
                        for i in range(len(rasch_nazv)):
                            za = rasch_zav[i].split()
                            for elem in za:
                                if el == elem:
                                    prov = False
                        if prov:
                            # Ищем другие зависимости
                            for i in range(len(nazv_obr)): 
                                za = zav_obr[i].split()
                                for elem in za:
                                    if (elem == el) and (cnt != i):
                                        indexes.append(i)
                            min_zn = dl_obr[cnt] - int(prod_obr[cnt])
                            for elem in indexes:
                                step = dl_obr[elem] - int(prod_obr[elem])
                                if min_zn > step:
                                    min_zn = step
                            dl_obr.append(min_zn)
                            
                            #Ищем индекс текущего пиздеца
                            index = 0
                            for i in range(len(rasch_nazv)):
                                if numb[i] == int(el):
                                    index = i
                            if len(rasch_nazv) != 0:
                                nazv_obr.append(rasch_nazv[index])
                                zav_obr.append(rasch_zav[index])
                                prod_obr.append(int(rasch_prod[index]))
                                numb_obr.append(numb[index])
                                ish_isha_obr.append(ish_isha[index])
                                dlina_obr.append(dlina[index])

                                rasch_nazv.pop(index)
                                rasch_zav.pop(index)
                                rasch_prod.pop(index)
                                numb.pop(index)
                                ish_isha.pop(index)
                                dlina.pop(index)

                                provereno[cnt] = True
                    else:
                        provereno[cnt] = True
            cnt += 1                    

    data_gpr.dlit = dlina_obr[0]        # ОБЩАЯ ПРОДОЛЖИТЕЛЬНОСТЬ

    #Ищем критический путь
    data_gpr.critic = []
    for i in range(len(nazv_obr)):
        if dl_obr[i] == dlina_obr[i]:
            data_gpr.critic.append(nazv_obr[i])     
    data_gpr.critic.pop(0)        

    #Удаляем состояние КОН
    nazv_obr.pop(0)
    zav_obr.pop(0)
    prod_obr.pop(0)
    numb_obr.pop(0)
    ish_isha_obr.pop(0)
    dlina_obr.pop(0)
    dl_obr.pop(0)

    #Отсортируем по порядку массив (не сортируем только исходники - они нас не интересуют больше)
    insertion_sort(numb_obr, nazv_obr, zav_obr, prod_obr, dlina_obr, dl_obr)

    #Создаем табличку данных по ГПО
    data_gpr.gpo = [0] * len(nazv_obr)
    for i in range(len(nazv_obr)):
        data_gpr.gpo[i] = [0] * (data_gpr.dlit + 1)

    #Просчитываем данные внутри самой ГПО
    for i in range(len(nazv_obr)):
        data_gpr.gpo[i][0] = nazv_obr[i]
        for j in range(1, data_gpr.dlit+1):
            if ((dlina_obr[i] - int(prod_obr[i]) + 1) <= j) and (dlina_obr[i] >= j):
                data_gpr.gpo[i][j] = 1
        print(data_gpr.gpo[i])

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

#Очередная попытка удалить пробелы
def del_probeli_zavisim(arr):
    for i in range(len(arr)):   #for per in arr
        n = len(arr[i])
        for j in range(n-1, 0, -1):
            if arr[i][j] == " ":
                arr[i] = arr[i][:-1]
            else:
                break

def del_probel_nazv(nm):
    n = len(nm)
    for j in range(n-1, 0, -1):
        if nm[j] == " ":
            nm = nm[:-1]
        else:
            return nm
