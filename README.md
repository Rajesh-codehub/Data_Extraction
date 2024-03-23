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

If the project doesn't already have a pyproject.toml file (which indicates it's managed by Poetry), you can initialize Poetry in the project directory:
# $ poetry init
This command will guide you through creating a pyproject.toml file where you can define your project dependencies

step-4

After initializing Poetry, you can install the project dependencies:
# $ poetry install

step-5

Activate the virtual environment created by Poetry:
# $ poetry shell

step-6

You can now run your project as you normally would. Use the poetry run command to run scripts within the virtual environment:
# $ poetry run python myscript.py

**user guide**

# before executing the main function you have to check the and modify the config file  in config folder and set sys path in main python file and check the data file is presented in the location or not.

**step-1**

add data file to the source files folder

**step-2**

give input path, format, and file name in the config.csv and give last line input path where you want to store the data files you extracted previously and format = csv and , at last that it.

**step-3**

modify the system path for accessing modules from the data_extraction in the main.py python file

**step-4**

execute the main.py file if all succedd you will redirect to the streamlit user interface

**step-5**

upload the previous config file here and Done. you will get the data profiling and data extraction done.


# docker installation

**install docker desktop from docker hub**

**go to download.exe in docker directary and double click*

**open terminal and check docker version*
**docker --verison** with this command

create docker image 
**docker build -t myimage .**

**docker commands**
docker run -v C:/Users/rajes/repo/repository/Data_Extraction:/Data_Extraction -p 8501:8501 data_extraction:datatag streamlit run main/main.py

