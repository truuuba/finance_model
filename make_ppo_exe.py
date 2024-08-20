import os
import pandas as pd
from connect_db import sql
from transliterate import translit

def create_tabel_ppo(id_pr):
    #Вытаскиваем статьи доходов по айди проекта
    dannie = sql.take_stat(id_pr=id_pr, param="Доходы")

    #Вытаскиваем данные из ППО
    ploshad_kv_m = ''

    t_ppo = cout_ppo(ploshad_kv_m, st_kv_m, prod, m, cnt_kvartir)
    filepath = create_empty_excel(columns=make_first_list(m, prod),
                                  filename=('gpo_' + name_work + '.xlsx'), data=t_ppo)
    
#Подумать над реализацией двух листов в файле экселя для каждой статьи доходов
