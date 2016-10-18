# prog

# to use this git

echo "# prog" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/icewaver/prog.git
git push -u origin master



1. 首先在本地创建ssh key；
    $ ssh-keygen -t rsa -C "icewaver@163.com"
    之后会要求确认路径和输入密码，我们这使用默认的一路回车就行。成功的话会在~/下生成.ssh文件夹，进去，打开id_rsa.pub，复制里面的key。
回到github，进入Account Settings，左边选择SSH Keys，Add SSH Key,title随便填，粘贴key。
2. 配置~/.ssh/config文件，
#Default Git
Host defaultgit
HostName vxgit.wrs.com #域名也可
User think
IdentityFile ~/.ssh/id_rsa

#Second Git
Host secondgit
HostName github.com #域名也可
User think
IdentityFile ~/.ssh/id_rsa_github
Host就是每个SSH连接的单独代号，IdentityFile告诉SSH连接去读取哪个私钥。

执行ssh-agent让ssh识别新的私钥。
ssh-add ~/.ssh/id_rsa_new
该命令如果报错：Could not open a connection to your authentication agent.无法连接到ssh agent，可执行ssh-agent bash命令后再执行ssh-add命令。

3. 为了验证是否成功，在git bash下输入：
    $ ssh -T git@github.com
如果是第一次的会提示是否continue，输入yes就会看到：You've successfully authenticated, but GitHub does not provide shell access 。这就表示已成功连上github。

4. 在github上建立一个仓库在本地clone下来
git clone git@github.com:icewaver/python-prog.git

接下来我们要做的就是把本地仓库传到github上去，在此之前还需要设置username和email，因为github每次commit都会记录他们。
    $ git config --global user.name "your name"
    $ git config --global user.email "your_email@youremail.com"


5. 如果要把本地的已经建好的仓库数据上传到服务器上时，需要在服务器上建立一个完全同名的仓库，然后进入要上传的仓库，右键git bash，添加远程地址：
    $ git remote add origin git@github.com:yourName/yourRepo.git
