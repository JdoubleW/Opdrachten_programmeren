import xmltodict

def processXML(filename):
    with open(filename) as myXMLFile:
        filecontentstring = myXMLFile.read()
        xmldictionary = xmltodict.parse(filecontentstring)
        return xmldictionary

voorraaddict = processXML('test')
voorraad = voorraaddict['artikelen']['artikel']

for namen in voorraad:
    print(namen['naam'])