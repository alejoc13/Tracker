import pandas as pd
import datetime
import helper.procesing as pr

def by_cfn(df,sp):
    name = input('Ingrese el nombre del archivo (Una unica columna titulada CFN): ')
    FileName = f'Documents\{name}.xlsx'
    ref = pd.read_excel(FileName,converters={'CFN':str})
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
    df1 = pr.prepareDateTracker(df)
    track = df1[df1['EXPIRATION DATE']<ref]
    sp = sp.drop(['SubOU'],axis = 1)
    pr.excel_by_Cluster(track,sp)

def TimeLapse(df,sp):
    init = input('Ingrese la fecha de inicio del tracker separado por guiones(DD-MM-AAA): ')
    end = input('Ingrese la fecha de finalización del tracker separado por guiones(DD-MM-AAA): ')
    df1 = pr.prepareDateTracker(df)
    track = df1[(df1['EXPIRATION DATE']>=init) & (df1['EXPIRATION DATE']<=end)]
    sp = sp.drop(['SubOU'],axis = 1)
    pr.excel_by_Cluster(track,sp)

def by_registration(df,sp):
    name = input('Ingrese el nombre del archivo (Una unica columna titulada REGISTRATION): ')
    FileName = f'Documents\{name}.xlsx'
    ref = pd.read_excel(FileName,converters={'REGISTRATION':str})
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
    lista = [cfn.strip() for cfn in ref['CFN']]
    for cfn in lista:
        temp = pr.sufix_search(df,cfn)
        sufix_df = pd.concat([sufix_df,temp])
    pr.create_excel(sufix_df,sp)

def missed(df):
    df1 = pr.filterDates(df)
    pr.excel_ClusterReport(df1)
    pr.excel_byTG(df1)

    
