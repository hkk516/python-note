1. python环境路径/变量设置：
在安装python或其他python IDE时，需要把"python 添加到环境路径"的选项选中，这样就可以正确安装其他模块/包，并且时程序运行正确

2. pycharm解释器选择：
需要选择pycharm的安装目录所在的解释器(自己的电脑的pycharm安装的D盘中，其解释器的路径为D:Python3.7.4\python.exe，
那么在project interpreter中就需要选择："python3.7 D:Python3.7.4\python.exe")
只有正确选择了解释器的路径，才能正确安装其他模块/包并且更新。

3.运行pycharm IDE时，需要下载python开发环境，需要到python官网下载相应的python版本，那么pycharm就会基于该版本来运行。

4.安装包的方法
(1)打开windows的DOS界面(cmd)：使用"pip install <packagename>"
(2)在pycharm中的file -> setting中的项目解释器中按加好安装
(3)在包的指定网站下载好和已经安装好的python解释器相匹配的版本的.whl(wheel)文件，然后将其安装到本机上。
如果安装的是python3.7版本的python解释器，那么就要选择下载"cp37"的.whl文件，python3.8就选择"cp38"的whl文件
需要先安装wheel包：pip install wheel
然后将下载好的.whl文件拷贝到python解释的安装目录的Scripts文件夹下，然后切换到该路径下安装.whl：pip install *.whl
(可以在系统终端中安装，也可以在pycharm IDE的终端中安装，使用的命令和操作步骤是相同的
在系统终端中安装的包会同步到pycharm IDE中)
(我们需要安装的python包一般通过pip工具下载，而pip的源地址是官方网址：pypi.python.org，网络协议：HTTPS。

但是我们在国内的某些站点下载速度特别慢！！！然后就会出现下载失败timeout的情况。出现这种情况有可能是网速慢或者是被限制了。)

所以我们选择使用果奶的镜像网站(非常重要)：
(5)pip install -i http://pypi.douban.com/simple --trusted-host pypi.douban.com <packagename>(最厉害的安装命令，速度超快)

一. 基本概念和注意点
编写python代码时，要充分利用python的特性编写（Python 风格”（ Pythonic） ）。


2.基本程序设计
2.1 Python中的变量是弱类型变量，Python会通过赋值给变量来自动判定数据类型

2.2 从控制台读取输入：
	var  = eval(input("Enter a value: "))	#eval函数来求值并将其转换成一个数值
	var  = int(input("Enter a value: "))	#int函数来求值并将其转换成一个整数值
   
2.3 在一行结尾使用反斜线(\)来继续在下一行输入
    sum = 1 + 2 + 3 \
          5 + 6

2.4 同时赋值
    var1, var2, ... ,varn = exp1, exp2, ..., expn
    
    #交换两个变量的值(利用python特性)
    x = 1
    y = 2
    x, y = y, x  
    
    
3.数字函数、字符串和对象
3.1 字符串和字符
    Python处理字符和字符串的方式是一样的。字符串必须被括在一对单引号或双引号里。Python没有字符数据类型
    一个字符的字符串代表一个字符。
    在Python中，为了和其他程序语言保持一致，应该使用双双引号来表示有多个字符的字符串，用单引号来表示
    只有一个字符的字符串。

3.2 不换行打印
    print(item, end = "anyendingstring")
    print("aaa", end = ' ')
    print("bbb", end = '')
    print("ccc", end = "***")
    
3.3 字符串连接操作(+, +=, 用jion()连接字符串效率更高)
    要想连接除了字符串数据类型的其他变量，需要使用str()将其转化为字符串
    
    
4.选择
4.1 布尔类型(bool: True, False)
    print(int(True))
    print(int(False))
    =>1
    =>0
    
    print(bool(4))
    print(bool(0))
    =>True
    =>False
   
4.2 产生随机数字
    import random
    randint(a, b): 产生一个a和b之间且包括a和b的随机整数
    randrange(a, b): 产生一个a和b-1之间且包括a和b的随机整数
    random(): 生成一个满足条件0<=r<=1.0的随机浮点数r
    

6.函数
6.1 return
    当函数不没有返回值时，可以使用
    return
    return None

    不管是否使用return，所有Python的函数都将返回一个值。如果某个函数没有返回值，默认情况下，
    它返回一个特殊值None。因此，无返回值函数不会返回值，它也被称作None函数。None函数可以赋值给一个变量来表明
    这个变量不指向任何对象。

6.2 位置参数和关键字参数  
    位置参数：传入的参数要和形参中的变量位置一一对应
    关键字参数：通过formal_name = value的形式传递每个参数，func(n = 5, messages = 'a')

6.3 通过传引用来传递参数
    当调用带参数的函数时，每个参数的引用值被传递给函数的参数(通过值传递)
    因为python中的所有数据都是对象， 所以对象的变量通常都是指向对象的引用
    如果实参是一个数字或者是一个字符串(不可变对象)，那么不管函数中的形参有无变化，这个实参是不受影响的
    如果实参是一个列表(可变对象)，那么函数中形参的变化会影响实参的变化
    
6.4 默认参数
    Python允许定义带默认参数值的函数。当函数调用时无参数，那么这些默认值就会被传递给实参。
    
6.5 返回多个值
    return var1, var2,...,varn

def f(x, y):
    return x + y, x - y, x * y, x / 
    
t1, t2, t3, t4 = f(9, 5)
print(t1, t2, t3, t4)


7.Python的内建类
Class               Description                         Immutable?          构造器（con）
bool        Boolean value                                   1
int         integer (arbitrary magnitude)                   1
float       floating-point number                           1
list        mutable sequence of objects                     0
tuple       immutable sequence of objects                   1
str         character string                                1
set         unordered set of distinct objects               0
frozenset   immutable form of set class                     1
dict        associative mapping (aka dictionary)            0     

每一个内建类的实例对象都包含值(value)，类型(class)和内存地址(id)等属性。

8. k for i in range(1, 10) 
9. 生成器yield和迭代器iter

10. 文件
10.1
文件的每一行以换行符结束
myfile.readlines(): 把整个文件按行为元素转化成列表，每个元素为字符串类型，每个元素后面附加换行符'\n'
myfile.readline(): 读取一行，附加换行符'\n'
myfile.read(): 一次性不换行读取整个文件
str.split()：把字符串按空格分隔开返回一个列表

