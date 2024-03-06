Description:

Our Key-Value Store (KVS) is a scalable and robust system built to efficiently store and retrieve data using Kubernetes (k8s), FastAPI, and Huey as a REDIS queue. The primary goal of this project is to provide a reliable solution for managing key-value pairs while ensuring scalability across multiple pods/deployments.

The KVS allows users to store, retrieve, update, and delete key-value pairs through a RESTful API provided by FastAPI. Underneath the hood, Huey, a lightweight task queue, is utilized as a Redis-backed queue to handle asynchronous tasks such as background processing and queuing requests. Kubernetes orchestrates and manages the deployment and scaling of our system, ensuring high availability and fault tolerance.

Technologies Used:

--> FastAPI: A modern, fast (high-performance) web framework for building APIs with Python 3.7+.

--> Huey: A lightweight task queue for Python that supports scheduling tasks and background processing with Redis as a backend.

--> Redis: Used as a backend for Huey task queue, providing persistence and scalability for queued tasks.

--> Python: Programming language used for implementing the backend logic and API endpoints.

--> Docker: Used for containerizing the application components for deployment within Kubernetes.

--> Git: Version control system for tracking changes and collaborating on the project.

--> GitHub: Hosting platform for the project repository, facilitating collaboration and version control.

--> YAML: Used for defining Kubernetes manifests for deploying and managing resources.

--> RESTful API: Utilized to interact with the key-value store, enabling CRUD operations on stored data.

--> JSON: Data interchange format used for transferring data between the client and the server via the API.

--> Documentation: Comprehensive documentation covering installation, usage, API endpoints, and architecture to guide users and contributors effectively.



This project aims to deliver a scalable, reliable, and well-documented key-value store solution leveraging modern technologies and best practices in software development and infrastructure engineering.



To run this project run the Dockerfile and build an image by running the command:

--> docker build . -f Dockerfile -t <docker_image_name>

Then tag the image:

--> docker tag <docker_image_name> <username/docker_image_name>

After that push the image:

--> docker push <username/docker_image_name>

Run the compose file:

--> docker-compose up


Kubernets files are present in the folder to run pods and scale them, run the below commands:

--> kubectl apply -f app-deployment.yaml

--> kubectl apply -f app-service.yaml

--> kubectl apply -f redis-deployment.yaml

--> kubectl apply -f redis-service.yaml
