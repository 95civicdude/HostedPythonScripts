from xml.etree.ElementTree import *
from xml.dom.minidom import Document, parse, parseString

######################################
# Client Response Name and Date
# 	cleanup script. 
######################################

clientFile = "/Path/to/file/new_data.xml"
outputFile = "bin/new_data.xml"

# Code needed for setting up the xml document
doc = parse(clientFile)
root = doc.documentElement
root.setAttribute('name', "PowerReviews")
root.setAttribute('extractDate', "0001-01-01T00:00:00.000+00:00")
root.setAttribute('xmlns', "http://www.bazaarvoice.com/xs/PRR/StandardClientFeed/5.6")

# Code for just adding the Name and Date for Client Response
products = doc.getElementsByTagName('Product')

for product in products:
	reviews = product.getElementsByTagName('Review')

	for review in reviews:
		submitDateNode = review.getElementsByTagName('SubmissionTime')
		submitDateText = submitDateNode[0].firstChild.nodeValue

		clientResponses = review.getElementsByTagName('ClientResponse')

		for clientResponse in clientResponses:

			nameNode = clientResponse.getElementsByTagName('Name')
			nameText = "Customer Care"
			nameTextNode = doc.createTextNode(nameText)
			nameNode[0].appendChild(nameTextNode)

			responseDate = doc.createElement('Date')
			responseDateTxt = doc.createTextNode(submitDateText)
			responseDate.appendChild(responseDateTxt)
			clientResponse.appendChild(responseDate)

outFile = open(outputFile, 'wb')
outFile.write(doc.toprettyxml(indent="", newl="", encoding="utf-8"))
outFile.close()
