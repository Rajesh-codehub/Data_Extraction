# Data Extraction
Extracting or ingecting data files from multiple sources and load into local repositary

**pre-requesites**
python
pandas
SQL
basic streamlit 



**installation and setup**

step-1

clone the github repository:
# $ git clone [RepoUrl](https://github.com/yourusername/yourproject.git)

step-2

navigate to the project directory
# $ cd project

step-3

download and install docker desktop from docker hub

link: **https://www.docker.com/products/docker-desktop/**

step -4

**open terminal and check docker version*

**docker --verison** with this command

step-5

create docker image 

cmd : **docker build -t data_extraction:datatag .**

step-6

**docker command**

$ docker run -v host_path:/Data_Extraction -p 8501:8501 data_extraction:datatag streamlit run 

: host_path = the path where your data_extraction repo cloned from the bitbucket see the example below
: data_extraction:datatag is a docker image we created previously.

** demo command **

docker run -v C:/Users/rajes/repo/repository/Data_Extraction:/Data_Extraction -p 8501:8501 data_extraction:datatag streamlit run main/main.py

**user guide**

# before running the container you need to add input parameters in the config file that is presented in the Config files directary

**step-1**

add data file to the source files folder

**step-2**

give input path, format, and file name in the config.csv and give last line input path where you want to store the data files you extracted previously and format = csv and add ',' at last and save.



**step-4**

run the docker container 

**step-5**

upload the previous config file here and Done. you will get the data profiling and data extraction done.







