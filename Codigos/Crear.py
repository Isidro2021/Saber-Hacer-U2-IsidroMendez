import xml.etree.cElementTree as et

root = et.Element("EDFIO2")


tree = et.ElementTree(root)
tree.write("EDFIO2.xml", xml_declaration=True)
