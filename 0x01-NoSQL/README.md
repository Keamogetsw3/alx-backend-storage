# 0x01. NoSQL
## Back-end
## NoSQL
## MongoDB
**Weight:** 1  
**Project over - took place from Oct 21, 2024 6:00 AM to Oct 23, 2024 6:00 AM**  
An auto review will be launched at the deadline  
## In a nutshell…  
Auto QA review: **0.0/135 mandatory & 0.0/32 optional**  
Altogether: **0.0%**  
Mandatory: **0.0%**  
Optional: **0.0%**  
Calculation: **0.0% + (0.0% * 0.0%) == 0.0%**  
## Resources  
Read or watch:  
- NoSQL Databases Explained  
- What is NoSQL?  
- MongoDB with Python Crash Course - Tutorial for Beginners  
- MongoDB Tutorial 2: Insert, Update, Remove, Query  
- Aggregation  
- Introduction to MongoDB and Python  
- mongo Shell Methods  
- Mongosh  
## Learning Objectives  
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:  
### General  
- What NoSQL means  
- What is difference between SQL and NoSQL  
- What is ACID  
- What is a document storage  
- What are NoSQL types  
- What are benefits of a NoSQL database  
- How to query information from a NoSQL database  
- How to insert/update/delete information from a NoSQL database  
- How to use MongoDB  
## Requirements  
### MongoDB Command File  
- All your files will be interpreted/compiled on **Ubuntu 18.04 LTS** using **MongoDB (version 4.2)**  
- All your files should end with a new line  
- The first line of all your files should be a comment: \`// my comment\`  
- A \`README.md\` file, at the root of the project folder, is **mandatory**  
- The length of your files will be tested using \`wc\`  
### Python Scripts  
- All your files will be interpreted/compiled on **Ubuntu 18.04 LTS** using **python3 (version 3.7)** and **PyMongo (version 3.10)**  
- All your files should end with a new line  
- The first line of all your files should be exactly:  
\`\`\`python
#!/usr/bin/env python3
\`\`\`  
- A \`README.md\` file, at the root of the folder of the project, is **mandatory**  
- Your code should use the **pycodestyle style (version 2.5.\*)**  
- The length of your files will be tested using \`wc\`  
- All your modules should have documentation:  
\`\`\`python
python3 -c 'print(__import__("my_module").__doc__)'
\`\`\`  
- All your functions should have documentation:  
\`\`\`python
python3 -c 'print(__import__("my_module").my_function.__doc__)'
\`\`\`  
- Your code should not be executed when imported:  
\`\`\`python
if __name__ == "__main__":
\`\`\`  
## More Info  
### Install MongoDB 4.2 in Ubuntu 18.04  
Official installation guide  
\`\`\`sh
wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | apt-key add -
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" > /etc/apt/sources.list.d/mongodb-org-4.2.list
sudo apt-get update
sudo apt-get install -y mongodb-org
sudo service mongod status
\`\`\`  
### Check MongoDB Version  
\`\`\`sh
mongo --version
\`\`\`  
### Install PyMongo  
\`\`\`sh
pip3 install pymongo
python3 -c "import pymongo; print(pymongo.__version__)"
\`\`\`  
### Fix Missing Data Directory  
\`\`\`sh
sudo mkdir -p /data/db
\`\`\`  
### Start MongoDB Service  
\`\`\`sh
service mongod start
\`\`\`  
### List Databases  
\`\`\`sh
cat 0-list_databases | mongo
\`\`\`  