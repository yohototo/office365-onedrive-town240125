# 重命名新创建的文件夹
new_folder.rename('Renamed_Test')

# 获取重命名后的文件夹
renamed_folder = root_folder.get_item('Renamed_Test')

# 在重命名后的文件夹中创建一个新的子文件夹
sub_folder = renamed_folder.create_child_folder('SubFolder')

# 上传另一个本地文件到子文件夹
sub_folder.upload_file('example.txt')

# 列出重命名后的文件夹中的所有内容
print("Contents of 'Renamed_Test':")
for item in renamed_folder.get_items():
    print(item.name, 'folder' if item.is_folder else 'file')

# 移动子文件夹到根目录
sub_folder.move(root_folder)

# 验证子文件夹是否已移动到根目录
print("Contents of root folder after moving 'SubFolder':")
for item in root_folder.get_items():
    print(item.name, 'folder' if item.is_folder else 'file')

# 删除子文件夹及其内容
moved_sub_folder = root_folder.get_item('SubFolder')
moved_sub_folder.delete()

# 检查子文件夹是否已被删除
print("Contents of root folder after deleting 'SubFolder':")
for item in root_folder.get_items():
    print(item.name, 'folder' if item.is_folder else 'file')

# 下载整个文件夹（递归下载）
def download_folder(folder, local_path):
    import os
    if not os.path.exists(local_path):
        os.makedirs(local_path)
    for item in folder.get_items():
        if item.is_folder:
            # 如果是文件夹，递归下载
            download_folder(item, os.path.join(local_path, item.name))
        else:
            # 如果是文件，直接下载
            item.download(os.path.join(local_path, item.name))
            print(f"Downloaded: {item.name}")

# 下载重命名后的文件夹到本地
download_folder(renamed_folder, './Renamed_Test_Local')

# 删除重命名后的文件夹及其内容
renamed_folder.delete()

# 检查根文件夹内容，确保所有操作已完成
print("Final contents of root folder:")
for item in root_folder.get_items():
    print(item.name, 'folder' if item.is_folder else 'file')
