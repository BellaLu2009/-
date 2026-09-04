import pandas as pd
import numpy as np

# ============================================================
# Pandas 进阶练习 - 深度数据分析
# ============================================================
# 这个文件包含了进阶的数据分析练习
# 主要涉及：多表联接、透视表、数据透视、复杂聚合、时间序列等

print("=" * 60)
print("PANDAS 进阶练习 - 深度数据分析")
print("=" * 60)

# --- 进阶练习 1: 多表联接和复杂聚合 ---
#
# 任务:
# 1. 加载 `products.csv`, `sales.csv`, 和 `transactions.csv` 三个文件。
# 2. 通过 Product（或相关字段）将 products 和 sales 数据合并。
#    提示: 需要创建一个关联字段。
# 3. 计算每个供应商（Supplier）的销售总额和平均订单金额。
# 4. 找出销售贡献最大的供应商。

print("\n--- 进阶练习 1: 多表联接和复杂聚合 ---")
# 请在下面编写你的代码

products_df = pd.read_csv('products.csv')
sales_df = pd.read_csv('sales.csv')
transactions_df = pd.read_csv('transactions.csv')

# 计算每个供应商的销售统计（基于产品库存和价格）
supplier_stats = products_df.groupby('Supplier').agg({
    'Price': ['sum', 'mean', 'count'],
    'Stock': 'sum'
}).round(2)
supplier_stats.columns = ['TotalPrice', 'AvgPrice', 'ProductCount', 'TotalStock']
print("\n供应商产品统计:")
print(supplier_stats)

# 找出库存最多的供应商
max_stock_supplier = products_df.groupby('Supplier')['Stock'].sum().idxmax()
max_stock_value = products_df.groupby('Supplier')['Stock'].sum().max()
print(f"\n库存最多的供应商: {max_stock_supplier}, 总库存: {max_stock_value}")


print("\n" + "=" * 60 + "\n")


# --- 进阶练习 2: 透视表和数据透视 ---
#
# 任务:
# 1. 使用 `sales.csv` 创建一个透视表，行为 Category，列为 City。
# 2. 在透视表中显示每个城市每个类别的总销售额（Price * Quantity）。
# 3. 计算每个城市的总销售额和每个类别的总销售额。
# 4. 找出销售额最高的城市-类别组合。

print("--- 进阶练习 2: 透视表和数据透视 ---")
# 请在下面编写你的代码

# 计算总销售额
sales_df['TotalSale'] = sales_df['Price'] * sales_df['Quantity']

# 创建透视表
pivot_table = pd.pivot_table(
    sales_df,
    values='TotalSale',
    index='Category',
    columns='City',
    aggfunc='sum',
    fill_value=0
)
print("\n城市-类别销售额透视表:")
print(pivot_table)

# 计算行合计和列合计
pivot_table['Total'] = pivot_table.sum(axis=1)
totals_row = pivot_table.sum()
totals_row['Total'] = sales_df['TotalSale'].sum()
pivot_table.loc['TOTAL'] = totals_row
print("\n包含合计的透视表:")
print(pivot_table)

# 找出最高销售额的城市-类别组合
sales_df_sorted = sales_df.groupby(['City', 'Category'])['TotalSale'].sum().sort_values(ascending=False)
print(f"\n销售额TOP 5的城市-类别组合:")
print(sales_df_sorted.head())


print("\n" + "=" * 60 + "\n")


# --- 进阶练习 3: 时间序列和趋势分析 ---
#
# 任务:
# 1. 加载 `transactions.csv`，将 OrderDate 转换为日期格式。
# 2. 按日期统计每天的交易数量和交易总金额。
# 3. 计算7天移动平均（Rolling Average）的交易金额。
# 4. 分析每周的交易趋势，找出交易最活跃的一周。

print("--- 进阶练习 3: 时间序列和趋势分析 ---")
# 请在下面编写你的代码

# 转换日期格式
transactions_df['OrderDate'] = pd.to_datetime(transactions_df['OrderDate'])

# 按日期统计
daily_stats = transactions_df.groupby(transactions_df['OrderDate'].dt.date).agg({
    'TransactionID': 'count',
    'Amount': ['sum', 'mean']
}).round(2)
daily_stats.columns = ['TransactionCount', 'TotalAmount', 'AvgAmount']
print("\n每日交易统计:")
print(daily_stats)

# 计算移动平均（需要日期排序的数据）
sorted_trans = transactions_df.sort_values('OrderDate').reset_index(drop=True)
sorted_trans['7DayAvg'] = sorted_trans['Amount'].rolling(window=7, min_periods=1).mean().round(2)
print("\n带有7天移动平均的交易:")
print(sorted_trans[['OrderDate', 'Amount', '7DayAvg']].tail(10))

