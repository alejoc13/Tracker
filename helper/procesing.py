import pandas as pd
def cut_values(row,column = 'MANUFACTURING ADDRESS'):
    var = str(row[column])
    if '\n' in var:
        var = var.split('\n')
        var1 = [name.strip() for name in var]
        return var1
    else:
        return var

def trim_column(row,column = 'REGISTRATION NUMBER'):
    a = str(row[column])
    a = a.strip()
    return a

def paste_problem(row,name ='CUT ADDRESS',address =  'CUT ADDRESS'):
    a = row[name]
    b = row[address]
    if type(a) is list:
        junto = ''
        for nombre,dir in zip(a,b):
            junto += nombre + ' ' + dir + '\n'
        return junto
    else:
        junto = a + ' ' + b + '\n'
        return junto

def concatMfg(row,colum1 = 'Manufacturing site 1',colum2 = 'Manufacturing site 2'):
    mfg1 = str(row[colum1])
    mfg2 = str(row[colum2])
    mfg = mfg1 + '\n' + mfg2
    return mfg

def create_excel(df,splan):
    file = input('Nombre del archico a guardar: ')
    path = f'trackResults\{file}.xlsx'
    df_registration = df.drop(['CFN','CFN DESCRIPTION'],axis = 1)
    df_registration = df_registration.drop_duplicates(subset=['REGISTRATION NUMBER'])
    repo = pd.merge(splan,df_registration, how='inner',on='REGISTRATION NUMBER')
    with pd.ExcelWriter(path) as writer1:
        df.to_excel(writer1, sheet_name = 'CFNs', index = False)
        df_registration.to_excel(writer1, sheet_name = 'Registros', index = False)
        repo.to_excel(writer1, sheet_name = 'Comparado con Submission Plan', index = False)

def excel_by_Cluster(df):
    file = input('Nombre del archico a guardar: ')
    path = f'trackResults\{file}.xlsx'
    nola = ['CR','MX','GT','SV','HN','CU','NI','PA']
    sola = ['AR','PE','BO','UY','PY']
    cela = ['EC','CO','VE','RD','PR']
    df_nola = df[df['Country'].isin(nola)]
    df_sola = df[df['Country'].isin(sola)]
    df_cela = df[df['Country'].isin(cela)]
    df_brasil = df[df['Country'] == 'BR']
    with pd.ExcelWriter(path) as writer1:
        df_nola.to_excel(writer1, sheet_name = 'NOLA', index = False)
        df_sola.to_excel(writer1, sheet_name = 'SOLA', index = False)
        df_cela.to_excel(writer1, sheet_name  = 'CELA',index = False)
        df_brasil.to_excel(writer1, sheet_name  = 'Brazil',index = False)



def prepareDateTracker(df):
    df1 = df.copy()
    df1 = df1.dropna(subset=['EXPIRATION DATE'])
    df1 = df1[~df1['Country'].isin(['DO','HN'])]
    df1['EXPIRATION DATE'] = pd.to_datetime(df1['EXPIRATION DATE'])
    return df1