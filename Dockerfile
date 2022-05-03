# Set base image (host OS)
FROM python:3.9.12

# By default, listen on port 6000
EXPOSE 6000/tcp

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .
COPY recommendation.py .
COPY Hewa.db .

# Install any dependencies
RUN pip install -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY app.py .

# Specify the command to run on container start
CMD [ "python", "./app.py" ]