10.2 当到达文件结尾时，readline()返回""
(1)以while语句一行一行地读取文件
line = infile.readline() # Read a line
while line != '':
	# Process the line here ...
	# Read next line
	line = infile.readline()
	
(2)以for循环一行一行地读取文件
for line in infile:
	# Process the line here ...
	
10.3 把源文件的内容读取到目标文件中，并记录文件的行数和字符数
import os.path
import sys

def main():
	# Prompt the user to enter filenames
	f1 = input("Enter a source file: ").strip()
	f2 = input("Enter a target file: ").strip()
	
	# Check if target file exists
	if os.path.isfile(f2):
		print(f2 + " already exists")
		sys.exit()
		
	# Open files for input and output
	infile = open(f1, "r")
	outfile = open(f2, "w")
	
	# Copy from input file to output file
	countLines = countChars = 0
	for line in infile:
		countLines += 1
		countChars += len(line)
		outfile.write(line)
	print(countLines, "lines and", countChars, "chars copied")
	
	infile.close() # Close the input file
	outfile.close() # Close the output file
	
	main() # Call the main function
	os.path.isfile(f2)

10.3 读写数字数据到文件末尾(append())
将数字写入到文件中，需要先使用str()将其转化为字符串。为了将数据准确地写入文件中，
建议用空格(" "或"\n")将每个数字分隔开。

from random import randint
def main():
	# Open file for writing data
	outfile = open("Numbers.txt", "w")
	for i in range(10):
		outfile.write(str(randint(0, 9)) + " ")
		
	# Close the file
	# Open file for reading data
	outfile.close()	
	infile = open("Numbers.txt", "r")
	s = infile.read()
	numbers = [eval(x) for x in s.split()]
	for number in numbers:
		print(number, end = " ")
		infile.close() # Close the file
		
	main() # Call the main function
	
