import pandas as pd

# ============================================================
# Pandas 巩固练习 - 强化基础知识
# ============================================================
# 这个文件包含了基础知识的巩固练习
# 主要涉及：基本过滤、排序、描述性统计、条件查询等

print("=" * 60)
print("PANDAS 巩固练习 - 基础知识强化")
print("=" * 60)

# --- 巩固练习 1: 基础数据加载和过滤 ---
#
# 任务:
# 1. 加载 `products.csv` 文件到一个名为 `products_df` 的 DataFrame 中。
# 2. 过滤出所有价格（Price）大于 100 的产品。
# 3. 找出 Stock（库存）最多的产品。
# 4. 计算所有产品的平均价格和中位数价格。

print("\n--- 巩固练习 1: 基础数据加载和过滤 ---")
# 请在下面编写你的代码

products_df = pd.read_csv('products.csv')

# 过滤价格 > 100 的产品
expensive_products = products_df[products_df['Price'] > 100]
print(f"\n价格大于100的产品数量: {len(expensive_products)}")
print(expensive_products[['ProductName', 'Price']])

# 找库存最多的产品
max_stock_product = products_df.loc[products_df['Stock'].idxmax()]
print(f"\n库存最多的产品: {max_stock_product['ProductName']}, 库存数: {max_stock_product['Stock']}")

# 计算平均价格和中位数
avg_price = products_df['Price'].mean()
median_price = products_df['Price'].median()
print(f"平均价格: ¥{avg_price:.2f}")
print(f"中位数价格: ¥{median_price:.2f}")


print("\n" + "=" * 60 + "\n")


# --- 巩固练习 2: 排序和条件查询 ---
#
# 任务:
# 1. 按 `Price` 从高到低排序产品，打印出前3个最贵的产品。
# 2. 按 `Category` 分组，找出每个分类中库存最少的产品。
# 3. 找出所有库存小于15的产品，并按 Category 进行分类统计。

print("--- 巩固练习 2: 排序和条件查询 ---")
# 请在下面编写你的代码

# 按价格排序，找出最贵的3个产品
top_3_expensive = products_df.nlargest(3, 'Price')
print("\n最贵的3个产品:")
print(top_3_expensive[['ProductName', 'Category', 'Price']])

# 按 Category 分组，找每个分类中库存最少的产品
print("\n每个分类库存最少的产品:")
for category in products_df['Category'].unique():
    category_df = products_df[products_df['Category'] == category]
    min_stock_product = category_df.loc[category_df['Stock'].idxmin()]
    print(f"{category}: {min_stock_product['ProductName']} (库存: {min_stock_product['Stock']})")

# 库存 < 15 的产品按 Category 统计
low_stock_products = products_df[products_df['Stock'] < 15]
low_stock_by_category = low_stock_products.groupby('Category').size()
print(f"\n库存少于15的产品按分类统计:")
print(low_stock_by_category)


print("\n" + "=" * 60 + "\n")


# --- 巩固练习 3: 数据转换和聚合 ---
#
# 任务:
# 1. 加载 `transactions.csv` 文件。
# 2. 创建一个新列 `TransactionYear` 提取订单日期的年份。
# 3. 计算每个支付方式（PaymentMethod）的交易数和平均金额。
# 4. 统计不同状态（Status）的交易数量。

print("--- 巩固练习 3: 数据转换和聚合 ---")
# 请在下面编写你的代码

transactions_df = pd.read_csv('transactions.csv')

# 提取年份
transactions_df['OrderDate'] = pd.to_datetime(transactions_df['OrderDate'])
transactions_df['TransactionYear'] = transactions_df['OrderDate'].dt.year

# 按支付方式统计
payment_stats = transactions_df.groupby('PaymentMethod').agg({
    'TransactionID': 'count',
    'Amount': 'mean'
}).rename(columns={'TransactionID': 'Count', 'Amount': 'AvgAmount'})
print("\n按支付方式统计交易:")
print(payment_stats)

# 按状态统计
status_counts = transactions_df['Status'].value_counts()
print("\n按状态统计交易数量:")
print(status_counts)


print("\n" + "=" * 60 + "\n")

