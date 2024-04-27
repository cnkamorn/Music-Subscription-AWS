# Music-Subscription-AWS

This document describes the AWS architecture for a music streaming application. <br> The application utilizes various AWS services to handle user accounts, music data, user subscriptions, and functionalities.

Services Used:<br>
Amazon DynamoDB: NoSQL database service for storing user login information (login table) and music data (music table).<br>
Amazon S3: Object storage service for storing artist images.<br>
AWS Lambda: Serverless compute service for handling user interactions through API Gateway.<br>
Amazon API Gateway: Service for creating, publishing, and managing APIs to access DynamoDB.<br>

Techology Used:<br>
Javascript : Calling APIs based on user action such as Register,Login,Search Music, Subscription Music and Unsubscription<br>
Bootstrap5 : Library for designing the frontend page<br>

Video demo: https://www.loom.com/share/ad72a27bd4584fd09b4a1e40c68d7bdf?sid=8adc4038-4e71-4723-959a-652eb799bdce

<img width="1043" alt="Diagram" src="https://github.com/cnkamorn/Music-Subscription-AWS/assets/92679212/94b7ffca-dffb-45cf-99b7-cf8fc6487482">
<img width="255" alt="API Gateway" src="https://github.com/cnkamorn/Music-Subscription-AWS/assets/92679212/a672d998-9f9f-4bb5-add9-2ebf7f7570e4">
<img width="1146" alt="Screenshot 2567-04-27 at 17 45 55" src="https://github.com/cnkamorn/Music-Subscription-AWS/assets/92679212/d998d595-3ac4-4604-98a7-7d06d13e46d4">
<img width="1095" alt="Screenshot 2567-04-27 at 17 46 24" src="https://github.com/cnkamorn/Music-Subscription-AWS/assets/92679212/2f7fb4ef-17a0-4019-aac7-11e7b04c14e8">
