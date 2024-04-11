import pandas as pd
import openpyxl

def get_excel_sheet_as_dataframe(file_path, index,skiprows):
    wb = openpyxl.load_workbook(file_path)
    sheet_name = wb.sheetnames[index]
    df = pd.read_excel(file_path, sheet_name=sheet_name,skiprows=skiprows)
    try:
        df=df.dropna(subset=df.columns[1]).set_index(df.columns[1])
    except:
        pass
    return df

sheet_index=0
skiprows=4
skipr=4
s1_21=get_excel_sheet_as_dataframe('PNT_12T2021.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s1_20=get_excel_sheet_as_dataframe('PNT_12T2020.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s1_19=get_excel_sheet_as_dataframe('PNT_12T2019.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s1_18=get_excel_sheet_as_dataframe('PNT_12T2018.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s1_17=get_excel_sheet_as_dataframe('PNT_12T2017.xlsx', sheet_index,skiprows).iloc[skipr:,1:]

sheet_index=1
skiprows=3
skipr=1
s2_21=get_excel_sheet_as_dataframe('PNT_12T2021.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s2_20=get_excel_sheet_as_dataframe('PNT_12T2020.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s2_19=get_excel_sheet_as_dataframe('PNT_12T2019.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s2_18=get_excel_sheet_as_dataframe('PNT_12T2018.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s2_17=get_excel_sheet_as_dataframe('PNT_12T2017.xlsx', sheet_index,skiprows).iloc[skipr:,1:]

sheet_index=2
skiprows=4
skipr=1
s3_21=get_excel_sheet_as_dataframe('PNT_12T2021.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s3_20=get_excel_sheet_as_dataframe('PNT_12T2020.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s3_19=get_excel_sheet_as_dataframe('PNT_12T2019.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s3_18=get_excel_sheet_as_dataframe('PNT_12T2018.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s3_17=get_excel_sheet_as_dataframe('PNT_12T2017.xlsx', sheet_index,skiprows).iloc[skipr:,1:]

sheet_index=3
skiprows=4
skipr=1
s4_21=get_excel_sheet_as_dataframe('PNT_12T2021.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s4_20=get_excel_sheet_as_dataframe('PNT_12T2020.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s4_19=get_excel_sheet_as_dataframe('PNT_12T2019.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s4_18=get_excel_sheet_as_dataframe('PNT_12T2018.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s4_17=get_excel_sheet_as_dataframe('PNT_12T2017.xlsx', sheet_index,skiprows).iloc[skipr:,1:]

sheet_index=4
skiprows=4
skipr=4
s5_21=get_excel_sheet_as_dataframe('PNT_12T2021.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s5_20=get_excel_sheet_as_dataframe('PNT_12T2020.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s5_19=get_excel_sheet_as_dataframe('PNT_12T2019.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s5_18=get_excel_sheet_as_dataframe('PNT_12T2018.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s5_17=get_excel_sheet_as_dataframe('PNT_12T2017.xlsx', sheet_index,skiprows).iloc[skipr:,1:]

sheet_index=5
skiprows=4
skipr=1
s6_21=get_excel_sheet_as_dataframe('PNT_12T2021.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s6_20=get_excel_sheet_as_dataframe('PNT_12T2020.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s6_19=get_excel_sheet_as_dataframe('PNT_12T2019.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s6_18=get_excel_sheet_as_dataframe('PNT_12T2018.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s6_17=get_excel_sheet_as_dataframe('PNT_12T2017.xlsx', sheet_index,skiprows).iloc[skipr:,1:]

sheet_index=6
skiprows=4
skipr=1
s7_21=get_excel_sheet_as_dataframe('PNT_12T2021.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s7_20=get_excel_sheet_as_dataframe('PNT_12T2020.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s7_19=get_excel_sheet_as_dataframe('PNT_12T2019.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s7_18=get_excel_sheet_as_dataframe('PNT_12T2018.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s7_17=get_excel_sheet_as_dataframe('PNT_12T2017.xlsx', sheet_index,skiprows).iloc[skipr:,1:]

sheet_index=7
skiprows=4
skipr=2
s8_21=get_excel_sheet_as_dataframe('PNT_12T2021.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s8_20=get_excel_sheet_as_dataframe('PNT_12T2020.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s8_19=get_excel_sheet_as_dataframe('PNT_12T2019.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s8_18=get_excel_sheet_as_dataframe('PNT_12T2018.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s8_17=get_excel_sheet_as_dataframe('PNT_12T2017.xlsx', sheet_index,skiprows).iloc[skipr:,1:]

sheet_index=8
skiprows=4
skipr=2
s9_21=get_excel_sheet_as_dataframe('PNT_12T2021.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s9_20=get_excel_sheet_as_dataframe('PNT_12T2020.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s9_19=get_excel_sheet_as_dataframe('PNT_12T2019.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s9_18=get_excel_sheet_as_dataframe('PNT_12T2018.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s9_17=get_excel_sheet_as_dataframe('PNT_12T2017.xlsx', sheet_index,skiprows).iloc[skipr:,1:]

sheet_index=9
skiprows=4
skipr=2
s10_21=get_excel_sheet_as_dataframe('PNT_12T2021.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s10_20=get_excel_sheet_as_dataframe('PNT_12T2020.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s10_19=get_excel_sheet_as_dataframe('PNT_12T2019.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s10_18=get_excel_sheet_as_dataframe('PNT_12T2018.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s10_17=get_excel_sheet_as_dataframe('PNT_12T2017.xlsx', sheet_index,skiprows).iloc[skipr:,1:]

sheet_index=10
skiprows=4
skipr=2
s11_21=get_excel_sheet_as_dataframe('PNT_12T2021.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s11_20=get_excel_sheet_as_dataframe('PNT_12T2020.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s11_19=get_excel_sheet_as_dataframe('PNT_12T2019.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s11_18=get_excel_sheet_as_dataframe('PNT_12T2018.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s11_17=get_excel_sheet_as_dataframe('PNT_12T2017.xlsx', sheet_index,skiprows).iloc[skipr:,1:]

sheet_index=11
skiprows=4
skipr=2
s12_21=get_excel_sheet_as_dataframe('PNT_12T2021.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s12_20=get_excel_sheet_as_dataframe('PNT_12T2020.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s12_19=get_excel_sheet_as_dataframe('PNT_12T2019.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s12_18=get_excel_sheet_as_dataframe('PNT_12T2018.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s12_17=get_excel_sheet_as_dataframe('PNT_12T2017.xlsx', sheet_index,skiprows).iloc[skipr:,1:]

sheet_index=12
skiprows=4
skipr=2
s13_21=get_excel_sheet_as_dataframe('PNT_12T2021.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s13_20=get_excel_sheet_as_dataframe('PNT_12T2020.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s13_19=get_excel_sheet_as_dataframe('PNT_12T2019.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s13_18=get_excel_sheet_as_dataframe('PNT_12T2018.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s13_17=get_excel_sheet_as_dataframe('PNT_12T2017.xlsx', sheet_index,skiprows).iloc[skipr:,1:]

sheet_index=13
skiprows=4
skipr=2
s14_21=get_excel_sheet_as_dataframe('PNT_12T2021.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s14_20=get_excel_sheet_as_dataframe('PNT_12T2020.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s14_19=get_excel_sheet_as_dataframe('PNT_12T2019.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s14_18=get_excel_sheet_as_dataframe('PNT_12T2018.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s14_17=get_excel_sheet_as_dataframe('PNT_12T2017.xlsx', sheet_index,skiprows).iloc[skipr:,1:]

sheet_index=14
skiprows=4
skipr=2
s15_21=get_excel_sheet_as_dataframe('PNT_12T2021.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s15_20=get_excel_sheet_as_dataframe('PNT_12T2020.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s15_19=get_excel_sheet_as_dataframe('PNT_12T2019.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s15_18=get_excel_sheet_as_dataframe('PNT_12T2018.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s15_17=get_excel_sheet_as_dataframe('PNT_12T2017.xlsx', sheet_index,skiprows).iloc[skipr:,1:]

sheet_index=15
skiprows=4
skipr=2
s16_21=get_excel_sheet_as_dataframe('PNT_12T2021.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s16_20=get_excel_sheet_as_dataframe('PNT_12T2020.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s16_19=get_excel_sheet_as_dataframe('PNT_12T2019.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s16_18=get_excel_sheet_as_dataframe('PNT_12T2018.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s16_17=get_excel_sheet_as_dataframe('PNT_12T2017.xlsx', sheet_index,skiprows).iloc[skipr:,1:]

sheet_index=16
skiprows=4
skipr=2
s17_21=get_excel_sheet_as_dataframe('PNT_12T2021.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s17_20=get_excel_sheet_as_dataframe('PNT_12T2020.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s17_19=get_excel_sheet_as_dataframe('PNT_12T2019.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s17_18=get_excel_sheet_as_dataframe('PNT_12T2018.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s17_17=get_excel_sheet_as_dataframe('PNT_12T2017.xlsx', sheet_index,skiprows).iloc[skipr:,1:]

sheet_index=17
skiprows=4
skipr=2
s18_21=get_excel_sheet_as_dataframe('PNT_12T2021.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s18_20=get_excel_sheet_as_dataframe('PNT_12T2020.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s18_19=get_excel_sheet_as_dataframe('PNT_12T2019.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s18_18=get_excel_sheet_as_dataframe('PNT_12T2018.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s18_17=get_excel_sheet_as_dataframe('PNT_12T2017.xlsx', sheet_index,skiprows).iloc[skipr:,1:]

sheet_index=18
skiprows=4
skipr=2
s19_21=get_excel_sheet_as_dataframe('PNT_12T2021.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s19_20=get_excel_sheet_as_dataframe('PNT_12T2020.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s19_19=get_excel_sheet_as_dataframe('PNT_12T2019.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s19_18=get_excel_sheet_as_dataframe('PNT_12T2018.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s19_17=get_excel_sheet_as_dataframe('PNT_12T2017.xlsx', sheet_index,skiprows).iloc[skipr:,1:]

sheet_index=19
skiprows=4
skipr=2
s20_21=get_excel_sheet_as_dataframe('PNT_12T2021.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s20_20=get_excel_sheet_as_dataframe('PNT_12T2020.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s20_19=get_excel_sheet_as_dataframe('PNT_12T2019.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s20_18=get_excel_sheet_as_dataframe('PNT_12T2018.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s20_17=get_excel_sheet_as_dataframe('PNT_12T2017.xlsx', sheet_index,skiprows).iloc[skipr:,1:]

sheet_index=20
skiprows=3
skipr=2
s21_21=get_excel_sheet_as_dataframe('PNT_12T2021.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s21_20=get_excel_sheet_as_dataframe('PNT_12T2020.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s21_19=get_excel_sheet_as_dataframe('PNT_12T2019.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s21_18=get_excel_sheet_as_dataframe('PNT_12T2018.xlsx', sheet_index,skiprows).iloc[skipr:,1:]
s21_17=get_excel_sheet_as_dataframe('PNT_12T2017.xlsx', sheet_index,skiprows).iloc[skipr:,1:]










