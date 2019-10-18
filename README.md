# Documentation Team Banh Mi
### Team Members: 
- Alexander Helber 
- Quang Thong Nguyen
- Dung Nguyen
- Kevin Cieslik
- Dinh An Ho
# Description of the project
### 1. The inital setting and problem
The target of the hackathon is the development of approaches for improving station-based carsharing. The given scenario is considered to be a landlord who offers *e.Base Home*, a carsharing service, to his tenants in a sub-urban neighbourhood . Although it was well received, it turned out that the service was not cost covering due to a low rate of utilization. Due to the landlord's desire to be climate-friendly, not only profitability is to be increased, but emissions are also to be reduced. Other factors to be considered are the improvement of charging behaviour of the users and the intuitive use of the interface. Moreover, an implementation of gamification is expected in order to enhance user engagement.
### 2. Our approach
We extended the existing application by two main features. 
#### 2.1 Repeated bookings
The tenants in the given scenario are families. It can be expected that there is a demand for transportation that usually occur on the same weekday and time range. Examples for this are daily routines (bringing children to school) and hobbies with fixed appointments (soccer practice). 
Therefore, it is possible to increase the utilization rate of the available cars by encouraging the tenants to use them not only for single rides, but also for their common trips. 
For this purpose, we added an option for repeating bookings of cars on the same day and time for a discounted price. The main advantages of this feature for the customers are that they do not have to worry about forgetting to book the cars for their planned events and benefit from the discount. From the landlord's perspective, the increased and reliable booking of the cars provides planning security and the coverage of costs.
#### 2.2 Gamification
In order to adress the issues *eco-friendlyness* and *user behaviour*, we implemented a gamification-based approach. The applications keeps track of the user's data and visualizes it. Based on the distance travelled by the electric vehicles an estimate of avoided carbon dioxide compared to ICE cars can be calculated. Additionally, based on the fact that a medium-sized tree on average binds 6 kgs of carbon dioxide per year, the value is converted into an equivalent of how many trees bind this avoided amount of emissions. 
### 3. Implementation and Data
We developed our features using Python and for the user interface we additionally employed the framework *Kivy*. We set up a client-server architecture with "bottle" to simulate a realistic usage environment.
The server can use the API to access the database (which includes booking and vehicle information).
The other databases such as the ones containing user data and recurring booking information have been hacked together by storing python data types with pickles. The server repeatedly/regularly runs a task to check if the repeating bookings have been added to the booking database and if not, adds the missing bookings.
Due to the lack of real data, we generated fictional bookings to prove the feasability of our implementation.
#### 4.1 File structure
The main.py file provides the gui functionality and uses the functions in the client.py file to communicate with the server.  
The server.py should be started as a background process first and will listen for requests from the client. It uses functions from the control.py and api_control.py files to access the db trough the API

<!--stackedit_data:
eyJoaXN0b3J5IjpbMzAzOTU0OTg0XX0=
-->
