#!/usr/bin/env python3
import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    root = ET.Element("data")
    for keys, value in dictionary.items():
        child = ET.Element(keys)
        child.text = value
        root.append(child)
    tree = ET.ElementTree(root)

    with open(filename, 'wb') as f:
        tree.write(f)

def deserialize_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    myDict = {}
    
    for child in root:
        myDict[child.tag] = child.text
    return myDict
