# Pandas 快速参考指南

## 📌 快速导航

- **原始练习**: pandas_exercises.py - 适合入门者
- **巩固练习**: pandas_consolidation.py - 强化基础
- **进阶练习**: pandas_advanced.py - 深度学习

---

## 🔧 常用函数速查

### 数据导入导出
```python
import pandas as pd

# 读取 CSV
df = pd.read_csv('file.csv')

# 写入 CSV
df.to_csv('output.csv', index=False)

# 读取其他格式
df = pd.read_excel('file.xlsx')
df = pd.read_json('file.json')
```

### 数据探索
```python
df.shape              # 查看形状 (行数, 列数)
df.info()             # 查看数据类型和缺失值
df.describe()         # 查看描述统计
df.head()             # 查看前5行
df.tail()             # 查看后5行
df.columns            # 查看列名
df.dtypes             # 查看数据类型
```

### 数据选择
```python
# 选择列
df['col_name']
df[['col1', 'col2']]

# 按位置选择
df.iloc[0]            # 选择第一行
df.iloc[:, 0]         # 选择第一列
df.iloc[0, 0]         # 选择第一行第一列

# 按标签选择
df.loc[0]             # 选择标签为0的行
df.loc[0, 'col_name'] # 选择特定单元格

# 条件过滤
df[df['col'] > 100]
df[df['col'].isin(['A', 'B'])]
df[(df['col1'] > 100) & (df['col2'] == 'yes')]
```

### 数据统计
```python
# 基本统计
df.sum()              # 求和
df.mean()             # 平均值
df.median()           # 中位数
df.std()              # 标准差
df.min()              # 最小值
df.max()              # 最大值
df.count()            # 计数

# 更多统计
df.quantile(0.25)     # 25分位数
df.value_counts()     # 频率统计
```

### 数据清洗
```python
# 处理缺失值
df.isnull()           # 检查缺失值
df.fillna(0)          # 填充缺失值
df.dropna()           # 删除缺失值

# 处理重复值
df.duplicated()       # 检查重复
df.drop_duplicates()  # 删除重复

# 数据类型转换
df['col'].astype(int)
df['col'] = pd.to_datetime(df['col'])
```

### 数据转换
```python
# 创建新列
df['new_col'] = df['col1'] + df['col2']

# 应用函数
df['col'].apply(lambda x: x * 2)
df.apply(lambda row: row['col1'] + row['col2'], axis=1)

# 字符串操作
df['col'].str.upper()
df['col'].str.contains('text')
df['col'].str.split(',')

# 日期操作
df['date'].dt.year
df['date'].dt.month
df['date'].dt.day
df['date'].dt.dayofweek
```

### 数据排序
```python
# 按值排序
df.sort_values('col')           # 升序
df.sort_values('col', ascending=False)  # 降序
df.sort_values(['col1', 'col2'])        # 多列排序

# 取最大/最小 N 个
df.nlargest(3, 'col')
df.nsmallest(3, 'col')
```

### 分组聚合
```python
# 基本分组
df.groupby('col1')['col2'].sum()

# 多列分组
df.groupby(['col1', 'col2'])['col3'].sum()

# 多函数聚合
df.groupby('col1').agg({
    'col2': 'sum',
    'col3': 'mean',
    'col4': 'count'
})

# 自定义聚合
df.groupby('col1').agg({
    'col2': lambda x: x.max() - x.min()
})
```

### 数据合并
```python
# 行合并
pd.concat([df1, df2])

# 列合并
pd.merge(df1, df2, on='key')           # 内连接
pd.merge(df1, df2, on='key', how='left')  # 左连接
pd.merge(df1, df2, on='key', how='outer') # 外连接

# 按索引合并
df1.join(df2)
```

### 透视表
```python
# 基本透视
pd.pivot_table(
    df,
    values='col3',
    index='col1',
    columns='col2',
    aggfunc='sum'
)

# 多值透视
pd.pivot_table(
    df,
    values=['col3', 'col4'],
    index='col1',
    columns='col2',
    aggfunc=['sum', 'mean']
)
```

### 时间序列
```python
# 转换为日期
df['date'] = pd.to_datetime(df['date'])

# 设置日期为索引
df.set_index('date', inplace=True)

# 按日期过滤
df['2023-01':'2023-12']
df[df['date'] > '2023-01-01']

# 日期提取
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['week'] = df['date'].dt.isocalendar().week

# 移动平均
df['col'].rolling(window=7).mean()

# 重采样
df.resample('M').sum()  # 按月汇总
```

