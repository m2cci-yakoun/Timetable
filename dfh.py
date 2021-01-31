import pandas as pd

exl_file='det.xlsx'
df=pd.read_excel(exl_file)


def show_day_work(day):
    l=[]

    for row in df[day]:
        if row != "NaN" :
            l.append(row)
    return l
print(show_day_work('01/05/2020'))
