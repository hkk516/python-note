4.1 Matplotlib常用技巧
4.1.1　导入Matplotlib
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

4.1.3 程序最后使用ply.show()显示图形，并且在一个图形中只使用一个ply.show()

4.1.4　将图形保存为文件: 
fig.savefig('my_figure.png')

在 savefig() 里面，保存的图片文件格式就是文件的扩展名。
通过 canvas 对象的方法查看系统支持的文件格式：
In[8]: fig.canvas.get_supported_filetypes()
Out[8]: {'eps': 'Encapsulated Postscript',
'jpeg': 'Joint Photographic Experts Group',
'jpg': 'Joint Photographic Experts Group',
'pdf': 'Portable Document Format',
'pgf': 'PGF code for LaTeX',
'png': 'Portable Network Graphics',
'ps': 'Postscript',
'raw': 'Raw RGBA bitmap',
'rgba': 'Raw RGBA bitmap',
'svg': 'Scalable Vector Graphics',
'svgz': 'Scalable Vector Graphics',
'tif': 'Tagged Image File Format',
'tiff': 'Tagged Image File Format'}

当你保存图形文件时，不需要使用 plt.show() 或者前面介绍过的命令

4.2.1 MATLAB风格接口
In[9]: plt.figure() # 创建图形
# 创建两个子图中的第一个，设置坐标轴
plt.subplot(2, 1, 1) # (行、列、子图编号)
plt.plot(x, np.sin(x))
# 创建两个子图中的第二个，设置坐标轴
plt.subplot(2, 1, 2)
plt.plot(x, np.cos(x));

这种接口最重要的特性是有状态的（ stateful） ：它会持续跟踪“当前的”图形和坐标轴，
所有 plt 命令都可以应用。

4.3　简易线形图
要画 Matplotlib 图形时，都需要先创建一个图形 fig 和一个坐标轴 ax。创建图形与坐标轴
的最简单做法如下所示:
In[2]:fig = plt.figure()
	  ax = plt.axes()

在 Matplotlib 里面， figure（ plt.Figure 类的一个实例）可以被看成是一个能够容纳各种坐
标轴、图形、文字和标签的容器。
axes（ plt.Axes 类的一个实例）是一个带有刻度和标签的矩形，最终会包含所有可视化的图形元素。
通常会用变量 fig 表示一个图形实例，用变量 ax 表示一个坐标轴实例或一组坐标轴实例
In[3]: fig = plt.figure()
	   ax = plt.axes()
	   x = np.linspace(0, 10, 1000)
	   ax.plot(x, np.sin(x));
	   
如果想在一张图中创建多条线，可以重复调用 plot 命令
In[5]: plt.plot(x, np.sin(x))
		plt.plot(x, np.cos(x));

4.3.1　调整图形： 线条的颜色与风格
plt.plot(x, np.sin(x - 0), color='blue') # 标准颜色名称
plt.plot(x, x + 4, linestyle='-') # 实线
plt.plot(x, x + 0, '-g') # 绿色实线

4.3.2　调整图形： 坐标轴上下限:	 plt.xlim() 和 plt.ylim()，plt.axis(xmin, xmax, ymin, ymax)
In[9]: plt.plot(x, np.sin(x))
		plt.xlim(-1, 11)
		plt.ylim(-1.5, 1.5);

逆序坐标：
In[10]: plt.plot(x, np.sin(x))
		plt.xlim(10, 0)
		plt.ylim(1.2, -1.2);

plt.axis():
plt.axis([-1, 11, -1.5, 1.5]);
plt.axis()可以按照图形的内容自动收紧坐标轴，不留空白区域：
plt.axis('tight');
还可以实现更高级的配置，例如让屏幕上显示的图形分辨率为 1:1， x 轴单位长度与 y 轴单位长度相等:
plt.axis('equal');

4.3.3　设置图形标签：图形标题、坐标轴标题、简易图例
图形标题与坐标轴标题：
In[14]: plt.plot(x, np.sin(x))
		plt.title("A Sine Curve")
		plt.xlabel("x")
		plt.ylabel("sin(x)");

图例：
In[15]: plt.plot(x, np.sin(x), '-g', label='sin(x)')
		plt.plot(x, np.cos(x), ':b', label='cos(x)')
		plt.axis('equal')
		plt.legend();

可以使用plt.legend()，但是在 plt.plot 函数中用 label 参数为每条线设置一个标签最简单

4.4　简易散点图：ply.plot(), plt.scatter()
plt.scatter 与 plt.plot 的主要差别在于，前者在创建散点图时具有更高的灵活性，可以
单独控制每个散点与数据匹配，也可以让每个散点具有不同的属性（大小、表面颜色、边
框颜色等）。

4.4.3 plot与scatter： 效率对比
plt.plot 与 plt.scatter 除了特征上的差异之外，还有什么影响我们选择的因素呢？在数
据量较小的时候，两者在效率上的差异不大。但是当数据变大到几千个散点时， plt.plot
的效率将大大高于 plt.scatter。这是由于 plt.scatter 会对每个散点进行单独的大小与颜
色的渲染，因此渲染器会消耗更多的资源。而在 plt.plot 中，散点基本都彼此复制，因此
整个数据集中所有点的颜色、尺寸只需要配置一次。由于这两种方法在处理大型数据集时
有很大的性能差异，因此面对大型数据集时， plt.plot 方法比 plt.scatter 方法好。


4.6　密度图与等高线图
在二维图上用等高线图或者彩色图来表示三维数据:
plt.contour 画等高线图
plt.contourf 画带有填充色的等高线图（ filled contour plot）的色彩
plt.imshow 显示图形
