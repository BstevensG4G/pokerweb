# Use the official Python 3.8 slim image as the base image
FROM python:3.8-slim

# Set the working directory within the container
WORKDIR /

# Copy the necessary files and directories into the container
COPY requirements.txt .
# Upgrade pip and install Python dependencies
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose port 8000 for the Flask application
EXPOSE 8000

# Define the command to run the Flask application using Gunicorn
#CMD ["gunicorn", "-b", "0.0.0.0:8000", "pokerweb:gunicorn_app", "-w", "4"]
CMD ["flask", "--app", "pokerweb", "run", "--debug"]
