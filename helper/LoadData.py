import pandas as pd
import helper.procesing as pr
import datetime
import re
import os
import warnings
import numpy as np
warnings.filterwarnings('ignore')

def uploadData():
    print('Cargando Bases de datos...')
    path = os.path.join(os.path.expanduser('~'), r'Medtronic PLC\Approvals and Databases SSC - Approvals')
    countries = {
        'BO': 'Bolivia',
        'CO': 'Colombia',
        'CR': 'Costa Rica',
        'EC': 'Ecuador',
        'SV': 'El Salvador',
        # 'GT': 'Guatemala',
        'MX': 'Mexico',
        'PE': 'Perú',
        # 'VE': 'Venezuela',
        'PY': 'Paraguay',
    }
    # Ruta para encontrar las BBDD
    path_db = {
        'BO': r'\Bolivia\MDT Bolivia DB.xlsm',
        'CO': r'\Colombia\MDT Colombia DB.xlsm',
        'CR': r'\Costa Rica\MDT Costa Rica DB.xlsm',
        'EC': r'\Ecuador\MDT Ecuador DB.xlsm', 
        'PE': r'\Perú\MDT Perú DB.xlsm', 
        'SV': r'\El Salvador\MDT El Salvador DB.xlsm', 
        'MX': r'\Mexico\MDT Mexico DB.xlsm',
        'GT': r'\Guatemala\MDT Guatemala DB.xlsm',
        'VE': r'\Venezuela\MDT Venezuela DB.xlsm',
        'PY': r'\Paraguay\MDT Paraguay DB.xlsm',
    }
    df = pd.DataFrame(columns= ['Country','REGISTRATION NUMBER','REGISTRATION NAME','STATUS','RISK CLASSIFICATION','APPROVAL DATE','EXPIRATION DATE','CFN','CFN DESCRIPTION','OU','MANUFACTURING SITE','LICENSE HOLDER'])
    for country in countries.keys():
        db_path = path+path_db[country]
        print(db_path)
        temporal =pd.read_excel(db_path,sheet_name = 'ACTIVE CODES',usecols= ['REGISTRATION NUMBER','REGISTRATION NAME','STATUS','RISK CLASSIFICATION','APPROVAL DATE','EXPIRATION DATE','CFN','CFN DESCRIPTION','OU','MANUFACTURING SITE','LICENSE HOLDER'],converters={'CFN':str,'REGISTRATION NUMBER':str},
                                date_parser = ['EXPIRATION DATE','APPROVAL DATE'])
        temporal['Country'] = country
        df = pd.concat([df,temporal],ignore_index=True)
    
    db_path = path + r'\Uruguay\MDT Uruguay DB.xlsm'
    temporal =pd.read_excel(db_path,sheet_name = 'ACTIVE CODES',usecols= ['REGISTRATION NUMBER','REGISTRATION NAME','STATUS','RISK CLASSIFICATION','APPROVAL DATE','EXPIRATION DATE','CFN','OU','MANUFACTURING SITE','LICENSE HOLDER'],converters={'CFN':str,'REGISTRATION NUMBER':str},
                                date_parser = ['EXPIRATION DATE','APPROVAL DATE'])
    temporal['Country'] = 'UY'
    temporal['CFN DESCRIPTION'] = 'No disponible en BD'
    df = pd.concat([df,temporal],ignore_index=True)
    
    countries = {
        'GT': 'Guatemala',
        'VE': 'Venezuela',
    }
    
    for country in countries.keys():
        db_path = path+path_db[country]
        print(db_path)
        temporal =pd.read_excel(db_path,sheet_name = 'ACTIVE CODES',usecols= ['REGISTRATION NUMBER','REGISTRATION NAME','STATUS','APPROVAL DATE','EXPIRATION DATE','CFN','CFN DESCRIPTION','OU','MANUFACTURING SITE','LICENSE HOLDER'],converters={'CFN':str,'REGISTRATION NUMBER':str},
                                date_parser = ['EXPIRATION DATE','APPROVAL DATE'])
        temporal['Country'] = country
        temporal['RISK CLASSIFICATION'] = 'No disponible en BD'
        df = pd.concat([df,temporal],ignore_index=True)
    
    
    
    brand_code = {
        'MDT':"Medtronic",
        'COV': "Covidien"
        }
    path_db = {
        'COV': r'\Brasil\Piloto Oficial_COV_2020.05.22.xlsm',
        'MDT': r'\Brasil\Piloto Oficial_MDT_2020.06.08.xlsm'
        }

    df_brasil = pd.DataFrame(columns= ['Country','Registro ANVISA','Nome do Registro','Status do Registro','Classe de Risco ','Data de Aprovação Inicial','Data de Vencimento do Registro ','Código','Descrição do Código','BU','Fabricante Físico (Real)','Detentor do Registro'])
    for bc in brand_code.keys():
        db_path = path+path_db[bc]
        print(db_path)
        temporal =pd.read_excel(db_path,sheet_name = 'Banco de Dados',
                                usecols= ['Registro ANVISA','Nome do Registro','Status do Registro','Classe de Risco ','Data de Aprovação Inicial','Data de Vencimento do Registro ','Código','Descrição do Código','BU','Fabricante Físico (Real)','Detentor do Registro'],converters={'Código':str,'Registro ANVISA':str},
                                date_parser = ['Data de Vencimento do Registro ','Data de Aprovação Inicial'])
        temporal['Country'] = 'BR'
        df_brasil = pd.concat([df_brasil,temporal],ignore_index=True)
    
    df_brasil = df_brasil.rename(columns={'Código':'CFN','BU':'OU','Registro ANVISA':'REGISTRATION NUMBER','Data de Vencimento do Registro ':'EXPIRATION DATE',
                                'Nome do Registro':'REGISTRATION NAME', 'Descrição do Código':'CFN DESCRIPTION','Status do Registro':'STATUS','Fabricante Físico (Real)':'MANUFACTURING SITE',
                                'Detentor do Registro':'LICENSE HOLDER','Data de Aprovação Inicial':'APPROVAL DATE','Classe de Risco ':'RISK CLASSIFICATION'})
    df_brasil = df_brasil[~df_brasil['STATUS'].isin(['Cancelado','OBSOLETO','obsoleto','Obsoleto','\\','Vencido'])]
    
    df = pd.concat([df,df_brasil],ignore_index=True)
    brand_code = {
    'MDT':"Medtronic",
    'COV': "Covidien"
        }
    path_db = {
        'COV': r'\Argentina\COV Argentina DB.xlsm',
        'MDT': r'\Argentina\MDT Argentina DB.xlsm'
        }
    df_AR = pd.DataFrame(columns = ['Country','REGISTRATION NUMBER','REGISTRATION NAME','STATUS','RISK CLASSIFICATION','APPROVAL DATE','EXPIRATION DATE','CFN','CFN DESCRIPTION','OU','MANUFACTURING NAME','MANUFACTURING ADDRESS','LICENSE HOLDER'] )
    for bc in brand_code.keys():
        db_path = path+path_db[bc]
        print(db_path)
        temporal =pd.read_excel(db_path,sheet_name = 'ACTIVE CODES',usecols= ['REGISTRATION NUMBER','REGISTRATION NAME','STATUS','RISK CLASSIFICATION','APPROVAL DATE','EXPIRATION DATE','CFN','CFN DESCRIPTION','OU','MANUFACTURING NAME','MANUFACTURING ADDRESS','LICENSE HOLDER'],
                                date_parser = ['EXPIRATION DATE','APPROVAL DATE'],converters = {'REGISTRTION NUMBER':str,'CFN':str,} )
        temporal['Country'] = 'AR'
        df_AR = pd.concat([df_AR,temporal],ignore_index=True)

    df_AR['CUT ADDRESS'] = df_AR.apply(pr.cut_values,axis = 1)
    df_AR['CUT NAME'] = df_AR.apply(pr.cut_values,axis = 1,column = 'MANUFACTURING NAME')
    df_AR['MANUFACTURING SITE'] = df_AR.apply(pr.paste_problem,axis=1)

    temporal = pd.DataFrame(columns=['REGISTRATION NUMBER','REGISTRATION NAME','STATUS','RISK CLASSIFICATION','APPROVAL DATE','EXPIRATION DATE','CFN','CFN DESCRIPTION','OU','Country','MANUFACTURING SITE','LICENSE HOLDER'])
    for column in temporal.columns:
        temporal[column] = df_AR[column]
    df = pd.concat([df,temporal],ignore_index=True)

    db_path = path + r'\Honduras\MDT-MITG Base de datos Honduras.xlsx'
    print(db_path)
    honduras = pd.read_excel(db_path,usecols='A:L',converters = {'Registration number':str,'CFN':str})
    honduras = honduras.rename(columns={'BU':'OU','Descripción':'CFN DESCRIPTION','Approval date \n(dia-Mes-YY)':'APPROVAL DATE','Expire date \n(dia-Mes-YY)':'EXPIRATION DATE',
                                        'Distribuidor':'DISTRIBUTOR','Product name':'REGISTRATION NAME','Manufacturing site 2 (If apply)':'Manufacturing site 2',
                                        'Registration number':'REGISTRATION NUMBER'}
                                        )
    honduras['Country'] = 'HN'
    
    honduras['MANUFACTURING SITE'] = honduras.apply(pr.concatMfg,axis=1)
    honduras['STATUS'] = 'No disponible en BD'
    honduras['LICENSE HOLDER'] = 'No disponible en BD'
    honduras['RISK CLASSIFICATION'] = 'No disponible en BD'
    
    temporal = pd.DataFrame(columns=['REGISTRATION NUMBER','REGISTRATION NAME','STATUS','RISK CLASSIFICATION','APPROVAL DATE','EXPIRATION DATE','CFN','CFN DESCRIPTION','OU','Country','MANUFACTURING SITE','LICENSE HOLDER'])
    for column in temporal.columns:
        temporal[column] = honduras[column]
    df = pd.concat([df,temporal],ignore_index=True)

    db_path = path + r'\Honduras\MDT-MITG Base de datos Honduras.xlsx'
    print(db_path)
    honduras = pd.read_excel(db_path,sheet_name='MITG Local',converters = {'Nº LICENSE':str,'CODES':str})
    honduras = honduras.rename(columns={'CODES':'CFN','LÍNEA':'OU','Nº LICENSE':'REGISTRATION NUMBER','DESCRPTION OF THE REFERENCE CODE':'CFN DESCRIPTION',
                                        'ADDRESS':'MANUFACTURING SITE','DESCRIPCION OF APPROVAL':'REGISTRATION NAME','EXPIRATION \nDAY':'EXPIRATION DATE',
                                        'APPROVAL \nDATE':'APPROVAL DATE'}
                            )
    honduras['Country'] = 'HN'

    honduras['STATUS'] = 'No disponible en BD'
    honduras['LICENSE HOLDER'] = 'No disponible en BD'
    honduras['RISK CLASSIFICATION'] = 'No disponible en BD'

    temporal = pd.DataFrame(columns=['REGISTRATION NUMBER','REGISTRATION NAME','STATUS','RISK CLASSIFICATION','APPROVAL DATE','EXPIRATION DATE','CFN','CFN DESCRIPTION','OU','Country','MANUFACTURING SITE','LICENSE HOLDER'])
    for column in temporal.columns:
        temporal[column] = honduras[column]
    df = pd.concat([df,temporal],ignore_index=True)

    db_path = path + r'\República Dominicana\MITG Base de datos Republica Dominicana.xlsx'
    RepDo = pd.read_excel(db_path,usecols='A:M',converters = {'REGISTRO SANITARIO No.':str,'REFERENCIA':str})
    print(db_path)

    RepDo = RepDo.rename(columns={'REFERENCIA':'CFN','REGISTRO SANITARIO No.':'REGISTRATION NUMBER','TITULAR':'LICENSE HOLDER','FABRICADO POR':'MANUFACTURING SITE',
                                'BU':'OU','VIGENCIA DEL REGISTRO SANITARIO (dd/mm/aaaa)':'EXPIRATION DATE','DESCRIPCIÓN DE REFERENCIA':'CFN DESCRIPTION',
                                'DENOMINACION DEL PRODUCTO SEGÚN REGISTRO SANITARIO':'REGISTRATION NAME','FECHA DE EXPEDICIÓN':'APPROVAL DATE'})

    RepDo['STATUS'] =  'No disponible en BD'
    RepDo['Country'] = 'DO'
    RepDo['RISK CLASSIFICATION'] =  'No disponible en BD'

    temporal = pd.DataFrame(columns=['REGISTRATION NUMBER','REGISTRATION NAME','STATUS','RISK CLASSIFICATION','APPROVAL DATE','EXPIRATION DATE','CFN','CFN DESCRIPTION','OU','Country','MANUFACTURING SITE','LICENSE HOLDER'])
    for column in temporal.columns:
        temporal[column] = RepDo[column]
    df = pd.concat([df,temporal],ignore_index=True)

    for col in ['CFN', 'REGISTRATION NUMBER','REGISTRATION NAME','OU']:
        df[col] = df.apply(pr.trim_column, axis = 1, column = col)
    df = df.sort_values(by = ['Country'])

    df = df.dropna(subset='REGISTRATION NUMBER')
    print('Bases de datos Cargadas')

    return df

