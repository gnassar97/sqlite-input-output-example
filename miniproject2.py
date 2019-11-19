from bsddb3 import db
import sys
import xml.etree.ElementTree as ET


#https://docs.python.org/2/library/xml.etree.elementtree.html

#First thing we want to use is element tree to iterate over the XML file and remove all of the useful info.
#Then we want to take that useful info and split it up into 4 files:

#terms.txt: This file includes terms extracted from email subject and body; for our purpose, suppose a term is a consecutive sequence of alphanumeric, underscore '_' and dashed '-' characters, i.e [0-9a-zA-Z_-]. 
#The format of the file is as follows: for every termT in the subject of an email with row id I, there is a row in this file of the form s-T':I whereT' is the lowercase form of T. 
#For every term T in the body field of an email with row id I, there is a row in this file of the form b-T':I, whereT' is again the lowercase form of T. Ignore all special characters coded as &#number; such as &#10; and &lt;, &gt;, &amp;, &apos; and &quot;. 
#Also ignore terms of length 2 or less. Convert the terms to all lowercase before writing them out. Here are the respective files for our input files with 10 records and 1000 records.

#emails.txt: This file includes one line for every email address that appears in a from, to, cc and bcc field. The format of each line is FLD-E:I where E is an email address all in lowercase, 
#I is the row id of the email and FLD is the field where the email is mentioned, which takes the values of from, to, cc and bcc. Email addresses that are not in lowercase are converted to lowercase before they are written to this file. 
#Here are the respective files for our input files with 10 records and 1000 records.

#dates.txt: This file includes one line for each email record in the form of d:l where d is the date of the email, and l is the row id. Here are the respective files for our input files with 10 records and 1000 records.

#recs.txt: This file includes one line for each email in the form of I:rec where I is the row id and rec is the full email record in XML. Here are the respective files for our input files with 10 records and 1000 records.

tree = ET.parse('10.xml')
root = tree.getroot()

def main():


	

	print("P1------------------------")
	print root.tag, root.attrib
	print("--------------------------")

	print("P2------------------------")
	for child in root:
		print child.tag, child.attrib
	print("--------------------------")

	print("P3------------------------")
	print root[0][1].text
	print("--------------------------")

	print("P4------------------------")
	for mail in root.iter('mail'):
		print mail.attrib
	print("--------------------------")

	print("P5------------------------")
	for mail in root.findall('mail'):
		mailfrom = mail.find('from').text
		to = mail.find('to').text
		print mailfrom, to
	print("--------------------------")










main()
#Get an instance of BerkeleyDB
#test = sys.argv[1]
#database = db.DB()
#database.open(test)

#cur = database.cursor()
#iter = cur.first()
#while iter:
# print(iter)
# iter = cur.next()
#cur.close()




#database.close()