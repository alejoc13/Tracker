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
    tr.Submitted_Control(df_plan)
