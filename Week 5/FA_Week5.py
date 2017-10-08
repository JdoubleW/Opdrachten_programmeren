import xmltodict

def processXML(filename):
    """"Er wordt een XML bestand gelezen en in een dictionary gedaan."""
    with open(filename) as myXMLFile:
        filecontentstring = myXMLFile.read()
        xmldictionary = xmltodict.parse(filecontentstring)
        return xmldictionary

stationdict = processXML('stations')
stations = stationdict['Stations']['Station']

print("Dit zijn de codes en types van de 4 stations:")
for station in stations:
    print("{:4} - {}".format(station['Code'], station['Type']))


print()


print("Dit zijn alle stations met één of meer synoniemen:")
for synoniem in stations:
    if synoniem['Synoniemen'] is not None:
        print("{:4} - {}".format(synoniem["Code"], synoniem['Synoniemen']))

print()


print("Dit is de lange naam van elk station:")
for station in stations:
    print("{:4} - {}".format(station['Code'], station['Namen']['Lang']))
