import datetime
from lxml import etree as ET
from pathlib import Path
import os


##############################
### Methode to delete node ###
##############################

def strip_node(element):

    text = element.xpath('string()')

    # Add tail to text
    text += (element.tail or '')

    if text is not None:
        # get parent node
        parent = element.getparent()
        # get previous node
        previous = element.getprevious()

        if previous is not None:
            if previous.tail is not None:
                previous.tail += text
            else:
                previous.tail = text


        else:
            parent.text = (parent.text or '') + text

        # removes node
        parent.remove(element)


print('Status: Program started, ', datetime.datetime.now())

text = ''
isXML = True
isPath = True
rightChoice = True
deleteByName = False
deleteByAttribute = False
deleteByBoth = False

try:
    ###########################
    ### Importpath xml file ###
    ###########################
    try:
        while isPath:
            # Import
            importFolder = Path(input('Enter input folder: '))

            if '.xml' in str(importFolder):
                print('Please enter a folder path, not a file path. For further information see README.md.')
            else:
                isPath = False

        isPath = True

        # Save filenames
        files = os.listdir(importFolder)


        ###########################
        ### Exportpath xml file ###
        ###########################

        # Export
        while isPath:
            exportFolder = Path(input('Enter different output folder: '))

            if '.xml' in str(exportFolder):
                print('Please enter a folder path, not a file path. For further information see README.md.')
            elif importFolder == exportFolder:
                print('Please enter different folder.')
            else:
                isPath = False


    except FileNotFoundError as fnfError:
        print(fnfError)


    for file in files:
        if '.xml' in file:
            try:
                # Open xml file
                tree = ET.parse(str(importFolder / file))
                root = tree.getroot()

            except FileNotFoundError as fnfError:
                print(fnfError)
            except OSError as osError:
                print(osError)

            while rightChoice:
                # Choice if delete node by node name or by attribute
                choice = input('Do you want to delete a node by name, by attribute or by both? Enter \'1\' for node, \'2\' for attribute and \'3\' for both: ')

                # Delete by name
                if choice == '1':
                    rightChoice = False
                    deleteByName = True
                    nodeName = input('Enter node name: ')
                    addValue = input('Filter by node value? (y/n): ')
                    if addValue == 'y':
                        nodeValue = input('Enter node value to filter (part of value possible): ')

                # Delete by attribute
                elif choice == '2':
                    rightChoice = False
                    deleteByAttribute = True
                    attributeName = input('Enter attribute name: ')
                    addValue = input('Filter by attribute value? (y/n): ')
                    if addValue == 'y':
                        attributeValue = input('Enter attribute value to filter (part of value possible): ')

                # Both
                elif choice == '3':
                    rightChoice = False
                    deleteByBoth = True
                    nodeName = input('Enter node name: ')
                    attributeName = input('Enter attribute name: ')
                    withoutAttr = input('Node with attribute (1) or without the attribute (2): ')
                    addValue = input('Filter by attribute value? (y/n): ')
                    if addValue == 'y':
                        attributeValue = input('Enter attribute value to filter: ')
                else:
                    print('Please enter \'1\', \'2\' or \'3\'. ')


            # delete by name
            if deleteByName:
                for element in tree.xpath('.//' + nodeName):
                    # attribute name and value
                    if addValue == 'y':
                        if nodeValue in element.text():
                            strip_node(element)
                    else:
                        strip_node(element)

            # delete by attribute
            elif deleteByAttribute:
                # attribute name
                for element in tree.xpath('.//*[@' + attributeName + ']'):
                    # attribute name and value
                    if addValue == 'y':
                        if attributeValue in element.get(attributeName, ''):
                            strip_node(element)

                    else:
                        strip_node(element)

            # delete by name and attribute
            elif deleteByBoth:
                for element in tree.xpath('.//'+nodeName+'[not(@'+attributeName+')]'):
                    if addValue == 'y':
                        if attributeValue in element.get(attributeName, ''):
                            strip_node(element)

                    else:
                        strip_node(element)


                ###########################
                ### Export new xml file ###
                ###########################
            try:
                tree.write(str(exportFolder / file))
                print('Status: ' + file + ' exported ', datetime.datetime.now())

            except FileNotFoundError as fnfError:
                print(fnfError)


except ValueError as valueError:
    print(valueError)
