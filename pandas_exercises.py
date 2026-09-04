import pandas as pd
from distributed import Nanny

# 欢迎来到 Pandas 练习！
# 在这个文件中，我们为你准备了三个挑战，难度从易到难。
# 每个挑战都需要你使用 pandas 库来处理提供的数据。
#
# 我们已经为你创建了两个 CSV 文件：
# 1. sales.csv: 包含销售记录
# 2. employees.csv: 包含员工信息
#
# 请在每个挑战下面的指定区域编写你的代码。

# --- 挑战 1: 数据加载和基本统计 ---
#
# 任务:
# 1. 加载 `sales.csv` 文件到一个名为 `sales_df` 的 DataFrame 中。
# 2. 计算并打印出 `Price` 列的总销售额。
# 3. 找出并打印出 `Quantity` 列的平均值。
# 4. 打印出 `sales_df` 的基本信息，包括每列的数据类型和非空值数量。

print("--- 挑战 1 ---")
# 1. 加载 sales.csv
sales_df = pd.read_csv('sales.csv')

# 2. 计算 Price 列的总销售额
total_sales = sales_df['Price'].sum()
print(f"总销售额: {total_sales}")

# 3. 计算 Quantity 列的平均值
avg_quantity = sales_df['Quantity'].mean()
print(f"平均销售量: {avg_quantity}")

# 4. 打印 sales_df 的基本信息
print("\n数据框信息:")
print(sales_df.info())
sales_df = pd.read_csv("sales.csv")
# print(sales_df)
# print(sales_df['Price'].sum())
print(sales_df['Quantity'].mean())
print(sales_df.info())


print("\\n" + "="*30 + "\\n")


# --- 挑战 2: 数据清洗和分组 ---
#
# 任务:
# 1. 在 `sales_df` 中，填充 `City` 列的缺失值。由于大部分销售在北京和上海，
#    我们假设缺失的城市是 'Unknown'。
# 2. 按 `Category` 分组，并计算每个类别的总销售额（Price * Quantity）。
#    提示: 你可能需要先创建一个新的 'TotalSale' 列。
# 3. 打印出每个类别的总销售额。

print("--- 挑战 2 ---")
# 1. 填充 City 列的缺失值为 'Unknown'
sales_df['City'].fillna('Unknown', inplace=True)
print("City 列缺失值已填充为 'Unknown'")

# 2. 创建 TotalSale 列并按 Category 分组
sales_df['TotalSale'] = sales_df['Price'] * sales_df['Quantity']

# 3. 按 Category 分组，计算每个类别的总销售额
category_sales = sales_df.groupby('Category')['TotalSale'].sum()
print("\n每个类别的总销售额:")
print(category_sales)
print(sales_df['City'])
new=sales_df.fillna(value={'City':'Unknown'})
print(new)


print("\\n" + "="*30 + "\\n")


# --- 挑战 3: 数据合并和复杂查询 ---
#
# 任务:
# 1. 加载 `employees.csv` 文件到一个名为 `employees_df` 的 DataFrame 中。
# 2. 将 `sales_df` 和 `employees_df` 进行合并，找出每个销售订单是由哪个部门的员工完成的。
#    假设销售城市和员工所在城市是关联的键。
# 3. 计算并打印出每个部门（'Department'）的总销售额（'TotalSale'）。
# 4. 找出在哪个城市（'City'）产生的销售订单数量最多，并打印出来。

print("--- 挑战 3 ---")
# 1. 加载 employees.csv
employees_df = pd.read_csv('employees.csv')

# 2. 合并 sales_df 和 employees_df，以 City 作为关联键
merged_df = pd.merge(sales_df, employees_df, left_on='City', right_on='City', how='left')

# 3. 计算每个部门的总销售额
department_sales = merged_df.groupby('Department')['TotalSale'].sum()
print("每个部门的总销售额:")
print(department_sales)

# 4. 找出哪个城市的销售订单数量最多
city_order_count = sales_df['City'].value_counts()
top_city = city_order_count.idxmax()
top_count = city_order_count.max()
print(f"\n销售订单最多的城市: {top_city}，订单数量: {top_count}")


print("\\n" + "="*30 + "\\n")
