# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt

# =============================================================================
# 步骤 0: 设置环境 (特别是为了正确显示中文)
# =============================================================================
# 在你的电脑上，为了显示中文，请取消下面这行的注释，并确保有'SimHei'字体
# plt.rcParams['font.sans-serif'] = ['SimHei']  # 'SimHei' 是黑体的意思
# plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示图表里的负号
print("--- 环境设置完成 ---")


# =============================================================================
# 步骤 1: 加载并准备数据
# =============================================================================
try:
    # 读取CSV文件到DataFrame中
    df = pd.read_csv('数据2.csv')

    # 将'日期'列从普通文本转换为真正的日期格式
    df['日期'] = pd.to_datetime(df['日期']) 

    # 按照日期排序，让图表更清晰
    df = df.sort_values('日期')
    
    print("--- 数据加载和预处理成功 ---")
    print("数据前5行预览:")
    print(df.head())

except FileNotFoundError:
    print("错误：找不到文件 '数据2.csv'。请确保它和你的python脚本在同一个文件夹里。")
    exit() # 如果文件找不到，则退出程序
except KeyError as e:
    print(f"错误：数据中缺少必需的列: {e}。请检查CSV文件中的列名是否为'日期', '销售额', '产品类别', '利润'。")
    exit()
except Exception as e:
    print(f"处理数据时发生未知错误: {e}")
    exit()


# =============================================================================
# 图形一：折线图 (Line Plot) - 查看销售额趋势
# =============================================================================
print("\n--- 正在生成：折线图 ---")
# 1. 设置画布大小
plt.figure(figsize=(12, 6)) 

# 2. 绘制折线图 (x轴是日期, y轴是销售额)
plt.plot(df['日期'], df['销售额'], marker='o', linestyle='-', label='每日销售额') 

# 3. 添加图表标题和坐标轴标签
plt.title('每日销售额变化趋势', fontsize=16)
plt.xlabel('日期', fontsize=12)
plt.ylabel('销售额', fontsize=12)

# 4. 优化X轴日期的显示
plt.gcf().autofmt_xdate() 

# 5. 添加网格线和图例
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()

# 6. 显示图表
plt.show()


# =============================================================================
# 图形二：柱状图 (Bar Chart) - 对比各产品类别总销售额
# =============================================================================
print("\n--- 正在生成：柱状图 ---")
# 1. 按“产品类别”分组，并计算每个类别的销售额总和
category_sales = df.groupby('产品类别')['销售额'].sum().sort_values(ascending=False)

# 2. 设置画布大小
plt.figure(figsize=(10, 6))

# 3. 绘制柱状图
category_sales.plot(kind='bar', color=['#3498db', '#e74c3c', '#2ecc71', '#f1c40f'])

# 4. 添加标题和标签
plt.title('各产品类别总销售额对比', fontsize=16)
plt.xlabel('产品类别', fontsize=12)
plt.ylabel('总销售额', fontsize=12)

# 5. 旋转X轴的标签，防止重叠
plt.xticks(rotation=0)

# 6. 显示图表
plt.show()


# =============================================================================
# 图形三：散点图 (Scatter Plot) - 探索销售额与利润的关系
# =============================================================================
print("\n--- 正在生成：散点图 ---")
# 1. 设置画布大小
plt.figure(figsize=(10, 6))

# 2. 绘制散点图 (c='利润'让点的颜色根据利润值变化, cmap='viridis'是颜色方案)
plt.scatter(df['销售额'], df['利润'], c=df['利润'], cmap='viridis', alpha=0.7)

# 3. 添加标题和标签
plt.title('销售额与利润关系散点图', fontsize=16)
plt.xlabel('销售额', fontsize=12)
plt.ylabel('利润', fontsize=12)

# 4. 添加一个颜色条来说明颜色代表的利润值
plt.colorbar(label='利润')

# 5. 添加网格线
plt.grid(True, linestyle='--', alpha=0.5)

# 6. 显示图表
plt.show()

print("\n--- 所有图表已生成完毕 ---")