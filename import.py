# 导入onedrivesdk模块
import onedrivesdk

# 创建一个OneDrive客户端对象
client = onedrivesdk.get_default_client(
    client_id='your_client_id', # 你的客户端ID
    scopes=['wl.signin', 'wl.offline_access', 'onedrive.readwrite'] # 你的授权范围
)

# 获取授权码并登录
auth_url = client.auth_provider.get_auth_url('https://login.microsoftonline.com/common/oauth2/nativeclient')
print('请在浏览器中打开以下链接，并复制授权码：')
print(auth_url)
code = input('请输入授权码：')
client.auth_provider.authenticate(code, 'https://login.microsoftonline.com/common/oauth2/nativeclient', 'your_client_secret') # 你的客户端密钥

# 获取OneDrive的根文件夹
root_folder = client.item(drive='me', id='root').children.get()

# 遍历根文件夹下的所有文件和文件夹，并打印它们的名称和类型
for item in root_folder:
    print(item.name, item.folder if item.folder else item.file)

# 创建一个新的文件夹
new_folder = onedrivesdk.Folder()
new_folder.name = 'Test'
new_folder.child_count = 0
client.item(drive='me', id='root').children.add(new_folder)

# 上传一个本地文件到新的文件夹
local_file = open('test.txt', 'rb')
client.item(drive='me', id=new_folder.id).children['test.txt'].upload(local_file)

# 下载一个云端文件到本地
remote_file = client.item(drive='me', id=new_folder.id).children['test.txt'].get()
remote_file.download('./test.txt')

# 删除一个云端文件
client.item(drive='me', id=new_folder.id).children['test.txt'].delete()
AI 生成的代码。仔细查看和使用。 有关常见问题解答的详细信息.
Python

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
