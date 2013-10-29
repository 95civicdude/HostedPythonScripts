#!/usr/bin/env python

import time, sys, csv, xml, re, subprocess, random
import xml.etree.ElementTree as ET

######################################
# Review Remover 
######################################

# file definitions
input_file = '/Path/to/file/review_data_complete.xml'
key_file = open('/Path/to/file/keys', 'w')
output_file = '/Path/to/file/clean_rei_complete.xml'
#reviewsList = {}
reviewers = {}
nicknames = {}

tree = ET.parse(input_file)
root = tree.getroot()
nickname_counter = 1

for product in root.findall('product'):

	for review in product.find('reviews').findall('fullreview'):

		try :
			reviewer = review.find('nickname').text.encode('utf-8') if not None else 'Anonymous'
		except:
			reviewer = review.find('nickname').text.decode('utf-8') if not None else 'Anonymous'
		
		try:
			location = review.find('location').text.encode('utf-8') if not None else 'Anonymous'
		except:
			location = review.find('location').text.decode('utf-8') if not None else 'Anonymous'

		review_id = review.find('id').text
		reviewer_id = review.find('merchantuserid').text

		if reviewer_id is None:
			reviewer_id = str(random.randint(1,9999999) * random.randint(1,9999999))
		elif '@' in reviewer_id:
			reviewer_id = str(random.randint(1,9999999)* random.randint(1,9999999))

		reviewer_key = reviewer + '|' + location
		#print reviewer_key

		if reviewer_key not in reviewers: 
			reviewers[reviewer_key] = reviewer_id
			review.find('merchantuserid').text = reviewer_id
		else: 
		 	review.find('merchantuserid').text = reviewer_id

		# if reviewer not in nicknames: 
		# 	nicknames[reviewer] = reviewer
		# else:
		# 	reviewer = reviewer + str(nickname_counter)
		# 	review.find('nickname').text = reviewer
		# 	nickname_counter += 1


		#reviewText = review.find('comments').text.encode('utf-8') if not None else ''
		#reviewText = re.sub('\n', '', reviewText)


tree.write(output_file, encoding="utf-8", xml_declaration=True, default_namespace='')				
