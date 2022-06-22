# cloud_tools

[![Build Status](http://bondi.local:3001/api/badges/Halfwalker/Cloud_tools/status.svg)](http://bondi.local:3001/Halfwalker/Cloud_tools)

This is a simple playbook to install a useful set of tools for dealing with cloud type things.

### Install latest ansible with :
```
sudo apt install --no-install-recommends software-properties-common
sudo add-apt-repository --yes --update ppa:ansible/ansible
sudo apt install -qq --yes --no-install-recommends ansible git
```

### Create a hosts file with the following contents
```
localhost ansible_connection=local ansible_python_interpreter=/usr/bin/python3
```

### Optional : Set a github user/token var to avoid rate-limiting

Github may sometimes rate-limit non-authenticated access, which can cause the playbook to fail.  If you don't already have one, you can [Create a personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) for github.  Then set the **GH_USER** and **GH_TOKEN** environment variables as follows
```
export GH_USER=my_github_username
export GH_TOKEN=3739blahblah873298573248597325
```

### Install all tools with
```
ansible-playbook -K -i hosts cloud_tools.yml -l localhost
```

### Default list of tools installed

* [vault](https://www.vaultproject.io/downloads)
* [minikube](https://kubernetes.io/docs/tasks/tools/install-minikube/)
* [kind](https://kind.sigs.k8s.io/docs/user/quick-start/)
* kubernetes (installs these packages)
    * [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
    * [kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/)
* [Kui](https://github.com/kubernetes-sigs/kui)
* [skaffold](https://skaffold.dev/docs/install/)
* [helm](https://helm.sh/docs/intro/install/)
* [docker-machine](https://github.com/docker/machine/releases)
* [docker-compose](https://github.com/docker/compose/releases)
* [dive (docker layer stats)](https://github.com/wagoodman/dive)
* [dlayer (docker layer stats](https://github.com/wercker/dlayer)
* [AWS awscli (v2)](https://aws.amazon.com/cli/)
* [AWS gimme-aws-creds](https://github.com/Nike-Inc/gimme-aws-creds)
* [AWS ecs-cli](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ECS_CLI_installation.html)
* [AWS eksctl](https://github.com/weaveworks/eksctl)
* [Azure azure-cli](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli)
* [Terraform](https://www.terraform.io/downloads)

### Install subset of tools

Build a list of the tools to install with the following syntax - set the variable **cloud_tools** to the list of desired tools by name above.  The list should be comma-delimited, inside square-brackets.
```
ansible-playbook -K -i hosts cloud_tools.yml -l localhost --extra-vars '{cloud_tools: [ awscli, eksctl, kubernetes ] }'
```