# 按周统计
transactions_df['WeekNumber'] = transactions_df['OrderDate'].dt.isocalendar().week
weekly_stats = transactions_df.groupby('WeekNumber').agg({
    'TransactionID': 'count',
    'Amount': 'sum'
}).rename(columns={'TransactionID': 'Count', 'Amount': 'Total'})
most_active_week = weekly_stats['Count'].idxmax()
print(f"\n按周统计，最活跃的一周: 第{most_active_week}周，交易数: {weekly_stats.loc[most_active_week, 'Count']}")


print("\n" + "=" * 60 + "\n")


# --- 进阶练习 4: 客户分析和RFM模型 ---
#
# 任务:
# 1. 使用 `transactions.csv` 计算每个客户的：
#    - R (Recency): 最后一次交易距离今天的天数
#    - F (Frequency): 交易次数
#    - M (Monetary): 总交易金额
# 2. 根据 RFM 值将客户分为：
#    - 高价值客户 (R < 中位数, F > 中位数, M > 中位数)
#    - 流失客户 (R > 中位数, F < 中位数, M < 中位数)
#    - 普通客户 (其他)
# 3. 统计各类客户的数量。

print("--- 进阶练习 4: 客户分析和RFM模型 ---")
# 请在下面编写你的代码

# 参考日期（使用最新交易日期）
reference_date = transactions_df['OrderDate'].max()

# 计算RFM值
rfm_df = transactions_df.groupby('CustomerName').agg({
    'OrderDate': lambda x: (reference_date - x.max()).days,  # Recency
    'TransactionID': 'count',  # Frequency
    'Amount': 'sum'  # Monetary
}).rename(columns={
    'OrderDate': 'Recency',
    'TransactionID': 'Frequency',
    'Amount': 'Monetary'
}).reset_index()

print("\nRFM 分析 - 客户价值指标:")
print(rfm_df)

# 计算中位数
r_median = rfm_df['Recency'].median()
f_median = rfm_df['Frequency'].median()
m_median = rfm_df['Monetary'].median()

# 客户分类
def classify_customer(row):
    if row['Recency'] < r_median and row['Frequency'] > f_median and row['Monetary'] > m_median:
        return '高价值客户'
    elif row['Recency'] > r_median and row['Frequency'] < f_median and row['Monetary'] < m_median:
        return '流失客户'
    else:
        return '普通客户'

rfm_df['CustomerSegment'] = rfm_df.apply(classify_customer, axis=1)
print("\n客户分类结果:")
print(rfm_df[['CustomerName', 'CustomerSegment']])

segment_counts = rfm_df['CustomerSegment'].value_counts()
print("\n客户分类统计:")
print(segment_counts)


print("\n" + "=" * 60 + "\n")


# --- 进阶练习 5: 数据清洗和异常检测 ---
#
# 任务:
# 1. 检查 `transactions.csv` 中是否有缺失值，并列出包含缺失值的列。
# 2. 识别异常交易（Amount > 3倍标准差或 Amount < 0）。
# 3. 统计 'Failed' 状态的交易，计算失败率。
# 4. 对数据进行清洗：删除异常值，并生成清洗后的报告。

print("--- 进阶练习 5: 数据清洗和异常检测 ---")
# 请在下面编写你的代码

# 检查缺失值
print("\n缺失值统计:")
missing_data = transactions_df.isnull().sum()
print(missing_data[missing_data > 0] if missing_data.sum() > 0 else "没有缺失值")

# 识别异常交易
mean_amount = transactions_df['Amount'].mean()
std_amount = transactions_df['Amount'].std()
upper_bound = mean_amount + 3 * std_amount
lower_bound = mean_amount - 3 * std_amount

anomalies = transactions_df[
    (transactions_df['Amount'] > upper_bound) | 
    (transactions_df['Amount'] < lower_bound) |
    (transactions_df['Amount'] < 0)
]
print(f"\n异常交易检测:")
print(f"正常交易范围: ¥{lower_bound:.2f} - ¥{upper_bound:.2f}")
print(f"发现异常交易: {len(anomalies)} 笔")
if len(anomalies) > 0:
    print(anomalies[['TransactionID', 'CustomerName', 'Amount', 'Status']])

# 计算失败率
total_transactions = len(transactions_df)
failed_transactions = len(transactions_df[transactions_df['Status'] == 'Failed'])
failure_rate = (failed_transactions / total_transactions) * 100
print(f"\n交易失败统计:")
print(f"总交易数: {total_transactions}")
print(f"失败交易数: {failed_transactions}")
print(f"失败率: {failure_rate:.2f}%")

# 数据清洗（移除失败和异常交易）
clean_transactions = transactions_df[
    (transactions_df['Status'] != 'Failed') & 
    (transactions_df['Amount'] <= upper_bound)
]
print(f"\n数据清洗结果:")
print(f"清洗前记录数: {len(transactions_df)}")
print(f"清洗后记录数: {len(clean_transactions)}")
print(f"移除比例: {((len(transactions_df) - len(clean_transactions)) / len(transactions_df) * 100):.2f}%")


print("\n" + "=" * 60 + "\n")

