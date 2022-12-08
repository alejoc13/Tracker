import pandas as pd
import datetime
import helper.procesing as pr

def by_cfn(df,sp):
    name = input('Ingrese el nombre del archivo (Una unica columna titulada CFN): ')
    FileName = f'Documents\{name}.xlsx'
    ref = pd.read_excel(FileName,converters={'CFN':str})
    lista = [cfn.strip() for cfn in ref['CFN']]
    track = df[df['CFN'].isin(lista)]
    pr.create_excel(track,sp)

def by_SubOU(df,df_plan):
    ref = input('Ingrese las SubOU a trackear separadas por coma(,): ')
    aux = ref.split(',')
    lista = [ou.strip() for ou in aux]
    track = df[df['OU'].isin(lista)]
    pr.create_excel(track,df_plan)

def expirated(df):
    ref = datetime.datetime.today()
    df1 = pr.prepareDateTracker(df)
    track = df1[df1['EXPIRATION DATE']<ref]
    pr.excel_by_Cluster(track)

def TimeLapse(df):
    init = input('Ingrese la fecha de inicio del tracker separado por guiones(DD-MM-AAA): ')
    end = input('Ingrese la fecha de finalización del tracker separado por guiones(DD-MM-AAA): ')
    df1 = pr.prepareDateTracker(df)
    track = df1[(df1['EXPIRATION DATE']>=init) & (df1['EXPIRATION DATE']<=end)]
    pr.excel_by_Cluster(track)

def by_registration(df,sp):
    name = input('Ingrese el nombre del archivo (Una unica columna titulada REGISTRATION): ')
    FileName = f'Documents\{name}.xlsx'
    ref = pd.read_excel(FileName,converters={'REGISTRATION':str})
    lista = [cfn.strip() for cfn in ref['REGISTRATION']]
    track = df[df['REGISTRATION NUMBER'].isin(lista)]
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
    pr.excel_by_Cluster(df1)
    pass

