# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt into the container
COPY requirements.txt /app/requirements.txt

# Copy main.py into the container
COPY main.py /app/main.py

# Copy the current directory contents of api into the container at /app
COPY api /app/api

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt --timeout=120

# Make port 4000 available to the world outside this container
EXPOSE 4000

# Define environment variable
ENV FLASK_APP=main.py
ENV FLASK_ENV=development

# Run main.py when the container launches
CMD ["python", "main.py"]