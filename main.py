import helper.LoadData as load
import helper.procesing as pr
import helper.trackerType as tr
import pandas as pd


def run():
    # df = load.uploadData()
    df_plan = load.load_SPlan()
    df_plan = pr.sp_trim(df_plan)
    tr.Plannig_review(df_plan)




if __name__ == "__main__":
    run()