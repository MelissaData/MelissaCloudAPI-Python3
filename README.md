# Melissa Cloud API Python Package Sample Code

## Purpose
This code showcases the Melissa Cloud API Python Package.

Please feel free to copy or embed this code to your own project. Happy coding!

For more details about how to use the Melissa Cloud API Python Package, please visit the [Melissa Docs](https://docs.melissa.com/cloud-api/cloud-api-packages/cloud-api-packages-installation.html#pip-installation-python)

For more details about Melissa Cloud APIs, please click [here](https://docs.melissa.com/cloud-api/cloud-api/cloud-api-index.html)

## Tested Environments
- Windows 10 64-bit

### Licensing
All Melissa Cloud APIs require a license in order to be accessed. This license is an encrypted series of letters, numbers, and symbols. This license can also either be a Credit license or a Subscription license. Both ways use the same service, so you do not need to change your code to move from one model to another.

To learn more about how to set up a license key with Melissa, please click [here](https://docs.melissa.com/cloud-api/cloud-api/licensing.html)

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

This project is compatible with Python3

#### Install Python3
Before starting, make sure that Python3 has been correctly installed on your machine and your environment paths are configured. 

You can download Python here: 
https://www.python.org/downloads/

To set up your Path to correctly to use the python3 command, execute the following steps:
1) Run Powershell as an administrator 
2) Execute the command: 
`New-Item -ItemType SymbolicLink -Path "Link" -Target "Target"`

    where "Target" is the path to py.exe (by default this should be "C:\Windows\py.exe")\
    and "Link" is the path to py.exe, but "py.exe" is replaced with "python3.exe"\
    For Example:\
    `New-Item -ItemType SymbolicLink -Path "C:\Windows\python3.exe" -Target "C:\Windows\py.exe"`

If you are unsure, you can check by opening a command prompt window and typing the following:
`python3 --version`

If you see the version number then you have installed Python3 and set up your environment paths correctly!

----------------------------------------

#### Download this project
```
git clone https://github.com/MelissaData/MelissaCloudAPI-Python3
cd melissacloudapi-python3
```
#### Add the package 

There are two ways to install the Melissa Cloud API Package.

#### Install with pip - reccommended method

1. Ensure that you have pip installed on your machine. You can check this by using : 
    ```
    pip --version
    ```
    a. For information on installing and using pip please see https://pip.pypa.io/en/stable/installation/
    
2. Run the command:
    ```
    pip install melissadatacloudapi
    ```

#### Import manually

1.  Navigate to the sample code project directory.

2.  Clone the package repository using the command:
    ```
    git clone [https://github.com/MelissaData/MelissaCloudAPI-PyPI](https://github.com/MelissaData/MelissaCloudAPI-PyPI)
    ```
    This will create a directory named `MelissaCloudAPI-PyPI` in your current location.

3.  Locate the package files: Inside the `MelissaCloudAPI-PyPI` directory, you will find the actual package files within a subdirectory also named `melissadatacloudapi`.

4.  Copy the `melissadatacloudapi` directory: Copy the entire `melissadatacloudapi` directory.

5.  Navigate to the project's main directory.

6.  Paste the `melissadatacloudapi` directory into the project's main directory. The project structure should now look something like this (example):

    ```
    melissacloudapi-python3/
    ├── sample.py
    ├── ...
    └── melissadatacloudapi/
        ├── __init__.py
        ├── cloudapis/
        │   ├── ...
        ├── apiresponse/
        │   ├── ...
        ├── PostReqestBase.py
        └── RecordRequests.py
    ```


The Melissa Cloud API Python Sample Code should now be set up. Enjoy!

## Contact Us
For free technical support, please call us at 800-MELISSA ext. 4 (800-635-4772 ext. 4) or email us at Tech@Melissa.com.

