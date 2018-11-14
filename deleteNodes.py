import datetime
from lxml import etree as ET
from pathlib import Path


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
            if parent is not None:
                parent.text = (parent.text or '') + text
            else:
                parent.text = text

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

    # Test if path contains xmlFile
    while isXML:
        # Import file
        importFile = input('Enter path to import file: ')

        if '.xml' in str(importFile):
            isXML = False
        else:
            print('No xml File detected, please try again. For further information see README.md.')


    ###########################
    ### Exportpath xml file ###
    ###########################

    # Test if folder path or file path
    while isPath:
        # Export path
        exportFolder = Path(input('Enter path to output folder: '))

        if '.xml' in str(exportFolder):
            print('Please enter a folder path, not a file path. For further information see README.md.')
        else:
            isPath = False


    # Export file
    exportFile = input('Enter output filename: ')
    # if filename does not contain data format, add .xml
    if '.xml' not in exportFile:
        exportFile += '.xml'


    # Open xml file
    tree = ET.parse(importFile)
    root = tree.getroot()


except FileNotFoundError as fnfError:
    print(fnfError)
except ValueError as valueError:
    print(valueError)

else:
    try:
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


    except ValueError as valueError:
        print(valueError)

    else:
        # delete by name
        if deleteByName:
            for element in tree.xpath('.//' + nodeName):
                # attribute name and value
                if addValue == 'y':
                    if nodeValue in element.text:
                        strip_node(element)
                # only node name
                else:
                    strip_node(element)

        # delete by attribute
        elif deleteByAttribute:
            for element in tree.xpath('.//*[@' + attributeName + ']'):
                # attribute name and value
                if addValue == 'y':
                    if attributeValue in element.get(attributeName, ''):
                        strip_node(element)
                # only attribute name
                else:
                    strip_node(element)


        # delete by name and attribute
        elif deleteByBoth:
            # delete node by name with attribute
            if withoutAttr == '1':
                for element in tree.xpath('.//' + nodeName + '[@' + attributeName + ']'):
                    # attribute with value
                    if addValue == 'y':
                        if attributeValue in element.get(attributeName, ''):
                            strip_node(element)
                    # attribute without value
                    else:
                        strip_node(element)

            # delete node by name without attribute
            elif withoutAttr == '2':
                if addValue == 'y':
                    for element in tree.xpath('.//' + nodeName + '[not(@' + attributeName + ')]'):
                        strip_node(element)
                    for element in tree.xpath('.//' + nodeName + '[not(@' + attributeName + '="' + attributeValue + '")]'):
                        strip_node(element)

                else:
                    for element in tree.xpath('.//' + nodeName + '[not(@' + attributeName + ')]'):
                        strip_node(element)


###########################
### Export new xml file ###
###########################

try:
    tree.write(str(exportFolder / exportFile))
    print('Status: ' + exportFile + ' exported ', datetime.datetime.now())

except FileNotFoundError as fnfError:
    print(fnfError)