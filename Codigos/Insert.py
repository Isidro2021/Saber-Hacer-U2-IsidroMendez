import xml.etree.cElementTree as et
from xml.etree.ElementTree import SubElement, parse

xml_file = parse('EDFIO2.xml')
root = et.Element("ALUMNOS")
xmlRoot = xml_file.getroot()

se = et.SubElement (root, "A16")
et.SubElement(se, "Especialidad").text = "Entornos"
et.SubElement(se, "Nombre").text = "Solovino_Casas_casas"
et.SubElement(se, "Matricula").text = "18040058"


xmlRoot.append(se)


xml_file.write("EDFIO2.xml", xml_declaration=True)
