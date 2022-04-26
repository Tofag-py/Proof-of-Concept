# Proof-of-Concept
DevOps Proof of Concept


### 1. Data extraction

As first task, we want you to write a Python script that fetches all breweries from our API. You will find the API endpoint below. The response by the API is paginated which means you will only get 20 results per page by default. This can be controlled with the `per_page` query param. To fetch another page but the first one, you can provide the `page` param.

The script should take the `page` and `per_page` parameters as input.

Endpoint: `https://informed-data-challenge.netlify.app/api/breweries`

### 2. Data Loading

In this step, we want to load the data into a PostgreSQL database. For this, we want you take use the Python script to fetch the data from the previous task and save the breweries it in the database. The goal is to have the data available for DevOps Deployment. Think about creating the correct database structure to store this information.

### 3. DevOps Practices.
1.	Deploy an ECC for the application to run
2.	Create systems for Dev, Testing and production
3.	If you can use AWS lambda, Deploy it as a serverless computing solution
4.	Deploy Version control, CICD, IAAC use your prefer tool
5.	Make sure the application is dockerized so that the APP can communicate with the DB
6.	You can push it to ECR and make the app to run in a cluster
7.	Basic AWS security practices on VPC, IAM etc should be implemented.


