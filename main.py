import helper.LoadData as load
import helper.procesing as pr
import helper.trackerType as tr
import pandas as pd


def run():
    # df = load.uploadData()
    df_plan = load.load_SPlan()
    print(df_plan.columns)
    tr.Submitted_Control(df_plan)




if __name__ == "__main__":
    run()