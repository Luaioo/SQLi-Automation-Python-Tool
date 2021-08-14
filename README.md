# Blind SQL injection Automation Python Tool

### Overview

The tool was used for a blind SQL injection vulnerability. The Vulnerable web application uses a tracking cookie for analytics, and performs an SQL query containing the value of the submitted cookie.

The results of the SQL query are not returned, and the application does not respond any differently based on whether the query returns any rows. If the SQL query causes an error, then the application returns a custom error message. 


### How to Setup
1. Setup your burpsuite proxy to `127.0.0.1:8080`
2. Write any SQLi query and paste it in the `sqli_payload` paramenter 
3. Paste the value of all your cookies value in the `cookies` paramenter


### How to Reproduce 
Use this command to run the python tool you just setup:

`Python3 (File-Name.py) "Vulnerable Applicatin URL"`


| Screenshot |
|------------|
|![Screenshot_2021-08-14_21-31-13](https://user-images.githubusercontent.com/68829493/129447871-2ea99dda-c312-4229-ab89-782ee70acc19.png)
|



