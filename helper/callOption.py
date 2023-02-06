import pandas as pd
import numpy as np 
import datetime
import helper.LoadData as load
import helper.procesing as pr
import helper.trackerType as tr

def option_cfn(token):
    df = load.uploadData()
    df_plan = load.load_SPlan(token)
    df_plan = pr.sp_trim(df_plan)
    tr.by_cfn(df,df_plan)

def option_reg(token):
    df = load.uploadData()
    df_plan = load.load_SPlan(token)
    df_plan = pr.sp_trim(df_plan)
    tr.by_registration(df,df_plan)

def option_SubOU(token):
    df = load.uploadData()
    df_plan = load.load_SPlan(token)
    df_plan = pr.sp_trim(df_plan)
    tr.by_SubOU(df,df_plan)

def option_Planning(token):
    df_plan = load.load_SPlan(token)
    tr.Plannig_review(df_plan)

def option_submitted(token):
    df_plan = load.load_SPlan(token)
    df_plan = pr.sp_trim(df_plan)
    tr.Submitted_Control(df_plan)

def option_voucher(token):
    df_plan = load.load_SPlan(token)
    df_plan = pr.sp_trim(df_plan)
    vou = load.load_vouchers()
    vou =  pr.sp_trim(vou)
    tr.vouchers(vou,df_plan)

def option_Timelapse(token):
    df = load.uploadData()
    sp = load.load_SPlan(token)
    tr.TimeLapse(df,sp)

def option_expired(token):
    df = load.uploadData()
    sp = load.load_SPlan(token)
    tr.expirated(df,sp)

def cancel_criticalOP(token):
    df = load.uploadData()
    criticals =load.load_criticals(token)
    criticals = pr.expandRows(criticals)
    criticals = pr.sp_trim(criticals)
    criticals=tr.cancel_criticals(criticals,df)

def CFN_WithdrawalOP(token):
    df = load.uploadData()
    criticals =load.load_criticals(token)
    criticals = pr.expandRows(criticals)
    criticals = pr.sp_trim(criticals)
    tr.approved_criticals(criticals,df)

def gaps_option(token):
    df = load.uploadData()
    print('Procesando las bases de datos...Espere')
    consolidate = pr.gapTracking(df)
    print('Datos preocesados')
    pr.simple_excel(consolidate)

def sufix_option(token):
    df = load.uploadData()
    df_plan = load.load_SPlan(token)
    df_plan = pr.sp_trim(df_plan)
    tr.by_cfn_sufix(df,df_plan)

def track_manual(token):
    df_plan = load.load_SPlan(token)
    df_plan = pr.sp_trim(df_plan)
    external = load.load_external()
    external = pr.sp_trim(external)
    pr.create_excel(external,df_plan)

def MissedExpectedDAte(token):
    df_plan = load.load_SPlan(token)
    df_plan = pr.sp_trim(df_plan)
    tr.missed(df_plan)

def planingRenewals(token):
    df = load.uploadData()
    df_plan = load.load_SPlan(token)
    df_plan = pr.sp_trim(df_plan)
    tr.noSubmissionID(df,df_plan)

def compareNoID(token):
    df_plan = load.load_SPlan(token)
    df_plan = pr.sp_trim(df_plan)
    tr.externalNoID(df_plan)
    pass

def DatesComparation(token):
    df = load.uploadData()
    df_plan = load.load_SPlan(token)
    tr.comparareDAtes(df,df_plan)




