import pandas as pd
import numpy as np

# 创建一个简单的 DataFrame
data = {
    'C': [3, 1, 4, 2, 5],
    'B': [9, 6, 3, 8, 5],
    'A': [7, 4, 1, 0, 2]
}

df = pd.DataFrame(data,index=[4,2,1,3,0])

# 按照行索引进行升序排序
sorted_df = df.sort_index(axis=1)

# 打印排序后的 DataFrame
print(df)
print(sorted_df)


