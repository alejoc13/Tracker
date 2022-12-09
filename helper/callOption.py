import pandas as pd
import numpy as np 
import datetime
import helper.LoadData as load
import helper.procesing as pr
import helper.trackerType as tr

def option_cfn():
    df = load.uploadData()
    df_plan = load.load_SPlan()
    df_plan = pr.sp_trim(df_plan)
    tr.by_cfn(df,df_plan)

def option_reg():
    df = load.uploadData()
    df_plan = load.load_SPlan()
    df_plan = pr.sp_trim(df_plan)
    tr.by_registration(df,df_plan)

def option_SubOU():
    df = load.uploadData()
    df_plan = load.load_SPlan()
    df_plan = pr.sp_trim(df_plan)
    tr.by_SubOU(df,df_plan)

def option_Planning():
    df_plan = load.load_SPlan()
    tr.Plannig_review(df_plan)

def option_submitted():
    df_plan = load.load_SPlan()
    df_plan = pr.sp_trim(df_plan)
    tr.Submitted_Control(df_plan)

def option_voucher():
    df_plan = load.load_SPlan()
    df_plan = pr.sp_trim(df_plan)
    vou = load.load_vouchers()
    vou =  pr.sp_trim(vou)
    tr.vouchers(vou,df_plan)

def option_Timelapse():
    df = load.uploadData()
    sp = load.load_SPlan()
    tr.TimeLapse(df,sp)

def option_expired():
    df = load.uploadData()
    sp = load.load_SPlan()
    tr.expirated(df,sp)

def cancel_criticalOP():
    df = load.uploadData()
    criticals =load.load_criticals()
    criticals = pr.expandRows(criticals)
    tr.cancel_criticals(criticals,df)

def CFN_WithdrawalOP():
    df = load.uploadData()
    criticals =load.load_criticals()
    criticals = pr.expandRows(criticals)
    tr.approved_criticals(criticals,df)




