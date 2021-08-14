# Blind SQL injection Automation Python Tool

### Overview

The tool was used for a blind SQL injection vulnerability. The Vulnerable web application uses a tracking cookie for analytics, and performs an SQL query containing the value of the submitted cookie.

The results of the SQL query are not returned, and no error messages are displayed. But the application includes a "Welcome back" message in the page if the query returns any rows. 


### How to Setup
1. Setup your burpsuite proxy to `127.0.0.1:8080`
2. Write any SQLi query and paste it in the `sqli_payload` paramenter 
3. Paste the value of all your cookies value in the `cookies` paramenter


### How to Reproduce 
Use this command to run the python tool you just setup:

`Python3 File-Name.py "Vulnerable URL"`


| Screenshot |
|------------|
|![Screenshot](https://user-images.githubusercontent.com/68829493/129448628-67a2a1f4-0bed-4a01-a30c-221be35646f6.jpg)


