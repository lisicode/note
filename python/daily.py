import pandas as pd


# 单位转换
def loans_unit(e):
    num = '{:.0f}'.format(e)
    if len(str(num)) < 5:
        return '{:.0f}元'.format(int(num))
    elif len(str(num)) < 9:
        return '{:.0f}万'.format(int(num) / 10000)
    elif len(str(num)) >= 9:
        return '{:.2f}亿'.format(int(num) / 100000000)


# 线上贷款余额
loans_balance_file = 'C:/Users/ncbk/下载/贷款产品日统计表.xlsx'
loans_balance_df = pd.read_excel(loans_balance_file, sheet_name='贷款产品日统计表', header=2, usecols=[0, 2, 6, 7, 13, 21, 25])
loans_balance_df.columns = ['序号', '产品名称', '当日新增放款笔数', '当日新增放款金额', '累计贷款户数', '未结清用户数', '未结清借据正常本金余额']
loans_balance_df.drop(loans_balance_df[loans_balance_df.累计贷款户数 == 0].index, inplace=True)
loans_balance_df.reset_index(drop=True)
loans_balance_df.set_index('序号', inplace=True)
loans_balance_list = [
    [7, 9, 50, 54, 55, 64],
    [10, 12, 14, 17, 26],
    [8, 13, 15, 19, 20, 23, 24, 25, 27, 30, 31, 32, 33, 35, 36, 37, 38, 39, 42, 43, 44, 45, 46, 47, 51]
]
for x in loans_balance_list:
    query_df = loans_balance_df.loc[x, ['产品名称', '当日新增放款笔数', '当日新增放款金额', '累计贷款户数', '未结清用户数', '未结清借据正常本金余额']]
    for key, row in query_df.iterrows():
        if '东方融e链' in row.产品名称 and row.当日新增放款金额 > 0:
            print('{0}：{1}（{2}户）'.format(row.产品名称, loans_unit(row.未结清借据正常本金余额), row.未结清用户数))
        elif '东方融e链' not in row.产品名称:
            print('{0}：{1}（{2}户）'.format(row.产品名称, loans_unit(row.未结清借据正常本金余额), row.未结清用户数))
    print('当日新增放款：{0}（{1}笔）'.format(loans_unit(query_df.当日新增放款金额.sum()), query_df.当日新增放款笔数.sum()))
    print('总余额：', loans_unit(query_df.未结清借据正常本金余额.sum()))
    print('>>>')

# 线上贷款逾期情况
loans_overdue_file = 'C:/Users/ncbk/下载/借据明细日报表.xlsx'
loans_overdue_df = pd.read_excel(loans_overdue_file, sheet_name='借据明细日报表', header=2, usecols=[2, 3, 14, 37, 44])
loans_overdue_df.columns = ['借款人名称', '借款人证件号', '贷款产品名称', '本月应收金额', '五级分类状态']
loans_overdue_df.drop(loans_overdue_df[loans_overdue_df.五级分类状态 == '正常'].index, inplace=True)
loans_overdue_sum = loans_overdue_df.groupby('贷款产品名称')['本月应收金额'].sum().reset_index()
loans_overdue_num = loans_overdue_df.groupby('贷款产品名称')['借款人证件号'].nunique().reset_index()
loans_overdue_num.columns = ['贷款产品名称', '关注人数']
loans_overdue_merge = pd.merge(loans_overdue_sum, loans_overdue_num, on='贷款产品名称')
for x, row in loans_overdue_merge.iterrows():
    print('{0}：{1}（{2}人）'.format(row.贷款产品名称, loans_unit(row.本月应收金额), row.关注人数))
print('网贷逾期共：{0}人'.format(loans_overdue_merge.关注人数.sum()))
print('逾期金额共：{0}'.format(loans_unit(loans_overdue_merge.本月应收金额.sum())))