def load_SPlan():
    print('Cargando Submission Plan...')
    df_plan = pd.read_excel('Documents\Submission Plan - Full Report.xlsx',usecols=['Id','RAS Name','Project/Product Name','Status','Submission Type','Expected Submission Date','Approval Date','Therapy Group',
                            'Expected Approval Date','Submission Date','Country','Cluster','License Number','RAC/RAN','SubOU','License Expiration Date'])
    df_plan = df_plan.rename(columns={'Project/Product Name':'PRODUCT NAME','License Number':'REGISTRATION NUMBER','License Expiration Date':'EXPIRATION DATE'})
    print('Submission Plan cargado')
    return df_plan

def load_vouchers():
    print('Cargando los datos de Vouchers...')
    df = pd.read_excel('Documents\Vouchers Report.xlsx',converters = {'Primary':str})
    df = df.rename(columns={'Project/Product Name':'PRODUCT NAME','Primary':'REGISTRATION NUMBER'})
    print('Vouchers Cargados')
    return df

def load_criticals():
    print('Cargando los datos de Expected Critical communications...')
    df = pd.read_excel('Documents\Expected Critical Communications Report.xlsx',date_parser=['License Expiration Date'],converters={'License Number':str})
    df = df.rename(columns={'PRODUCT NAME':'PRODUCT NAME','License Number':'REGISTRATION NUMBER'})
    print('Critical communications cargados')
    return df

def load_external():
    Name = input('Ingrese el nombre del documento a cruzar con el Submission plan: ')
    FileName = f'Documents/{Name}.xlsx'
    hoja = input('Ingrese el nombre de la hoja principal con la que se cruzará el Submission Plan: ')
    print(f'Cargando {FileName}')
    df = pd.read_excel(FileName,sheet_name = hoja )
    return df

    


