import helper.LoadData as load
import helper.procesing as pr
import helper.trackerType as tr
import pandas as pd


def run():
    df = load.uploadData()
    df_plan = load.load_SPlan()
    tr.by_registration(df,df_plan)




if __name__ == "__main__":
    run()