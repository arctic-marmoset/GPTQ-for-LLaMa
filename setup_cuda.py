from setuptools import setup, Extension
from torch.utils import cpp_extension

# Torch defines __HIP_NO_HALF_CONVERSIONS__ and __HIP_NO_HALF_OPERATORS__ for
# some reason, preventing implicit casts in the faster kernels. This just
# undefs them.
HIP_HALF_CONVERSION_FLAGS = [
    "-U__HIP_NO_HALF_CONVERSIONS__",
    "-U__HIP_NO_HALF_OPERATORS__",
]

setup(
    name='quant_cuda',
    ext_modules=[cpp_extension.CUDAExtension(
        name='quant_cuda',
        sources=['quant_cuda.cpp', 'quant_cuda_kernel.cu'],
        extra_compile_args={
            'nvcc': HIP_HALF_CONVERSION_FLAGS,
        }
    )],
    cmdclass={'build_ext': cpp_extension.BuildExtension}
)
