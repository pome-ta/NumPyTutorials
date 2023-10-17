import numpy as np


# This structure defines the layout of vertices sent to the vertex shader. This header is shared between the .metal shader and C code, to guarantee that the layout of the vertex array in the C code matches the layout that the .metal vertex shader expects.
# この構造体は頂点シェーダに送られる頂点のレイアウトを定義します。このヘッダーは.metalシェーダーとCコードの間で共有され、Cコード内の頂点配列のレイアウトが.metal頂点シェーダーが期待するレイアウトと一致することを保証します。
'''
typedef struct
{
    vector_float2 position;
    vector_float4 color;
} AAPLVertex;
'''

