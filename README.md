# Pandas 完整练习系列

## 📚 项目概览

这是一个完整的 Pandas 学习系列，包含三个层次的练习：
1. **原始练习** - 基础知识入门
2. **巩固练习** - 强化基础技能
3. **进阶练习** - 深度数据分析

---

## 📋 文件清单

### 数据文件
- **sales.csv** - 销售记录数据（10条记录）
- **employees.csv** - 员工信息数据（6条记录）
- **products.csv** - 产品信息数据（10条记录）
- **transactions.csv** - 交易记录数据（12条记录）

### 练习文件
- **pandas_exercises.py** - 原始练习（3个挑战）
- **pandas_consolidation.py** - 巩固练习（3个练习）
- **pandas_advanced.py** - 进阶练习（5个练习）

---

## 🎯 知识点覆盖

### 第一阶段 - 原始练习 (pandas_exercises.py)

#### 挑战 1: 数据加载和基本统计
- **知识点**: `read_csv()`, `sum()`, `mean()`, `info()`
- **任务**: 
  - 加载 CSV 文件
  - 计算列求和和平均值
  - 查看数据框信息
- **输出示例**:
  ```
  总销售额: 3167
  平均销售量: 1.8
  ```

#### 挑战 2: 数据清洗和分组
- **知识点**: `fillna()`, 创建新列, `groupby()`, `sum()`
- **任务**:
  - 填充缺失值
  - 创建计算列
  - 按类别分组统计
- **输出示例**:
  ```
  Category
  Apparel         410
  Electronics    3202
  ```

#### 挑战 3: 数据合并和复杂查询
- **知识点**: `merge()`, `groupby()`, `value_counts()`
- **任务**:
  - 合并多个数据框
  - 按部门统计
  - 找出最频繁的类别

---

### 第二阶段 - 巩固练习 (pandas_consolidation.py)

#### 巩固练习 1: 基础数据加载和过滤
- **知识点**: 布尔索引、`nlargest()`, `idxmax()`, `median()`
- **任务**:
  - 条件过滤数据
  - 找出最大值和最小值
  - 计算描述性统计量
- **难度**: ⭐⭐

#### 巩固练习 2: 排序和条件查询
- **知识点**: `nlargest()`, 循环分组, 条件过滤, `size()`
- **任务**:
  - 按值排序并取前N个
  - 按类别分别处理
  - 复杂条件过滤
- **难度**: ⭐⭐

#### 巩固练习 3: 数据转换和聚合
- **知识点**: 日期转换, `dt.year`, `agg()`, `value_counts()`
- **任务**:
  - 提取日期字段
  - 多列聚合统计
  - 计数和分类统计
- **难度**: ⭐⭐⭐

---

### 第三阶段 - 进阶练习 (pandas_advanced.py)

#### 进阶练习 1: 多表联接和复杂聚合
- **知识点**: 多列 `groupby()`, `agg()` 多函数, `idxmax()`
- **任务**:
  - 多表数据聚合
  - 每个供应商的综合统计
  - 找出关键指标最高的记录
- **难度**: ⭐⭐⭐⭐

#### 进阶练习 2: 透视表和数据透视
- **知识点**: `pivot_table()`, 多维度聚合, 行列合计
- **任务**:
  - 创建透视表
  - 多维度分析
  - 计算小计和合计
- **难度**: ⭐⭐⭐⭐

#### 进阶练习 3: 时间序列和趋势分析
- **知识点**: `dt` 属性, `rolling()`, `isocalendar()`, 移动平均
- **任务**:
  - 日期分解
  - 计算移动平均
  - 周期性分析
- **难度**: ⭐⭐⭐⭐

#### 进阶练习 4: 客户分析和RFM模型
- **知识点**: 分组聚合, `apply()` 自定义函数, `median()`, Lambda 表达式
- **任务**:
  - 计算 RFM 指标
  - 自定义客户分类
  - 客户分层分析
- **难度**: ⭐⭐⭐⭐⭐

