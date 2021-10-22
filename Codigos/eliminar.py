from xml.etree.ElementTree import parse, Element

file_name = "EDFIO2.xml"
doc_xml = parse(file_name)
root = doc_xml.getroot()

root.remove(root.find('A16'))

new_file = 'EDFIO3.xml'
doc_xml.write(new_file, xml_declaration=True)