---

## 📊 常见操作场景

### 场景 1: 数据清洗
```python
# 加载数据
df = pd.read_csv('data.csv')

# 查看数据质量
print(df.info())
print(df.isnull().sum())

# 清洗数据
df = df.dropna()  # 删除缺失值
df = df.drop_duplicates()  # 删除重复值
df['col'] = df['col'].str.strip()  # 去除空格

# 保存清洁数据
df.to_csv('clean_data.csv', index=False)
```

### 场景 2: 数据统计
```python
# 计算统计量
stats = {
    'count': df['col'].count(),
    'mean': df['col'].mean(),
    'median': df['col'].median(),
    'std': df['col'].std(),
    'min': df['col'].min(),
    'max': df['col'].max()
}

# 或使用 describe()
df['col'].describe()
```

### 场景 3: 分类分析
```python
# 按类别统计
grouped = df.groupby('category').agg({
    'amount': ['sum', 'mean', 'count'],
    'quantity': 'sum'
})

# 排序
grouped = grouped.sort_values(('amount', 'sum'), ascending=False)

print(grouped)
```

### 场景 4: 时间分析
```python
# 转换日期
df['date'] = pd.to_datetime(df['date'])

# 按时间段统计
daily = df.groupby(df['date'].dt.date)['amount'].sum()
weekly = df.groupby(df['date'].dt.isocalendar().week)['amount'].sum()
monthly = df.groupby(df['date'].dt.month)['amount'].sum()

print(daily)
print(weekly)
print(monthly)
```

### 场景 5: RFM 分析
```python
# 计算 RFM 指标
reference_date = df['date'].max()

rfm = df.groupby('customer').agg({
    'date': lambda x: (reference_date - x.max()).days,  # Recency
    'order_id': 'count',  # Frequency
    'amount': 'sum'  # Monetary
}).rename(columns={
    'date': 'Recency',
    'order_id': 'Frequency',
    'amount': 'Monetary'
})

print(rfm)
```

---

## 💡 高级技巧

### 1. 链式操作
```python
# 可以链式调用多个操作
result = (df
    .filter(['col1', 'col2', 'col3'])
    .dropna()
    .sort_values('col1', ascending=False)
    .head(10)
)
```

### 2. apply 配合 lambda
```python
# 简单转换
df['new_col'] = df['col'].apply(lambda x: x * 2)

# 条件转换
df['category'] = df['price'].apply(lambda x: 'expensive' if x > 1000 else 'cheap')

# 行操作
df['total'] = df.apply(lambda row: row['price'] * row['quantity'], axis=1)
```

### 3. 多条件过滤
```python
# 使用 & (and) 和 | (or)
result = df[
    (df['col1'] > 100) & 
    (df['col2'] == 'A') | 
    (df['col3'] < 50)
]

# 使用 isin 检查多个值
result = df[df['category'].isin(['A', 'B', 'C'])]
```

### 4. 自定义聚合函数
```python
# 定义函数
def custom_agg(x):
    return {
        'count': x.count(),
        'range': x.max() - x.min(),
        'mean': x.mean()
    }

# 应用
result = df.groupby('category')['value'].apply(custom_agg)
```

### 5. 条件创建新列
```python
# 使用 np.where
df['status'] = np.where(df['score'] >= 60, 'pass', 'fail')

# 使用 pd.cut 分箱
df['score_level'] = pd.cut(
    df['score'],
    bins=[0, 60, 80, 100],
    labels=['low', 'medium', 'high']
)
```

---

## ⚠️ 常见错误

| 错误 | 原因 | 解决方案 |
|------|------|---------|
| `KeyError: 'col'` | 列不存在 | 检查列名，使用 `df.columns` 查看 |
| `TypeError: unsupported operand type` | 数据类型不匹配 | 使用 `astype()` 转换类型 |
| `ValueError: cannot reindex` | 索引问题 | 重置索引 `df.reset_index()` |
| `SettingWithCopyWarning` | 视图操作 | 使用 `df.copy()` 或 `df.loc[]` |
| `NaN in groupby` | 缺失值问题 | 先使用 `fillna()` 或 `dropna()` |

---

## 🎯 练习建议

1. **重复操作**: 每个函数至少练习3次
2. **修改参数**: 尝试改变参数看效果
3. **组合操作**: 尝试组合多个操作
4. **自己创建数据**: 创建小的测试数据集
5. **查看文档**: 使用 `help(pd.function)` 查看详情

---

**加油，继续学习！ 💪**

