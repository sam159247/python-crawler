# Python crawler - Taiwan Pay ATM Maps

----
## Introduction
Taiwan Pay provides an overseas withdrawal service which the transaction fee is cheaper than wire transfer's. It's an useful service for foreign travellers if they have no cash. see [Taiwan Pay](https://www.taiwanpay.com.tw/content/info/japan.aspx). 

The problem is where are those ATMs. Taiwan Pay provides a search function to search the information of ATMs. see [Taiwan Pay search ATMs](https://www.taiwanpay.com.tw/content/info/others.aspx). It's good enough but most of foreign travellers may not know about the system of address in other countries so that they have no idea how to input the keywords.

----
## Solution
Output all the address from Taiwan Pay and input to Google MyMaps.

----
## Requirements
* Python 3

----
## Usage
1. Excute taiwanpay_crawler.py to get the `mapsdata.csv`
2. Open [Google MyMaps](https://www.google.com/mymaps)
3. Click `CREATE A NEW MAP` button.
4. Click `import` link.
5. Select `mapsdata.csv` file made from taiwanpay_crawler.py
6. Done!

----
## Note 
This website built using ASP.net, access the website first time to get 
`__VIEWSTATE`, 
`__VIEWSTATEGENERATOR`, 
`__EVENTVALIDATION`.
And use them with post next time.


