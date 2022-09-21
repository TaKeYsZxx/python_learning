

## Git概述

1. git 是一个免费的、开源的分布式版本控制系统，可以快速高效地处理从小型到大型的各种项目。

2. Git易于学习，占地面积小，性能极快。它具有廉价的本地库，方便的暂存区域和多个工作流分支等特性。

   





## 基本工作流程图

<img src="C:\Users\LENOVO\Desktop\1.png" style="zoom:150%;" />

命令如下:

1. clone (克隆) :从远程仓库中克隆代码到本地仓库
2. checkout (检出):从本地仓库中检出一个仓库分支然后进行修订
3. add (添加):在提交前先将代码提交到暂存区
4. commit (提交) :提交到本地仓库。本地仓库中保存修改的各个历史版本
5. fetch (抓取):从远程库,抓取到本地仓库,不进行任何的合并动作,一般操作比较少。
6. pull (拉取) :从远程库拉到本地库,自动进行合并(merge),然后放到到工作区,相当于fetch+merge
7. push (推送) :修改完成后,需要和团队成员共享代码时,将代码推送到远程仓库

## 基本原理



Git工作区:

1.  Remote:远程仓库,托管代码的服务器(类似git hub)
2. Repository:仓库区,也就是本地仓库(.git文件夹),文全行放数据的位置,里面有提交所有版 本的数据,其中HEAD指向最新放入仓库的版本;
3.  index/Stage:暂存区,用于临时存放改动,实际上是一个文件,用于保存即将提交到文件列表的 信息;
4. workspace:工作区,也就是编辑文件的位置;
5. ![](https://img-blog.csdnimg.cn/123490cbeb804c729671f8803d8d84f0.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5LiA5Liq54Ot54ix5a2m5Lmg55qE5rex5bqm5rij5rij,size_10,color_FFFFFF,t_70,g_se,x_16)





## 基本配置

1. 打开Git Bash

2. 设置用户信息

   ![image-20220921213355950](C:\Users\LENOVO\AppData\Roaming\Typora\typora-user-images\image-20220921213355950.png)

   ![image-20220921213440426](C:\Users\LENOVO\AppData\Roaming\Typora\typora-user-images\image-20220921213440426.png)

## 获取本地仓库

1. 在电脑的任意位置创建一个空目录(例如test)作为我们的本地Git仓库 

2. 进入这个目录中,点击右键打开Git bash窗口

3. 执行命令git inti

4. 如果创建成功后可在文件夹下看到隐藏的.git目录。

   ![image-20220921214608134](C:\Users\LENOVO\AppData\Roaming\Typora\typora-user-images\image-20220921214608134.png)

## 基础操作指令

#####   查看修改的状态(status)

-   作用:查看的修改的状态(暂存区、工作区)
- 命令形式: git status

##### 添加工作区到暂存区(add)

- 作用:添加工作区一个或多个文件的修改到暂存区
- 命令形式: git add 单个文件名1通配符 。
- 作用将所有修改加入暂存区: git add

##### 提交暂存区到本地仓库(commit)

- 作用:提交暂存区内容到本地仓库的当前分支
- 命令形式: git commit -m注释内容 

##### 查看提交日志(log)

- 作用:查看提交记录
- 命令形式: git log [option]

​             options

​                   --all显示所有分支 

​                   -abbrev-commit使得输出的commit更简短 

​                    -graph 以图的形式显示





#####   git revert[^revert]

[^revert]: git revert 命令用于撤销对仓库提交历史的更改。其他“撤销”命令，例如：git checkout \git reset，将HEAD和分支引用指针移动到指定的提交。git revert 也需要一个指定的提交，但是，它并不会将ref指针移动到这个提交。revert操作将采用反转指定的提交的更改，并创建一个新的“还原提交”。让后更新ref指针以指向新的还原提交，使其成为分支的HEAD。git revert命令可以被认为是“撤销”命令。但是它不是传统的撤销操作。不是从项目历史中删除提交，而是计算如何要撤销的提交所引入的更改，  并附加一个新的提交及生成的反向内容。这种方式可以防止git丢失历史记录，这对于我们修订历史记录的完整性和可靠的协作非常重要。

​              

git reset 是撤销更改的方法，用于回退版本，可以指定回退某一次提交的版本。