10.4 计算文件中每个字母出现的次数
步骤：
(1)将文件一行一行的以字符串的形式读取
(2)使用字符串的lower()方法将每行的大写字母转化为小写字母(string.lower())
(3)创建一个具有26个int类型的名为counts的列表，每个元素初始化为0，以此累加每个字母出现的次数(counts = 26 * [0])
(4)判断字符串中每个字符，先判断其是否是字母，若是，则加1，若不是则跳过(ch.isalpha(), counts[ord(ch) - ord("a")] += 1
(5)最后，显示每个字母出现的次数



	

11 对序列使用+和*以及增量运算符+=和*=
(1)+= 背后的特殊方法是__iadd__（用于“就地加法”） 。 但是如果一个类
没有实现这个方法的话， Python 会退一步调用 __add__ 。 

>>> a += b

(2)如果 a 实现了 __iadd__ 方法， 就会调用这个方法。 同时对可变序列
（ 例如 list、 bytearray 和 array.array） 来说， a 会就地改动， 就
像调用了 a.extend(b) 一样。 但是如果 a 没有实现 __iadd__ 的话， a
+= b 这个表达式的效果就变得跟 a = a + b 一样了： 首先计算 a +
b， 得到一个新的对象， 然后赋值给 a。 也就是说， 在这个表达式中，
变量名会不会被关联到新的对象， 完全取决于这个类型有没有实现
__iadd__ 这个方法。

(3)总体来讲， 可变序列一般都实现了 __iadd__ 方法， 因此 += 是就地加
法。 而不可变序列根本就不支持这个操作， 对这个方法的实现也就无从
谈起。
上面所说的这些关于 += 的概念也适用于 *=， 不同的是， 后者相对应的
是 __imul__。

(4)对不可变序列进行重复拼接操作的话， 效率会很低， 因为每次都有一个
	新对象， 而解释器需要把原来对象中的元素先复制到新的对象里， 然后
再追加新的元素。
(str 是一个例外， 因为对字符串做 += 实在是太普遍了， 所以 CPython 对它做了优化。 为 str
初始化内存的时候， 程序会为它留出额外的可扩展空间， 因此进行增量操作的时候， 并不会涉
及复制原有字符串到新位置这类操作)


12 正则表达式
12.1 步骤
1．用 import re 导入正则表达式模块。
2．用 re.compile()函数创建一个 Regex 对象（记得使用原始字符串）。
3．向 Regex 对象的 search()方法传入想查找的字符串。它返回一个 Match 对象。
4．调用 Match 对象的 group()方法，返回实际匹配文本的字符串。

	import re
	phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
	mo = phoneNumRegex.search('My number is 415-555-4242.')
	print('Phone number found: ' + mo.group())
>>> Phone number found: 415-555-4242

12.2 用正则表达式匹配更多模式
1. 括号(())：分组(re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)'))
2. 管道(|)：匹配多个分组(re.compile (r'Batman|Tina Fey'))
3. 问号(?)：其前面的字符匹配零次或一次(re.compile(r'Bat(wo)?man'))
   星号(*)：其前面的字符匹配零次或多次(re.compile(r'Bat(wo)*man'))
   加号(+)：其前面的字符匹配一次或多次(re.compile(r'Bat(wo)+man'))
   点号(.)：通配字符，匹配除了换行之外的所有字符(只匹配一个字符)(re.compile(r'.at'))
   点-星(.*)：匹配所有字符串(匹配任意文本，它属于“贪心” 模式：它总是匹配尽可能多的文本)
			  (re.compile(r'First Name: (.*) Last Name: (.*)'))
   点-星和问号(.*?)：要使用“非贪心” 模式匹配所有文本， 就使用点-星和问号。像和大括号一起使用时那样， 问号告诉 Python 用非贪
心模式匹配
   点号字符匹配换行：点-星将匹配除换行外的所有字符。通过传入 re.DOTALL 作为 re.compile()的第
二个参数， 可以让句点字符匹配所有字符， 包括换行字符(re.compile('.*', re.DOTALL))
   花括号({})：其前面的字符匹配特定次数(re.compile(r'(Ha){3}'))
			   (Ha){n, m}(匹配n到m次)
			   (Ha){n, }(匹配n到更多次)
			   (Ha){, m}(匹配0到m次)
			   
12.3 贪心和非贪心匹配
“贪心” 模式：它总是匹配尽可能多的文本
“非贪心” 模式(?)：它总是匹配尽可能少的文本

12.4 findall()方法
myRegex = re.compile()：正则表达式	
myRegex.search()：需要匹配的文本
myRegex.group()：以分组的形式输出第一次匹配的文本
myRegex.findall()：不以分组的形式输出匹配所有的文本
sub()

	除了 search方法外，Regex对象也有一个 findall()方法。search()将返回一个 Match
对象， 包含被查找字符串中的“ 第一次” 匹配的文本，而 findall()方法将返回一组
字符串， 包含被查找字符串中的所有匹配。
	findall()不是返回一个 Match 对象， 而是返回一个字符串列表， 只要
在正则表达式中没有分组。列表中的每个字符串都是一段被查找的文本， 它匹配该
正则表达式。
>>> phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no groups
>>> phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
['415-555-9999', '212-555-0000']

	如果在正则表达式中有分组， 那么 findall 将返回元组的列表。每个元组表示一个找
到的匹配，其中的项就是正则表达式中每个分组的匹配字符串。为了看看 findall()的效果，
请在交互式环境中输入以下代码（ 请注意， 被编译的正则表达式现在有括号分组）：
>>> phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # has groups
>>> phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
[('415', '555', '1122'), ('212', '555', '0000')]

作为 findall()方法的返回结果的总结，请记住下面两点：
1． 如果调用在一个没有分组的正则表达式上， 例如\d\d\d-\d\d\d-\d\d\d\d， 方法
findall()将返回一个匹配字符串的列表， 例如['415-555-9999', '212-555-0000']。
2． 如果调用在一个有分组的正则表达式上， 例如(\d\d\d)-(\d\d\d)-(\d\d\d\d)， 方
法 findall()将返回一个字符串的元组的列表 （ 每个分组对应一个字符串），例如[('415',
'555', '1122'), ('212', '555', '0000')]。

12.5 字符分类
\d 		0 到 9的任何数字
\D 		除 0到 9的数字以外的任何字符
\w 		任何字母、数字或下划线字符（可以认为是匹配“单词”字符）
\W 		除字母、数字和下划线以外的任何字符
\s 		空格、制表符或换行符（可以认为是匹配“空白”字符）
\S 		除空格、制表符和换行符以外的任何字符

[0-5]	只匹配数字 0到 5
re.compile(r'\d+\s\w+')

12.6  建立自己的字符分类
1. 用方括号定义自己的字符分类：[aeiouAEIOU]将匹配所有元音字符，不论大小写(re.compile(r'[aeiouAEIOU]'))

2. 用短横表示字母或数字的范围：[a-zA-Z0-9]将匹配所有小写字母、大写字母和数字
(注意，在方括号内，普通的正则表达式符号不会被解释。这意味着，你不需
要前面加上倒斜杠转义.、 *、 ?或()字符。例如，字符分类将匹配数字 0 到 5 和一个
句点。你不需要将它写成[0-5\.])

3. 插入字符(^)：在字符分类的左方括号后加上一个插入字符（ ^）， 就可以得到“ 非字符类”。
非字符类将匹配不在这个字符类中的所有字符(re.compile(r'[^aeiouAEIOU]'))

12.7  插入字符和美元字符
1. 插入符号(^):	在正则表达式的开始处使用插入符号（ ^），表明匹配必须发生在被查找文
本开始处
re.compile(r'^Hello')：匹配以'Hello'开始的字符串

2. 美元符号($)：表示该字符串必须以这个正则表达式的模式结束
re.compile(r'\d$')：匹配以数字 0 到 9 结束的字符串

3. 同时使用^和$：表明整个字符串必须匹配该模式，也就是说，只匹配该字符串的某个子集是不够的
re.compile(r'^\d+$')：匹配从开始到结束都是数字的字符串

12.7 不区分大小写的匹配
	有时候你只关心匹配字母，不关心它们是大写或小写。要让正则表达式
不区分大小写，可以向 re.compile()传入 re.IGNORECASE 或 re.I，作为第二个参数
re.compile(r'robocop', re.I)

12.8 用 sub()方法替换字符串

12.9 管理复杂的正则表达式
	如果要匹配的文本模式很简单， 正则表达式就很好。但匹配复杂的文本模式，
可能需要长的、费解的正则表达式。你可以告诉 re.compile()， 忽略正则表达式字符
串中的空白符和注释， 从而缓解这一点。 要实现这种详细模式， 可以向 re.compile()
传入变量 re.VERBOSE， 作为第二个参数。

12.10 组合使用 re.IGNOREC ASE、 re.DOTALL 和 re.VERBOSE
	如果你希望在正则表达式中使用 re.VERBOSE 来编写注释，还希望使用
re.IGNORECASE 来忽略大小写，该怎么办？遗憾的是， re.compile()函数只接受一
个值作为它的第二参数。可以使用管道字符（ |）将变量组合起来，从而绕过这个限
制。管道字符在这里称为“按位或”操作符。
 re.compile('foo', re.IGNORECASE | re.DOTALL)
 re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)
 
12.11 正则表达式符号复习
 ?匹配零次或一次前面的分组。
 *匹配零次或多次前面的分组。
 +匹配一次或多次前面的分组。
 {n}匹配 n 次前面的分组。
 {n,}匹配 n 次或更多前面的分组。
 {,m}匹配零次到 m 次前面的分组。
 {n,m}匹配至少 n 次、至多 m 次前面的分组。
 {n,m}?或*?或+?对前面的分组进行非贪心匹配。
 ^spam 意味着字符串必须以 spam 开始。
 spam$意味着字符串必须以 spam 结束。
 .匹配所有字符，换行符除外。
 \d、 \w 和\s 分别匹配数字、单词和空格。
 \D、 \W 和\S 分别匹配出数字、单词和空格外的所有字符。
 [abc]匹配方括号内的任意字符（诸如 a、 b 或 c）。
 [^abc]匹配不在方括号内的任意字符。
 
12.12
()：分组作用
{}：重复作用
[]：创建自己的字符分类

二. 基于Python的算法(algorithms)
1.基本概念
1.1 数据结构(data structure):组织和访问数据的系统方法
1.2 数据算法(data algorithms): 在有限的时间内按步骤执行相关任务


3. Algorithm Analysis
3.1 一次简单的赋值操作：O(1)
    +, -, *, /
    
3.2 对一个列表一次性赋值n个值：o(n)
    a = [0]*n
    
3.2 pop()方法，删除第一个元素，然后把其余元素全部往左移n-1次：o(n-1)
    a.pop(0)
    
3.3 for循环n次：O(n)；for嵌套循环，外部循环n次，内部循环n次：O(n**2)
    for i in range(n):
        for j in range(n):
            body statements
            
