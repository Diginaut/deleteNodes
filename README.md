# Delete Node

This repository hosts code for automated data manipulation in xml files. You can delete nodes by it's name or its value, by a selected attribute or attribute value or by a combination of the name of the node and one of it's attributes.

Please note that the script requieres python3 and the following libraries: pathlib from Path, [lxml](https://lxml.de/), datetime and os.

## How to
### Run
#### Linux
Check for installed Python version:
```
$ python3 --version
```
If not installed:
```
$ sudo apt-get update
$ sudo apt-get install python3.6
```
To run a script in Linux just start it in the terminal and follow the instructions. If the repository is in Downloads use:
```
$ python3 /home/user/Downloads/tgn-Pleiades/programName.py
```

#### Windows
Check for installed Python version:
```
$ python --version
```
If not installed see [Python Download](https://www.python.org/downloads/windows/).

To run a script in Windows just start it in the command prompt (cmd) and follow the instructions. If the repository is in Downloads use:
```
$ python C:\Users\User\Downloads\tgn-Pleiades\programName.py
```

#### macOS
Check for the installed Python version:
```
$ python3 --version
```
If not installed:
```
$ xcode-select --install
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
$ brew doctor
$ brew install python3
$ python3 --version
```

To run one of script on macOS just start it in the mac terminal and follow the instructions. If the repository is in Downloads use:
```
$ python3 Users/user/Downloads/programName.py
```

### Example

#### Linux
Enter path to xml file:
```
> Status: Program started 2018-11-05 16:10:01.258239
> Enter path to import file: /home/user/Dokumente/myProject/file.xml
```
Enter folder where to save manipulated xml. Please note that the folder has to be created in advanced.
```
> Enter path to output folder: /home/user/Dokumente/myProject/output
```
Enter file name for manipulated xml:
```
> Enter output filename: manipulatedFile.xml
```
Choose if you want to select a node by its name (1), by one of its attribute (2) or by a combination of name and attribute (3):
```
> Do you want to delete a node by name, by attribute or by both? Enter '1' for node, '2' for attribute and '3' for both:
```

#### Windows
```
Status: Program started 2018-11-05 16:10:01.258239
> Enter path to import file: C:\Users\User\Documents\myProject\file.xml
```
Enter folder where to save manipulated xml. Please note that the folder has to be created in advanced.
```
> Enter path to output folder: C:\Users\User\Documents\myProject\output\file.xml
```
Enter file name for manipulated xml:
```
> Enter output filename: manipulatedFile.xml
```
Choose if you want to select a node by its name (1), by one of its attribute (2) or by a combination of name and attribute (3):
```
> Do you want to delete a node by name, by attribute or by both? Enter '1' for node, '2' for attribute and '3' for both:
```

#### macOS
Enter path to xml file:
```
> Status: Program started 2018-11-05 16:10:01.258239
> Enter path to import file: Users/user/Dokumente/myProject/file.xml
```
Enter folder where to save manipulated xml. Please note that the folder has to be created in advanced.
```
> Enter path to output folder: Users/user/Dokumente/myProject/output
```
Enter file name for manipulated xml:
```
> Enter output filename: manipulatedFile.xml
> Status: manipulatedFile.xml exported  2018-11-05 16:16:39.904738
```
Choose if you want to select a node by its name (1), by one of its attribute (2) or by a combination of name and attribute (3):
```
> Do you want to delete a node by name, by attribute or by both? Enter '1' for node, '2' for attribute and '3' for both:
```

### Setting
#### (1) Node name
Select the node(s) you want to delete in your xml file by it's name. If needed you can filter the selected nodes by their value.
```
> Enter node name: nodeName
> Filter by node value? (y/n): y
> Enter node value to filter (part of value possible): nodeValue
> Status: manipulatedFile.xml exported  2018-11-05 16:16:39.904738
```
#### (2) Attribute
Select the node(s) you want to delete in your xml file by one of it's attributes. If needed you can filter the selected nodes by the attributes value.
```
> Enter attribute name: attributeName
> Filter by attribute value? (y/n): y
> Enter attribute value to filter (part of value possible): attributeValue
> Status: manipulatedFile.xml exported  2018-11-05 16:16:39.904738
```
#### (3) Node name and attribute
Select the node(s) you want to delete in your xml file by it's name and one of it's attributes. If needed you can filter the selected nodes by the attributes value.
```
> Enter node name: nodeName
> Enter attribute name: attributeName
> Filter by attribute value? (y/n): y
> Enter attribute value to filter: attributeValue
> Status: manipulatedFile.xml exported  2018-11-05 16:16:39.904738
```
