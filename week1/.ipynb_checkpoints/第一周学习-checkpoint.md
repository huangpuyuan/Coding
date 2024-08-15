# 第一周学习计划

| 周数 | 星期 | 学习内容                     | 目标                                       | 任务                                                                                          | 资源                                                                                                  |
|------|------|------------------------------|-------------------------------------------|-----------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| 1    | 周一 | Python 面向对象编程         | 理解面向对象编程的基本概念               | - 学习类和对象的定义。<br>- 理解继承和多态的概念。<br>- 编写简单的类（如 `Person` 类）。  | - [Python 官方文档 - 类和对象](https://docs.python.org/3/tutorial/classes.html) <br> - [视频教程](https://www.bilibili.com/video/BV1Z4411f7hD) |
| 1    | 周二 | Python 常用库               | 了解常用的 Python 库及其应用              | - 学习 NumPy 的基本操作（如数组创建、索引、切片）。<br>- 学习 Pandas 的基本操作。<br>- 完成简单的数据处理示例。 | - [NumPy 官方文档](https://numpy.org/doc/stable/) <br> - [Pandas 官方文档](https://pandas.pydata.org/docs/) <br> - [视频教程](https://www.bilibili.com/video/BV1h4411f7hD) |
| 1    | 周三 | Python 数据处理             | 掌握数据处理的基本技巧                   | - 学习数据清洗的基本步骤。<br>- 学习数据转换。<br>- 使用 Pandas 完成一个小项目。          | - [数据清洗教程](https://towardsdatascience.com/data-cleaning-in-python-using-pandas-5c0c8c5c5c8f) <br> - [视频教程](https://www.bilibili.com/video/BV1g4411f7hD) |
| 1    | 周四 | Python 数据可视化           | 学习数据可视化的基本方法                 | - 学习 Matplotlib 的基本用法。<br>- 学习 Seaborn 的基本用法。<br>- 完成一个数据可视化项目。 | - [Matplotlib 官方文档](https://matplotlib.org/stable/contents.html) <br> - [Seaborn 官方文档](https://seaborn.pydata.org/) <br> - [视频教程](https://www.bilibili.com/video/BV1K4411f7hD) |
| 1    | 周五 | Transformer 架构基础概念    | 了解 Transformer 架构的基本概念          | - 学习 Transformer 的基本结构。<br>- 理解自注意力机制的原理。<br>- 学习多头注意力的概念。 | - [Transformer 论文](https://arxiv.org/abs/1706.03762) <br> - [视频讲解](https://www.bilibili.com/video/BV1Z4411f7hD) |
| 1    | 周六 | 大模型训练与微调基础概念    | 了解大模型训练与微调的基本概念          | - 学习大模型的定义及其应用场景。<br>- 理解微调的概念及其应用。<br>- 学习如何选择预训练模型。 | - [大模型概述文章](https://towardsdatascience.com/understanding-large-language-models-1e3c9d3b3c4e) <br> - [视频讲解](https://www.bilibili.com/video/BV1g4411f7hD) |
| 1    | 周日 | TensorFlow 安装与基础概念   | 安装 TensorFlow 并了解其基本概念        | - 安装 TensorFlow。<br>- 学习 TensorFlow 的基本概念。<br>- 了解 TensorFlow 的工作原理。  | - [TensorFlow 官方安装指南](https://www.tensorflow.org/install) <br> - [TensorFlow 基础概念](https://www.tensorflow.org/guide/tensor) |

# 周一：Python 面向对象编程

## 学习目标
- 理解面向对象编程（OOP）的基本概念。
- 掌握类和对象的定义与使用。
- 理解继承和多态的概念。

## 具体任务

1. **学习类和对象的定义**
   - 理解什么是类（Class）和对象（Object）。
   - 学习如何定义一个类，并创建对象。
   - 示例代码：
     ```python
     class Person:
         def __init__(self, name, age):
             self.name = name
             self.age = age

         def greet(self):
             print(f"Hello, my name is {self.name} and I am {self.age} years old.")

     # 创建对象
     person1 = Person("Alice", 30)
     person1.greet()  # 输出: Hello, my name is Alice and I am 30 years old.
     ```

2. **理解继承和多态的概念**
   - 学习如何使用继承创建子类。
   - 理解方法重写（Override）和多态的概念。
   - 示例代码：
     ```python
     class Employee(Person):  # 继承 Person 类
         def __init__(self, name, age, position):
             super().__init__(name, age)  # 调用父类的构造函数
             self.position = position

         def greet(self):
             print(f"Hello, my name is {self.name}, I am {self.age} years old, and I work as a {self.position}.")

     # 创建 Employee 对象
     employee1 = Employee("Bob", 25, "Engineer")
     employee1.greet()  # 输出: Hello, my name is Bob, I am 25 years old, and I work as a Engineer.
     ```

3. **编写简单的类**
   - 创建一个简单的类（如 `Car` 类），包含属性和方法。
   - 示例代码：
     ```python
     class Car:
         def __init__(self, make, model, year):
             self.make = make
             self.model = model
             self.year = year

         def display_info(self):
             print(f"{self.year} {self.make} {self.model}")

     # 创建 Car 对象
     car1 = Car("Toyota", "Camry", 2020)
     car1.display_info()  # 输出: 2020 Toyota Camry
     ```

4. **了解 TensorFlow 安装与基础概念**
   - 学习如何安装 TensorFlow（使用 pip 或 Anaconda）。
   - 理解 TensorFlow 的基本概念（张量、计算图）。
   - 了解 TensorFlow 的工作原理。
   - 示例代码（安装 TensorFlow）：
     ```bash
     pip install tensorflow
     ```

## 学习资源
- **文档**：
  - [Python 官方文档 - 类和对象](https://docs.python.org/3/tutorial/classes.html)
  - [TensorFlow 官方安装指南](https://www.tensorflow.org/install)
- **视频教程**：
  - [Bilibili 视频教程](https://www.bilibili.com/video/BV1Z4411f7hD)
  - [TensorFlow 基础概念视频](https://www.bilibili.com/video/BV1g4411f7hD)

## 学习时间安排
- **09:00 - 10:00**：学习类和对象的定义（阅读文档和观看视频）。
- **10:00 - 11:00**：理解继承和多态的概念（阅读文档和观看视频）。
- **11:00 - 12:00**：编写简单的类（如 `Car` 类），并进行练习。
- **12:00 - 13:00**：午餐休息。
- **13:00 - 14:00**：完成练习，巩固所学知识。
- **14:00 - 15:00**：总结学习内容，记录学习笔记。
- **15:00 - 17:00**：自由时间，复习或进行额外练习。
- **17:00 - 18:00**：了解 TensorFlow 的安装与基础概念（阅读文档和观看视频）。


## 遇到的困难
今天的学习任务尚未开始，待完成后可在此记录学习进度和遇到的困难。


- 类是对象的蓝图，定义了对象的属性和方法。
- 对象是类的实例，具有自己的属性值。
- 继承允许创建新类，复用现有类的代码。
- 封装通过限制对属性的访问来保护数据。

## 总结
通过今天的学习，你将对 Python 的面向对象编程有一个初步的了解，掌握类、对象、继承和多态的基本概念，并了解 TensorFlow 的安装与基础概念。这将为后续的学习打下良好的基础。


### 周二

#### 1. NumPy 基本操作

- **数组创建**：
  
  - 使用 `numpy.array()` 创建数组。
  - 使用 `numpy.zeros()`、`numpy.ones()` 和 `numpy.arange()` 创建特定形状的数组。
  - 使用 `numpy.linspace()` 创建等间隔的数组。

- **数组索引与切片**：
  
  - 学习如何访问数组中的元素。
  - 使用切片操作获取数组的子数组。
  - 理解布尔索引的使用。

- **基本数组操作**：
  
  - 学习数组的形状、大小和维度。
  - 进行数组的基本运算（加、减、乘、除）。
  - 学习常用的 NumPy 函数，如 `numpy.sum()`、`numpy.mean()`、`numpy.max()` 等。

#### 2. Pandas 基本操作

- **数据结构**：
  
  - 理解 Pandas 的基本数据结构：Series 和 DataFrame。
  - 学习如何创建 Series 和 DataFrame。

- **数据读取与写入**：
  
  - 学习如何从 CSV 文件读取数据（使用 `pd.read_csv()`）。
  - 学习如何将 DataFrame 写入 CSV 文件（使用 `DataFrame.to_csv()`）。

- **数据操作**：
  
  - 学习基本的数据选择和过滤。
  - 使用 `loc` 和 `iloc` 进行行列选择。
  - 学习数据的排序和重置索引。

- **数据清洗**：
  
  - 学习如何处理缺失值（使用 `dropna()` 和 `fillna()`）。
  - 学习数据类型转换。

#### 3. TensorFlow 安装与基础概念

- **安装 TensorFlow**：
  
  - 使用 `pip` 安装 TensorFlow：
    
    <BASH>
    
    `pip install tensorflow`
  
  - 验证安装是否成功：
    
    <PYTHON>
    
    `import tensorflow as tf print(tf.__version__)`

- **TensorFlow 基础概念**：
  
  - 理解 TensorFlow 的基本概念，如张量（Tensor）、计算图（Computational Graph）和会话（Session）。
  - 学习如何创建和操作张量。
  - 理解 TensorFlow 的基本数据流。

#### 4. 资源

#### NumPy

- [NumPy 官方文档](https://numpy.org/doc/stable/)

- [NumPy 教程](https://numpy.org/doc/stable/user/quickstart.html)
  
#### Pandas

- [Pandas 官方文档](https://pandas.pydata.org/docs/)

- [Pandas 教程](https://pandas.pydata.org/pandas-docs/stable/getting_started/intro_tutorials/index.html)
  
#### TensorFlow

- [TensorFlow 官方文档](https://www.tensorflow.org/learn)

- [TensorFlow 安装指南](https://www.tensorflow.org/install)

``` python
  # 数组加法
  array_sum = array_1d + 10
  print("加法结果:", array_sum)

  # 数组乘法
  array_product = array_1d * 2
  print("乘法结果:", array_product)

  # 计算数组的和、均值和最大值
  print("数组和:", np.sum(array_1d))
  print("数组均值:", np.mean(array_1d))
  print("数组最大值:", np.max(array_1d))
```


### 总结

根据你的兴趣和学习目标，选择适合的内容进行学习。如果你有特定的主题或技术想要深入了解，请告诉我，我可以提供更详细的学习资源和建议！祝你今天的学习顺利！



