# 示例二：使用python-o365库来操作OneDrive的文件和文件夹

# 导入O365模块
from O365 import Account, FileSystemTokenBackend

# 创建一个账户对象
credentials = ('your_client_id', 'your_client_secret') # 你的客户端ID和密钥
token_backend = FileSystemTokenBackend(token_path='.', token_filename='my_token.txt') # 用于保存和加载令牌的后端
account = Account(credentials, token_backend=token_backend)

# 如果没有令牌，就获取授权并登录
if not account.is_authenticated:
    account.authenticate(scopes=['onedrive.all'])

# 获取OneDrive的存储对象
storage = account.storage()

# 获取OneDrive的根文件夹
root_folder = storage.get_root_folder()

# 遍历根文件夹下的所有文件和文件夹，并打印它们的名称和类型
for item in root_folder.get_items():
    print(item.name, 'folder' if item.is_folder else 'file')

# 创建一个新的文件夹
new_folder = root_folder.create_child_folder('Test')

# 上传一个本地文件到新的文件夹
new_folder.upload_file('test.txt')

# 下载一个云端文件到本地
remote_file = new_folder.get_item('test.txt')
remote_file.download('./test.txt')

# 删除一个云端文件
remote_file.delete()
