# cloud_tools

This is a simple playbook to install a useful set of tools for dealing with cloud type things.

### Install latest ansible with :
```
sudo apt install --no-install-recommends software-properties-common
sudo add-apt-repository ppa:ansible/ansible
sudo apt install --no-install-recommends ansible
```

### Create a hosts file with the following contents
```
localhost ansible_connection=local ansible_python_interpreter=/usr/bin/python3
```

### Install with
```
ansible-playbook -K -i hosts cloud_tools.yml -l localhost
```
### Tools installed

* [Minikube](https://kubernetes.io/docs/tasks/tools/install-minikube/)
* [Kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
* [Skaffold](https://skaffold.dev/docs/install/)
* [docker-machine](https://github.com/docker/machine/releases)
* [docker-compose](https://github.com/docker/compose/releases)
* [dive docker layer stats](https://github.com/wagoodman/dive)
* [AWS aws-cli](https://aws.amazon.com/cli/)
* [AWS ecs-cli](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ECS_CLI_installation.html)
* [Azure azure-cli](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli)
