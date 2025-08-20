"# mongodb-CRUD-Server" 
# mongodb-CRUD-Server

Basic CRUD server for MongoDB.

## Getting Started
1. Install dependencies:
	```bash
	pip install -r requirements.txt
	```
2. Run the server:
	```bash
	python services/data_loader/server.py
	```

## Usage
The server provides a CRUD interface for working with a MongoDB database.

## OpenShift Deployment
This project includes basic configuration files for deploying the MongoDB CRUD server on OpenShift.

Deployment files are located in the `infrastructure/k8s/` directory.

To deploy:
1. Make sure you have access to an OpenShift cluster.
2. Apply the Kubernetes manifests using the OpenShift CLI:
	```bash
	oc apply -f infrastructure/k8s/
	```
3. Update secrets and environment variables as needed for your environment.
