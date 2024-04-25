## Extracting Sonar scans from LLM-generated code and human-written code
### Prerequisites
In order to be able to run the code scans and export their findings, you need a SonarQube server first. For the purpose of this study, the server deployment implementation occurred as a release of [this](https://github.com/SonarSource/helm-chart-sonarqube/tree/master/charts/sonarqube) helm chart on K3D Kubernetes cluster.

Make sure to follow [this](https://k3d.io/v5.6.3/#releases) documentation to install K3D on your local environment if you want an exact replication. The K3D Kubernetes cluster was created on a Windows 11 machine following 2.1 of [this](https://k3d.io/v5.0.0/usage/exposing_services/#2-via-nodeport). Make sure to expose port 30800 as stated in the documentation. Once that is done, install both [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl-windows/) and [helm](https://helm.sh/docs/intro/install/) command line utilities. Once the Kubernetes cluster is functional, run the following commands in the project root :

```
helm repo add sonarqube https://SonarSource.github.io/helm-chart-sonarqube
helm repo update
helm upgrade --install sonarqube sonarqube/sonarqube --version 10.4.1 -f values.yaml
kubectl apply -f service.yaml
```
Note that at the given version of the helm chart, exposing the server permanently through a Kubernetes service in a K3D setting was only possible via creating a custom service (the one with the manifest in ```service.yaml```)

Also, make sure to have pip 24.0 and Python 3.12.2 on the environment on which you'll run the script for generating scans and exporting them. Run the following command in the root of this project in order tohave all dependencies to run the latter script :

```pip install -r requirments.txt```

Make sure to download the Sonar Scanner executable into the system on which the code scanning and exporting script will run. The Sonar scanner used for generating the findings used in the analysis in the paper is the Sonar Scanner 5.0.1. You can download it from [here](https://docs.sonarsource.com/sonarqube/latest/analyzing-source-code/scanners/sonarscanner/).

### Populating script with environment-specific variables

Before proceeding with running the script to run the code to scan project and export the findings, change the ```sonarqube_url``` and ```sonarqube_token``` variables in ```extract.py```. ```sonarqube_url``` is the SonarQube server address, it is supposed to stay as the default value if the same K3D and helm chart setup was used, otherwise it has be be changed accordingly. For the ```sonarqube_token```, log into the SonarQube server as admin, go to 'My Account'.
<img src="assets\myaccount.png" alt="My account" style="zoom: 150%;" />
Click on 'Security' (the second navbar item from the left) and add a User Token by entering its name and setting its validity period then clicking 'Generate'. Make sure to copy the token and to hold on to it.
<img src="assets\create_token.png" alt="My account" style="zoom: 150%;" />
Assign the value to ```sonarqube_token```.

Now, in the ```sonar_scanner_command``` variables, make sure to replace the sonar scanner placeholder with the path of the Sonar Scanner that is on your local environment.

### File structure

Once obtained, LLM-generated (and human written) code snippets should be placed in the folder suffixed with ```-solutions```, where the canonical solutions are placed in the projects folder prefixed with ```canonical```, the initial LLM solutions are placed in the projects folder prefixed with ```llm```, the LLM-enhanced solutions are placed in the projects folder prefixed with ```llm-enhanced```. Make sure to have an empty folder suffixed with ```-projects``` and prefixed with the same convention for ```-solutions```.

### Running the scanning and exporting
 Run the following command :

 ```python extract.py```

 Three CSV files suffixed with ```-findings.csv``` will be generated, each one is prefixed with the same convention used for ```-projects``` and ```-solutions``` folders.