# -*- coding: utf-8 -*-
import openpyxl
import xlsxwriter
import os
import pandas as pd


pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

data_path_input = input('입력할 엑셀 파일 경로 + 파일명을 입력하세요: ')
print('\n')
data_path_output = input('저장할 엑셀 파일 경로 + 파일명을 입력하세요: ')
print('\n')
print('회선 분류 진행중....')
print('\n')

    #r"C:/Users/SKNS/PycharmProjects/pythonProject2/sample.xlsx"

df = pd.read_excel(data_path_input,engine='openpyxl',header=1,index_col=0)

df_data = df[['회선명','CUID','회선비고3','RT선번내용']] #원하는 Columns만 추출

CUID_yes = df_data[df_data['CUID'].notnull()] #CUID가 존재하는 index 추출 후 저장
CUID_no = df_data[df_data['CUID'].isnull()] #CUID가 존재하지 않는 index 추출 후 저장

notduplicateDFRow=CUID_yes.drop_duplicates(['CUID'], keep=False) #CUID 값 1개만 존재하는 index → <불량,조치필요#2>

two_over_duplicateDFRow = CUID_yes.drop(notduplicateDFRow.index) # 동일 CUID 2개 이상 존재 index

one_circuit_compare = two_over_duplicateDFRow.drop_duplicates(['회선비고3'], keep=False) # CUID 중복 2개이상 & 회선비고 값 1개 존재하는 index → <불량,조치필요3>

two_circuit_compare = two_over_duplicateDFRow.drop(one_circuit_compare.index) # CUID 중복 2개이상 & 회선비고 값 2개이상 → <양호>

total_data=pd.DataFrame({'기지국전체' : len(df_data),
                         'RT 이원화 불량' : len(CUID_no.index)+len(notduplicateDFRow.index)+len(one_circuit_compare.index),
                         '조치필요#1' : CUID_no['회선명'],
                         '수량#1' : len(CUID_no.index),
                         '조치필요#2' : notduplicateDFRow['회선명'],
                         '수량#2' : len(notduplicateDFRow.index),
                         '조치필요#3' : one_circuit_compare['회선명'],
                         '수량#3' : len(one_circuit_compare.index)})

two_circuit_compare['장비명'] = two_circuit_compare['RT선번내용'].str.split('/').str[0] # <이원화 양호> 회선들의 RT 선번내용을 '/' 기준으로 text 분리 작업
two_circuit_compare['포트'] = two_circuit_compare['RT선번내용'].str.split('/').str[1] # <이원화 양호> 회선들의 RT 선번내용을 '/' 기준으로 text 분리 작업

column_null = two_circuit_compare[two_circuit_compare['RT선번내용'].isnull()] #<이원화 양호> 중 'RT선번내용'이 Null인 index

df_merge = pd.merge(two_circuit_compare, column_null, on='CUID', how='inner') #<이원화 양호>와 column_null의 inner join(CUID기준)

df_merge.rename(columns={'회선명_x':'회선명'},inplace=True)
df_merge.rename(columns={'회선비고3_x':'회선비고3'},inplace=True)
df_merge.rename(columns={'RT선번내용_x':'RT선번내용'},inplace=True)
df_merge.rename(columns={'장비명_x':'장비명'},inplace=True)
df_merge.rename(columns={'포트_x':'포트'},inplace=True)

df_merge = df_merge[df_merge.columns.drop(list(df_merge.filter(regex='_y')))]

df_merge = df_merge.drop_duplicates()

test = pd.concat([two_circuit_compare,df_merge])

test2 = test.drop_duplicates(keep=False)


total_data.to_excel(data_path_output, index=False, encoding = 'utf-8-sig', sheet_name='test')

writer = pd.ExcelWriter(data_path_output, engine='xlsxwriter')
total_data.to_excel(writer, index=False, encoding = 'utf-8-sig', sheet_name='RT 이원화 추출')
CUID_no.to_excel(writer, index=False, encoding = 'utf-8-sig', sheet_name='조치필요#1')
notduplicateDFRow.to_excel(writer, index=False, encoding = 'utf-8-sig', sheet_name='조치필요#2')
one_circuit_compare.to_excel(writer, index=False, encoding = 'utf-8-sig', sheet_name='조치필요#3')
two_circuit_compare.to_excel(writer, index=False, encoding = 'utf-8-sig', sheet_name='이원화 양호')
df_merge.to_excel(writer, index=False, encoding = 'utf-8-sig', sheet_name='검증 필요')

test2.to_excel(writer, index=False, encoding = 'utf-8-sig', sheet_name='new')

writer.save()


os.system("pause")

