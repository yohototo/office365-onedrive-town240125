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

# 列出特定文件夹中的所有文件和文件夹
def list_folder_items(folder_id):
    try:
        folder_items = client.item(drive='me', id=folder_id).children.get()
        for item in folder_items:
            print(item.name, item.folder if item.folder else item.file)
    except Exception as e:
        print(f"Error listing items in folder: {e}")

# 更新一个云端文件
def update_file(folder_id, file_name, new_content):
    try:
        file_item = client.item(drive='me', id=folder_id).children[file_name].get()
        file_item.content = new_content
        file_item.update()
        print(f"File {file_name} updated successfully.")
    except Exception as e:
        print(f"Error updating file: {e}")

# 错误处理示例
try:
    # 尝试获取一个不存在的文件
    non_existent_file = client.item(drive='me', id='non_existent_id').get()
except onedrivesdk.error.OneDriveError as e:
    print(f"OneDrive error: {e}")
except Exception as e:
    print(f"General error: {e}")

# 示例用法
# 列出新文件夹中的所有文件和文件夹
list_folder_items(new_folder.id)

# 更新新文件夹中的文件
update_file(new_folder.id, 'test.txt', 'This is the updated content of the file.')

# 关闭本地文件
local_file.close()


