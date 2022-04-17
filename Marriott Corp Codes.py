from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
import io
import csv
import re
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




#input destination name here with the same format (City, State, Country)
destinationName = "Las Vegas, Nevada, USA"



c = webdriver.ChromeOptions()
c.add_argument("--incognito")

driver = webdriver.Chrome(ChromeDriverManager().install())



#creates a csv file and writes collected data on it
fname="project.csv"
f = open('project.csv', 'w')
#creates coolumn titles in csv file
f.write("HotelName" + "," + "HotelPrice" + "," "Code used")

count = 0

#keeps script running until all codes are used
while count <= 145:
	


	#code used
	if count == 0:
		codeused = "ACC"
	if count == 1:
		codeused = "ATT"
	if count == 2:
		codeused = "DELL"
	if count == 3:
		codeused = "DTC"
	if count == 4:
		codeused = "EMC"
	if count == 5:
		codeused = "FRD"
	if count == 6:
		codeused = "GEE"
	if count == 7:
		codeused = "GMC"
	if count == 8:
		codeused = "IBM"
	if count == 9:
		codeused = "HPQ"
	if count == 10:
		codeused = "ORA"
	if count == 11:
		codeused = "PEP"
	if count == 12:
		codeused = "SAP"
	if count == 13:
		codeused = "SIE"
	if count == 14:
		codeused = "SEM"
	if count == 15:
		codeused = "UBS"
	if	count	== 16:
		codeused = "AAC"
	if	count	== 17:
			codeused = "A70"
	if	count	== 18:
			codeused = "A9M"
	if	count	== 19:
			codeused = "ACC"
	if	count	== 20:
			codeused = "ACS"
	if	count	== 21:
			codeused = "ADP"
	if	count	== 22:
			codeused = "AET"
	if	count	== 23:
			codeused = "AFI"
	if	count	== 24:
			codeused = "AIG"
	if	count	== 25:
			codeused = "ALL"
	if	count	== 26:
			codeused = "AMX"
	if	count	== 27:
			codeused = "AOL"
	if	count	== 28:
			codeused = "APP"
	if	count	== 29:
			codeused = "APL"
	if	count	== 30:
			codeused = "APC"
	if	count	== 31:
			codeused = "ARN"
	if	count	== 32:
			codeused = "ARP"
	if	count	== 33:
			codeused = "ASG"
	if	count	== 34:
			codeused = "ATT"
	if	count	== 35:
			codeused = "AXC"
	if	count	== 36:
			codeused = "BAC"
	if	count	== 37:
			codeused = "BAR"
	if	count	== 38:
			codeused = "BEC"
	if	count	== 39:
			codeused = "BOA"
	if	count	== 40:
			codeused = "BOB"
	if	count	== 41:
			codeused = "BOG"
	if	count	== 42:
			codeused = "BPA"
	if	count	== 43:
			codeused = "BWG"
	if	count	== 44:
			codeused = "C9N"
	if	count	== 45:
			codeused = "C8E"
	if	count	== 46:
			codeused = "C7J"
	if	count	== 47:
			codeused = "CDH"
	if	count	== 48:
			codeused = "CFA"
	if	count	== 49:
			codeused = "CIT"
	if	count	== 50:
			codeused = "CLX"
	if	count	== 51:
			codeused = "CNL"
	if	count	== 52:
			codeused = "COK"
	if	count	== 53:
			codeused = "COX"
	if	count	== 54:
			codeused = "CRP"
	if	count	== 55:
			codeused = "CVG"
	if	count	== 56:
			codeused = "CUE"
	if	count	== 57:
			codeused = "DBK"
	if	count	== 58:
			codeused = "DCX"
	if	count	== 59:
			codeused = "DEL"
	if	count	== 60:
			codeused = "DEV"
	if	count	== 61:
			codeused = "DIS"
	if	count	== 62:
			codeused = "DLA"
	if	count	== 63:
			codeused = "DTC"
	if	count	== 64:
			codeused = "D18"
	if	count	== 65:
			codeused = "D50"
	if	count	== 66:
			codeused = "D52"
	if	count	== 67:
			codeused = "D55"
	if	count	== 68:
			codeused = "D55"
	if	count	== 69:
			codeused = "D56"
	if	count	== 70:
			codeused = "D58"
	if	count	== 71:
			codeused = "D60"
	if	count	== 72:
			codeused = "D86"
	if	count	== 73:
			codeused = "EAT"
	if	count	== 74:
			codeused = "EDD"
	if	count	== 75:
			codeused = "EDS"
	if	count	== 76:
			codeused = "EMC"
	if	count	== 77:
			codeused = "EMP"
	if	count	== 78:
			codeused = "EMV"
	if	count	== 79:
			codeused = "ENC"
	if	count	== 80:
			codeused = "E0P"
	if	count	== 81:
			codeused = "ESC"
	if	count	== 82:
			codeused = "ES8"
	if	count	== 83:
			codeused = "F8L"
	if	count	== 84:
			codeused = "FAL"
	if	count	== 85:
			codeused = "FAL"
	if	count	== 86:
			codeused = "FBL"
	if	count	== 87:
			codeused = "FDU"
	if	count	== 88:
			codeused = "FED"
	if	count	== 89:
			codeused = "FLT"
	if	count	== 90:
			codeused = "FML"
	if	count	== 91:
			codeused = "FPL"
	if	count	== 92:
			codeused = "FRD"
	if	count	== 93:
			codeused = "FUJ"
	if	count	== 94:
			codeused = "FUS"
	if	count	== 95:
			codeused = "FXL"
	if	count	== 96:
			codeused = "GAP"
	if	count	== 97:
			codeused = "GAR"
	if	count	== 98:
			codeused = "GGL"
	if	count	== 99:
			codeused = "GMC"
	if	count	== 100:
			codeused = "GOV"
	if	count	== 101:
			codeused = "H30"
	if	count	== 102:
			codeused = "H77"
	if	count	== 103:
			codeused = "HOL"
	if	count	== 104:
			codeused = "HON"
	if	count	== 105:
			codeused = "HPR"
	if	count	== 106:
			codeused = "HSB"
	if	count	== 107:
			codeused = "I24"
	if	count	== 108:
			codeused = "IBM"
	if	count	== 109:
			codeused = "IBS"
	if	count	== 110:
			codeused = "INC"
	if	count	== 111:
			codeused = "JCP"
	if	count	== 112:
			codeused = "JPM"
	if	count	== 113:
			codeused = "KRO"
	if	count	== 114:
			codeused = "LEH"
	if	count	== 115:
			codeused = "LGM"
	if	count	== 116:
			codeused = "LHS"
	if	count	== 117:
			codeused = "LLR"
	if	count	== 118:
			codeused = "LOW"
	if	count	== 119:
			codeused = "LPR"
	if	count	== 120:
			codeused = "LRR"
	if	count	== 121:
			codeused = "LTS"
	if	count	== 122:
			codeused = "LVU"
	if	count	== 123:
			codeused = "M9W"
	if	count	== 124:
			codeused = "M11"
	if	count	== 125:
			codeused = "M12"
	if	count	== 126:
			codeused = "MAA"
	if	count	== 127:
			codeused = "MAJ"
	if	count	== 128:
			codeused = "MCO"
	if	count	== 129:
			codeused = "MEB"
	if	count	== 130:
			codeused = "MFF"
	if	count	== 131:
			codeused = "MMM"
	if	count	== 132:
			codeused = "MMP"
	if	count	== 133:
			codeused = "MMR"
	if	count	== 134:
			codeused = "MOG"
	if	count	== 135:
			codeused = "MOS"
	if	count	== 136:
			codeused = "N8R"
	if	count	== 137:
			codeused = "N9R"
	if	count	== 138:
			codeused = "NCL"
	if	count	== 139:
			codeused = "NCY"
	if	count	== 140:
			codeused = "NIS"
	if	count	== 141:
			codeused = "NKE"
	if	count	== 142:
			codeused = "NOR"
	if	count	== 143:
			codeused = "NOV"
	if	count	== 144:
			codeused = "NPR"
	if	count	== 145:
			codeused = "NVL"






	#webpage select
	driver.get("https://www.marriott.com/default.mi")


	#clicks on destination text box
	destination = WebDriverWait(driver, 20).until(
	EC.element_to_be_clickable((By.NAME, "destinationAddress.destination")))
	destination.click()

	#enters destination name
	destination.send_keys(Keys.CONTROL + "a")
	destination.send_keys(Keys.DELETE)
	destination.send_keys(destinationName)
	destination.send_keys(Keys.TAB)

	#clicks dropdown to show corp button
	dropdown = driver.find_element_by_xpath("/html/body/main/div/div/div/div/div/div/div/div/div[1]/div/div/form/div[2]/div[2]/button")
	dropdown.click()
	time.sleep(1)

	#selects corp code as an option
	corpselect = driver.find_element_by_xpath("/html/body/main/div/div/div/div/div/div/div/div/div[1]/div/div/form/div[2]/div[2]/div/fieldset/div/div[5]")
	corpselect.click()
	time.sleep(1)

	#types in promo code
	entercode = driver.find_element_by_xpath("/html/body/main/div/div/div/div/div/div/div/div/div[1]/div/div/form/div[2]/div[2]/div/fieldset/div/div[6]/div/input")
	entercode.send_keys(codeused)
	entercode.send_keys(Keys.ENTER)
	time.sleep(1)

	#clicks on search
	clickSearch = driver.find_element_by_xpath("/html/body/main/div/div/div/div/div/div/div/div/div[1]/div/div/form/span[2]/button")
	clickSearch.click()
	time.sleep(2)

	#gets Hotel Names
	hotelpricesR = []
	hotelnames = driver.find_elements_by_class_name("l-property-name")
	hotelprices = driver.find_elements_by_xpath("//*[@class='t-price  m-display-block ']")
	print("\n")


	#make sure length of data is at least >1 (price data sometimes has spaces in it for some reason)
	hotelpricesR = [x.text for x in hotelprices if len(x.text) > 0]

	
	i = 0
	for hotelname, x in zip(hotelnames, hotelpricesR):
		print(hotelname.text)
		print(x)
		

		#writes the data into csv file (excluding commas because of obvious reasons)
		f.write("\n"+ hotelname.text.replace(',','') + "," + x + "," + codeused)

	

	#indicates script to use next code
	count = count + 1


	time.sleep(2)





	driver.delete_all_cookies()


	time.sleep(2)




