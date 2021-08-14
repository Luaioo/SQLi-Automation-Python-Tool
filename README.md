# SQL injection Automation Python Tool

The tool was used for a blind SQL injection vulnerability. The Vulnerable web application uses a tracking cookie for analytics, and performs an SQL query containing the value of the submitted cookie.

The results of the SQL query are not returned, and the application does not respond any differently based on whether the query returns any rows. If the SQL query causes an error, then the application returns a custom error message. 


### Design application architecture (MVVM)
| MVVM diagram |
| ----------- |
|![Capture](https://user-images.githubusercontent.com/33663456/122086927-c561aa00-ce36-11eb-9758-472c7e99c91a.PNG)

The application will be developed using MVVM architecture
#### Activity Diagram will be used for the following activity and fragments
1. Main Activity 
2. Discover Fragment 
3. popluar news
 #### View Model And Live Data
1. popular ViewModel
2. Article ViewModel
#### Repository
1. App Repository
 #### Repository
1. Remote Data Source which is the API https://developer.nytimes.com/

### implementation 
| Main Fragment |Movie Details |Search Articles |
| ----------- | ----------- | ----------- |
| ![Capture](https://user-images.githubusercontent.com/33663456/122086588-6bf97b00-ce36-11eb-8261-31a627fc54bc.PNG)| ![Capture1](https://user-images.githubusercontent.com/33663456/122086626-761b7980-ce36-11eb-9c55-32001c12d90f.PNG)|![Capture3](https://user-images.githubusercontent.com/33663456/122086635-7a479700-ce36-11eb-8598-845414b43434.PNG)|

## Testing  
## unit testing 
The develoepr has tested only  two major functions which are get list of movies as well as get movie by ID 
### implementation 
| Listing News (Unit Testing) |Searching News (Unit testing) |
| ----------- | ----------- |
| ![getAllMoviews](https://user-images.githubusercontent.com/33663456/122535170-e0f6cb80-d055-11eb-9c30-0c8db852768a.PNG)|![searchApi](https://user-images.githubusercontent.com/33663456/122535217-ebb16080-d055-11eb-8a1f-ee1f5c0a88d6.PNG)
|
## Running this app
To run this app you will need to have an Android device or emulator that supports Android version 6 onward. The device should have an internet connection. 
