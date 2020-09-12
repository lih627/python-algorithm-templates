# CentOS 非root服务器配置

## 前言

实习生终于有了自己的远程服务器，但是没有root权限。安装软件有点困难。记录一下配置过程遇到的问题。

## Anaconda3

1. 从THU镜像下载最新的Anaconda3

```shell
 wget https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/Anaconda3-2020.07-Linux-x86_64.sh
```

2. 安装, 注意后续执行`conda init`, 将`conda`命令路径加入到`$HOME/.bashrc$`中。

```shell
sh Anaconda3-2020.07-Linux-x86_64.sh 
# 安装结束后进入安装位置
cd $HOME/anaconda3/bin
# 执行 conda init
./conda init
```

3. 测试一下conda命令可用：

```shell
source ~/.bashrc
conda -V # conda 4.8.3
```
4. 在`$HOME`下新建`.bash_profile`，写入：

```shell
if test -f ~/.bashrc ; then
source ~/.bashrc
fi
```

这样每次SSH后，都可以自动加载一下自己的`.bashrc`



## zsh

先下载`zsh`

```shell
cd $HOME/app/
wget -O zsh.tar.xz https://sourceforge.net/projects/zsh/files/latest/download
# 解压后出现 zsh-5.7.1
tar -xvf zsh.tar.xz
```



配置和编译和安装`zsh`

```shell
cd zsh-5.7.1/
 ./configure --prefix=$HOME/Applications/zsh 
make -j $(nproc)
make install
```

`zsh` 加入 `PATH`:

```shell
vim ~/.bashrc
# 加入zsh
export PATH="$HOME/Applications/zsh/bin:$PATH"
source ~/.bashrc
```

### zsh配置报错: ncurses-devel 相关

`./configure` 可能报错:

```shell
onfigure: error: in `/home/lihao/app/zsh-5.7.1':
configure: error: "No terminal handling library was found on your system.
This is probably a library called 'curses' or 'ncurses'.  You may
need to install a package called 'curses-devel' or 'ncurses-devel' on your
system."
```

此时需要非root安装`ncurses-devel`，首先查看系统支持哪个版本

```shell
ls /usr/lib64/libncurses*
# 显示5.9
/usr/lib64/libncurses.so.5    /usr/lib64/libncurses++.so.5.9  /usr/lib64/libncurses++w.so.5.9
/usr/lib64/libncurses++.so.5  /usr/lib64/libncurses++w.so.5   /usr/lib64/libncursesw.so.5.9
/usr/lib64/libncurses.so.5.9  /usr/lib64/libncursesw.so.5
```

所以对应下载`5.9`版本

```shell
cd $HOME/app
wget https://ftp.gnu.org/gnu/ncurses/ncurses-5.9.tar.gz
tar -zxvf ncurses-5.9.tar.gz
cd ncurses-5.9
# 添加环境变量
export CXXFLAGS=" -fPIC"
export CFLAGS=" -fPIC"
# 生成动态链接库
./configure --prefix=$HOME/Applications/ncurses --enable-shared
make -j $(nproc)
make install
# 安装结束后执行
./test/ncurses	
# 如果不出问题则可以使用
```

配置环境变量

```shell
export NCURSES_HOME=$HOME/Applications/ncurses
export PATH=$NCURSES_HOME/bin:$PATH
export LD_LIBRARY_PATH=$NCURSES_HOME:$LD_LIBRARY_PATH
export CPPFLAGS="-I$NCURSES_HOME/include" LDFLAGS="-L$NCURSES_HOME"
```

然后配置zsh

```shell
export CXXFLAGS=" -fPIC"
export CFLAGS=" -fPIC"
./configure --prefix=$HOME/Applications/zsh --en able-shared LDFLAGS=-L$HOME/Applications/ncurses/lib  CPPFLAGS=-I$HOME/Applications/ncurses/include 
```



## oh-my-zsh

进入zsh

```shell
zsh
sh -c "$(wget -O- https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
# 后续会选择是否让zsh成为默认shell 我选的no
```

配置常用插件：

```shell
git clone https://github.com/zsh-users/zsh-autosuggestions $ZSH_CUSTOM/plugins/zsh-autosuggestions
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git $ZSH_CUSTOM/plugins/zsh-syntax-highlighting
git clone https://github.com/zsh-users/zsh-history-substring-search.git $ZSH_CUSTOM/plugins/history-substring-search
```

`.zshrc` `plugins` 更新如下：	

```
plugins=(
  git
  zsh-autosuggestions 
  zsh-syntax-highlighting
  colored-man-pages
  history-substring-search
)
```



## VS Code Remote

这里是Memtor帮忙配的。大致的流程是使用`VSCode Remote-SSH` 这个插件，`command+shift+P`，输入；
```
Remote-SSH: Connect to Host
```

通过跳板机链接到服务器

其配置大致内容为

```
Host *
 AddKeysToAgent yes
 UseKeychain yes
 IdentityFile ~/.ssh/id_rsa

 Host xxx.xxx.xxx.xxx(服务器IP)
  HostName xxx
  User xxx(服务器用户名)
  IdentityFile /path_to/.ssh/id_rsa.dms (本地私钥)
  ProxyCommand ssh xxx(跳板机) -W %h:%p
```

然后可以就可以连上服务器了。

按照个人需求服务器那段安装了Shell/Python相关的插件。

### VSCode修改默认Bash

首先查一下``$HOME/.zshrc`，一定要加上这句话

```shell
# If you come from bash you might have to change your $PATH.
export PATH=$HOME/bin:/usr/local/bin:$PATH
```

然后修改默认bash为zsh，VSCode通过Remote-SSH 连上服务器后，`comand+shift+P` 输入
```
Open Remote Settings(SSH: 服务器IP)
```

然后打开`setting.json`文件，加入zsh所在的地址

```json
{
    "terminal.integrated.shell.linux": "$HOME/Applications/zsh/bin/zsh"
}
```

经测试，打开的Terminal默认是zsh

## 总结

现在的跑代码的解决思路就是conda创建环境，用VScode 远程过去直接运行就可以。VScode也支持单步调试，虽然没有Pycharm那么智能。已经够用了。使用zsh是由于其更为智能化，同时支持高亮，方便纠错。
