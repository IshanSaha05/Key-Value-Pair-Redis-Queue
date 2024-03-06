# Using Python image
FROM python:3.12.2-slim

# Set the working directory to /app
WORKDIR /app/

# Copy the current directory contents into the container at /app/
COPY . /app/

# Install all the needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make the entry point script executable
RUN chmod +x /app/entrypoint.sh

# Make port 8000 available to the world outside to this container.
EXPOSE 8000

# Run the entry point script when the container starts
ENTRYPOINT ["/app/entrypoint.sh"]
