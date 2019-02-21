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
	
	if req.status_code == 200:

		info = req.json()
		
		a = info ["titre"]
		
		if info["type"] == "audio":
			infos = []
			infos.append(info["titre"][:(a.find("/"))])
			infos.append(info["createurs"][0])
			infos.append(info["dateCreation"])
			infos.append(info["descriptionMat"])
			
			print(info["titre"][:(a.find("/"))])
			print(info["createurs"][0])
			print(info["dateCreation"])
			print(info["descriptionMat"])
			print(url)
			
			info_bitstreams = info["bitstreams"] 
			info_fils = info_bitstreams["racine"]["fils"]
			info_formats = info_fils[0]["formats"]
			
			a = info_formats[0]
			b = a.keys()
			
			if str(b) == "dict_keys(['restriction', 'id'])":
				infos.append(info["url"])

			else:
				info_url = info_formats[0]["url"]
				infos.append(info_formats[0]["url"])
				print(info_url)
		


		f2 = open(fichier, "a")
		banq = csv.writer(f2)
		banq.writerow(infos)