3.3 对一个序列进行排序：O(nlogn)

	一些常见的大O运行时间：
	O(log n)：也叫对数时间，包括二分法查找等
	O(n)：也叫线性时间，包括简单查找(从头到尾一一查找)
	O(nlogn)：包括快速排序等
	O(n2)：选择排序等
	O(n!)：全排列算法(旅行商问题)
	
	注意：
	大O表示法指出了最糟糕情况下的运行时间
	算法的速度指的并非时间，而是操作数的增速
	谈论算法的速度时，我们说的是随着输入的增加，其运行时间将以什么样的速度增加
	各种算法的增速：
		O(log n) < O(n) < O(nlogn) < O(n2) < O(n!)
	
3.4 The Ceiling and Floor Functions
floor function(向下取整函数)：the largest integer less than or equal to x：1.6 - 1；2.1 - 2
ceiling function(向上取整函数)：the smallest integer greater than or equal to x：2.9 - 3；2,3 - 3

4. 递归(Recursion): 
函数自己调用自己
本质上是循环
例子：n！；分形图案(自己包含更小的自己)；
每一个递归都有一个base case(基线条件)和一个recursive base(递归条件)：
base case是防止递归无限循环，recursive base是函数自己调用自己
    n！的base case是参数0
    二分法查找的base case是最后一个mid数
    文件系统的base case是最后一个子目录

递归执行过程：
	When one invocation of the function make a recursive call, that invocation is suspended 
until the recursive call completes.
	When the execution of a function leads to a nested function call, the execution of the former 
call is suspended and its activation record stores the place in the source code at which the flow of 
control should continue upon return of the nested call. 

4.1 例子
4.1.1 The Factorial Function(n!)(阶乘函数)
def factorial(n):
	if n == 0:
		return 1
	else:
		return n factorial(n−1)
'''
执行过程：
函数执行过程：
f(5) -> f(4) -> f(3) -> f(2) -> f(1) -> f(0)
当f(5)调用f(4)时，f(5)被挂起，执行f(4);
当f(4)调用f(3)时，f(4)被挂起，执行f(3);
当f(3)调用f(2)时，f(3)被挂起，执行f(2);
当f(2)调用f(1)时，f(2)被挂起，执行f(1);
当f(1)调用f(0)时，f(1)被挂起，执行f(0);
当递归调用全部完成之后，函数执行过程将按原路返回，即：
f(0；1) -> f(1: 1*1) -> f(2: 2*1*1) -> f(3: 3*2*1*1) -> f(4: 4*3*2*1*1) 
-> f(5: 5*4*3*2*1*1) 
最终结果就是：120
'''

4.1.2 Binary Search
    对已经排好序的序列n进行指定值查找，查找时间为0(logn)
    mid = (low + high)/2;
    low = 0;
    high = n− 1
    
    consider three cases:
    • If the target equals data[mid], then we have found the item we are looking
    for, and the search terminates successfully.
    • If target < data[mid], then we recur on the first half of the sequence, that is,
    on the interval of indices from low to mid−1.
    • If target > data[mid], then we recur on the second half of the sequence, that
    is, on the interval of indices from mid + 1 to high.
    
 def binary_search(data, targetValue, low, mid, high):
    if low > high:
        return False
    
    else:
        mid = (low + high) // 2
        if targetValue == data[mid]:
            return True

        elif targetValue < data[mid]:
            return binary_search(data, targetValue, low, mid -1)

        elif targetValue > data[mid]:
            return binary_search(data, targetValue, mid + 1, high)
        else:
            return False

