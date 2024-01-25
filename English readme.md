# office365-onedrive

This is a project written in Python that allows you to use Office 365's OneDrive service on Linux systems. You can sync your local folders and cloud folders, as well as upload or download files.

## Features

- Supports OneDrive personal and OneDrive business
- Supports shared folders and SharePoint sites
- Supports real-time monitoring of local and cloud file changes
- Supports resuming and file verification
- Supports national cloud deployments (US government cloud, German cloud, China cloud, etc.)
- Supports traffic limit and test mode

## Installation

You can use the pip command to install this project:

```
bash pip install office365-onedrive
```
Or you can install it from the source code:
```
git clone https://github.com/yourname/office365-onedrive.git
cd office365-onedrive
python setup.py install
```
Configuration
You need to create a configuration file, specifying your OneDrive account and the folders you want to sync. The configuration file format is as follows:
```
[onedrive]
client_id = your_client_id
client_secret = your_client_secret
redirect_uri = https://login.microsoftonline.com/common/oauth2/nativeclient
sync_dir = /home/user/OneDrive
```
You can find instructions on how to get the client_id and client_secret here. You can also modify other configuration options, such as excluding some files or folders, setting the log level, etc. For more configuration options, please refer to here.

##Usage
You can use the following command to run this project:

onedrive [options]

Where, options can be the following parameters:

-h or --help: Show help information
-m or --monitor: Start real-time monitoring mode
-s or --synchronize: Perform a sync operation once
-r or --resync: Force resync all files
-d or --dry-run: Test if the configuration is correct, do not actually perform sync operation
-v or --verbose: Show detailed log information
For more usage methods, please refer to here.

## Contribution
You are welcome to suggest or contribute code to this project. You can participate in the following ways:

#### Submit issues or suggestions here
#### Submit pull requests or code reviews here
#### View documentation or examples [here]
## License
This project is open sourced under the GPL-3.0 license. You can view the license content [here].
