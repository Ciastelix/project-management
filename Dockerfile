# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Set environment variables
ENV DB_URL=sqlite:///./db.sqlite3
ENV JWT_SECRET=fJJZNs9LnU356LmyTQA8
ENV JWT_ALGORITHM=HS256

# Run the command to start uvcorn server
CMD cd ./src/project_managment && uvicorn main:app --host 0.0.0.0 --port 80