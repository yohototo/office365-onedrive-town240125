##像风一样自由

获取api
Rclone 进阶使用教程 – 自建私有 API 挂载 OneDrive – 大为的博客 (jybest.ltd)
https://blog.csdn.net/diqiudq/article/details/122754919

token超出长度解决方法
https://blog.csdn.net/diqiudq/article/details/129898866

1.申请onedrive api

 前往Microsoft Azure管理界面，登录你的微软账号，打开“应用注册”服务。
 点击“新注册”注册一个应用程序。
 输入名称，勾选权限后注册应用。
 注册成功后将跳转到管理页面，记下图中所示的“应用程序(客户端) ID”，供将来挂载使用。
 此时点击“证书与密码”→“新客户端密码”，填写说明和截至期限后，添加密码。
 添加密码后，我们记录密码值，供将来挂载使用。注意这里一定要将密码记录下来，因为它只显示一次。
 接下来，点击“API权限”，为我们的api获取权限。Files中的权限全部勾选。
 至此，我们已经申请好了onedrive的api，目前我们已经得到了客户端ID以及密码值。

以下步骤在linux服务器上进行。

1.
在rclone官网文档查看你系统的安装方式，下面以ubuntu为例。
```
apt update && apt install curl
```
```
curl https://rclone.org/install.sh | sudo bash
```
安装成功后，命令行输入rclone config挂载onedrive网盘，输入“n”新建一个云盘，并输入名称。这个名称就是挂载后磁盘的名称，我起的是“onedrive”。
接下来，找到onedrive这一项，并输入前面的序号。随着rclone版本的更新，每一种网盘序号的顺序可能会改变，注意仔细辨别。
  接下来，输入前面保存的客户端ID、密码以及网盘类型。此处注意区分你的网盘是什么类型，国内大多高校邮箱都是国际版(1)，部分高校是世纪互联版(4)。
接下来不进行高级配置(n)，也不进行自动配置(n)。
 配置完成后，我们选择类型为onedrive(1)。此时系统会读取网盘路径，我们输入y确认。
此时，我们看到一个"onedrive"类型的、名为“onedrive”的网盘已经创建好，我们输入q退出程序，准备将这块网盘挂载到本地目录。

注意！配置文件路径获取指令：rclone config file

2.
先安装fuse
```
apt update && apt install fuse
```
 在linux终端中输入以下命令挂载网盘。挂载的命令为：
rclone mount 网盘名:网盘下的目录 即将挂载到的目录 --copy-links --no-gzip-encoding --no-check-certificate --allow-other --allow-non-empty --umask 000
1.mkdir -p /home/onedrive
2.rclone mount onedrivejp3:/jp3 /home/onedrive --copy-links --no-gzip-encoding --no-check-certificate --allow-other --allow-non-empty --umask 000



要断开本地映射，可以使用以下命令：
```
fusermount -u /home/onedrive
```

```
rclone mount onedrivejp3:/ /home/onedrive --copy-links --no-gzip-encoding --no-check-certificate --allow-other --allow-non-empty --umask 000 --vfs-cache-mode full
```
#使用完全缓存模式，即将文件完全缓存在本地磁盘上。
```
rclone mount onedrivejp3:/jp3 /home/onedrive --copy-links --no-gzip-encoding --no-check-certificate --allow-other --allow-non-empty --umask 000 --vfs-cache-mode writes
```
#只上传本地更改
```
rclone mount onedrivejp3:/ /home/onedrive --copy-links --no-gzip-encoding --no-check-certificate --allow-other --allow-non-empty --umask 000 --vfs-cache-mode off
```
#--vfs-cache-mode off，表示不使用缓存模式，文件将直接从远程读取而不缓存在本地。

windows 挂载
```
rclone mount gaogao: E:\winod --vfs-cache-mode writes
```

```
mv /home/onedrive/"tiny11 b2.iso" /root/
```


```
rclone config
```
配置网盘
```
rclone config show gaogao
```

Rclone挂载OneDrive为本地硬盘-Windows篇 (lanxh.com)
 下载winfsphttp://www.secfs.net/winfsp/rel/
