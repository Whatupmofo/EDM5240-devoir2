#coding: utf-8

import json
import csv
import requests

fichier = "banq.csv"

x = "http://collections.banq.qc.ca/api/service-notice?handle=52327/"

entete = {
	"User-Agent": "Michaël Laforest",
	"From": "438-825-0075"
}




#l1 = range(1000,2001)
l1 = range(1000,2001)

count_liens = 0
count_audio = 0

for n in l1:
	
	url = x + str(n)
	req = requests.get(url,headers=entete)
	# print(url)
	# print(req)


	if req.status_code == 200:
		count_liens = count_liens + 1
		print("nombre de liens valides: ", str(count_liens))

		infos = req.json()
		
		a = infos ["titre"]
		
		if infos["type"] == "audio":
			s = []
			s.append(infos["titre"][:(a.find("/"))])
			s.append(infos["createurs"][0])
			s.append(infos["dateCreation"])
			s.append(infos["descriptionMat"])
			# count_audio = count_audio + 1
			# print("nombre de liens audio: ", str(count_audio) + "\n")
			# s = []
			# s.append(infos["titre"][:(a.find("/"))])
			# s.append(infos["createurs"])
			# s.append(infos["dateCreation"])
			# s.append(infos["descriptionMat"])
			# s.append(url)
			
			print(infos["titre"][:(a.find("/"))])
			print(infos["createurs"][0])
			print(infos["dateCreation"])
			print(infos["descriptionMat"])
			print(url)
			
			info_bitstreams = infos["bitstreams"] 
			info_fils = info_bitstreams["racine"]["fils"]
			info_formats = info_fils[0]["formats"]
			
			a = info_formats[0]
			b = a.keys()
			
			if str(b) == "dict_keys(['restriction', 'id'])":
				s.append(infos["url"])

			else:
				info_url = info_formats[0]["url"]
				s.append(info_formats[0]["url"])
				print(info_url)


		f2 = open(fichier, "a")
		banq = csv.writer(f2)
		banq.writerow(s)





