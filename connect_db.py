import pyodbc

class stt:
    def __init__(self, id_, nazv):
        self.id_= id_
        self.nazv = nazv

class bdr:
    def __init__(self, id_, mnt, yr):
        self.id_= id_
        self.mnt = mnt
        self.yr = yr

class bdr_d:
    def __init__(self, id_, mnt, yr, doh):
        self.id_= id_
        self.mnt = mnt
        self.yr = yr
        self.doh = doh

class bdr_r:
    def __init__(self, id_, id_st, mnt, yr, trt):
        self.id_= id_
        self.id_st = id_st
        self.mnt = mnt
        self.yr = yr
        self.trt = trt

class bdr_dh:
    def __init__(self, id_, id_st, mnt, yr, doh):
        self.id_= id_
        self.id_st = id_st
        self.mnt = mnt
        self.yr = yr
        self.doh = doh

class Sql:
    def __init__(self, database="FM_model", server=r"NODE2\DBLMSSQLSRV", username="connect_FM_model", password=r"9*%dA6lU&T6)p2PX", driver="ODBC Driver 17 for SQL Server"):
        connectionString = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'
        #return pyodbc.connect(connectionString)
        self.cnxn = pyodbc.connect(connectionString)

    def take_nazv_comp(self):
        cursor = self.cnxn.cursor()
        zapros = "SELECT nazv FROM company;"
        cursor.execute(zapros)
        data = cursor.fetchall()
        cursor.close
        del_probel(data, 0)
        datas = make_arr_list(data)
        return datas

    #для проверки названий проектов
    def take_nazv_projects(self, nazv_comp):
        cursor = self.cnxn.cursor()
        zapros = "SELECT project.nazv FROM project INNER JOIN company ON project.Id_c = company.ID WHERE company.nazv = '" + nazv_comp + "';"
        cursor.execute(zapros)
        data = cursor.fetchall()
        cursor.close
        del_probel(data, 0)
        datas = make_arr_list(data)
        return datas

    def take_log_empl(self, id_comp):
        cursor = self.cnxn.cursor()
        zapros = "SELECT employe.log_ FROM employe WHERE employe.Id_c = " + str(id_comp) + ";"
        cursor.execute(zapros)
        data = cursor.fetchall()
        cursor.close
        del_probel(data, 0)
        datas = make_arr_list(data)
        return datas

    def found_ind_company(self, nazv):
        cursor = self.cnxn.cursor()
        zapros = "SELECT ID FROM company WHERE nazv = "+ "'"+ nazv + "'" +";"
        cursor.execute(zapros)
        data = cursor.fetchall()
        #берем и вытаскиваем переменную
        n_normal = 0
        for el in data:
            for e in el:
                n_normal = e
        return n_normal
    
    def found_id(self, name_):
        cursor = self.cnxn.cursor()
        zapros = 'SELECT MAX(ID) FROM ' + name_ + ';'
        cursor.execute(zapros)
        data = cursor.fetchall()
        #берем и вытаскиваем переменную
        id_emp = 0
        for el in data:
            for e in el:
                id_emp = e
        return id_emp + 1

    def take_log_pass_adm(self, n):
        cursor = self.cnxn.cursor()
        zapros = "SELECT administ.log_, administ.pas_ FROM administ INNER JOIN company ON administ.Id_k = company.ID WHERE company.nazv = " + "'" + n + "'" + ';'
        cursor.execute(zapros)
        data = cursor.fetchall()
        del_probel(data, 0)
        del_probel(data, 1)
        datas = make_arr_matrix(data)
        cursor.close()
        return datas
    
    def input_empl(self, id_c, fam, im, otch, log_, pas_):
        cursor = self.cnxn.cursor()
        id_empl = self.found_id(name_='employe')
        zapros = 'INSERT INTO employe (ID, Id_c, fam, imya, otch, log_, pas_) VALUES ('+ str(id_empl) + ', '+ str(id_c) + ", '" + fam + "', " + "'" + im + "', " + "'" + otch + "', " + "'" + log_ +  "', " + "'" + pas_ + "');"
        print(zapros)
        cursor.execute(zapros)
        self.cnxn.commit()
        cursor.close()

    def take_log_pas_empl(self, nazv):
        cursor = self.cnxn.cursor()
        zapros = "SELECT employe.log_, employe.pas_ FROM employe INNER JOIN company ON employe.Id_c = company.ID WHERE company.nazv = " + "'" + nazv + "'" + ';'
        cursor.execute(zapros)
        data = cursor.fetchall()
        del_probel(data, 0)
        del_probel(data, 1)
        datas = make_arr_matrix(data)
        cursor.close()
        return datas
    
    def take_project(self, nazv):
        cursor = self.cnxn.cursor()
        zapros = "SELECT project.nazv FROM project INNER JOIN company ON project.Id_c = company.ID WHERE company.nazv = " + "'" + nazv + "';"
        cursor.execute(zapros)
        data = cursor.fetchall()
        del_probel(data, 0)
        datas = make_arr_list(data)
        return datas

    def input_project(self, nazv_comp, nazv, mount_w, yr_w, mount_pr, yr_pr):
        cursor = self.cnxn.cursor()
        #Поиск айдишника компании по названию
        id_c = self.found_ind_company(nazv_comp)
        id_ = self.found_id(name_='project')
        zapros = 'INSERT INTO project (ID, Id_c, nazv, mount_w, yr_w, mount_pr, yr_pr) VALUES (' + str(id_) + ', ' + str(id_c) + ", '" + nazv + "', " + "'" + mount_w + "', " + "'" + yr_w + "', " + "'" + mount_pr + "', " + "'" + yr_pr + "');"
        print(zapros)
        cursor.execute(zapros)
        self.cnxn.commit()
        cursor.close()
        return id_

    def input_stati(self, id_pr, nazv, param):
        cursor = self.cnxn.cursor()
        id_ = self.found_id(name_='stati')
        zapros = 'INSERT INTO stati (ID, id_p, d_r, nazv) VALUES (' + str(id_) + ", " + str(id_pr) + ", '" + param +"', " + "'" + nazv + "');"
        print(zapros)
        cursor.execute(zapros)
        self.cnxn.commit()
        cursor.close()

    def take_stat(self, id_pr, param):
        cursor = self.cnxn.cursor()
        zapros = 'SELECT ID, nazv FROM stati WHERE Id_p = ' + str(id_pr) + " and d_r = '" + param + "';"
        print(zapros)
        cursor.execute(zapros)
        data = cursor.fetchall()
        del_probel(data, 1)
        datas = []
        for i in range(len(data)):
            el = stt(data[i][0], data[i][1])
            datas.append(el)
        return datas

    def input_gpr(self, id_st, prod, zav):
        cursor = self.cnxn.cursor()
        id_ = self.found_id(name_='GPR')
        zapros = 'INSERT INTO GPR (ID, Id_st, Prodolj, Zavisim) VALUES (' + str(id_) + ", " + str(id_st) + ", " + str(prod) + ", '" + zav + "');"
        print(zapros)
        cursor.execute(zapros)
        self.cnxn.commit()
        cursor.close()

    def input_ppo(self, id_st, pr_pl, stoim, kv_cnt):
        cursor = self.cnxn.cursor()
        id_ = self.found_id(name_='PPO')
        zapros = 'INSERT INTO PPO (ID, Id_st, Prod_pl, Stoim, Kv_cnt) VALUES (' + str(id_) + ", " + str(id_st) + ", " + str(pr_pl) + ", " + str(stoim) + ", " + kv_cnt + ");"
        print(zapros)
        cursor.execute(zapros)
        self.cnxn.commit()
        cursor.close()

    def take_gpr_zavisim(self, id_st):
        cursor = self.cnxn.cursor()
        zapros = 'SELECT Zavisim FROM GPR WHERE Id_st = '+ str(id_st) +';'
        print(zapros)
        cursor.execute(zapros)
        data = make_arr_list(cursor.fetchall())
        n_data = data[0]
        return n_data
    
    def take_gpr_prod(self, id_st):
        cursor = self.cnxn.cursor()
        zapros = 'SELECT Prodolj FROM GPR WHERE Id_st = '+ str(id_st) +';'
        print(zapros)
        cursor.execute(zapros)
        data = make_arr_list(cursor.fetchall())
        return str(data[0])
    
    def take_mnth_st_w(self, id_p):
        cursor = self.cnxn.cursor()
        zapros = 'SELECT mount_w FROM project WHERE ID = ' + str(id_p) +';'
        print(zapros)
        cursor.execute(zapros)
        data = make_arr_list(cursor.fetchall())
        del_probel(data, 1)
        return data[0]
    
    def take_yr_st_w(self, id_p):
        cursor = self.cnxn.cursor()
        zapros = 'SELECT yr_w FROM project WHERE ID = ' + str(id_p) +';'
        print(zapros)
        cursor.execute(zapros)
        data = make_arr_list(cursor.fetchall())
        return data[0]
    
    def take_nazv(self, id_p):
        cursor = self.cnxn.cursor()
        zapros = 'SELECT nazv FROM project WHERE ID = ' + str(id_p) +';'
        print(zapros)
        cursor.execute(zapros)
        data = make_arr_list(cursor.fetchall())
        del_probel(data, 1)
        return data[0]
    
    def take_id_nazv_project(self, nazv_pr, nazv_comp):
        cursor = self.cnxn.cursor()
        zapros = "SELECT project.ID FROM project INNER JOIN company ON project.Id_c = company.ID WHERE company.nazv = '" + nazv_comp + "' AND project.nazv = '" + nazv_pr + "';"
        print(zapros)
        cursor.execute(zapros)
        data = make_arr_list(cursor.fetchall())
        return data[0]
        
    def input_prod_project(self, prod, id_pr):
        cursor = self.cnxn.cursor()
        zapros = "UPDATE project SET prod = " + str(prod) + " WHERE ID = " + str(id_pr) + ";"
        print(zapros)
        cursor.execute(zapros)
        self.cnxn.commit()
        cursor.close()
    
    def take_data_gpo(self, id_st, param):
        cursor = self.cnxn.cursor()
        zapros = "SELECT " + param + " FROM PPO WHERE Id_st = " + str(id_st) + ";"
        print(zapros)
        cursor.execute(zapros)
        data = make_arr_list(cursor.fetchall())
        return data[0]
    
    def take_mount_pr(self, id_p):
        cursor = self.cnxn.cursor()
        zapros = 'SELECT mount_pr FROM project WHERE ID = ' + str(id_p) +';'
        print(zapros)
        cursor.execute(zapros)
        data = make_arr_list(cursor.fetchall())
        del_probel(data, 1)
        return data[0]
    
    def take_dlit_project(self, id_p):
        cursor = self.cnxn.cursor()
        zapros = 'SELECT prod FROM project WHERE ID = ' + str(id_p) +';'
        print(zapros)
        cursor.execute(zapros)
        data = make_arr_list(cursor.fetchall())
        return data[0]
    
    def input_BDR(self, id_st, mnt, yr):
        cursor = self.cnxn.cursor()
        id_ = self.found_id(name_='BDR_r')
        zapros = "INSERT INTO BDR_r (ID, Id_st, mnt, yr) VALUES (" + str(id_) + ", " + str(id_st) + ", '" + mnt + "', " + str(yr) + ");"
        print(zapros)
        cursor.execute(zapros)
        self.cnxn.commit()
        cursor.close()

    def take_data_bdr(self, id_st):
        cursor = self.cnxn.cursor()
        zapros = "SELECT ID, mnt, yr FROM BDR_r WHERE Id_st = " + str(id_st) + ";"
        print(zapros)
        cursor.execute(zapros)
        data = cursor.fetchall()
        del_probel(data, 1)
        datas = []
        for i in range(len(data)):
            el = bdr(data[i][0], data[i][1], data[i][2])
            datas.append(el)
        return datas
    
    def update_bdr(self, id_, trt):
        cursor = self.cnxn.cursor()
        zapros = "UPDATE BDR_r SET trati = " + str(trt) + " WHERE ID = " + str(id_) + ";"
        print(zapros)
        cursor.execute(zapros)
        self.cnxn.commit()
        cursor.close()
    
    def update_bdr2(self, id_, mnt, yr):
        cursor = self.cnxn.cursor()
        zapros = "UPDATE BDR_r SET mnt = '" + mnt + "', yr = " + str(yr) + " WHERE ID = " + str(id_) + ";"
        print(zapros)
        cursor.execute(zapros)
        self.cnxn.commit()
        cursor.close()

    def input_bdr_d(self, id_st, mnt, yr, doh):
        cursor = self.cnxn.cursor()
        id_ = self.found_id(name_='BDR_d')
        zapros = "INSERT INTO BDR_d (ID, Id_st, mnt, yr, dohodi) VALUES (" + str(id_) + ", " + str(id_st) + ", '" + mnt + "', " + str(yr) + ", " + str(doh) + ");"
        print(zapros)
        cursor.execute(zapros)
        self.cnxn.commit()
        cursor.close()

    def take_bdr_d(self, id_st):
        cursor = self.cnxn.cursor()
        zapros = "SELECT ID, mnt, yr, dohodi FROM BDR_d WHERE id_st = " + str(id_st) + ";"
        print(zapros)
        cursor.execute(zapros)
        data = cursor.fetchall()
        del_probel(data, 1)
        datas = []
        for i in range(len(data)):
            el = bdr_d(data[i][0], data[i][1], data[i][2], data[i][3])
            datas.append(el)
        return datas
    
    def update_bdr_d(self, id_, mnt, yr, doh):
        cursor = self.cnxn.cursor()
        zapros = "UPDATE BDR_d SET mnt = '" + mnt + "', yr = " + str(yr) + ", dohodi = " + str(doh) + " WHERE ID = " + str(id_) + ";"
        print(zapros)
        cursor.execute(zapros)
        self.cnxn.commit()
        cursor.close()
    
    def take_bdr_r_id(self, id_st):
        cursor = self.cnxn.cursor()
        zapros = "SELECT ID FROM BDR_r WHERE Id_st = " + str(id_st) + ";"
        cursor.execute(zapros)
        data = make_arr_list(cursor.fetchall())
        return data

    def take_data_bdr_r(self, id_):
        cursor = self.cnxn.cursor()
        zapros = "SELECT trati FROM BDR_r WHERE ID = " + str(id_) + ";"
        print(zapros)
        cursor.execute(zapros)
        data = make_arr_list(cursor.fetchall())
        return data[0]
    
    def take_year_prod(self, id_):
        cursor = self.cnxn.cursor()
        zapros = "SELECT yr_pr FROM project WHERE ID = " + str(id_) + ";"
        print(zapros)
        cursor.execute(zapros)
        data = make_arr_list(cursor.fetchall())
        return data[0]
    
    def take_data_bdr_rashodi(self, id_st):
        cursor = self.cnxn.cursor()
        zapros = "SELECT ID, Id_st, mnt, yr, trati FROM BDR_r WHERE Id_st = " + str(id_st) + ";"
        print(zapros)
        cursor.execute(zapros)
        data = cursor.fetchall()
        del_probel(data, 2)
        datas = []
        for i in range(len(data)):
            el = bdr_r(data[i][0], data[i][1], data[i][2], data[i][3], data[i][4])
            datas.append(el)
        return datas
    
    def take_data_bdr_dohodi(self, id_st):
        cursor = self.cnxn.cursor()
        zapros = "SELECT ID, Id_st, mnt, yr, dohodi FROM BDR_d WHERE Id_st = " + str(id_st) + ";"
        print(zapros)
        cursor.execute(zapros)
        data = cursor.fetchall()
        del_probel(data, 2)
        datas = []
        for i in range(len(data)):
            el = bdr_dh(data[i][0], data[i][1], data[i][2], data[i][3], data[i][4])
            datas.append(el)
        return datas
    
    def take_list_users(self, id_c):
        cursor = self.cnxn.cursor()
        zapros = "SELECT log_ FROM employe WHERE Id_c = " + str(id_c) + ";"
        print(zapros)
        cursor.execute(zapros)
        data = make_arr_list(cursor.fetchall())
        return data
    
    def del_user(self, Id_c, log_):
        cursor = self.cnxn.cursor()
        zapros = "DELETE FROM employe WHERE Id_c = " + str(Id_c) + " AND log_='" + log_ + "';"
        print(zapros)
        cursor.execute(zapros)
        self.cnxn.commit()
        cursor.close()

    def del_project(self, Id_c, nazv):
        cursor = self.cnxn.cursor()
        #Поиск ID проекта по которому удаляем данные
        zapros = "SELECT ID FROM project WHERE Id_c = " + str(Id_c) + " AND nazv = '" + nazv + "';"
        print(zapros)
        cursor.execute(zapros)
        data = cursor.fetchall()
        id_p = 0
        for el in data:
            for e in el:
                id_p = e
        #Поиск ID статей по которому удаляем эти статьи
        zapros = "SELECT ID FROM stati WHERE Id_p = " + str(id_p) + ";"
        print(zapros)
        cursor.execute(zapros)
        data = make_arr_list(cursor.fetchall())
        #Удаление таблиц по ID
        for id_st in data:
            #Удаление БДР расходы
            zapros = "DELETE FROM BDR_r WHERE Id_st = " + str(id_st) + ";"
            print(zapros)
            cursor.execute(zapros)
            self.cnxn.commit()
            #Удаление БДР доходы
            zapros = "DELETE FROM BDR_d WHERE Id_st = " + str(id_st) + ";"
            print(zapros)
            cursor.execute(zapros)
            self.cnxn.commit()
            #Удаление ГПР
            zapros = "DELETE FROM GPR WHERE Id_st = " + str(id_st) + ";"
            print(zapros)
            cursor.execute(zapros)
            self.cnxn.commit()
            #Удаление ППО
            zapros = "DELETE FROM PPO WHERE Id_st = " + str(id_st) + ";"
            print(zapros)
            cursor.execute(zapros)
            self.cnxn.commit()

        #Удаление самих статей
        zapros = "DELETE FROM stati WHERE Id_p = " + str(id_p) + ";"
        print(zapros)
        cursor.execute(zapros)
        self.cnxn.commit()
        #Удаление проекта
        zapros = "DELETE FROM project WHERE ID = " + str(id_p) + ";"
        print(zapros)
        cursor.execute(zapros)
        self.cnxn.commit()
        cursor.close()

sql = Sql()

def del_probel(arr, ind):
    for el in arr:
        n = len(el[ind]) - 1 
        while n > 0:
            per = el[ind]
            if el[ind][-1] == " ":
                el[ind] = per[:-1]
                n -= 1
            else:
                break

def make_arr_list(arr):
    arr_normal = []
    for el in arr:
        for e in el:
            arr_normal.append(e)
    return arr_normal

def make_arr_matrix(arr):
    arr_normal = []
    for i in range(len(arr)):
        a = []
        for j in range(len(arr[0])):
            a.append(arr[i][j])
        arr_normal.append(a)
    return arr_normal
