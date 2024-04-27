# Music-Subscription-AWS

This document describes the AWS architecture for a music streaming application. The application utilizes various AWS services to handle user accounts, music data, user subscriptions, and functionalities.

Services Used:
Amazon DynamoDB: NoSQL database service for storing user login information (login table) and music data (music table).
Amazon S3: Object storage service for storing artist images.
AWS Lambda: Serverless compute service for handling user interactions through API Gateway.
Amazon API Gateway: Service for creating, publishing, and managing APIs to access DynamoDB.

Techology Used:
Javascript : Calling APIs based on user action such as Register,Login,Search Music, Subscription Music and Unsubscription
Bootstrap5 : Library for designing the frontend page

<img width="1043" alt="Diagram" src="https://github.com/cnkamorn/Music-Subscription-AWS/assets/92679212/94b7ffca-dffb-45cf-99b7-cf8fc6487482">
<img width="255" alt="API Gateway" src="https://github.com/cnkamorn/Music-Subscription-AWS/assets/92679212/a672d998-9f9f-4bb5-add9-2ebf7f7570e4">
