import pandas as pd
import datetime

def cut_values(row,column = 'MANUFACTURING ADDRESS',sep = '\n' ):
    var = str(row[column])
    if sep in var:
        var = var.split(sep)
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
    file = input('Nombre del archivo a guardar: ')
    path = f'trackResults\{file}.xlsx'
    try:
        df_registration = df.drop(['CFN','CFN DESCRIPTION'],axis = 1)
        df_registration = df_registration.drop_duplicates(subset=['REGISTRATION NUMBER'])
    except:
        df_registration = df_registration
    repo = pd.merge(splan,df_registration, how='inner',on='REGISTRATION NUMBER')
    with pd.ExcelWriter(path) as writer1:
        df.to_excel(writer1, sheet_name = 'CFNs', index = False)
        df_registration.to_excel(writer1, sheet_name = 'Registros', index = False)
        repo.to_excel(writer1, sheet_name = 'Comparado con Submission Plan', index = False)

def excel_by_Cluster(df,splan):
    print('Este documento esta seccionado por Cluster')
    file = input('Nombre del archivo a guardar: ')
    path = f'trackResults\{file}.xlsx'
    nola = ['CR','MX','GT','SV','HN','CU','NI','PA']
    sola = ['AR','PE','BO','UY','PY']
    cela = ['EC','CO','VE','RD','PR']
    df_nola = df[df['Country'].isin(nola)]
    df_sola = df[df['Country'].isin(sola)]
    df_cela = df[df['Country'].isin(cela)]
    df_brasil = df[df['Country'] == 'BR']
    df_registration = df.drop(['CFN','CFN DESCRIPTION','Country'],axis = 1)
    df_registration = df_registration.rename(columns={'STATUS':'Status base de datos'})
    df_registration = df_registration.drop_duplicates(subset=['REGISTRATION NUMBER'])
    repo = pd.merge(splan,df_registration, how='inner',on='REGISTRATION NUMBER')
    with pd.ExcelWriter(path) as writer1:
        df_nola.to_excel(writer1, sheet_name = 'NOLA', index = False)
        df_sola.to_excel(writer1, sheet_name = 'SOLA', index = False)
        df_cela.to_excel(writer1, sheet_name  = 'CELA',index = False)
        df_brasil.to_excel(writer1, sheet_name  = 'Brazil',index = False)
        repo.to_excel(writer1, sheet_name = 'Comparado con Submission Plan', index = False)

def excel_ClusterReport(df):
    print('Este documento esta seccionado por Cluster')
    file = input('Nombre del archico a guardar: ')
    path = f'trackResults\{file}.xlsx'
    df_nola = df[df['Cluster'] == 'NOLA']
    df_sola = df[df['Cluster']=='SOLA']
    df_cela = df[df['Cluster']=='CELA']
    df_brasil = df[df['Cluster'] == 'BRAZIL']
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

def reference(row,col='Expected Approval Date'):
    a = row[col]
    delta = datetime.timedelta(90)
    ref = a + delta
    return ref

def excel_byTG(df):
    print('Este documento esta seccionado por Therapy Group')
    file = input('Nombre del archivo a guardar: ')
    path = f'trackResults\{file}.xlsx'
    df_at = df[df['Therapy Group']=='AT']
    df_cat = df[df['Therapy Group']=='CathLab']
    df_oricu = df[df['Therapy Group']=='OR&ICU']
    
    with pd.ExcelWriter(path) as writer1:
        df_at.to_excel(writer1, sheet_name = 'AT', index = False)
        df_oricu.to_excel(writer1, sheet_name  = 'OR&ICU',index = False)
        df_cat.to_excel(writer1,sheet_name='CathLab',index = False)

def excel_Vouchers(mx,ar):
    file = input('Nombre del archivo a guardar: ')
    path = f'trackResults\{file}.xlsx' 
    with pd.ExcelWriter(path) as writer1:
        mx.to_excel(writer1, sheet_name = 'Mexico', index = False)
        ar.to_excel(writer1, sheet_name  = 'Argentina',index = False)

