import os
import shutil


def main():
    fileManagement()


# read the folder path
def fileManagement():
    extensionList = []
    downloadFolderPath = input("Enter the Folder path for Management: ")
    os.chdir(downloadFolderPath)
    for file in os.listdir():
        extension = file.split(".")[-1]
        extensionList.append(extension)
    extensionList = set(extensionList)
    fileManagementPath = input("Enter the folder path to store the new files: ")
    try:
        os.mkdir(fileManagementPath)
    except:
        pass

    # creating folder for each extension!
    for ex in extensionList:

        try:
            os.mkdir(fileManagementPath+"/"+ex)
        except:
            pass

        for file in os.listdir(downloadFolderPath):
            if ex in file and file != "FileManagement":
                shutil.move(file, fileManagementPath + "/" + ex)


if __name__ == "__main__":
    main()
