# Blind SQL injection Automation Python Tool

### Vulnerability
The tool was used for a blind SQL injection vulnerability. The application uses a tracking cookie for analytics, and performs an SQL query containing the value of the submitted cookie.

The results of the SQL query are not returned, and the application does not respond any differently based on whether the query returns any rows. If the SQL query causes an error, then the application returns a custom error message. 

### Tool Overview

The tool Brute-force multiple requests trying all the alphanumeric characters based on the ascii table. when any charicter matches the first letter of the password it moves on to checkes the secound charcter and so on until the full password is identified.

### How to Setup
1. Setup your burpsuite proxy to `127.0.0.1:8080`

2. Write the SQLi query and paste it in the `sqli_payload` paramenter 

3. Paste the value of all the cookies in the `cookies_sqli` paramenter

| Screenshot |
|------------|
|![Screenshot_2021-08-15_02-38-32](https://user-images.githubusercontent.com/68829493/129457161-22384c76-c433-4a7e-814c-8e8db48152b6.png)

### How to Reproduce 
Use this command to run the python tool you just setup:

`Python3 File-Name.py "Vulnerable URL"`


| Screenshot |
|------------|
|![Screenshot](https://user-images.githubusercontent.com/68829493/129448628-67a2a1f4-0bed-4a01-a30c-221be35646f6.jpg)


