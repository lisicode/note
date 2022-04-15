import pandas as pd
import numpy as np

# 创建DataFrame对象
df = pd.DataFrame({
    'Name': ['John', 'Helen', 'Sona', 'Ella', 'Ella'],
    'course': ['C#', 'Python', 'Java', 'C', 'C'],
    'score': [82, 98, 91, 87, 99]
}, index=['a', 'b', 'c', 'd', 'e'])
print(df)

# 分组函数
# groupby
# 查看分组结果
print(df.groupby('Name').groups)

# 指定多列标签进行分组
print(df.groupby(['Name', 'score']).groups)

# 根据对应组的数据值，选择一个组
grouped = df.groupby('Name')
print(df.groupby('Name').get_group('Sona'))

# 根据Name来分组
for label, course in grouped:
    print(label, course)

# 去重函数
# drop_duplicates
new_df = df.drop_duplicates(subset=['Name'])
print(new_df)

# 基于标签索引选取数据
# loc
name_list = ['John', 'Helen']
for i in name_list:
    for x in new_df.index:
        if df.loc[x].Name == i:
            print(df.loc[x].Name, df.loc[x].score)

# 遍历
# iteration
# 行遍历
# iterrows
for i in name_list:
    for row_index, row in df.iterrows():
        if row.Name == i:
            print(row.Name, row.course, row.score)

# 列遍历
# iteritems
for row_index, row in df.iteritems():
    print(row)

# 每遍历一行生成一个元组
# itertuples
for row in df.itertuples():
    print(row)

# 填充缺失值
# fillna()
df = pd.DataFrame(np.random.randn(3, 3), index=['b', 'c', 'e'], columns=['one', 'two', 'three'])
df = df.reindex(['a', 'b', 'c'])
print(df)
print(df.fillna({'one': 1, 'two': 2, 'three': 3}))

# 按列条件删除行
# drop
df.drop(df[df.two == 2].index, inplace=True)
print(df)