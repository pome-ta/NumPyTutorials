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
# aa: [[0. 0. 0.], [0. 0. 0.], [0. 0. 0.]]


# 形を指定して、要素が全て1 で埋められた`ndarray` を作成
bb = np.ones((2, 3))
# bb: [[1. 1. 1.], [1. 1. 1.]]


# 形と値を指定して、要素が指定した値で埋められた`ndarray` を作成
cc = np.full((3, 2), 9)
# cc: [[9 9], [9 9], [9 9]]


# 指定された大きさの単位行列を表す`ndarray` を作成
dd = np.eye(5)
# dd: [[1. 0. 0. 0. 0.], [0. 1. 0. 0. 0.], [0. 0. 1. 0. 0.], [0. 0. 0. 1. 0.], [0. 0. 0. 0. 1.]]

# 形を指定して、0 ~ 1 の間の乱数で要素を埋めた`ndarray` を作成
ee = np.random.random((4, 5))
# ee: [
#   [0.38027383 0.24220944 0.66292493 0.47030649 0.41320992],
#   [0.90959387 0.72909953 0.08840376 0.10229914 0.50166369],
#   [0.51936646 0.95125911 0.5293427  0.08698286 0.47692896],
#   [0.92416279 0.92754017 0.46170889 0.03702078 0.85775026]
# ]


# 3 から始まり10 になるまで 1つずつ増加する数列を作る(10 は含まない)
ff = np.arange(3, 10, 1)
# ff: [3 4 5 6 7 8 9]

# 多次元配列の選択
# 整数の要素選択
_e = np.arange(0, 4 * 5).reshape((4, 5))
# _e: [
#   [ 0  1  2  3  4],
#   [ 5  6  7  8  9],
#   [10 11 12 13 14],
#   [15 16 17 18 19]
# ]
val = _e[0, 1]
# val: 1

# スライスでの要素選択
center = _e[1:3, 1:4]
# center: [[ 6  7  8], [11 12 13]]

# 値を代入
_e[1:3, 1:4] = 0
# _e: [
#   [ 0  1  2  3  4],
#   [ 5  0  0  0  9],
#   [10  0  0  0 14],
#   [15 16 17 18 19]
# ]

# ブロードキャスト

_ = 1
