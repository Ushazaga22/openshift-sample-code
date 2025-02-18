# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install dependencies
#RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8080
EXPOSE 8080

# Define the command to run the application
CMD ["python", "app.py"]