def main():
    data = [1, 3, 5, 6, 8, 9, 10, 21, 23, 43, 45]
    low = 0
    high = len(data) - 1
    targetValue = 21
    print("is " + str(targetValue) + "in" + "data? " + \
          binary_search(data, targetValue, low, high)

main()


4.2 递归分类
4.2.1 线性递归(Linear Recursion)求和：每次只调用一次递归
def linear_sum(S, n):
    if n == 0:
        return 0
    else:
        return linear_sum(S, n-1) + S[n-1]
		
def main():
    total = 0
    S = [1, 3, 5, 7, 8]
    n = len(S)
    print(linear_sum(S, n))
main()

'''
函数执行过程：
s(4) - s(3) - s(2) - s(1) - s(0)
s(0):s[0]
s(1):s[1] + s[0]
s(2):s[2] + s[1] + s[0]
s(3):s[3] + s[2] + s[1] + s[1]
s(4):s[4] + s[3] + s[2] + s[1] + s[0]
把最高阶(最大的数和最小的数单独拿出来，最小的数作为base-case，其余递归)
'''

4.2.2 Binary Recursion(双重递归)
a function makes two recursive calls
def binary sum(S, start, stop):
	if start >= stop: # zero elements in slice
		return 0
	elif start == stop−1: # one element in slice
		return S[start]
	else: # two or more elements in slice
		mid = (start + stop) // 2
		return binary sum(S, start, mid) + binary sum(S, mid, stop)

'''		
	The size of the range is divided in half at each recursive call, and
so the depth of the recursion is 1 + log2 n. Therefore, binary sum uses O(logn)
amount of additional space, which is a big improvement over the O(n) space used
by the linear sum function of Code Fragment 4.9. However, the running time of
binary sum is O(n), as there are 2n−1 function calls, each requiring constant time
'''

4.2.3 Multiple Recursion(多重递归)
	a function may make more than two recursive calls.

4.3 Designing Recursive Algorithms
In general, an algorithm that uses recursion typically has the following form:
• Test for base cases. We begin by testing for a set of base cases (there should
be at least one). These base cases should be defined so that every possible
chain of recursive calls will eventually reach a base case, and the handling of
each base case should not use recursion.
• Recur. If not a base case, we perform one or more recursive calls. This recursive step may involve a test that decides which of several possible recursive
calls to make. We should define each possible recursive call so that it makes
progress towards a base case.


#Parameterizing a Recursion(参数化一个递归，用参数表示一个递归)
	 If one has difficulty finding the repetitive structure needed
to design a recursive algorithm, it is sometimes useful to work out the problem on
a few concrete examples to see how the subproblems should be defined.


5. Array-Based Sequences
5.1 Python’s Sequence Types(list, tuple, and str classes)
	most notably: each supports indexing to access an individual element of a
sequence, using a syntax such as seq[k], and each uses a low-level concept known
as an array to represent the sequence.

6. Stacks(栈), Queues(对列), and Deques(双端对列)
    6.1 Stacks(last-in, first-out (LIFO), 后进先出)
        A stack is a collection of objects that are inserted and removed according to the
    last-in, first-out (LIFO) principle.
    例如：图书馆从下往上放书和取书

    6.2 Queues(first-in, first-out (FIFO), 先进先出)
        Another fundamental data structure is the queue. It is a close “cousin” of the stack,
    as a queue is a collection of objects that are inserted and removed according to the
    first-in, first-out (FIFO) principle.
    例如：排队情况
    
#queue(FIFO):先进先出
'''
className: Queue
datafield:
    queueFront = 0
    queueSize = 0
    queueData = []
methods:
    enQueue(e: int) #加入元素到队列的back
    deQueue(): int  #删除第一个（front）元素并返回该元素
    getQueueFirst():int #返回对列的第一个元素
    isEmpty(): bool #判断队列是否为空，为空返回False，非空返回True
    __str__(): str  #显示此时对列中元素
'''

class Queue:
    def __init__(self):
        self.__queueFront = 0
        self.__queueSize = 0
        self.__queueData = []
        
    def enQueue(self, e):
        self.__queueData.append(e)
    
    def deQueue(self):
        if self.isEmpty():
            return "Error: Queue is empty!"
        
        else:
            old = self.__queueData
            availFrontElement = self.__queueData[self.__queueFront]
            #self.__queueData[self.__queueFront] = None
            self.__queueFront = (self.__queueFront + 1) % len(self.__queueData)
            self.__queueData = old[self.__queueFront:]
            self.__queueFront = 0
            return "The front element is delet and it is: " + str(availFrontElement)
    
    def getQueueFirst(self):
        if self.isEmpty():
            return "Error: Queue is empty!"
        
        else:
            return "The first element of queue is: " + self.__queueData[self.__queueFront]
    
    def isEmpty(self):
            return len(self.__queueData) == 0
    
    def __str__(self):
        return "Queue elements is: " + str(self.__queueData)
    
def main():
    queue = Queue()
    queue.enQueue('a')
    queue.enQueue('b')
    queue.enQueue('c')
    print(queue.getQueueFirst())
    print(queue.__str__())
    print(queue.deQueue())
    print(queue.getQueueFirst())
    print(queue.__str__())
    queue.enQueue('d')
    queue.enQueue('e')
    queue.enQueue('f')
    print(queue.__str__())
    print(queue.deQueue())
    print(queue.__str__())
main()
=>
The first element of queue is: a
Queue elements is: ['a', 'b', 'c']
The front element is delet and it is: a
The first element of queue is: b
Queue elements is: ['b', 'c']
Queue elements is: ['b', 'c', 'd', 'e', 'f']
The front element is delet and it is: b
Queue elements is: ['c', 'd', 'e', 'f']

    6.3 Double-Ended Queues(insertion and deletion at both the front and the back of the queue)
        We next consider a queue-like data structure that supports insertion and deletion
    at both the front and the back of the queue. Such a structure is called a doubleended queue, or deque
    



7. Linked lists
7.1 Singly Linked Lists
    单链表由一个节点连接下一个节点形成一个线性序列。
    每个节点包括两个元素，前一个元素是对该节点中的元素的引用，后一个节点是对下一个节点的引用，
即指向下一个节点。
    单链表的第一个节点称为head，最后一个节点称为tail，并且最后一个节点的后一个元素引用None。
    #对链表节点的添加和删除，只需要改变节点中指针的指向即可，被删除的节点虽然还存在内存中，但是不管从哪里
    #都无法访问到该数据，所以也就没有特意删除它的必要了
	
	#链表和数组对比：
	(1)数组的元素紧密的排列在一大块内存中，为数组分配的内存是固定的。当添加的数据没有填满内存时，剩余的内存将浪费，
	当内存不足时，需要申请新的更大的内存空间，这样需要把数据移动到新的内存块中
	(2)链表的元素是分开的，其中每个元素都存储了下一个元素的地址
	(3)访问数组元素时，可以使用下标索引一次性任意访问元素；访问链表元素时，需要从链表开头遍历元素，直到遍历到指定元素为止
	(4)当在数组中插入和删除元素后，需要移动其他元素重新排布成紧密序列；链表的插入和删除可以在任意位置进行，且不需要重新排布序列
	(5)因此，数组的读取速度很快，而链表的插入和删除速度很快。
				数组          链表
		读取	O(1)		  O(n)
		插入	O(n)		  O(1)
		删除	O(n)		  O(1)
	
    
    例如下面的链表：
    blue -> green -> yellow -> blue
    
    (1)假设要在green和yellow中间添加一个数据为white，那么green的指针要指向该新的数据white的，且节点white
    的指针要指向yellow。
    
        green.next = white
        white.next = yellow
        
    (2)假设要删除数据yellow，那么只需把green的指针指向blue即可。
    
        green.next = blue
        
    (3)假设要在链表的头部(head)添加数据，则最新的数据newest的指针要指向当前head，当前head成为第二个数据节点，
    并且newest要成为head。
    
        newest.next = head  #最新的数据newest的指针要指向当前head，当前head成为第二个数据节点
        L.head = newest     #newest要成为head，即始终保持head节点为头节点
        
    (4)假设要删除链表的head，则head的下一个数据节点(即当前L.head.next所指向的数据节点)成为head。
    
        L.head = L.head.next
        
    (5)假设要向链表的尾部(tail)添加新的数据节点newest，则newest成为新的tail数据节点。因此链表的当前尾部数据
    节点指针要指向新的数据节点newest，使当前的尾部数据节点成为倒数第二个节点，同时newest成为最新的尾部数据，
    并且newest的指针指向None
	
        newest.next = None      # newest的指针指向None
        L.tail.next = newest    #链表的当前尾部数据节点指针要指向新的数据节点newest，使当前的尾部数据节点成为倒数第二个节点
        L.tail = newest         #newest成为最新的尾部数据
		
	(6)用单链表实现队列， pop head，push tail(加入的元素为第一个定义为head，删除了最后一个元素)
		#pop head：(队列中有0个，1个，2个)
		#if 0个
		if isEmpty()：
			return None
		#if 1个，先删除，再判断是否为空，如果删除后为空，那么定义最后self.__tail = None, 而不会同时定义self.__head = None
		answer = self.__head.element
		L.head = L.head.next(当删除后剩下一个元素后, L.head自动指向最后一个元素)
		self.__size -= 1
		if isEmpty():
			self.__tail = None	#这里的意思既是self.__tail = None, 也是self.__head = None
		return answer
			
		
		#push tail:	(队列中已经有0个，1个)
		#if 0个，那么第一个定义为head，而不会同时定义为tail
		newest = self.Node(element, None) #因为加入了数据始终是在tail，因此它指向的地址为None
		if isEmpty(): 
			self.__head = newest
		#不为空，则加入的元素定义为tail
		else：
			L.tail.next = newest    #链表的当前尾部数据节点指针要指向新的数据节点newest，使当前的尾部数据节点成为倒数第二个节点
			L.tail = newest 		#newest成为最新的尾部数据
		self.__size += 1
	
		
        
'''
7.1.1 Implementing a Stack with a Singly Linked List
class LinkedStack:
    class Node:
        data fields:
            __element:int
            __next: reference to next node
    data fields:
        __head: #creating a empty linked list
        __size: #count total node of linked list
    
    methods:
        push(element): #add a node with a value of e
        pop(): #remove and return the top of stack
        top(): #fetch a value of head node
        isEmpty(): #judge the node is empty
        __len__(): #return the length of the linked list
'''            

#第一种写法：嵌套类
class LinkedStack:
    '''-----------------------------Nested class: Node--------------------------------'''
    class Node:
        __slots__ = 'element', 'next'
    
        def __init__(self, element, nxt):
            self.element = element
            self.next = nxt    #self.next point next node, including element and next 
    
    '''----------------------------LinkedStack class---------------------------------'''
    def __init__(self):
        self.__head = None
        self.__size = 0
    
    def __len__(self):
        return self.__size
    
    def isEmpty(self):
        return self.__size == 0
    
    def push(self, element):
        #self.__head.__element = element, self.__head.__next = Node
        self.__head = self.Node(element, self.__head)
        self.__size += 1
    
    def top(self):
        if self.isEmpty():
            return "The stack is empty!"
        
        else:
            topValue = self.__head.element
            return "The top value of stack is:" + str(topValue)
    
    def pop(self):
        topValue = self.__head.element
        self.__head = self.__head.next    #删除head，则新的self.__head指向self.__head.__next当前指向的对象
        self.__size -= 1
        return "The top is remove and its value is: " + str(topValue)
		
	def printAllElement(self):
			if self.__head.next == None:
				return None
			else:
				probe = self.__head
				while probe.next != None:
					print(probe.element)
					probe = probe.next
				print(probe.element)
			
def main():
	linkedStack = LinkedStack()
	linkedStack.push('a')
	linkedStack.push('b')
	linkedStack.push('x')
	linkedStack.push('s')
	linkedStack.printAllElement()

main()
=>
s
x
b
a


#第二种写法，不嵌套类
#created a new node
class Node:
        #__slots__ = '__element', '__next', 使用__slots__节省内存
        def __init__(self, element, nxt):
            self.element = element    #given data
            self.next = nxt     #the next pointer of next point next node address

#create a single linked list            
class LinkedStack:
    def __init__(self):
        self.__head = None
        self.__size = 0
    
    def __len__(self):
        return self.__size
    
    def isEmpty(self):
        return self.__size == 0
    
    def push(self, element):
        newestnode = Node(element, self.__head)    #created a new node
        newestnode.__next = self.__head    #newestnode's __next reference point the current self.__head
        self.__head = newestnode    #update head to newestnode
        self.__size += 1
    
    def top(self):
        if self.isEmpty():
            return "The stack is empty!"
        
        else:
            topValue = self.__head.element
            return "The top value of stack is:" + str(topValue)
    
    def pop(self):
        topValue = self.__head.element
        self.__head = self.__head.next    #删除head，则新的self.__head指向当前self.__head.__next当前指向的对象
        self.__size -= 1
        return "The top is remove and its value is: " + str(topValue)
    
def main():
    linkedStack = LinkedStack()
    linkedStack.push('a')
    print(linkedStack.top())
    linkedStack.pop()
    linkedStack.top()

main()
=>
The top value of stack is:a
The stack is empty!


7.2 Circularly Linked Lists
7.2.1 Implementing a Queue with a Circularly Linked List
	(1)the queue has a head and a tail, but with the next reference of the tail linked to the head. 
	
		self.__tail.next = head
		
	(2)there is no need for us to explicitly store references to both the head and the tail; as long
	   as we keep a reference to the tail, we can always find the head by following the tail’s next reference.
	   
	   head = self.__tail.next
	   
	(3)two instance variables initialial:
	
		self.__tail = None
		self.__size = 0
		
	(4)When an operation involves the front of the queue, we recognize self.__tail.next as the head of the queue. 
	   When enqueue is called, a new node is placed just after the tail but before the current head, and then the new 
	   node becomes the tail.
	   
	(5)self.__tail = self.__tail.next to make the old head become the new tail (with the node after the old head becoming 
	   the new head).
		
		#make the old head become the new tail
		oldhead = self.__tail.next
		self.__tail = self.__tail.next
	
		#the node after the old head becoming the new head
		newhead = oldhead.next
		
		oldhead = self.__tail.next
		self.__tail.next = oldhead.next
		return oldhead.element
		
'''
#7.2.1 Implementing a Queue with a Circularly Linked List(注意时刻记住：logic实现)
#special methods:
    enqueu():   #adding element onto qeue tail
        #if queue is empty, 那么该新的节点既是tail也是head，在循环链表中，即是自己指向自己，
            #而不是指向None
            #self.__tail.element = element
            #self.__tail.next = None
            newest.next = newest
        
        #if queue is not empty, so 新的节点成为新的tail，旧的尾部成为新的head
        #当前tail成为倒数第二个节点，它的next指向新的节点，新的节点的next指向head，而当前head由
        #当前的tail的next指向，同时更新当前tail为新的tail
        #以下三条语句顺序不能换
            newest.next = self.__tail.next    #首先新的节点next只指向head(即self.__tail.next )
            self.__tail.next = newest         #而后当前tail的next指向新的节点，使当前tail成为倒数第二节点
            self.__tail = newest              #最后更新tail为新的节点
        
    dequeue(): #删除head
        #1.如果队列为空：
            #返回描述队列空的字符串
            
        #2. 如果对列只有一个元素，删除之后队列为空，那么此时
            self.__tail = None
            
        #3. 如果队列有两个及以上个元素，删除head之后，head的next指向的节点成为新的head，
        #tail的next指向该新的head，即tail的next指向当前head的next指向的节点。定义一个临时
        #变量oldhead表示当前head
                oldhead = self.__tail.next
                self.__tail.next == oldhead.next
                #self.__tail.next = self__tail.next.next #这种写法错误
'''
    
class CircularlyLinkedQueue:
    '''-----------------------------Nested class: Node--------------------------------'''
    class Node:
        __slots__ = 'element', 'next'
    
        def __init__(self, element, nxt):
            self.element = element
            self.next = nxt    #self.next point next node, including element and next 
    
    '''----------------------------LinkedStack class---------------------------------'''
    def __init__(self):
        self.__head = None
        self.__size = 0
    
    def __len__(self):
        return self.__size
    
    def isEmpty(self):
        return self.__size == 0
    
    def enqueu(self, element):
        newest = self.Node(element, None)
        
        if self.isEmpty():
            newest.next = newest
            
        else:
            newest.next = self.__tail.next    
            self.__tail.next = newest         
        self.__tail = newest                #update tail every added a element
        self.__size += 1
        
    def dequeu(self):
        if self.isEmpty():
            return "The queue is empty!"
        
        oldhead = self.__tail.next
        if self.__size == 1:
            self.__tail = None
        
        else:
            self.__tail.next = oldhead.next
        self.__size -= 1
        return "The front element has been delete and it's " + oldhead.element
          
    def first(self):
        if self.isEmpty():
            return "The queue is empty!"
        
        else:
            head = self.__tail.next
            return "The front element of the queue is " + head.element
    
    def last(self):
        if self.isEmpty():
            return "The queue is empty!"
        
        else:
            return "The last element of the queue is " + self.__tail.element
        
    def printAllElement(self):
        for i in range(self.__size):
            oldhead = self.__tail.next
            print(str(i) + ":"  + oldhead.element)
            self.__tail.next = oldhead.next
        
def main():
    circularlyLinkedQueue = CircularlyLinkedQueue()
    circularlyLinkedQueue.enqueu('a')
    circularlyLinkedQueue.enqueu('b')
    circularlyLinkedQueue.enqueu('c')
    circularlyLinkedQueue.enqueu('d')
    print(circularlyLinkedQueue.dequeu())
    print(circularlyLinkedQueue.first())
    circularlyLinkedQueue.enqueu('e')
    print(circularlyLinkedQueue.last())
    circularlyLinkedQueue.printAllElement()

main()
=>
The front element has been delete and it's a
The front element of the queue is b
The last element of the queue is e
0:b
1:c
2:d
3:e


7.3 Doubly Linked Lists
	(1)单链表是一种不太对称的链表，使得它在插入和删除一个结点时，尤其是空链表时，不太方便。
	(2)为了链表更加的对称，可以使用双端链表：每一个节点都有一个引用(next)指向它之后的节点以及一个引用指向它之前(prev)的节点。
	   (each node keeps an explicit reference to the node before it and a reference to the node after it)
	 
	(3)Header and Trailer Sentinels(标记)
	   1. In order to avoid some special cases when operating near the boundaries of a doubly
         linked list, it helps to add special nodes at both ends of the list: 
			a header node at the beginning of the list；
			a trailer node at the end of the list. 
	     These “dummy” nodesare known as sentinels (or guards), and they do not store elements of the primary equence. 
	   
	   2. an empty list is initialized： 
			#the next field of the header points to the trailer；
			
				header.next = trailer
				
			#the prev field of the trailer points to the header;
			
				trailer.prev = header
				
			#the remaining fields of the sentinels are irrelevant (presumably None, in Python)
				header.prev = None
				trailer.next = None
				
		3. Advantage of Using Sentinels
			Most notably, the header and trailer nodes never change—only the nodes between them change. Furthermore,
		we can treat all insertions in a unified manner, because a new node will always be
		placed between a pair of existing nodes. In similar fashion, every element that is to
		be deleted is guaranteed to be stored in a node that has neighbors on each side.
			However, its implementation required a conditional to manage the special
		case of inserting into an empty list. In the general case, the new node was linked
		after the existing tail. But when adding to an empty list, there is no existing tail;
		instead it is necessary to reassign self. head to reference the new node. The use of
		a sentinel node in that implementation would eliminate the special case, as there
		would always be an existing node (possibly the header) before a new node.
		
		
'''
7.3.1 Basic Implementation of a Doubly Linked List
class Node:
    data fields:
        __slots__ = 'element', 'next', 'prev'

class DoublyLinkedListBase:
    data fields:
        __header:
        __tailer:
        __size:
    
    methods:
        isEmpty():str
        __len__():int
        insert_between(e: data, predecessor: node, successor: node):
        delete_node(node: node):node.element
'''     

class DoublyLinkedListBase:
    class Node:
        __slots__ = 'element', 'next', 'prev'
        
        def __init__(self, element, nxt, prev):
            self.element = element
            self.next = nxt
            self.prev = prev
    
    def __init__(self):
        self.header = self.Node(None, None, None)    # initialize header and tailer sentinal
        self.tailer = self.Node(None, None, None)    
        self.header.next = self.tailer             # header and tailer reference to each other 
        self.tailer.prev = self.header             # when the doubly linked list is empty
        self.size = 0
        
    def __len__(self):
        return self.size
    
    def isEmpty(self):
        return self.size == 0
    
    def insert_between(self, element, predecessor, successor):
        newest = self.Node(element, predecessor, successor)
        predecessor.next = newest
        successor.prev = newest
        #newest.prev = predecessor    # 这两行不用写，再声明newest的时候已经被赋值了
        #newest.next = successor      # newest = self.Node(element, predecessor, successor)
        self.size += 1
        return "the newest node has been insert and it's " + str(newest.element)
    
    def delete_node(self, node):
        predecessor = node.prev        # 指定node的predecessor
        successor = node.next          # 指定node的sucessor
        predecessor.next = successor   # 删除node
        successor.prev = predecessor
        self.size -= 1
        nodeVaule = node.element
        node.element = node.next = node.prev = None
        return "The node has been delete and it's " + str(nodeVaule)
		
'''
7.3.2 Implementing a Deque with a Doubly Linked List
栈和队列的链表实现大体相同(LinkedStack和LinkedQueue)，都使用了一个单链表Node类来实现节点。
'''
class LinkedQueue:
    '''-----------------------------Nested class: Node--------------------------------'''
    class Node:
        __slots__ = 'element', 'next'
    
        def __init__(self, element, nxt):
            self.element = element
            self.next = nxt    #self.next point next node, including element and next 
    
    '''----------------------------LinkedStack class---------------------------------'''
    def __init__(self):
        self.__front = None  # point the first node
		self.__rear = None   # point the last node
        self.__size = 0
    
    def __len__(self):
        return self.__size
    
    def isEmpty(self):
        return self.__size == 0
    
    def add(self, element):
		#新的元素加到队列的末尾
		#newNode.element = element; newNode.next = None
		newNode = self.Node(element, None) #create new node instance storing reference to element;set new node’s next to reference None
		if self.isEmpty():
			self.__front = newNode         #set variable self.__front to reference the new node
		else：
			self.__rear.next = newNode     #make old rear node point to new node
		self.__rear = newNode              #set variable tail to reference the new node; self.__rear.element = element; self.__rear.next = newNode
		self.size += 1                     #increment the node count
    
    def pop(self):
		#删除头结点并返回该节点中保存的数据
        topValue = self.__front.element
        self.__front = self.__front.next    #删除head，则新的self.__head指向当前self.__head.__next当前指向的对象
		if self.__front is None:
			self.__rear = None
        self.__size -= 1
        return topValue
		
	def printAllElement(self):
        if self.isEmpty():
			return "The LinkedQueue is empty!"
		else:
			probe = self.__front
			while probe.next != None:
				print(probe.element)
				probe = probe.next
			print(probe.element)

def main():
    linkedQueue = LinkedQueue()
    linkedQueue.add('a')
	linkedQueue.add('b')
	linkedQueue.add('c')
	linkedQueue.add('d')
    linkedQueue.printAllElement()

main()
        
'''
7.3.2 Implementing a Deque with a Doubly Linked List
class LinkedDequeue(DoublyLinkedListBase):
    methods:
        first():str, printing the front element of the dequeu
        last():str, printing the back element of the dequeu
        insert_first(element:data, header:node, successor:node):str
        insert_last(element:data, predecessor:node, tailer:node):str
        delete_first():str
        delete_last():str
        printAllElement():str
            value = self.__header.next.element
            tempheader = self.__header.next
            self.__header.next = tempheader.next
'''

class LinkedDequeue(DoublyLinkedListBase):
    def __init__(self):
        super().__init__()
    
    def first(self):
        #首先，header已经确定，还要自己指定第一个结点的successor
        #header.next指向的就是第一个结点
        #首先判断队列是否为空
        if self.isEmpty():
            return "Sorry, the dequeue is empty!"
        
        else:
            firstNode = self.header.next
            return "The first element of the dequeue is " + str(firstNode.element)
            #or: return self.header.next.element
    
    def last(self):
        #首先，tailer已经确定，还要自己指定第一个结点的predecessor
        #tailer.prev指向的就是最后一个结点
        #首先判断队列是否为空
        if self.isEmpty():
            return "Sorry, the dequeue is empty!"
        
        else:
            lastNode = self.tailer.prev
            return "The last element of the dequeue is " + str(lastNode.element)
            #or: return self.tailer.prev.element
            
    def insert_first(self, element):
        if self.isEmpty():
            self.insert_between(element, self.header, self.tailer)       #use inherted methods
        else:
            self.insert_between(element, self.header, self.header.next)
    
    def insert_last(self, element):
        if self.isEmpty():
            self.insert_between(element, self.header, self.tailer)
        else:    
            self.insert_between(element, self.tailer.prev, self.tailer)
        
    def delete_first(self):
        if self.isEmpty():
            return "Sorry, the dequeue is empty!"
        else:
            self.delete_node(self.header.next)        #use inherted methods
    
    def delete_last(self):
        if self.isEmpty():
            return "Sorry, the dequeue is empty!"
        else:
            self.delete_node(self.tailer.prev)       
    
    def printAllElement(self):
        for i in range(self.size):
            value = self.header.next.element
            tempheader = self.header.next
            self.header.next = tempheader.next
            print(str(i) + ':' + str(value))

def main():
    linkedDequeue = LinkedDequeue()
    print(linkedDequeue.first())
    linkedDequeue.insert_first('a')
    linkedDequeue.insert_first('b')
    linkedDequeue.insert_last('c')
    linkedDequeue.insert_last('d')
    print(linkedDequeue.first())
    print(linkedDequeue.last())
    linkedDequeue.insert_first('e')
    linkedDequeue.insert_last('f')
    print(linkedDequeue.first())
    print(linkedDequeue.last())
    #print(linkedDequeue.delete_first())
    #print(linkedDequeue.first())
    #linkedDequeue.printAllElement()

main()
=>
Sorry, the dequeue is empty!
The first element of the dequeue is b
The last element of the dequeue is d
The first element of the dequeue is e
The last element of the dequeue is f    


def merge(S1, S2, S):
	i = j = 0
	while i + j < len(S):
		if j == len(S2) or (i < len(S1) and S1[i] < S2[j]):
			S[i+j] = S1[i] # copy ith element of S1 as next item of S
			i += 1
		else:
			S[i+j] = S2[j] # copy jth element of S2 as next item of S
			j += 1

def merge_sort(S):
	n = len(S)
	if n < 2:
		return # list is already sorted
		
	# divide
	mid = n // 2
	S1 = S[0:mid] # copy of first half
	S2 = S[mid:n] # copy of second half
	
	# conquer (with recursion)
	merge_sort(S1) # sort copy of first half
	merge_sort(S2) # sort copy of second half
	
	# merge results
	merge(S1, S2, S)
	
def main():
    S = [2, 1, 6, 7, 10, 21, 4, 8]
    merge_sort(S)   
    print(S)
	
main()
=>
[1, 2, 4, 6, 7, 8, 10, 21]

node with thick lines：          current call
empty nodes with thin lines：    completed calls.
remaining nodes with thin lines: calls that are waiting for a child invocation to return. 


S = [1, 3, 5, 7, 8]
n = len(S) - 1
def sum_S(n):
	# base-case
    if n == 0:
        return 0
	
    return S[0] + sum_S(n-1)

s(5) - s(4) - s(3) - s(2) - s(1) - s(0)
s(0: 0) - s(1: 0+1) - s(2：0+1+3) - s(3： )




















       
    
            