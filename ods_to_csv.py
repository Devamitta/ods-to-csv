def convert_dps_ods_to_csv():
    import pandas as pd
    from pandas_ods_reader import read_ods 
    import re

    df_convert_dps = read_ods("/home/deva/Documents/pali/vicara.ods")
    df_convert_dps.fillna("", inplace=True)
    df_convert_dps = df_convert_dps.astype(str)
    df_convert_dps.rename(columns=df_convert_dps.iloc[0], inplace = True)
    df_convert_dps.drop([0], inplace = True)

    df_convert_dps.to_csv("/home/deva/Documents/pali/dps.csv", sep="\t", index=None)


def convert_dpd_ods_to_csv():
    import pandas as pd
    from pandas_ods_reader import read_ods 
    import re

    df_convert_dpd = read_ods("/home/deva/Documents/pali/dpd.ods")
    df_convert_dpd.fillna("", inplace=True)
    df_convert_dpd = df_convert_dpd.astype(str)
    df_convert_dpd.rename(columns=df_convert_dpd.iloc[0], inplace = True)
    df_convert_dpd.drop([0], inplace = True)

    df_convert_dpd.to_csv("/home/deva/Documents/pali/dpd.csv", sep="\t", index=None)