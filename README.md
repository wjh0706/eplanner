# eplanner
### CodeBase
Front End: https://github.com/wjh0706/eplanner_frontend
Auth: https://github.com/wjh0706/eplanner_auth
User: https://github.com/wjh0706/eplanner_user
Event: https://github.com/janisme/Eventplanning (branch: Json_version, Cloud-env)


Authentication -> AWS EC2 with docker
http://ec2-18-206-88-110.compute-1.amazonaws.com/api/auth/user
 
User Profile -> AWS E2C
http://ec2-18-118-30-126.us-east-2.compute.amazonaws.com:8012/


Event -> GCP
URL for web: https://event-service-xwpcijvmmq-uc.a.run.app/
URL for json version: https://event-service-json-xwpcijvmmq-uc.a.run.app/


Front end -> S3
http://eplanner-frontend.s3-website.us-east-2.amazonaws.com/


##Demo Video

Enhance Microservices Implementation:

Service 1:
https://drive.google.com/file/d/1r43fsjhzqJ-0daw36aSis0Ut9LgBDRwE/view?usp=sharing
Service 2:
https://youtu.be/obSC0Md9Yr4?si=rKhDGraW4JdfswuP

Service 3:
https://drive.google.com/file/d/1UBKM8q-d-KGX6Le8n_hdZM5XVeTU1_d-/view?usp=sharing

Pagination:
https://drive.google.com/file/d/1calgiUk1sKtbXTVqVMYUDkvX52B1R6F8/view?usp=sharing


Events, Notifications, Pub/Sub:

Take a screenshot of your code publishing events to any queue systems (SNS, Google Pub/Sub).


Record a video of making a request to a microservice and Lambda function handling the published events.
https://drive.google.com/file/d/138tX-krsdwgdstcsbIqBEePtPKp00Tiq/view?usp=sharing


Composition/Aggregators:

Record a video of a synchronous call that prints a log when get a response from each microservice.
https://drive.google.com/file/d/1uyoRZi-G9nrPvrIJ1aF3ol15vqlkoHab/view

Record a video of an asynchronous call that prints a log when get a response from each microservice. (repeat it 10 times, and it should microservices should be done in a different order at least once).
https://drive.google.com/file/d/1uyoRZi-G9nrPvrIJ1aF3ol15vqlkoHab/view



API Gateway:

Record a video demonstrating your API Gateway Implementation, which shows both authorized and unauthorized cases.
https://clipchamp.com/watch/i67q949oF6s


Record a screenshot and link a code encoding and decoding JWT token.
Decode

Encode


Link
https://github.com/wjh0706/eplanner_auth/tree/main/src/jwt_auth

SSO:

Record a video demonstrating SSO login and making an authorized request using the given token.
https://drive.google.com/file/d/1mZWbhPx1HcbDhvK2CTSm3UceVWAyAg_y/view?usp=sharing


External API:

Explain what External API you are using and what this is for in your application, demonstrate the functionality with a video.

I am using AWS SES to send the verification link to an unverified user’s email to verify the ownership of the email. 

https://drive.google.com/file/d/1bvYlcfwVL1fSUCb0ccd7alfvbmXrGmHJ/view?usp=sharing

Middleware

Introduce one Middleware functionality in your application and explain what it does.
https://drive.google.com/file/d/16Xq7U_zxlwX9WethF8JAXyUXE50-qkHp/view?usp=drive_link

CI/CD

Demonstrate your CI/CD pipelines running on specific events.
https://drive.google.com/file/d/1juDPmvxfY1h1nibMUTfhHsDHb4SpduaJ/view?usp=sharing

Infrastructure As Code

Deploy and shut down any simple infrastructure in your project.
https://clipchamp.com/watch/0LnxkgfpwFf

GraphQL

Implement a simple example of GraphQL using one of the functionalities of your application.
https://drive.google.com/file/d/16Xq7U_zxlwX9WethF8JAXyUXE50-qkHp/view?usp=drive_link


##Introduction
1. Introduction: Description of your service.
As students at Columbia University, we observed that many campus seminars and events held by non-profit organizations resort to using Google Sheets for convenience and cost considerations. However, Google Sheets presents difficulties for organizers in managing user modifications after registration. Additionally, it requires organizers to manually send out post-event surveys to obtain reviews on the event. For attendees, tracking their participation, check-in on events, and searching for similar events are challenging.
To address these issues, We developed this cloud-native application to streamline the management of events organized by domain organizers(Ex, Columbia computer science department to CS students). 
Eplanner enables organizers to organize events, track participants, and acquire feedback efficiently. Moreover, participants can also have a clearer view of the events their domain organizer held with a quicker check-in process.

2. Personas and Roles: Potential Users and Roles in your service.
There are two personas:
User
Event holder is the person who holds events. An event holder is a user who creates an event. The event holder can edit, delete, and mark complete the event as long as he/she is the event holder of this event. If the person is an Event holder, he/she can not be the participant in the specific event.

Participant is the person who joins the event. A participant is a user who can enter any event for which he/she is not an event holder. The participant can register, cancel registration and check-in on the events he/she participates in.
Admin
An administrator can be the event holder or participant of a event(mentioned above). The administrator can also have the right to edit, delete, and mark complete the event even though he/she is not the event holder of this event. An administrator can also register, cancel registration and check-in on the events for other users.
3. Key Features: Main features of your application
Authentication
This feature includes the following actions:
Sign up using their domain email. After signup, the Eplanner will automatically create a user profile within the application. Also, verification of organization email is required.
Log in/log in with their domain email.
Forget and reset password.
User Profile
Each user would have their own profile to record the participation history and personal information. This feature includes the following actions:
Change the user’s information.
Change the user’s picture.
List of the events (past and upcoming events)Plan an event
This feature includes the following actions:
Create an Event.
Delete an Event.
Edit the details of the event.
Mark the event as complete after the completion of the event. 
Take participant
A user who is not an organizer of the event can participate in the event, and this feature includes the following actions:
Register for an event.
Cancel the registration for an event.
Check-in on the event. When a user takes part in the event, the user can check in and take an attendance record.
4. Domain Model Diagram: Visualization of your data in your microservices (Please Indicate what microservice each model belongs to by surrounding them in the same box.)



5. Resource Paths: API Paths for your application for each microservice.
Authentication
Signin: POST api/auth/signin
Signout: POST api/auth/signout
Signup: POST api/auth/signup
Get All Users: GET api/auth/all/{page}{pageSize}
Get Current User: GET api/auth/user
Forget Password: PUT api/auth/forgetpwd
Reset Password: PUT api/auth/resetpwd/{token}
Verification: PUT api/auth/verify/{token}
Send Verification: PUT api/auth/snedverification
Delete Account: PUT api/auth/delete

User Profile
Create Profile: POST api/user/create
Get User Info: GET api/user/{userid}/info
Change Info: PUT api/user/{userid}/info
Change Photo: PUT api/user/{userid}/photo

Event
Get All Event: GET events/
Create: POST events/create/
Delete: DELETE events/view/<event_id>/delete/
Get Event Details: GET events//view/<event_id>/
Edit: PUT events/view/<event_id>/edit/
