import pandas as pd
import numpy as np
import os
from tqdm import tqdm

os.chdir('C:\\Users\\user\\Documents\\2020년 2학기\\Raw\\rest Export')
home = os.getcwd()

raw_list = os.listdir()

result_df = pd.DataFrame(columns=['피험자','set','FAA','FAA2'])


for i in tqdm(range(len(raw_list))):
    raw=raw_list[i]
    set_nm = raw.split('_')[1]
    p_nm = raw.split('_')[0]
    p_nm = 'P'+p_nm[-2:]

    data = pd.read_csv(raw)
    col_nm = data.columns

    t_len = len(data)/256
    df = pd.DataFrame(columns = col_nm)
    for t in range(int(t_len)):
        df = df.append(data.iloc[(256*t+16):(256*t+24)].mean(), ignore_index=True)

    df['FAA']=df['F4']/df['F3']
    df['FAA2']=df['Right']/df['Left']

    log_data = np.log(df[['FAA','FAA2']])

    FAA = np.average(log_data['FAA'])
    FAA2 = np.average(log_data['FAA2'])

    result_df = result_df.append({'피험자':p_nm,'set':set_nm,'FAA':FAA,'FAA2':FAA2},ignore_index=True)

print(len(raw_list),'개 파일 전처리 완료')


os.chdir('C:\\Users\\user\\Documents\\2020년 2학기\\Raw')
f_nm = 'rest_FFT.csv'
result_df.to_csv(f_nm, index = False)
print(f_nm,'파일 생성 완료')