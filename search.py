#! usr/bin/python3
# Search the web

import webbrowser
address=""
print("********************WELCOME TO SEARCH ********************")
print("====================Search the web========================")
print("**********************MENU********************************")
print("Please chose where u want to search")
print("1.Google \n 2.Wikipedia \n 3.Youtube \n 4.Facebook \n 5.Google Maps \n 6. AmaZon \n 7. Flipkart \n 8. Quora \n")
i = int(input())

if i == 1:
	print("welcome to google search")
	print("please enter your query")
	address = input()
	address = address.split(" ")
	address = "+".join(address)
	print("Do you want direct download link to it ?")
	answer = str(input())

	if answer == "yes" or answer == "y":
		print("Enter the year in which it was released otherwise leave blank if you don't know")
		year = str(input())
		webbrowser.open("https://www.google.co.in/search?q=index+of+%2B+%22" + "+" + address +"%22" + "+" + year)
		
	else:

		webbrowser.open("https://www.google.co.in/search?q=" + address)
  
elif i == 2:
	print("Welcome to Wikipedia search")
	print("please enter your query")
	address = input()
	address = address.split(" ")
	address = "+".join(address)
	webbrowser.open("https://en.wikipedia.org/wiki/" + address)
elif i==3:
	print("Welcome to Youtube search")
	print("please enter your query")
	address = input()
	address = address.split(" ")
	address = "+".join(address)
	webbrowser.open("https://www.youtube.com/results?search_query=" + address)
elif i==4:
	print("Welcome to Facebook search")
	print("please enter your query")
	address = input()
	address = address.split(" ")
	address = "+".join(address)
	webbrowser.open("https://www.facebook.com/search/str/" + address + "/keywords_top")
elif i==5:
	print("Welcome to Facebook search")
	print("please enter your query")
	address = input()
	address = address.split(" ")
	address = "+".join(address)
	webbrowser.open('https://www.google.co.in/maps?q=' + address)
elif i ==6:
	print("Welcome to Amazon search")
	print("please enter your product name ")
	address = input()
	address = address.split(" ")
	address = "+".join(address)
	print("Do u want discount?")
	ans = str(input())
	ans = ans.lower()
	if ans == "yes" or ans=="y":
		print("How much discount you want ? ex 50-60 ")
		disc = str(input())
		webbrowser.open("http://www.amazon.in/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=" + address + "&pct-off=" + disc)
	
	else:
		webbrowser.open('http://www.amazon.in/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=' + address)

elif i == 7:
	print("Welcome to Flipkart search")
	print("please enter your product")
	address = input()
	address = address.split(" ")
	address = "+".join(address)
	webbrowser.open('http://www.flipkart.com/search?q=' + address)
elif i == 8:
	print("welcome to Quora search")
	print("please enter your query")
	address = input()
	address = address.split(" ")
	address = "+".join(address)
	webbrowser.open("https://www.quora.com/search?q=" + address)
else:
	print("Chose from no. 1-7")
