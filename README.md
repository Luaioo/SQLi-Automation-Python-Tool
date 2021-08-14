# Blind SQL injection Automation Python Tool

### Overview

The tool was used for a blind SQL injection vulnerability. The Vulnerable web application uses a tracking cookie for analytics, and performs an SQL query containing the value of the submitted cookie.

The results of the SQL query are not returned, and the application does not respond any differently based on whether the query returns any rows. If the SQL query causes an error, then the application returns a custom error message. 


### How to Setup
1. Setup your burpsuite proxy to `127.0.0.1:8080`
2. Write any SQLi query and paste it in the `sqli_payload` paramenter 
3. Paste the value of all your cookies value in the `cookies` paramenter


#### Setup the App Proxy

| Main Fragment |
| -----------  |
|![Capture](https://user-images.githubusercontent.com/33663456/122086588-6bf97b00-ce36-11eb-8261-31a627fc54bc.PNG)|

## Testing  

The develoepr has tested only  two major functions which are get list of movies as well as get movie by ID 


