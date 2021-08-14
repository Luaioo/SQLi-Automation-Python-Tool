# SQL injection Automation Python Tool

The tool was used for a blind SQL injection vulnerability. The Vulnerable web application uses a tracking cookie for analytics, and performs an SQL query containing the value of the submitted cookie.

The results of the SQL query are not returned, and the application does not respond any differently based on whether the query returns any rows. If the SQL query causes an error, then the application returns a custom error message. 


### Implementation 
| Main Fragment |Movie Details |Search Articles |
| ----------- | ----------- | ----------- |
| ![Capture](https://user-images.githubusercontent.com/33663456/122086588-6bf97b00-ce36-11eb-8261-31a627fc54bc.PNG)
| ![Capture1](https://user-images.githubusercontent.com/33663456/122086626-761b7980-ce36-11eb-9c55-32001c12d90f.PNG)
| ![Capture3](https://user-images.githubusercontent.com/33663456/122086635-7a479700-ce36-11eb-8598-845414b43434.PNG)|

## Testing  

The develoepr has tested only  two major functions which are get list of movies as well as get movie by ID 


