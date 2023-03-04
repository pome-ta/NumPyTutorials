import numpy as np
from PIL import Image as ImageP

sq_size = 512
RGB_SIZE = 255
COLOR_CH = 3


def _vec(w: int, h: int, c: int) -> np.array:
  return np.empty((w, h, c)).astype(np.float32)


def create_img(*args):
  print(args)


canvas_px = np.zeros((sq_size, sq_size, COLOR_CH)).astype(np.uint8)

create_img(0)
_row = np.arange(0, sq_size)
_col = np.arange(0, sq_size).reshape(sq_size, 1)
_x, _y = np.meshgrid(_row, _col)
_pos = _vec(sq_size, sq_size, 2)
_pos[..., 0] = _x
_pos[..., 1] = _y
print(_pos.shape)

vs = np.dstack(np.meshgrid(_row, _col))

print(vs.shape)

print(np.allclose(_pos, vs))

imgp = ImageP.fromarray(canvas_px)

