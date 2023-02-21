import numpy as np

# ベクトルの定義
a = np.array([1, 2, 3])
print(a.shape)
print(a.ndim)

# 行列の定義
b = np.array(
    [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
)

print('Shape:', b.shape)
print('Rank:', b.ndim)
print('Size:', b.size)

# `np.array` 以外にも`ndarray` の作成方法はある
# 形を指定して、要素が全て0 で埋められた`ndarray` を作成
aa = np.zeros((3, 3))

# 形を指定して、要素が全て1 で埋められた`ndarray` を作成
bb = np.ones((2, 3))

# 形と値を指定して、要素が指定した値で埋められた`ndarray` を作成
cc = np.full((3, 2), 9)

# 指定された大きさの単位行列を表す`ndarray` を作成
dd = np.eye(5)

# 形を指定して、0 ~ 1 の間の乱数で要素を埋めた`ndarray` を作成
ee = np.random.random((4, 5))

# 3 から始まり10 になるまで 1つずつ増加する数列を作る(10 は含まない)
ff = np.arange(3, 10, 1)

_ = 1
