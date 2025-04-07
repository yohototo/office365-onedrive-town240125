# 递归列出文件夹中的所有文件和子文件夹
def list_folder_items_recursive(folder_id, indent=""):
    try:
        folder_items = client.item(drive='me', id=folder_id).children.get()
        for item in folder_items:
            print(f"{indent}{item.name} ({'Folder' if item.folder else 'File'})")
            if item.folder:  # 如果是文件夹，则递归列出其内容
                list_folder_items_recursive(item.id, indent + "  ")
    except Exception as e:
        print(f"Error listing items recursively: {e}")

# 移动文件或文件夹
def move_item(item_id, new_parent_id):
    try:
        # 创建一个新的引用对象，指定目标父文件夹
        new_parent_reference = onedrivesdk.ItemReference()
        new_parent_reference.id = new_parent_id

        # 执行移动操作
        moved_item = client.item(drive='me', id=item_id).move(new_parent_reference).post()
        print(f"Item moved successfully to new parent folder: {moved_item.name}")
    except Exception as e:
        print(f"Error moving item: {e}")

# 复制文件或文件夹
def copy_item(item_id, new_parent_id):
    try:
        # 创建一个新的引用对象，指定目标父文件夹
        new_parent_reference = onedrivesdk.ItemReference()
        new_parent_reference.id = new_parent_id

        # 执行复制操作
        copied_item = client.item(drive='me', id=item_id).copy(name=None, parent_reference=new_parent_reference).post()
        print(f"Item copied successfully to new parent folder: {copied_item.name}")
    except Exception as e:
        print(f"Error copying item: {e}")

# 搜索文件
def search_files(query):
    try:
        # 使用 OneDrive 的搜索功能
        search_results = client.item(drive='me', id='root').search(q=query).get()
        if search_results:
            print(f"Search results for '{query}':")
            for item in search_results:
                print(f"- {item.name} ({'Folder' if item.folder else 'File'})")
        else:
            print(f"No results found for query: {query}")
    except Exception as e:
        print(f"Error searching files: {e}")

# 示例用法
if __name__ == "__main__":
    # 递归列出新文件夹中的所有文件和子文件夹
    print("\n--- Recursive Listing of Folder Items ---")
    list_folder_items_recursive(new_folder.id)

    # 移动文件或文件夹
    print("\n--- Moving an Item ---")
    move_item(new_folder.id, root_folder[0].id)  # 将新文件夹移动到根目录的第一个文件夹中

    # 复制文件或文件夹
    print("\n--- Copying an Item ---")
    copy_item(new_folder.id, root_folder[0].id)  # 将新文件夹复制到根目录的第一个文件夹中

    # 搜索文件
    print("\n--- Searching Files ---")
    search_files("test.txt")  # 搜索名为 test.txt 的文件

    # 清理资源
    print("\n--- Cleaning Up Resources ---")
    try:
        # 删除新创建的文件夹及其内容
        client.item(drive='me', id=new_folder.id).delete()
        print("New folder and its contents deleted successfully.")
    except Exception as e:
        print(f"Error cleaning up resources: {e}")