def simple_excel(df):
    file = input('Nombre del archivo a guardar: ')
    path = f'trackResults\{file}.xlsx'
    with pd.ExcelWriter(path) as writer1:
        df.to_excel(writer1, sheet_name = 'Cosolidado', index = False)

def sp_trim(df):
    print('Pre proesando los datos....')
    for name in df.columns:
        if name not in ['Expected Submission Date','Submission Date','Approval Date','Expected Approval Date','Created','PC3 Due Date','DM Complete date','PC3 Complete Date','License Expiration Date','EXPIRATION DATE']:
            df[name] = df.apply(trim_column,axis = 1,column = name)
    print('Los datos fueron correctamente trimeados')
    return df

def chageSeparator(row,col = 'Submission Type'):
    a = str(row[col])
    a = a.replace("\n", "/")
    return a

def newCol(df):
    df2 = pd.DataFrame(columns=df.columns)
    for i in range(len(df)):
        if type(df['ST cut'][i]) is list:
            temporal = pd.DataFrame(columns=df.columns)
            a = [val for val in df['ST cut'][i]]
            for j in range(len(a)):
                for name in df.columns:
                    temporal[name] = [df[name][i]]
                temporal['Submission Type']= [a[j]]
                df2 = pd.concat([df2,temporal],ignore_index = True)
        else:
            temporal = pd.DataFrame(columns=df.columns)
            for name in df.columns:
                temporal[name] = [df[name][i]]
        
            temporal['Submission Type'] =df['Submission Type'][i]
            df2 = pd.concat([df2,temporal],ignore_index = True)
    df2 = df2.drop('ST cut',axis=1)
    df2 = df2[df2['Submission Type'].isin(['CFN Withdrawal','Renewal'])]
    return df2

def expandRows(df):
    df['Submission Type'] = df.apply(chageSeparator,axis=1,col = 'Submission Type')
    df['ST cut'] = df.apply(cut_values,axis =1,column='Submission Type',sep='/')
    new_criticals = newCol(df)
    return new_criticals

def obtain_row(df):

    list_RS  = df["REGISTRATION NUMBER"].unique()
    list_error= {}
    for rs in list_RS:
        guarda = []
        for i in range(len(df["REGISTRATION NUMBER"])):
                if df["REGISTRATION NUMBER"][i]== rs:
                    guarda.append(i+2)
        contador = 0
        gap = []
        for j in range(len(guarda)-1):
            if guarda[j+1] != (guarda[j]+1):
                gap.append([guarda[j],guarda[j+1]])
                contador = contador + 1
        if contador != 0:
            list_error[rs] = gap
    return list_error

def gapTracking(df1):
    final_report = pd.DataFrame(columns=["RSS","gaps","Country"])
    contries = df1['Country'].unique()
    for country in contries:
        print(f'Procesando los datos de {country}')
        df = df1[df1['Country']==country]
        df= df.reset_index(drop=True)
        list_error = obtain_row(df)
        report = pd.DataFrame(columns=["RSS","gaps","Country"])
        report["RSS"],report["gaps"],report["Country"] = list_error.keys(),list_error.values(),country
        final_report = pd.concat([final_report,report])
        print(f'Report for {country} was done!')
    return final_report

def sufix_search(df,ref):
     temp = df[df['CFN'].str.startswith(ref)]
     return temp

def filterDates(df):
    df1 = df[(df['Expected Submission Date'].isna()) & (df['Status'] != 'CANCELLED')]
  
    return df1

def ProccesNoID(df,sp):
    val = [rs.strip() for rs in sp['REGISTRATION NUMBER']]
    df = df[~df['REGISTRATION NUMBER'].isin(val)]
    df = df.drop('CFN',axis = 1)
    df = df.drop_duplicates(subset = ['REGISTRATION NUMBER'])
    return df

def excelnoID(df):
    file = input('Nombre del archivo a guardar: ')
    path = f'trackResults\{file}.xlsx' 
    df.to_excel(path,index = False)

def PrepareDats(df):
    df = df.dropna(subset='EXPIRATION DATE')
    return df

def SepareteRegistrations(df):
    df = df.drop('CFN',axis=1)
    df =df.drop_duplicates(subset='REGISTRATION NUMBER')
    df = sp_trim(df)
    return df
