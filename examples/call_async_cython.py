"""
Simple Lithops example using one single function invocation
with a cythonized function located in function.so

Commands to compile the function.py into function.so:
cython3 -3 --embed -X always_allow_keywords=true -o function.c function.py
gcc -shared -o function.so -fPIC -I /usr/include/python3.9 function.c
"""
import lithops
from function import my_c_function


def my_function(x):
    return my_c_function(x)


if __name__ == '__main__':
    fexec = lithops.FunctionExecutor()
    fexec.call_async(my_function, 3)
    print(fexec.get_result())
