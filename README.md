## mlflow_mlop
Machine Learning Model, MLflow for tracking, Flask for user input, Docker for package containerization, AzureDevops for MLOP

## To build, Docker needs:
	Dockerfile
	app.py
	requirements.txt
	
## Inside Docker File:
    FROM python:3.7.3-stretch
    EXPOSE 5000
    # Working Directory
    WORKDIR /app
    
    # Copy source code to working directory
    COPY .  /app/
    
    # Install packages from requirements.txt
    # hadolint ignore=DL3013
    RUN pip install --upgrade pip &&\
    pip install --trusted-host pypi.python.org -r requirements.txt

    ENTRYPOINT [ "python" ] 
    CMD [ "app.py" ] 
	
## Type in requirements.txt:
    flask == 1.1.2
    sklearn
    scipy
    numpy
    pandas
    matplotlib
    seaborn
    schedule
    jupyter
    mlflow
    requests
    schedule

## from command prompt type:

	pip install --user virtualenv
	python -m venv myenvi
	.\myenvi\Scripts\activate

## Install requirements:
	pip install -r requirements.txt
  
## From command prompt type:
	docker build -t testimage .
	docker images --all
	docker run --name testcontainer -p 5000:5000 testimage

Go to docker app, containers/Apps, cick "Open in Browser"
Standard Port : 80, 443,5000  
	
## Flask:
User input A1 and A2 between number 0 or 1
Model predict and show prediction between 0 or 1, 0 for Not Fraud, 1 for Fraud probability.	

## MlFlow
	import mlflow
	import mlflow.sklearn
	remote_server_uri = "http://0.0.0.0:5000"
	mlflow.tracking.get_tracking_uri()
	exp_name = "evaluate_metric"
	mlflow.set_experiment(exp_name)
	mlflow.start_run():
     	
