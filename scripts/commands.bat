oc apply -f mongo-pvc.yaml
oc apply -f mongo-secret.yaml
oc apply -f mongo-deployment.yaml
oc apply -f mongo-service.yaml

docker build -t chaimshvadron/data_loader_mongo:latest .
oc apply -f data_loader_mongo_deployment.yaml
oc apply -f data_loader_mongo_service.yaml

docker build -t chaimshvadron/data_loader_mongo:V2 .
docker push chaimshvadron/data_loader_mongo:V2
