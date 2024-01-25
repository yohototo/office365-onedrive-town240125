# office365-onedrive

这是一个使用Python编写的项目，可以让你在Linux系统上使用Office 365的OneDrive服务。你可以同步你的本地文件夹和云端的文件夹，也可以上传或下载文件。

## [English]()


## 功能

- 支持OneDrive个人版和OneDrive商业版
- 支持共享文件夹和SharePoint网站
- 支持实时监控本地和云端的文件变化
- 支持断点续传和文件校验
- 支持国家云部署（美国政府云，德国云，中国云等）
- 支持流量限制和测试模式

## 安装

你可以使用pip命令来安装这个项目：

```
bash pip install office365-onedrive
```

或者你可以从源码编译安装：

```
git clone https://github.com/yourname/office365-onedrive.git
cd office365-onedrive
python setup.py install
```

配置
你需要创建一个配置文件，指定你的OneDrive账号和要同步的文件夹。配置文件的格式如下：
```
[onedrive]
client_id = your_client_id
client_secret = your_client_secret
redirect_uri = https://login.microsoftonline.com/common/oauth2/nativeclient
sync_dir = /home/user/OneDrive
```
你可以在这里找到如何获取client_id和client_secret的说明。你也可以修改其他的配置选项，比如排除某些文件或文件夹，设置日志级别等。更多的配置选项，请参考这里。

# 使用
你可以使用以下命令来运行这个项目：

onedrive [options]

其中，options可以是以下的参数：

-h 或 --help：显示帮助信息
-m 或 --monitor：启动实时监控模式
-s 或 --synchronize：执行一次同步操作
-r 或 --resync：强制重新同步所有文件
-d 或 --dry-run：测试配置是否正确，不实际执行同步操作
-v 或 --verbose：显示详细的日志信息
更多的使用方法，请参考这里。

# 贡献
欢迎你对这个项目提出建议或贡献代码。你可以通过以下方式参与：

#### 在[这里](https://github.com/yohototo/office365-onedrive/issues)提交问题或建议
#### 在[这里](https://github.com/yohototo/office365-onedrive/pulls)提交拉取请求或代码审查
#### 在[这里]()查看文档或示例
#### 许可
这个项目使用GPL-3.0协议开源。你可以在这里查看许可证的内容。
