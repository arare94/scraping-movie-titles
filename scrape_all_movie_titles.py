from bs4 import BeautifulSoup
import requests
import csv

filename = "roberbert_titles_scrapped.csv"
#programm asking us the page number form 1 to 478(all pages+1) 
page_number = int(input("Please enter the page number from (1) to (478) which you wants to scrap -> "))
#cheking if our passed number in range from 1 to 478
if page_number in range(1, 478):

	with open(filename,'w') as csv_file:
		csv_writer = csv.writer(csv_file)
		#writing row(Title) into file
		csv_writer.writerow(['Title'])
		#getting page link by passed number
		source = requests.get("https://www.rogerebert.com/reviews/page/{}".format(page_number)).text
		soup = BeautifulSoup(source, 'lxml')
		#finding all titles
		items = soup.find_all('h5', {'class' : 'title'})

		#print(page_number)
		for item in items:
			# print(item.a.text)

			#writing page titles into file
			csv_writer.writerow([item.a.text])

#program printing Error if passed value is not a number or its a symbol
else:
	print("Invalid page number")