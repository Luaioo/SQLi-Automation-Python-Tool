# SQL injection Automation Python Tool

The tool was used for a blind SQL injection vulnerability. The Vulnerable web application uses a tracking cookie for analytics, and performs an SQL query containing the value of the submitted cookie.

The results of the SQL query are not returned, and the application does not respond any differently based on whether the query returns any rows. If the SQL query causes an error, then the application returns a custom error message. 


#Implementation

Vulnerable parameter - tracking cookie