#### 进阶练习 5: 数据清洗和异常检测
- **知识点**: `isnull()`, 统计学应用, 条件过滤, 数据质量检查
- **任务**:
  - 缺失值检测
  - 异常值识别（3-sigma 规则）
  - 数据质量评估
- **难度**: ⭐⭐⭐⭐

---

## 🔑 核心知识点速查表

| 知识点 | 描述 | 使用场景 |
|--------|------|---------|
| `read_csv()` | 读取CSV文件 | 数据导入 |
| `sum()` / `mean()` | 聚合函数 | 数值统计 |
| `fillna()` | 填充缺失值 | 数据清洗 |
| `groupby()` | 分组操作 | 分类汇总 |
| `merge()` | 数据合并 | 多表关联 |
| `pivot_table()` | 透视表 | 多维分析 |
| `apply()` | 自定义函数 | 行列变换 |
| `dt` 属性 | 日期处理 | 时间序列 |
| `rolling()` | 移动窗口 | 趋势分析 |
| `value_counts()` | 频率统计 | 分类计数 |
| `nlargest()` | 取最大N个 | 排序取值 |
| `agg()` | 多函数聚合 | 复杂统计 |

---

## 💡 学习路线建议

### 初学者路线
1. 完成 **pandas_exercises.py** (挑战 1-3)
2. 完成 **pandas_consolidation.py** (巩固 1-2)

### 中级学者路线
1. 完成所有原始练习
2. 完成所有巩固练习
3. 尝试 **pandas_advanced.py** (进阶 1-3)

### 高级开发者路线
1. 快速完成所有基础练习
2. 重点掌握 **pandas_advanced.py** 全部内容
3. 尝试自己设计类似的数据分析项目

---

## 📊 数据样本

### sales.csv 结构
```
OrderID | Product | Category | Price | Quantity | OrderDate | City
1       | Laptop  | Electron | 1200  | 1        | 2023-01-15| Beijing
...
```

### products.csv 结构
```
ProductID | ProductName | Category | Price | Stock | Supplier
1001      | Dell XPS 15 | Laptop   | 1299.99| 15   | TechCorp
...
```

### transactions.csv 结构
```
TransactionID | CustomerID | CustomerName | OrderDate | Amount | PaymentMethod | Status
T001          | C001       | Alice        | 2023-01-05| 1200   | Credit Card   | Completed
...
```

---

## 🚀 进阶建议

### 在这些练习之后，你可以学习：
1. **Pandas 性能优化** - 大数据处理
2. **Matplotlib / Seaborn** - 数据可视化
3. **NumPy** - 数值计算
4. **SQL 与 Pandas** - 数据库交互
5. **实际项目** - 结合真实数据分析案例

### 常用的 Pandas 命令速查
```python
# 数据导入导出
pd.read_csv('file.csv')
df.to_csv('output.csv', index=False)

# 数据探索
df.info()
df.describe()
df.head()

# 数据选择
df[['col1', 'col2']]
df[df['col1'] > 100]

# 数据转换
df['new_col'] = df['col1'] * df['col2']
df.apply(lambda x: x.upper())

# 数据聚合
df.groupby('col1')['col2'].sum()
df.pivot_table(values='col2', index='col1', columns='col3', aggfunc='sum')

# 数据清洗
df.fillna(0)
df.drop_duplicates()
df.sort_values('col1', ascending=False)
```

---

## 📝 练习提示

- 每个练习都有详细的任务描述和注释
- 建议先阅读任务，尝试独立完成
- 如果卡住了，可以参考代码注释或重新阅读相关 pandas 文档
- 鼓励尝试修改代码，测试不同的参数
- 尝试创建自己的数据集进行练习

---

## 🎓 完成后的收获

通过完成所有练习，你将能够：

✅ 熟练使用 Pandas 进行数据导入和导出  
✅ 掌握数据清洗和预处理技能  
✅ 能够进行多维度数据分析  
✅ 理解并应用 RFM 等常见分析模型  
✅ 编写可复用的数据处理代码  
✅ 解决实际工作中的数据问题  

---

**祝学习愉快！ 🎉**

