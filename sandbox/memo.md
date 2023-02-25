# 📝 2023/02/25

```text
         12580047 function calls (12580046 primitive calls) in 8.241 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        4    2.723    0.681    7.672    1.918 function_base.py:2400(_vectorize_call)
  4193297    2.685    0.000    4.209    0.000 230225_1628.py:52(floatBitsToUint)
  4193297    0.809    0.000    0.809    0.000 {method 'unpack' of '_struct.Struct' objects}
       10    0.741    0.074    0.741    0.074 {built-in method numpy.asanyarray}
  4193297    0.715    0.000    0.715    0.000 {method 'pack' of '_struct.Struct' objects}
        4    0.171    0.043    7.843    1.961 function_base.py:2301(__call__)
        2    0.151    0.075    0.170    0.085 230225_1628.py:96(uhash33)
        2    0.114    0.057    0.120    0.060 230225_1628.py:76(uhash22)
        7    0.052    0.007    0.052    0.007 {method 'astype' of 'numpy.ndarray' objects}
       14    0.035    0.002    0.035    0.002 {method 'copy' of 'numpy.ndarray' objects}
        1    0.020    0.020    8.239    8.239 230225_1628.py:141(profile_run)
        1    0.005    0.005    2.102    2.102 230225_1628.py:135(hash31)
        1    0.004    0.004    0.004    0.004 {built-in method numpy.zeros}
        1    0.004    0.004    2.009    2.009 230225_1628.py:124(hash33)
        2    0.003    0.002    0.039    0.020 230225_1628.py:27(_vec)
        1    0.003    0.003    2.243    2.243 230225_1628.py:129(hash21)
        1    0.003    0.003    0.031    0.031 230225_1628.py:32(FragCoord)
        1    0.002    0.002    8.241    8.241 <string>:1(<module>)
        1    0.002    0.002    1.803    1.803 230225_1628.py:119(hash22)
        1    0.001    0.001    0.001    0.001 {method 'decode' of 'ImagingDecoder' objects}
        1    0.000    0.000    0.000    0.000 {built-in method PIL._imaging.fill}
        1    0.000    0.000    8.241    8.241 {built-in method builtins.exec}
        2    0.000    0.000    0.000    0.000 stride_tricks.py:340(_broadcast_to)
        1    0.000    0.000    0.001    0.001 Image.py:3030(fromarray)
        2    0.000    0.000    0.000    0.000 {built-in method numpy.empty}
        4    0.000    0.000    0.000    0.000 function_base.py:2331(_get_ufunc_and_otypes)
        4    0.000    0.000    0.377    0.094 function_base.py:2410(<listcomp>)
        1    0.000    0.000    0.000    0.000 {built-in method PIL._imaging.raw_decoder}
        1    0.000    0.000    0.000    0.000 Image.py:2896(new)
        1    0.000    0.000    0.000    0.000 {built-in method numpy.frompyfunc}
        1    0.000    0.000    0.010    0.010 function_base.py:4892(meshgrid)
        2    0.000    0.000    0.000    0.000 {built-in method numpy.arange}
        1    0.000    0.000    0.000    0.000 stride_tricks.py:416(_broadcast_shape)
        1    0.000    0.000    0.000    0.000 stride_tricks.py:480(broadcast_arrays)
        1    0.000    0.000    0.000    0.000 Image.py:543(_new)
        1    0.000    0.000    0.000    0.000 Image.py:393(_getdecoder)
        1    0.000    0.000    0.001    0.001 Image.py:2935(frombytes)
        1    0.000    0.000    0.001    0.001 Image.py:807(frombytes)
        2    0.000    0.000    0.000    0.000 Image.py:512(__init__)
        1    0.000    0.000    0.010    0.010 function_base.py:5045(<listcomp>)
       17    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.010    0.010 <__array_function__ internals>:177(meshgrid)
        3    0.000    0.000    0.000    0.000 Image.py:2875(_check_size)
        1    0.000    0.000    0.000    0.000 function_base.py:5032(<listcomp>)
      2/1    0.000    0.000    0.010    0.010 {built-in method numpy.core._multiarray_umath.implement_array_function}
        3    0.000    0.000    0.000    0.000 {method 'reshape' of 'numpy.ndarray' objects}
        1    0.000    0.000    0.001    0.001 Image.py:2973(frombuffer)
        7    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
        1    0.000    0.000    0.000    0.000 {method 'setimage' of 'ImagingDecoder' objects}
        1    0.000    0.000    0.000    0.000 stride_tricks.py:546(<listcomp>)
        4    0.000    0.000    0.000    0.000 {method 'setdefault' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 stride_tricks.py:538(<listcomp>)
        2    0.000    0.000    0.000    0.000 function_base.py:346(iterable)
        1    0.000    0.000    0.000    0.000 <__array_function__ internals>:177(broadcast_arrays)
        2    0.000    0.000    0.000    0.000 {built-in method builtins.any}
        2    0.000    0.000    0.000    0.000 stride_tricks.py:542(<genexpr>)
        4    0.000    0.000    0.000    0.000 {built-in method numpy.array}
        6    0.000    0.000    0.000    0.000 stride_tricks.py:345(<genexpr>)
        2    0.000    0.000    0.000    0.000 stride_tricks.py:25(_maybe_view_as_subclass)
        2    0.000    0.000    0.000    0.000 {method '__exit__' of 'numpy.nditer' objects}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.getattr}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.all}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.iter}
        1    0.000    0.000    0.000    0.000 {method 'copy' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 function_base.py:4887(_meshgrid_dispatcher)
        1    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 stride_tricks.py:476(_broadcast_arrays_dispatcher)

```

# 📝 2023/02/24

[NumPyのファンシーインデックス（リストによる選択と代入） | note.nkmk.me](https://note.nkmk.me/python-numpy-fancy-indexing/)

# 📝 2023/02/23

[世界一分かりやすいnp.meshgridの使い方 (メッシュグリッド) | 機械学習と情報技術](https://disassemble-channel.com/np-meshgrid/)

[NumPy入門 通常の関数をユニバーサル関数に変換する frompyfunc | Python学習講座](https://www.python.ambitious-engineer.com/archives/1333)

[numpy.vectorize, frompyfunc：ユニバーサル関数への変換](https://python.atelierkobato.com/universal/)
