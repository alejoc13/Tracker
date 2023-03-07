import pandas as pd
import datetime
import helper.procesing as pr

def by_cfn(df,sp):
    name = input('Ingrese el nombre del archivo (Una unica columna titulada CFN): ')
    FileName = f'Documents\{name}.xlsx'
    ref = pd.read_excel(FileName,converters={'CFN':str})
    ref = ref.dropna()
    lista = [cfn.strip() for cfn in ref['CFN']]
    track = df[df['CFN'].isin(lista)]
    sp = sp.drop(['SubOU'],axis = 1)
    pr.create_excel(track,sp)

def by_SubOU(df,df_plan):
    ref = input('Ingrese las SubOU a trackear separadas por coma(,): ')
    aux = ref.split(',')
    lista = [ou.strip() for ou in aux]
    track = df[df['OU'].isin(lista)]
    df_plan = df_plan.drop(['SubOU'],axis = 1)
    pr.create_excel(track,df_plan)

def expirated(df,sp):
    ref = datetime.datetime.today()
    df['EXPIRATION DATE'] = pd.to_datetime(df['EXPIRATION DATE'],errors='coerce')
    df['EXPIRATION DATE'] = df['EXPIRATION DATE'].fillna(datetime.datetime.today())
    track = df[(df['EXPIRATION DATE']<ref) & (df['STATUS'].isin(['Vigente','No disponible en BD']))]
    sp = sp.drop(['SubOU'],axis = 1)
    pr.excel_by_Cluster(track,sp)

def TimeLapse(df,sp):
    init = input('Ingrese la fecha de inicio del tracker separado por guiones(DD-MM-AAA): ')
    end = input('Ingrese la fecha de finalización del tracker separado por guiones(DD-MM-AAA): ')
    init = datetime.datetime(int(init.split('-')[2]),int(init.split('-')[1]),int(init.split('-')[0]))
    end = datetime.datetime(int(end.split('-')[2]),int(end.split('-')[1]),int(end.split('-')[0]))
    df['EXPIRATION DATE'] = pd.to_datetime(df['EXPIRATION DATE'],errors='coerce')
    df['EXPIRATION DATE'] = df['EXPIRATION DATE'].fillna(datetime.datetime.today())
    df = df.drop_duplicates(subset='REGISTRATION NUMBER')
    track = df[(df['EXPIRATION DATE']>=init) & (df['EXPIRATION DATE']<=end) & (df['STATUS'].isin(['vigente','Vigente','No disponible en BD']))]
    sp = sp.drop(['SubOU'],axis = 1)
    pr.excel_by_Cluster(track,sp)

def by_registration(df,sp):
    name = input('Ingrese el nombre del archivo (Una unica columna titulada REGISTRATION): ')
    FileName = f'Documents\{name}.xlsx'
    ref = pd.read_excel(FileName,converters={'REGISTRATION':str})
    ref= ref.dropna()
    lista = [cfn.strip() for cfn in ref['REGISTRATION']]
    track = df[df['REGISTRATION NUMBER'].isin(lista)]
    sp = sp.drop(['SubOU'],axis = 1)
    pr.create_excel(track,sp)

def Submitted_Control(sp):
    sp = sp[sp['Status'] == "SUBMITTED"]
    sp = sp.dropna(subset=['Submission Date'])
    sp['referencia'] = sp.apply(pr.reference,axis=1)
    track = sp[sp['referencia']<datetime.datetime.today()]
    pr.excel_ClusterReport(track)
    pr.excel_byTG(track)

def Plannig_review(sp):
    df_out = sp[((sp['Status'].isin(['SUBMITTED'])) & (sp['Submission Date'].isna())) | ((sp['Approval Date'].isna()) & (sp['Status'] == 'APPROVED'))] 
    pr.excel_byTG(df_out)

def vouchers(vou,df_plan):
    dfmx = df_plan[(df_plan['Status'] == 'SUBMITTED') & (df_plan['Country'] == 'MX - Mexico')]
    dfar = df_plan[(df_plan['Status'] == 'SUBMITTED') & (df_plan['Country'] == 'AR - Argentina')]
    voumx = vou[vou['Country']=='MX - Mexico']
    vouar = vou[vou['Country']=='AR - Argentina']
    refmx = set(voumx['REGISTRATION NUMBER'])
    refar = set(vouar['REGISTRATION NUMBER'])
    mx_missed = dfmx[~dfmx['REGISTRATION NUMBER'].isin(refmx)]
    ar_missed = dfar[~dfar['REGISTRATION NUMBER'].isin(refar)]
    pr.excel_Vouchers(mx_missed,ar_missed)

