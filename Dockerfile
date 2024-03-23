# Use an official Python runtime as the base image
FROM python:3.10

# Set the working directory in the container
WORKDIR /Data_Extraction

# Copy the current directory contents into the container at /Data_Extraction
COPY . /Data_Extraction

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Define environment variable
ENV PYTHONPATH "${PYTHONPATH}:/Data_Extraction"

# Define a volume for storing uploaded configuration files
VOLUME /Data_Extraction

# Expose port
EXPOSE 8501

# Command to run the application
# CMD ["python", "/main/main.py"]
