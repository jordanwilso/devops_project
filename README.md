# Devops_project - Learning Tracker
## Project Overview
For your portfolio project, you will design and implement the back end for a web-based application with a database component. 
The final web-based application will:
*Implement a 2-tier architecture that includes a Postgres database and the web-based application that interacts with the database. 
* Use Docker Compose to define and manage the tiers. 
* Be pushed to an online repository on GitHub.
* Be deployed to the cloud. 



## Report Instructions
1. What are the various features you would like your project to offer? 
    - My portfolio project is a learning tracker. Users can log in and post projects as their are learning new skills.  
3. What are the API endpoints that you would need to set up for each feature? List them along with the respective HTTP verb, endpoint URL, and any special details (query parameters, request bodies, headers). 

      Request  | URL
      ------------- | -------------
      GET - get a list of projects| http://ec2-52-0-11-54.compute-1.amazonaws.com:8000/api/projects/
     POST - add a project | http://ec2-52-0-11-54.compute-1.amazonaws.com:8000/api/projects/

3. Provide a description of the database tables required for your application, including column names, data types, constraints, and foreign keys. Include your database name. You can optionally include an ER diagram. 
    - The database name. learning_tracker_db. I set up Postgres database using the AWS RDS.
```
      class Project(models.Model):
          title = models.CharField(max_length=100)
          description = models.TextField()
          technology = models.CharField(max_length=20)
          image = models.FilePathField(path="/img")
          tag = models.CharField(max_length=20)
          project_url = models.URLField(max_length=200)
```
## Portfolio Project - Cloud Deployment
I deployed my project in AWS using Docker and AWS Elastic Container Registry. 
![API View](https://github.com/jordanwilso/devops_project/blob/main/API_learning_tracker.png)
![API View](https://github.com/jordanwilso/devops_project/blob/main/insomnia_POST_LT.png)
![error message](https://github.com/jordanwilso/devops_project/blob/main/error_msg.png)

