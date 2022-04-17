# Marriott-Corporate-Code-Tester
***Disclaimer: this is for educational purposes only and for data gathering. I am not affiliated with Marriott hotels, and not responsible for how you use the codes/prices retrieved from this script.***

***Description***
This script is meant to test out each Corporate code in order to see which one has the greatest discount for the city of your choice. Specific hotels per city have better partnerships with each company depending on their usage. So instead of typing each code individually, this script will find the best prices and input it into a .csv file which you can then turn into an excel file and sort by price. 

There is no option to select dates however, since in general these rates to not change by the time of the year. These rates depend on the type of partnership said company has with the individual hotel. 

***Dependancies:***
Please download and install all dependancies for script to work.
- Python https://www.python.org/downloads/
- Selenium https://selenium-python.readthedocs.io/installation.html
- Webdriver Manager https://pypi.org/project/webdriver-manager/

If you have any trouble installing these, a simple google search will help you out.

The scirpt of course works with any operating system in which python and selenium are available including Mac OS and Windows.


***Steps***
Download .py file 

Install dependancies. 

Once dependancies are installed. It is recommended to create a folder in your desktop and then save the python script file to that file. This is because when the .csv file is created it is better for it to be easily accesible. 

Open the .py file with the code editor of your choice and change "destinationName" to whatever destiantion you want in the following format: "City, State, Country". After this, you can build and run the script. 


***Known Bugs:***
Since script inputs data into CSV file (comma separated values), prices over $1,000 USD will create a new row of data for such hotel since the extra comma will create the new column. This is not to worry however since it does not interfere with the rest of the data. 