def cancel_criticals(criticals,df):
    criticals = criticals[(criticals['Status'] == 'CANCELLED') & (criticals['Submission Type'] == 'Renewal')]
    listado = [var.strip() for var in criticals['REGISTRATION NUMBER']]
    listado = set(listado)
    df1 = df[(df['REGISTRATION NUMBER'].isin(listado)) & (df['STATUS']!= 'Vigente, no se renovará')]
    pr.create_excel(df1,criticals)

def approved_criticals(criticals,df):
    criticals = criticals[(criticals['Status'] == 'APPROVED') & (criticals['Submission Type'] == 'CFN Withdrawal')]
    listado = [var.strip() for var in criticals['REGISTRATION NUMBER']]
    listado = set(listado)
    df1 = df[(df['REGISTRATION NUMBER'].isin(listado))]
    pr.create_excel(df1,criticals)

def by_cfn_sufix(df,sp):
    sufix_df = pd.DataFrame(columns=df.columns)
    name = input('Ingrese el nombre del archivo (Una unica columna titulada CFN): ')
    FileName = f'Documents\{name}.xlsx'
    ref = pd.read_excel(FileName,converters={'CFN':str})
    ref = ref.dropna()
    lista = [cfn.strip() for cfn in ref['CFN']]
    for cfn in lista:
        temp = pr.sufix_search(df,cfn)
        sufix_df = pd.concat([sufix_df,temp])
    pr.create_excel(sufix_df,sp)

def missed(df):
    df1 = pr.filterDates(df)
    pr.excel_ClusterReport(df1)
    pr.excel_byTG(df1)

def noSubmissionID(df,sp):
    init = input('Ingrese la fecha de inicio del tracker separado por guiones(DD-MM-AAA): ')
    end = input('Ingrese la fecha de finalización del tracker separado por guiones(DD-MM-AAA): ')
    df1 = pr.prepareDateTracker(df)
    track = df1[(df1['EXPIRATION DATE']>=init) & (df1['EXPIRATION DATE']<=end)]
    sp = sp[sp['Submission Type'].str.contains('Renewal')]
    sp = sp[~sp['Status'].isin(['APPROVED','CANCELLED'])]
    track = pr.ProccesNoID(track,sp)
    pr.excelnoID(track)

def externalNoID(sp):
    name = input('Ingrese el nombre del archivo: ')
    sheet = input('Ingrese el nombre de la hoja en la que estan almacenados los datos: ')
    FileName = f'Documents\{name}.xlsx'
    track = pd.read_excel(FileName,sheet_name=sheet,converters={'REGISTRATION NUMBER':str})
    sp = sp[sp['Submission Type'].str.contains('Renewal')]
    track = pr.ProccesNoID(track,sp)
    pr.excelnoID(track)

def comparingDates(row):
    if row['EXPIRATION DATE BD'] == row['EXPIRATION DATE SP']:
        return 'Consistente'
    else:
        return 'Inconsistente'

def comparareDAtes(df,df_plan):
    df1 = pd.DataFrame(columns=['REGISTRATION NUMBER','EXPIRATION DATE'])
    df = pr.SepareteRegistrations(df)
    df = pr.sp_trim(df)
    df1['REGISTRATION NUMBER'] = df['REGISTRATION NUMBER']
    df1['EXPIRATION DATE BD'] = df['EXPIRATION DATE']
    df_plan = pr.sp_trim(df_plan)
    df_plan = df_plan[~df_plan['Status'].isin(['APPROVED','CANCELLED'])]
    df_plan = df_plan.rename(columns={'EXPIRATION DATE':'EXPIRATION DATE SP'})
    df_merge = pd.merge(df_plan,df1, how='inner',on='REGISTRATION NUMBER')
    df_merge['Consistencia'] = df_merge.apply(comparingDates,axis=1)
    df_merge = df_merge[df_merge['Consistencia'] == 'Inconsistente']
    df_merge.to_excel('trackResults\Consistencia en Fechas de vencimientos.xlsx',index=False)

def ApprovalsOnFuture(df,sp):
    df = pr.sp_trim(df)
    df = pr.preparaApprovlas(df)
    df1 = df[df['APPROVAL DATE']>datetime.datetime.today()]
    ref = datetime.timedelta(1)+datetime.datetime.today()
    df = df.replace({ref:'review'})
    pr.excel_by_Cluster(df1,sp)
    pass


    

    
    

