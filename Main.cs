using Microsoft.OneDrive.Sdk; // 引入 OneDrive SDK
using System;
using System.IO;
using System.Threading.Tasks;

namespace OneDriveDemo
{
    class Program
    {
        // 定义一些常量，你需要用你自己的值替换它们
        const string clientId = "your_client_id"; // 你的应用程序的客户端 ID
        const string returnUrl = "https://login.live.com/oauth20_desktop.srf"; // 你的应用程序的返回 URL
        const string[] scopes = { "onedrive.readwrite", "wl.signin" }; // 你的应用程序需要的权限范围
        const string folderPath = "/Documents/MyFolder"; // 你要上传文件到的 OneDrive 文件夹的路径
        const string filePath = @"C:\Users\Me\MyFile.txt"; // 你要上传的本地文件的路径

        static async Task Main(string[] args)
        {
            try
            {
                // 创建一个认证提供者，用于获取访问令牌
                var authProvider = new MsaAuthenticationProvider(clientId, returnUrl, scopes);
                // 认证用户并获取访问令牌
                await authProvider.AuthenticateUserAsync();
                // 创建一个 OneDrive 客户端，用于调用 OneDrive API
                var oneDriveClient = new OneDriveClient("https://api.onedrive.com/v1.0", authProvider);
                // 获取要上传文件到的 OneDrive 文件夹的 DriveItem 对象
                var folder = await oneDriveClient.Drive.Root.ItemWithPath(folderPath).Request().GetAsync();
                // 打开要上传的本地文件的流
                using (var fileStream = new FileStream(filePath, FileMode.Open))
                {
                    // 上传文件到 OneDrive 文件夹，并获取上传后的 DriveItem 对象
                    var uploadedFile = await oneDriveClient.Drive.Items[folder.Id].Children.Request().AddAsync(new Item { Name = Path.GetFileName(filePath), File = new File() }, fileStream);
                    // 打印上传后的文件的信息
                    Console.WriteLine($"Uploaded file: {uploadedFile.Name}, Id: {uploadedFile.Id}, Size: {uploadedFile.Size}");
                }
                // 关闭 OneDrive 客户端
                oneDriveClient.Dispose();
            }
            catch (Exception ex)
            {
                // 打印异常信息
                Console.WriteLine($"Error: {ex.Message}");
            }
        }
    }
}
using Microsoft.OneDrive.Sdk; // 引入 OneDrive SDK
using System;
using System.IO;
using System.Threading.Tasks;

namespace OneDriveDemo
{
    class Program
    {
        // 定义一些常量，你需要用你自己的值替换它们
        const string clientId = "your_client_id"; // 你的应用程序的客户端 ID
        const string returnUrl = "https://login.live.com/oauth20_desktop.srf"; // 你的应用程序的返回 URL
        const string[] scopes = { "onedrive.readwrite", "wl.signin" }; // 你的应用程序需要的权限范围
        const string folderPath = "/Documents/MyFolder"; // 你要上传文件到的 OneDrive 文件夹的路径
        const string filePath = @"C:\Users\Me\MyFile.txt"; // 你要上传的本地文件的路径
        const string downloadPath = @"C:\Users\Me\DownloadedFile.txt"; // 你要下载的本地文件的路径

        static async Task Main(string[] args)
        {
            try
            {
                // 创建一个认证提供者，用于获取访问令牌
                var authProvider = new MsaAuthenticationProvider(clientId, returnUrl, scopes);
                // 认证用户并获取访问令牌
                await authProvider.AuthenticateUserAsync();
                // 创建一个 OneDrive 客户端，用于调用 OneDrive API
                var oneDriveClient = new OneDriveClient("https://api.onedrive.com/v1.0", authProvider);
                // 获取要上传文件到的 OneDrive 文件夹的 DriveItem 对象
                var folder = await oneDriveClient.Drive.Root.ItemWithPath(folderPath).Request().GetAsync();
                // 打开要上传的本地文件的流
                using (var fileStream = new FileStream(filePath, FileMode.Open))
                {
                    // 上传文件到 OneDrive 文件夹，并获取上传后的 DriveItem 对象
                    var uploadedFile = await oneDriveClient.Drive.Items[folder.Id].Children.Request().AddAsync(new Item { Name = Path.GetFileName(filePath), File = new File() }, fileStream);
                    // 打印上传后的文件的信息
                    Console.WriteLine($"Uploaded file: {uploadedFile.Name}, Id: {uploadedFile.Id}, Size: {uploadedFile.Size}");
                }

                // 下载文件
                var fileToDownload = await oneDriveClient.Drive.Items[folder.Id].ItemWithPath("MyFile.txt").Request().GetAsync();
                using (var fileStream = new FileStream(downloadPath, FileMode.Create))
                {
                    await oneDriveClient.Drive.Items[fileToDownload.Id].Content.Request().DownloadAsync(fileStream);
                    Console.WriteLine($"Downloaded file: {fileToDownload.Name}, Id: {fileToDownload.Id}, Size: {fileToDownload.Size}");
                }

                // 列出文件夹内容
                var folderContents = await oneDriveClient.Drive.Items[folder.Id].Children.Request().GetAsync();
                Console.WriteLine("Folder contents:");
                foreach (var item in folderContents)
                {
                    Console.WriteLine($"Name: {item.Name}, Id: {item.Id}, Size: {item.Size}");
                }

                // 关闭 OneDrive 客户端
                oneDriveClient.Dispose();
            }
            catch (Exception ex)
            {
                // 打印异常信息
                Console.WriteLine($"Error: {ex.Message}");
            }
        }
    }
}

