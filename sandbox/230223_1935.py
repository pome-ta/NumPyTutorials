import numpy as np
from PIL import Image as ImageP

sq_size: int = 256

width = sq_size
height = sq_size
# `gl_FragCoord.xy` ピクセル座標
# pos = np.array([])

# x_pos = np.arange(0, sq_size)

# y_pos = np.arange(0, sq_size).reshape((sq_size, 1))

# pos = np.array([x_pos, y_pos])

# x = np.full((sq_size, sq_size), np.array([x_pos, y_pos]))
_pos_x, _pos_y = np.meshgrid(np.arange(0, sq_size), np.arange(0, sq_size).reshape(sq_size, 1))
pos = np.empty((sq_size, sq_size, 2), dtype=np.uint32)
pos[:, :, 0] = _pos_x
pos[:, :, 1] = _pos_y

# print(pos[:, :, 1])

print(pos[0][255])

_ = 1
