# PIP-University-Administration-System

## This web application is meant to comprise the goals posited in the [Case Study pdf file](CaseStudy.pdf). The folder for this application is [PIP_WebApp](PIP_WebApp/); once inside this folder and with a virtual environment with python 3.7 or higher and the required libraries setup, the application runs with the following command line: `python app.py` or `python3 app.py`. If execution is running properly, open your preferred browser on `http://localhost:5000` to interact with frontend.

## [Data Model](Data_Model/) contains the mysql ERR diagram.

## [PIP-RAMG](PIP-RAMG.md) is a Markdown with links and references to the different technologies and concepts touched in this project. As well, it includes some courses and tutorials. 

## [PIP Backlog](PIP-Backlog.xlsx) is Microsoft ® Excel ™ file with the backlog of this project. Includes Estimated deadlines and the actual dates of completion. 

## [Resources & Cheatsheets](Resources_&_Cheatsheets/) contains tips and tricks for different technologies and material from courses from which this project got its basis. The [Flask Web App from Coursera](Flask_Web_App_Coursera/) folder contains the material from a [Coursera Guided Project](https://www.coursera.org/projects/python-flask) from which I based the app distribution, functionality, layout and modularity. The [Flask SQLAlchemy Basics from Pretty Print](Resources_&_Cheatsheets/flask_sqlalchemy_basics_Pretty_Print) contains useful material from [Anthony Herbert's courses website](https://prettyprinted.com/) from which I based the data models and relationships. 

### about migrations: [SQLAlchemy db migrate](https://www.youtube.com/watch?v=wCa_H4U-QTM)
### more about SQLAlchemy with [Real Python GitHub](https://github.com/realpython/materials/tree/master/python-sqlite-sqlalchemy)

## Docker: 
## [PSL Fusion Course](https://ehec.fa.em2.oraclecloud.com/hcmUI/faces/FuseWelcome?_adf.ctrl-state=hm4yqnd1y_1&_adf.no-new-window-redirect=true&_afrLoop=8373842398717950&_afrWindowMode=2&_afrWindowId=obntqs4nr&_afrFS=16&_afrMT=screen&_afrMFW=1215&_afrMFH=649&_afrMFDW=1280&_afrMFDH=720&_afrMFC=8&_afrMFCI=0&_afrMFM=0&_afrMFR=144&_afrMFG=0&_afrMFS=0&_afrMFO=0) has a complete introduction about the fundamentals of Docker. 
## As a basis for Dockerfile and Docker-Compose, this article in _Medium_ helped perfectly: [Docker + Flask](https://towardsdatascience.com/how-to-dockerize-an-existing-flask-application-115408463e1c)

## [How to push a docker image into docker hub](https://jhooq.com/requested-access-to-resource-is-denied/)

## A basis on [loading directories to a Docker Image](https://towardsdatascience.com/how-to-mount-a-directory-inside-a-docker-container-4cee379c298b)
## Some input on [Pipenv and the importance on virtual environments](https://towardsdatascience.com/virtual-environments-for-data-science-running-python-and-jupyter-with-pipenv-c6cb6c44a405)
## I chose to use Google Cloud Platform as a Cloud service provider because they offer $ 300.00 US just for opening a starting trial account. 
## After enrolling to the trial subscription, they threw in another $ 100.00 US. ($ 400.00 US for 90 days)

## Therefore, I followed this _Towards Data Science_ article about deploying dockerized flask apps into  [GCP](https://towardsdatascience.com/deploying-containers-with-docker-gcp-cloud-run-and-flask-restful-809e0ffa1f3) and [Edward Kruger Repository on Deploying Flask Apps with GCP's Cloud Run](https://github.com/edkrueger/sars-fastapi) following this _Towards Data Science_ [article](https://towardsdatascience.com/deploy-a-dockerized-flask-app-to-google-cloud-platform-71d91b39b25e),

## [Abby Carey Repository as an introduction to Cloud Run](https://github.com/abbycar/python-tabs-vs-spaces-public/blob/main/app.py) with [video on PyCharm IDE and Cloud Code Infra](https://www.youtube.com/watch?v=1hd05Ti79AM)