## Speed Up your Algorithms Part 2— Numba

## 加速你的算法第2部分 -  Numba


> Get C++/Fortran like speed for your functions with Numba

> Numba 使您的函数像 C++/Fortran 一样快速



![IMG](https://cdn-images-1.medium.com/max/2600/0*S9e58pstVLokmajz)

“brown snake” by [Duncan Sanchez](https://unsplash.com/@joseph3088?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)



This is the third post in a series I am writing. All posts are here:

1. [Speed Up your Algorithms Part 1 — PyTorch](https://towardsdatascience.com/speed-up-your-algorithms-part-1-pytorch-56d8a4ae7051)
2. [Speed Up your Algorithms Part 2 — Numba](https://towardsdatascience.com/speed-up-your-algorithms-part-2-numba-293e554c5cc1)
3. [Speed Up your Algorithms Part 3 — Parallelization](https://towardsdatascience.com/speed-up-your-algorithms-part-3-parallelization-4d95c0888748)
4. [Speed Up your Algorithms Part 4 — Dask](https://towardsdatascience.com/speeding-up-your-algorithms-part-4-dask-7c6ed79994ef)

And these goes with **Jupyter Notebooks** available here:

[[Github-SpeedUpYourAlgorithms](https://github.com/PuneetGrov3r/MediumPosts/tree/master/SpeedUpYourAlgorithms)] and **[**[**Kaggle**](https://www.kaggle.com/puneetgrover/kernels)**]**



这是我写的该系列文章中的第二篇。所有的文章如下：

1. [加速您的算法第1部分 -  PyTorch](https://towardsdatascience.com/speed-up-your-algorithms-part-1-pytorch-56d8a4ae7051)
2. [加速您的算法第2部分 -  Numba](https://towardsdatascience.com/speed-up-your-algorithms-part-2-numba-293e554c5cc1)
3. [加速您的算法第3部分 - 并行化](https://towardsdatascience.com/speed-up-your-algorithms-part-3-parallelization-4d95c0888748)
4. [加速您的算法第4部分 -  Dask](https://towardsdatascience.com/speeding-up-your-algorithms-part-4-dask-7c6ed79994ef)

这些文章对应的 *Jupyter Notebooks* 代码如下：

[[Github-SpeedUpYourAlgorithms](https://github.com/PuneetGrov3r/MediumPosts/tree/master/SpeedUpYourAlgorithms)] and **[**[**Kaggle**](https://www.kaggle.com/puneetgrover/kernels)**]**

------

### Index

1. Introduction
2. Why Numba?
3. How does Numba Works?
4. Using basic numba functionalities (Just @jit it!)
5. The @vectorize wrapper
6. Running your functions on GPU
7. Further Reading
8. References

NOTE:
This post goes with Jupyter Notebook available in my Repo on Github: [SpeedUpYourAlgorithms-Numba](https://nbviewer.jupyter.org/github/PuneetGrov3r/MediumPosts/blob/master/SpeedUpYourAlgorithms/2%29%20Numba.ipynb)

### 目录

1. 介绍
2. 为什么选择 Numba？
3. Numba 是如何工作的？
4. 使用 Numba 的基本功能（只需要加上 `@jit`！）
5. @vectorize 装饰器
6. 在 GPU 上运行函数
7. 扩展阅读
8. 参考

注意：
这篇文章的  Jupyter Notebook 代码在我的 Github 上：[SpeedUpYourAlgorithms-Numba](https://nbviewer.jupyter.org/github/PuneetGrov3r/MediumPosts/blob/master/SpeedUpYourAlgorithms/2%29%20Numba.ipynb)

------

### 1. Introduction

Numba is a *Just-in-time* compiler for python, i.e. whenever you make a call to a python function all or part of your code is converted to machine code “*just-in-time*” of execution, and it will then run on your native machine code speed! It is sponsored by Anaconda Inc and has been/is supported by many other organisations.

With the help of Numba you can speed up all of your calculation focused and computationally heavy python functions(eg loops). It also has support for numpy library! So, you can use numpy in your calculations too, and speed up the overall computation as loops in python are really slow. You can also use many of the functions of math library of python standard library like sqrt etc. For comprehensive list of all compatible functions look [here](http://numba.pydata.org/numba-doc/0.17.0/reference/pysupported.html).



### 1. 介绍

Numba 是 python 的即时（Just-in-time）编译器，即当您调用 python 函数时，您的全部或部分代码就会被转换为“即时”执行的机器码，它将以您的本地机器码速度运行！它由 Anaconda 公司赞助，并得到了许多其他组织的支持。

在 Numba 的帮助下，您可以加速所有计算负载比较大的 python 函数（例如循环）。它还支持 numpy 库！所以，您也可以在您的计算中使用 numpy，并加快整体计算，因为 python 中的循环非常慢。 您还可以使用 python 标准库中的 math 库的许多函数，如 `sqrt` 等。有关所有兼容函数的完整列表，请查看 [此处](http://numba.pydata.org/numba-doc/0.17.0/reference/pysupported.html)。

------

### 2. Why Numba?

![IMG](https://cdn-images-1.medium.com/max/880/1*7wHgolEzegBX41BW0cxVYQ.jpeg)

[[Source](http://rebloggy.com/post/snake-crown-zeus-ball-python-python-i-cant-believe-he-let-me-do-this-snakes-in-h/30972529459)]

So, why numba? When there are many other compilers like [cython](http://cython.org/), or any other similar compilers or something like [pypy](http://doc.pypy.org/en/latest/faq.html#what-is-pypy).

For a simple reason that here you don’t have to leave the comfort zone of writing your code in python. Yes, you read it right, you don’t have to change your code at all for basic speedup which is comparable to speedup you get from similar cython code with type definitions. Isn’t that great?

You just have to add a familiar python functionality, a decorator (a wrapper) around your functions. A [wrapper for class](https://numba.pydata.org/numba-doc/dev/user/jitclass.html) is also under development.

So, you just have to add a decorator and you are done. eg:

```python
from numba import jit
@jit
def function(x):
    # your loop or numerically intensive computations
    return x
```

It still looks like a pure python code, doesn’t it?



### 2. 为什么选择 Numba？

![IMG](https://cdn-images-1.medium.com/max/880/1*7wHgolEzegBX41BW0cxVYQ.jpeg)

[图片来源](http://rebloggy.com/post/snake-crown-zeus-ball-python-python-i-cant-believe-he-let-me-do-this-snakes-in-h/30972529459)



那么，当有像 [cython](http://cython.org/) 和 [Pypy](http://doc.pypy.org/en/latest/faq.html#what-is-pypy) 之类的许多其他编译器时，为什么要选择 numba？

原因很简单，这样您就不必离开写 python 代码的舒适区。是的，就是这样，您根本不需要为了获得一些的加速来改变您的代码，这与您从类似的具有类型定义的 cython 代码获得的加速相当。那不是很好吗？

您只需要添加一个熟悉的 python 功能，即添加一个包装器（一个装饰器）到您的函数上。[类的装饰器](https://numba.pydata.org/numba-doc/dev/user/jitclass.html)也在开发中了。

所以，您只需要添加一个装饰器就可以了。例如：

```python
from numba import jit
@jit
def function(x):
    # your loop or numerically intensive computations
    return x
```

这仍然看起来像一个原生 python 代码，不是吗？

------

### 3. How does numba work?

![IMG](https://cdn-images-1.medium.com/max/880/0*bJ6XIUE05phjWZgz)

“question mark neon signage” by [Emily Morter](https://unsplash.com/@emilymorter?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)



Numba generates optimized machine code from pure python code using [LLVM compiler infrastructure](http://llvm.org/). Speed of code run using numba is comparable to that of similar code in C, C++ or Fortran.

Here is how the code is compiled:

![IMG](https://cdn-images-1.medium.com/max/880/1*9n6WpEXjuD2lBSlX2_pU0g.png)

[[Source](https://github.com/ContinuumIO/gtc2017-numba/blob/master/1%20-%20Numba%20Basics.ipynb)]

First, Python function is taken, optimized and is converted into numba’s intermediate representation, then after type inference which is like numpy’s type inference (so python float is a float64) it is converted into LLVM interpretable code. This code is then fed to LLVM’s just-in-time compiler to give out a machine code.

You can [generate](http://numba.pydata.org/numba-doc/latest/user/jit.html#jit) code at runtime or import time on CPU (default) or [GPU](http://numba.pydata.org/numba-doc/latest/cuda/index.html), as you prefer it.

### 3. 如何使用 Numba？

![IMG](https://cdn-images-1.medium.com/max/880/0*bJ6XIUE05phjWZgz)

“question mark neon signage” by [Emily Morter](https://unsplash.com/@emilymorter?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)

Numba 使用 [LLVM 编译器基础结构](http://llvm.org/) 将原生 python 代码转换成优化的机器码。使用 numba 运行代码的速度可与 C/C++ 或 Fortran 中的类似代码相媲美。

以下是代码的编译方式：

![IMG](https://cdn-images-1.medium.com/max/880/1*9n6WpEXjuD2lBSlX2_pU0g.png)

[图片来源](https://github.com/ContinuumIO/gtc2017-numba/blob/master/1%20-%20Numba%20Basics.ipynb)

首先，Python 函数被传入，优化并转换为 numba 的中间表达，然后在类型推断（type inference）之后，就像 numpy 的类型推断（所以 python float 是一个 float64），它被转换为 LLVM 可解释代码。 然后将此代码提供给 LLVM 的即时编译器以生成机器码。

您可以根据需要在运行时或导入时 [生成](http://numba.pydata.org/numba-doc/latest/user/jit.html#jit) 机器码，导入需要在 CPU（默认）或 [GPU](http://numba.pydata.org/numba-doc/latest/cuda/index.html) 上进行。

------

### 4. Using basic numba functionalities (Just @jit it!)

![IMG](https://cdn-images-1.medium.com/max/880/0*4IukKwm5RO0PWjmZ)

Photo by [Charles Etoroma](https://unsplash.com/@charlesetoroma?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)

> *Piece of cake!*

For best performance numba actually recommends to use `nopython = True`argument with your jit wrapper, using which it won’t use the Python interpreter at all. Or you can also use `@njit` too. If your wrapper with `nopython = True` fails with an error, you can use simple `@jit` wrapper which will compile part of your code, loops it can compile, and turns them into functions, to compile into machine code and give the rest to python interpreter.

So, you just have to do:

```python
from numba import njit, jit
@njit      # or @jit(nopython=True)
def function(a, b):
    # your loop or numerically intensive computations
    return result
```

### 4. 使用 numba 的基本功能（只需要加上 @jit ！）

![IMG](https://cdn-images-1.medium.com/max/880/0*4IukKwm5RO0PWjmZ)

Photo by [Charles Etoroma](https://unsplash.com/@charlesetoroma?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)

> *小菜一碟！*

为了获得最佳性能，numba 实际上建议在您的 jit 装饰器中加上 `nopython=True` 参数，加上后就不会使用 Python 解释器了。或者您也可以使用 `@njit`。如果您加上 `nopython=True` 的装饰器失败并报错，您可以用简单的 `@jit` 装饰器来编译您的部分代码，对于它能够编译的代码，将它们转换为函数，并编译成机器码。然后将其余部分代码提供给 python 解释器。

所以，您只需要这样做：

```python
from numba import njit, jit
@njit      # or @jit(nopython=True)
def function(a, b):
    # your loop or numerically intensive computations
    return result
```

------

When using `@jit` make sure your code has something numba can compile, like a compute intensive loop, maybe with libraries (numpy) and functions it support. Otherwise it won’t be able to compile anything and your code will be slower than what it would have been without using numba, because of the numba internal code checking overhead.

To put cherry on top, numba also caches the functions after first use as a machine code. So after first time it will be even faster because it doesn’t need to compile that code again, given that you are using same argument types that you used before.

And if your code is [parallelizable](http://numba.pydata.org/numba-doc/latest/user/parallel.html#numba-parallel) you can also pass `parallel = True` as an argument, but it must be used in conjunction with `nopython = True`. For now it only works on CPU.

You can also specify function signature you want your function to have, but then it won’t compile for any other types of arguments you give to it. For example:

```python
from numba import jit, int32
@jit(int32(int32, int32))
def function(a, b):
    # your loop or numerically intensive computations
    return result
# or if you haven't imported type names
# you can pass them as string
@jit('int32(int32, int32)')
def function(a, b):
    # your loop or numerically intensive computations
    return result
```

当使用 `@jit` 时，请确保您的代码有 numba 可以编译的内容，比如包含库（numpy）和它支持的函数的计算密集型循环。否则它将不会编译任何东西，并且您的代码将比没有使用 numba 时更慢，因为存在 numba 内部代码检查的额外开销。

还有更好的一点是，numba 会对首次作为机器码使用后的函数进行缓存。 因此，在第一次使用之后它将更快，因为它不需要再次编译这些代码，如果您使用的是和之前相同的参数类型。

如果您的代码是 [可并行化](http://numba.pydata.org/numba-doc/latest/user/parallel.html#numba-parallel) 的，您也可以传递 `parallel=True` 作为参数，但它必须与 `nopython=True` 一起使用，目前这只适用于CPU。

您还可以指定希望函数具有的函数签名，但是这样就不会对您提供的任何其他类型的参数进行编译。 例如：

```python
from numba import jit, int32
@jit(int32(int32, int32))
def function(a, b):
    # your loop or numerically intensive computations
    return result
# or if you haven't imported type names
# you can pass them as string
@jit('int32(int32, int32)')
def function(a, b):
    # your loop or numerically intensive computations
    return result
```

------

Now your function will only take two int32’s and return an int32. By this you can have more control over your functions. You can even pass [multiple](http://numba.pydata.org/numba-doc/latest/reference/jit-compilation.html#numba.jit) functional signatures if you want.

![IMG](https://cdn-images-1.medium.com/max/880/1*aU6HSr8OGNilxhTR2A25XQ.png)

You can also use other wrappers provided by numba:

1. [@vectorize](http://numba.pydata.org/numba-doc/latest/user/vectorize.html): allows scalar arguments to be used as numpy ufuncs,
2. [@guvectorize](http://numba.pydata.org/numba-doc/latest/user/vectorize.html#guvectorize): produces NumPy generalized `ufunc` s,
3. [@stencil](http://numba.pydata.org/numba-doc/latest/user/stencil.html#numba-stencil): declare a function as a kernel for a stencil like operation,
4. [@jitclass](http://numba.pydata.org/numba-doc/latest/user/jitclass.html#jitclass): for jit aware classes,
5. [@cfunc](http://numba.pydata.org/numba-doc/latest/user/cfunc.html#cfunc): declare a function for use as a native call back (to be called from C/C++ etc),
6. [@overload](http://numba.pydata.org/numba-doc/latest/extending/high-level.html#high-level-extending): register your own implementation of a function for use in nopython mode, e.g. `@overload(scipy.special.j0)`.

Numba also has **Ahead of time** ([AOT](https://numba.pydata.org/numba-doc/dev/user/pycc.html)) compilation, which produces compiled extension module which does not depend on Numba. But:

1. It allows only regular functions (not ufuncs),
2. You have to specify function signature. You can only specify one, for many specify under different names.

It also produces generic code for your CPU’s architectural family.



现在您的函数只能接收两个 int32 类型的参数并返回一个 int32 类型的值。 通过这种方式，您可以更好地控制您的函数。 如果需要，您甚至可以传递多个函数签名。

![IMG](https://cdn-images-1.medium.com/max/880/1*aU6HSr8OGNilxhTR2A25XQ.png)

您还可以使用 numba 提供的其他装饰器：

1. [@vectorize](http://numba.pydata.org/numba-doc/latest/user/vectorize.html)：允许将标量参数作为 numpy 的 ufuncs 使用，
2. [@guvectorize](http://numba.pydata.org/numba-doc/latest/user/vectorize.html#guvectorize)：生成 NumPy 广义上的 `ufunc`s，
3. [@stencil](http://numba.pydata.org/numba-doc/latest/user/stencil.html#numba-stencil)：定义一个函数使其成为 stencil 类型操作的核函数
4. [@jitclass](http://numba.pydata.org/numba-doc/latest/user/jitclass.html#jitclass)：用于 jit 类，
5. [@cfunc](http://numba.pydata.org/numba-doc/latest/user/cfunc.html#cfunc)：声明一个函数用于本地回调（被C/C++等调用），
6. [@overload](http://numba.pydata.org/numba-doc/latest/extending/high-level.html#high-level-extending)：注册您自己的函数实现，以便在 `nopython` 模式下使用，例如： `@overload（scipy.special.j0）`。

Numba 还有 **Ahead of time**（[AOT](https://numba.pydata.org/numba-doc/dev/user/pycc.html)）编译，它生成不依赖于 Numba 的已编译扩展模块。 但：

1. 它只允许常规函数（ufuncs 就不行），
2. 您必须指定函数签名。并且您只能指定一种签名，如果需要指定多个签名，需要使用不同的名字。

它还根据您的CPU架构系列生成通用代码。

------

### 5. The @vectorize wrapper

![IMG](https://cdn-images-1.medium.com/max/880/0*E9-BCxGFbXYIegax)

“gray solar panel lot” by [American Public Power Association](https://unsplash.com/@publicpowerorg?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)

By using @vectorize wrapper you can convert your functions which operates on scalars only, for example if you are using python’s `math`library which only works on scalars, to work for arrays. This gives speed similar to that of a numpy array operations (ufuncs). For example:

```python
@vectorize
def func(a, b):
    # Some operation on scalars
    return result
```

You can also pass `target` argument to this wrapper which can have value equal to `parallel` for parallelizing code, `cuda` for running code on cuda\GPU.

```python
@vectorize(target="parallel")
def func(a, b):
    # Some operation on scalars
    return result
```

Vectorizing with `target = "parallel"` or `"cuda"` will generally run faster than numpy implementation, given your code is sufficiently compute intensive or array is sufficiently large. If not then it comes with an overhead of the time for making threads and splitting elements for different threads, which can be larger than actual compute time for whole process. So, work should be sufficiently heavy to get a speedup.

![IMG](https://cdn-images-1.medium.com/max/880/1*B-pN5BguZzGeoFX706QTAA.png)

This great video has an example of speeding up Navier Stokes equation for computational fluid dynamics with Numba:

### 5. @vectorize 装饰器

![IMG](https://cdn-images-1.medium.com/max/880/0*E9-BCxGFbXYIegax)

“gray solar panel lot” by [American Public Power Association](https://unsplash.com/@publicpowerorg?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)

通过使用 @vectorize 装饰器，您可以对仅能对标量操作的函数进行转换，例如，如果您使用的是仅适用于标量的 python 的 `math` 库，则转换后就可以用于数组。 这提供了类似于 numpy 数组运算（ufuncs）的速度。 例如：

```python
@vectorize
def func(a, b):
    # Some operation on scalars
    return result
```

您还可以将 `target` 参数传递给此装饰器，该装饰器使 target 参数为 `parallel` 时用于并行化代码，为 `cuda` 时用于在 cuda\GPU 上运行代码。

```python
@vectorize(target="parallel")
def func(a, b):
    # Some operation on scalars
    return result
```

使 `target=“parallel”` 或 `“cuda”` 进行矢量化通常比 numpy 实现的代码运行得更快，只要您的代码具有足够的计算密度或者数组足够大。如果不是，那么由于创建线程以及将元素分配到不同线程需要额外的开销，因此可能耗时更长。所以运算量应该足够大，才能获得明显的加速。

![IMG](https://cdn-images-1.medium.com/max/880/1*B-pN5BguZzGeoFX706QTAA.png)

这个视频讲述了一个用 Numba 加速用于计算流体动力学的Navier Stokes方程的例子：

------

### 6. Running your functions on GPU

![IMG](https://cdn-images-1.medium.com/max/880/0*EpVwxeU9OQgi2pb4)

“time-lapsed of street lights” by [Marc Sendra martorell](https://unsplash.com/@marcsm?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)

You can also pass @jit like wrappers to run functions on cuda/GPU also. For that you will have to import `cuda` from `numba` library. But running your code on GPU is not going to be as easy as before. It has some initial computations that needs to done for running function on hundreds or even thousands of threads on GPU. Actually, you have to declare and manage hierarchy of grids, blocks and threads. And its not that hard.

To execute a function on GPU, you have to either define something called a **kernel function** or a **device function**. Firstly lets see a **kernel function**.

Some points to remember about kernel functions:

a) kernels explicitly declare their thread hierarchy when called, i.e. the number of blocks and number of threads per block. You can compile your kernel once, and call it multiple times with different block and grid sizes.

b) kernels cannot return a value. So, either you will have to do changes on original array, or pass another array for storing result. For computing scalar you will have to pass 1 element array.

```python
# Defining a kernel function
from numba import cuda
@cuda.jit
def func(a, result):
    # Some cuda related computation, then
    # your computationally intensive code.
    # (Your answer is stored in 'result')
```

### 6. 在GPU上运行函数

![IMG](https://cdn-images-1.medium.com/max/880/0*EpVwxeU9OQgi2pb4)

“time-lapsed of street lights” by [Marc Sendra martorell](https://unsplash.com/@marcsm?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)

您也可以像装饰器一样传递 @jit 来运行 cuda/GPU 上的函数。 为此您必须从 `numba` 库中导入 `cuda`。 但是要在 GPU 上运行代码并不像之前那么容易。为了在 GPU 上的数百甚至数千个线程上运行函数，需要先做一些初始计算。 实际上，您必须声明并管理网格，块和线程的层次结构。这并不那么难。

要在GPU上执行函数，您必须定义一个叫做 **核函数** 或 **设备函数** 的函数。首先让我们来看 **核函数**。

关于核函数要记住一些要点：

a）核函数在被调用时要显式声明其线程层次结构，即块的数量和每块的线程数量。您可以编译一次核函数，然后用不同的块和网格大小多次调用它。

b）核函数没有返回值。因此，要么必须对原始数组进行更改，要么传递另一个数组来存储结果。为了计算标量，您必须传递单元素数组。

```python
# Defining a kernel function
from numba import cuda
@cuda.jit
def func(a, result):
    # Some cuda related computation, then
    # your computationally intensive code.
    # (Your answer is stored in 'result')
```

------

So for launching a kernel you will have to pass two things:

1. Number of threads per block,
2. Number of blocks.

For example:

```python
threadsperblock = 32
blockspergrid = (array.size + (threadsperblock - 1)) // threadsperblock
func[blockspergrid, threadsperblock](array)
```

Kernel function in every thread has to know in which thread it is, to know which elements of array it is responsible for. Numba makes it easy to get these positions of elements, just by one call.

```python
@cuda.jit
def func(a, result):
    pos = cuda.grid(1)  # For 1D array
    # x, y = cuda.grid(2) # For 2D array
    if pos < a.shape[0]:
        result[pos] = a[pos] * (some computation)
```

因此，要启动核函数，您必须传入两个参数：

1. 每块的线程数，
2. 块的数量。

例如：

```python
threadsperblock = 32
blockspergrid = (array.size + (threadsperblock - 1)) // threadsperblock
func[blockspergrid, threadsperblock](array)
```

每个线程中的核函数必须知道它在哪个线程中，以便了解它负责数组的哪些元素。Numba 只需调用一次即可轻松获得这些元素的位置。

```python
@cuda.jit
def func(a, result):
    pos = cuda.grid(1)  # For 1D array
    # x, y = cuda.grid(2) # For 2D array
    if pos < a.shape[0]:
        result[pos] = a[pos] * (some computation)
```

------

To save the time which will be wasted in copying numpy array to a specific device and then again storing result in numpy array, Numba provides some [functions](https://numba.pydata.org/numba-doc/dev/cuda/memory.html) to declare and send arrays to specific device, like: `numba.cuda.device_array`, `numba.cuda.device_array_like`, `numba.cuda.to_device`, etc. to save time of needless copies to cpu(unless necessary).

On the other hand, a `**device function**` can only be invoked from inside a device only (by a kernel or another device function). The plus point is, you can return a value from a `**device function**`. So, you can use this return value of function to compute something inside a `kernel function` or a `device function`.

```python
from numba import cuda
@cuda.jit(device=True)
def device_function(a, b):
    return a + b

```

为了节省将 numpy 数组复制到指定设备，然后又将结果存储到 numpy 数组中所浪费的时间，Numba 提供了一些 [函数](https://numba.pydata.org/numba-doc/dev/cuda/memory.html) 来声明并将数组送到指定设备，如：`numba.cuda.device_array`，`numba.cuda。 device_array_like`，`numba.cuda.to_device` 等函数来节省不必要的复制到 cpu 的时间（除非必要）。

另一方面，**设备函数** 只能从设备内部（通过核函数或其他设备函数）调用。 比较好的一点是，您可以从 **设备函数** 中返回一个值。 因此，您可以用此函数的返回值来计算 `核函数` 或 `设备函数` 里的内容。

```python
from numba import cuda
@cuda.jit(device=True)
def device_function(a, b):
    return a + b

```

------

You should also look into supported functionality of Numba’s cuda library, [here](https://numba.pydata.org/numba-doc/dev/cuda/cudapysupported.html).

Numba also has its own [atomic operations](https://numba.pydata.org/numba-doc/dev/cuda/intrinsics.html), [random number generators](https://numba.pydata.org/numba-doc/dev/cuda/random.html), [shared memory implementation](https://numba.pydata.org/numba-doc/dev/cuda/memory.html#cuda-shared-memory) (to speed up access to data) etc within its cuda library.

ctypes/cffi/cython interoperability:

- `cffi` - The calling of [CFFI](http://numba.pydata.org/numba-doc/latest/reference/pysupported.html#cffi-support) functions is supported in `nopython` mode.
- `ctypes` - The calling of [ctypes](http://numba.pydata.org/numba-doc/latest/reference/pysupported.html#ctypes-support) wrapped functions is supported in `nopython` mode. .
- Cython exported functions [are callable](http://numba.pydata.org/numba-doc/latest/extending/high-level.html#cython-support).



您还应该在这里查看 Numba 的 cuda 库支持的功能。

Numba 在其 cuda 库中也有自己的[ 原子操作](https://numba.pydata.org/numba-doc/dev/cuda/intrinsics.html)，[随机数生成器](https://numba.pydata.org/numba-doc/dev/cuda/random.html)，[共享内存实现](https://numba.pydata.org/numba-doc/dev/cuda/memory.html#cuda-shared-memory)（以加快数据的访问）等功能。

ctypes/cffi/cython 的互用性：

- `cffi`  - 在 nopython 模式下支持调用 [CFFI](http://numba.pydata.org/numba-doc/latest/reference/pysupported.html#cffi-support) 函数。
- `ctypes`  - 在 nopython 模式下支持调用 [ctypes](http://numba.pydata.org/numba-doc/latest/reference/pysupported.html#ctypes-support) 包装函数。
- Cython 导出的函数是 [可调用](http://numba.pydata.org/numba-doc/latest/extending/high-level.html#cython-support) 的。

------

### 7. Further Reading

1. <https://nbviewer.jupyter.org/github/ContinuumIO/gtc2017-numba/tree/master/>
2. <https://devblogs.nvidia.com/seven-things-numba/>
3. <https://devblogs.nvidia.com/numba-python-cuda-acceleration/>
4. <https://jakevdp.github.io/blog/2015/02/24/optimizing-python-with-numpy-and-numba/>
5. <https://www.youtube.com/watch?v=1AwG0T4gaO0>

### 8. References

1. <http://numba.pydata.org/numba-doc/latest/user/index.html>
2. <https://github.com/ContinuumIO/gtc2018-numba>
3. <http://stephanhoyer.com/2015/04/09/numba-vs-cython-how-to-choose/>

> Thank You for reading!

### 7. 扩展阅读

1. <https://nbviewer.jupyter.org/github/ContinuumIO/gtc2017-numba/tree/master/>
2. <https://devblogs.nvidia.com/seven-things-numba/>
3. <https://devblogs.nvidia.com/numba-python-cuda-acceleration/>
4. <https://jakevdp.github.io/blog/2015/02/24/optimizing-python-with-numpy-and-numba/>
5. <https://www.youtube.com/watch?v=1AwG0T4gaO0>

### 8. 参考

1. <http://numba.pydata.org/numba-doc/latest/user/index.html>
2. <https://github.com/ContinuumIO/gtc2018-numba>
3. <http://stephanhoyer.com/2015/04/09/numba-vs-cython-how-to-choose/>

> 谢谢阅读！



原文链接：<https://towardsdatascience.com/speed-up-your-algorithms-part-2-numba-293e554c5cc1>
