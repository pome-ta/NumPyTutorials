import numpy as np

# uint8 = np.array([1, 0, 0xffff_ffff], dtype=np.uint8)
uint32 = np.array([1, 0, 0xffff_ffff]).astype(np.uint32)
float32 = uint32.astype(np.float32)

pf = np.array([0.0, -0.01, 0.02, 0.9]).astype(np.float32)

pu = pf.astype(np.uint32)

_ = 1
