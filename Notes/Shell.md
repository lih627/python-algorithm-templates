# 计算机教育中缺失的一课: Shell

[toc]

# 简介

最近打算刷完MIT 的[The Missing Semester of Your CS Education](https://missing.csail.mit.edu/), 通常 Computing Ecosystem Literacy 相关的知识都是交给 CS 系的学生自己去学习, 因此这门课的目的是教给学生如何实用工具. 我会按照每个章节记录一下相关的内容.

# 基础

Shell 通过最基本的文字接口让我们充分使用计算机的各项功能. 这门课程使用 **Bourne Again SHell(bash)**, 首先打开终端尝试以下命令

```shell
➜  ~ date
2020年 7月 9日 星期四 16时30分49秒 CST
➜  ~ echo hello
hello
➜  ~ echo Hello World
Hello World
```
`空格`在 Shell 中极其重要, 它通过空格分隔参数, 例如想要访问文件夹`My Photos`, 需要使用转义字符, 因此产生单引号和双引号, 其区别在于, 单引号中所有字符为字面值(不进行转义), 双引号中的`$` (参数替换) 进行转义操作, 例如:

```shell
➜  Downloads mkdir "My Photos"
➜  Downloads cd My Photos
cd: string not in pwd: My
➜  Downloads cd My\ Photos
➜  My Photos cd ..
➜  Downloads cd "My Photos"
➜  My Photos ..
➜  Downloads cd 'My Photos'
➜  My Photos cd ..
➜  Downloads foo=bar
➜  Downloads echo "$foo"
bar
➜  Downloads echo '$foo'
$foo
➜  Downloads echo $foo  
bar
```



# 环境变量

Shell 通过环境变量寻找`data`和`echo`, 环境变量为`$PATH`, 可以采用`which` 判断某条指令所在的路径

```shell
➜  Downloads echo $PATH
/Users/lihao/anaconda3/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Library/TeX/texbin:/usr/local/share/dotnet:/opt/X11/bin:~/.dotnet/tools
➜  Downloads which python
/Users/lihao/anaconda3/bin/python
```

# 流和管道

`>` 和 `<` 分表表示输出流和输入流的操作, 此外`>>`表示追加输出, `|`表示管道操作, 他会将两个不相关的程序联系起来, 前者的输出作为后者的输入. 例如:

```shell
➜  Downloads echo hello > hello.txt
➜  Downloads cat hello.txt 
hello
➜  Downloads cat < hello.txt 
hello
➜  Downloads cat < hello.txt > hello2.txt
➜  Downloads cat hello2.txt 
hello
➜  Downloads cat hello.txt >> hello2.txt 
➜  Downloads cat hello2.txt 
hello
hello
➜  Downloads ls -l / | tail -n1
lrwxr-xr-x@  1 root  admin    11 10  8  2019 var -> private/var
```
注意最后一条, `ls` 显示根目录`/`下的内容, 然后教给`tail -n1` 输出内容的最后一条.

# 权限

对于某些操作需要采用`sudo`, 赋予超级用户(super user) 或者(root) 权限, 在管道操作时, 由于各个操作分隔开来, 可能需要多条 sudo, 例如:
```shell
➜  Downloads sudo ls -l / | sudo tail -n2
drwxr-xr-x@  11 root  wheel   352 10  8  2019 usr
lrwxr-xr-x@   1 root  admin    11 10  8  2019 var -> private/var
```

# Shell Scripting

脚本可以通过如下方式编写:

```shell
➜  Downloads cat mcd.sh 
mcd () {
    mkdir -p "$1"
    cd "$1"
}
➜  Downloads source mcd.sh 
➜  Downloads mcd test 
➜  test cd ..
# mkdir test , cd test  
```
`$` 后面可以跟一些特殊的参数, 例如

1. `$0` 表示脚本的名字, 例如在本例中, 为`mcd`
2. `$1` 到 `$9` 表示, `$1` 表示输入的第一个变量, 在本例中为`test`
3. `$@` 表示所有变量
4. `$#` 变量的数目
5. `$?` 上一条变量的返回值, 一般成功运行返回为`0`
6. `$$` 当前脚本的进程号[Process identification number(PID)](https://en.wikipedia.org/wiki/Process_identifier)
7. `!!` 返回上一条完整命令, 通常用于没有超级用户权限的时候, 可以通过 `sudo !!` 实现
8. `$_` 返回上一条命令的最后一个变量, 等用于快捷键`Esc` + `.`

可以看下面这个例子:

```shell
➜  Downloads cat showall.sh 
showall () {
    echo $@
    echo $#
    echo $?
    echo $$
    echo $_
}
➜  Downloads source showall.sh 
➜  Downloads showall a b c d e
a b c d e
5
0
76058
76058
➜  Downloads cat showall.sh 
showall () {
    echo $@
    echo $#
    echo $?
    echo $$
    echo $_
}
➜  Downloads echo $_
showall.sh
```



脚本支持短路运算符如下面的例子,注意`fals` 返回值为`1`, `true` 返回值为`0`


```shell
false || echo "Oops, fail"
# Oops, fail

true || echo "Will not be printed"
#

true && echo "Things went well"
# Things went well

false && echo "Will not be printed"
#

true ; echo "This will always run"
# This will always run

false ; echo "This will always run"
# This will always run
```

同时可以将一个命令运行结果赋值给一个变量, 其使用方式为`Var=$(CMD)`, 同时还有一个比较冷门的用法 [进程替代(Process Substitution)](https://www.zmonster.me/2015/01/03/process-substitution.html), 他讲程序的输出看做一个文件. 例如`diff file1 file2` 可以比较两个文件的差异, 因此可采用`diff <(ls) <(ls ..)` 方法比较两个目录内文件的不同.

```shell
➜  Downloads var=$(pwd)
➜  Downloads echo $var                  
/Users/lihao/Downloads
➜  Downloads echo "We are in $(pwd)"
We are in /Users/lihao/Downloads
```

下面是一个综合的例子, 注释写在了程序里面:

```shell
#!/bin/bash
# $(date) 显示当前日期
echo "Starting program at $(date)" # Date will be substituted
# $0 脚本名字 $# 参数个数 $$ PID
echo "Running program $0 with $# arguments with pid $$"

# $@ 所有变量
for file in "$@"; do
    grep foobar "$file" > /dev/null 2> /dev/null
    # 输出重定向 1> 正常输出 2> 错误输出
    # 重定向到 /dev/null 一个特殊的区域, 使其不显示任何输出
    # When pattern is not found, grep has exit status 1
    # We redirect STDOUT and STDERR to a null register since we do not care about them
    # [[ $? -ne 0 ]] $? grep的退出码
    # [[ xx -ne xx ]] 表示的是 linux test 的用法, -ne 表示不等于
    # 如果退出码不为 0, 输出未搜索到 foobar
    if [[ $? -ne 0 ]]; then
        echo "File $file does not have any foobar, adding one"
        echo "# foobar" >> "$file"
    fi
done
```
该脚本运行时候，首先像是当前的日期的 PID，然后依次在输入变量对应文件中查询`foobar`, 注意`grep`的标准和错误输出重定向到磁盘上的一个特殊区域`/dev/null`. 然后用过`$?`判断`grep` 执行结束后的状态码, 如果没有搜索到,状态码非 0,通过`[[ $? -ne 0 ]]`(test 模块的一种写法)来判断状态码是否为 0. 进而进行下一步的操作.

可以使用[shellchek](https://github.com/koalaman/shellcheck)工具对脚本做检查, 其基本用法为

```shell
shellcheck script.sh
```



# Shell Globbing

类似正则表达式:
- Wildcards通配符,  使用`?`匹配一个或者`*`任意多个字符串
- Curly braces`{}`, 当一个指令包含多个公共子串时 可以使用花括号自动展开

例子如下:

```shell
convert image.{png,jpg}
# Will expand to
convert image.png image.jpg

cp /path/to/project/{foo,bar,baz}.sh /newpath
# Will expand to
cp /path/to/project/foo.sh /path/to/project/bar.sh /path/to/project/baz.sh /newpath

# Globbing techniques can also be combined
mv *{.py,.sh} folder
# Will move all *.py and *.sh files


mkdir foo bar
# This creates files foo/a, foo/b, ... foo/h, bar/a, bar/b, ... bar/h
# {a..h} 展开为 a, b, c, d, e, f, h
touch {foo,bar}/{a..h}
touch foo/x bar/y
# Show differences between files in foo and bar
diff <(ls foo) <(ls bar)
# Outputs
# < x
# ---
# > y
```

# Shebang

Shebang 的解释[Wiki: shebang](https://en.wikipedia.org/wiki/Shebang_(Unix))

Script 的第一行`#!/usr/bin/bash` 为 Unxi shebang, 因此可以修改它指定终端运行 Python 脚本:

```shell
#!/usr/local/bin/python
import sys
for arg in reversed(sys.argv[1:]):
    print(arg)
```
此时 shell 使用 Python 解释器而不是 shell命令来运行. 但是由于`python`在不同机器上的路径可能不同, 有一个更为通用的 shebang写法为
```shell
#!/usr/bin/env python
```
`env`利用`PATH`环境变量来进行定位. 执行的时候可以通过 python 和 shell 来执行(shell 直到使用 pyhton 解释器)

```shell
python script.py a b c
# 下面是直接运行
./script.py a b c
```

# Shell Script vs Function

脚本和函数不同点总结如下:

- 函数只能用与 shell 使用相同的语言，脚本可以使用任意语言。因此在脚本中包含 shebang 是很重要的。
- 函数仅在定义时被加载，脚本会在每次被执行时加载。这让函数的加载比脚本略快一些，但每次修改函数定义，都要重新加载一次。
- 函数会在当前的 `shell` 环境中执行，脚本会在单独的进程中执行。因此，函数可以对环境变量进行更改，比如改变当前工作目录，脚本则不行。脚本需要使用 `export` 将环境变量导出，并将值传递给环境变量。
- 与其他程序语言一样，函数可以提高代码模块性、代码复用性并创建清晰性的结构。shell 脚本中往往也会包含它们自己的函数定义。


# Shell Tools

## 寻找如何使用命令

一般可用过 `cmd -h` , `cmd --help` 或者`man cmd` 来获取帮助. `man`(mannual)命令手册的缩写, 如果使用第三方命令, 如果开发者编写了说侧, 一般可以通过键入`:help` 或者`?`获得帮助.

此外可以通过[`TLDR pages`](https://tldr.sh/) 快速获得帮助. macOS可以通过

```shell
brew install tldr
```

来安装这个工具包, 使用方法为`tldr cmd` 如下 

```shell
➜  ~ tldr ls

ls

List directory contents.

- List files one per line:
    ls -1

- List all files, including hidden files:
    ls -a

- List all files, with trailing `/` added to directory names:
    ls -F

- Long format list (permissions, ownership, size and modification date) of all files:
    ls -la

- Long format list with size displayed using human readable units (KB, MB, GB):
    ls -lh

- Long format list sorted by size (descending):
    ls -lS

- Long format list of all files, sorted by modification date (oldest first):
    ls -ltr
```

## 查找命令

### find (查找文件)

`find` 可以用于查找文件, 它包含很多有用的参数选项,
例如
`-name src`, 
`-type d` (路径)
`-type f` (file)
`-mtime -l` modified time 是昨天
`-iname src` 忽略大小写

`find` 在还可以结合指令使用,  一些常用命令总结如下:
```shell
# 查找所有名称为src的文件夹
find . -name src -type d
# 查找所有文件夹路径中包含test的python文件
find . -path '**/test/**/*.py' -type f
# 查找前一天修改的所有文件
find . -mtime -1
# 查找所有大小在500k至10M的tar.gz文件
find . -size +500k -size -10M -name '*.tar.gz'
# 删除所有tmp 拓展的文件
find . -name '*.tmp' -exec rm {} \;
```
### locate (通过名称查找文件)

`locate` 只能通过名称来进行搜索

> locate 命令可以在搜寻数据库时快速找到档案，locate 为模糊查找，数据库由 updatedb 程序来更新，updatedb 是由 cron daemon 周期性建立的，locate 命令在搜寻数据库时比由整个由硬盘资料来搜寻资料来得快，但较差劲的是 locate 所找到的档案若是最近才建立或 刚更名的，可能会找不到，在内定值中，updatedb 每天会跑一次，可以由修改 crontab 来更新设定值。(etc/crontab)

>unix 或 linux 下使用 locate 指令在其数据库中查询文件要比 find 更快更高效, 据 Linux 使用经验，使用 updatedb 命令可以更新 locate 命令的数据库, 而在 mac os X 下却找不到 updatedb 这个程序.
> 使用 man locate 查看，得知 locate 数据库位置在：
> `/var/db/locate.datebase`
> 而所谓的 updatedb 程序在：
> `/usr/libexec/locate.updatedb`
> 知道了位置直接调用就可以了。

使用方法例如:

```shell
➜  ~ locate word_1.jpg
/Users/xxxxxxx/dataset/word_1.jpg
```

### grep 和 Ripgrep(rg) 查找内容

有的时候不仅仅需要查找到文件, 也关心文件中的内容, 在文件中查找可以使用 `grep`, 例子如下:

```shell
grep foobar mcd.sh
# 返回包含 foobar 的那一行
```

也可以以递归查找某个文件夹下面的所有文件, 例如:

```shell
grep -R foobar .
# 查看当前文件中所有文件中包含 foobar 的文件
```

> Ripgrep 是命令行下一个基于行的搜索工具，RipGrep 使用 Rust 开发，可以在多平台下运行，支持 Mac、Linux 和 Windows 等平台。RipGrep 与 The Silver Searcher、Ack 和 GNU Grep 的功能类似。RipGrep 官方号称比其它类似工具在搜索速度上快上 N 倍，VSCode 也从 1.11 版本开始默认将 RipGrep 做为其搜索工具，由此其功能强大可见一斑。

对于 MacOS,首先需要安装`rg`,

```shell
brew install ripgrep
```

例如, 查找某个文件夹内 py 文件使用`requests`库的代码

```shell
➜  ~ rg "import requests" -t py ~/Code/spider 
/Users/lihao/Code/spider/Spider.py
# 显示上下10行
➜  ~ rg "import requests" -t py  -C 10 ~/Code/spider
/Users/lihao/Code/spider/Spider.py
1-from bs4 import BeautifulSoup
2:import requests
3-from selenium import webdriver
4-import os
5-import time
6-import urllib.parse
7-from datetime import datetime
8-
9-# disable SSL warnings
10-requests.packages.urllib3.disable_warnings()
11-
12-
# --stats 显示查找过程中的统计信息
➜  ~ rg "import requests" -t py  -C 3 --stats ~/Code/spider
/Users/lihao/Code/spider/Spider.py
1-from bs4 import BeautifulSoup
2:import requests
3-from selenium import webdriver
4-import os
5-import time

1 matches
1 matched lines
1 files contained matches
1 files searched
144 bytes printed
8877 bytes searched
0.000096 seconds spent searching
0.004793 seconds
```
找到当前文件夹内所有`c++`文件, 其中内容不以`#include`开头

```shell
➜  Downloads rg -u --files-without-match "^#include" -t cpp 
solution.cpp
build-sample-project-Desktop_Qt_5_14_1_clang_64bit-Debug/moc_predefs.h
sample-project/lib/StanfordCPPLib/private/randompatch.h
sample-project/lib/StanfordCPPLib/util/bigfloat.h
sample-project/lib/StanfordCPPLib/private/static.h
CS106B/Assignment 0/lib/StanfordCPPLib/util/bigfloat.h
CS106B/Assignment 0/lib/StanfordCPPLib/private/randompatch.h
CS106B/Assignment 0/lib/StanfordCPPLib/private/static.h
```

### 查找使用过的命令

一个简单的做法是使用向上的箭头. 此外 `history` 可以显示之前输入的命令. 例如

```shell
# 显示所有包含 find 的历史命令
hsitory | grep find
```
**backword search**, 在前命令行之前使用`Ctrl+R` 然后就可以匹配输入的历史命令了, 还可以结结合`fuzzy finder(fzf)`模糊搜索神奇, 来提高`Ctrl+R`效率. [fuzzy finder介绍](https://justcode.ikeepstudying.com/2018/03/shell%E8%84%9A%E6%9C%AC%EF%BC%9A%E6%A8%A1%E7%B3%8A%E6%90%9C%E7%B4%A2%E7%A5%9E%E5%99%A8fzf-bash%E7%A5%9E%E5%99%A8-fzf%E7%94%A8%E6%B3%95-fzf%E8%AF%A6%E8%A7%A3/)

MacOS 通过以下命令安装:
```shell
brew install fzf
```
然后在`~/.zshrc` 里面加入这一行, 就可以愉快的用`Ctrl+R`来对历史命令模糊搜索.

```shell
# fzf
[ -f ~/.fzf.zsh ] && source ~/.fzf.zsh
```

同时`zsh`支持历史命令不全和语法高亮, 对应的工具包为`zsh-autosuggestions` 和`zsh-syntax-highlighting`, 可以自行安装.

## Directory Navigation 文件夹导航

可以使用`ls -R` 来递归显示文件

也可以使用`tree` 显示文件的树形结构

一个更好的工具为`broot`, 是一个交互式命令行工具. 安装后可以通过`br` 浏览文件, 并执行其他指令例如`cd`













