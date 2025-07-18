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

* [minikube](https://kubernetes.io/docs/tasks/tools/install-minikube/)
* [kind](https://kind.sigs.k8s.io/docs/user/quick-start/)
* [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
* [kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/)
* [kubectx](https://github.com/ahmetb/kubectx)
* [kubens](https://github.com/ahmetb/kubectx)
* [Kui](https://github.com/kubernetes-sigs/kui)
* [skaffold](https://skaffold.dev/docs/install/)
* [helm](https://helm.sh/docs/intro/install/)
* [docker-machine](https://github.com/docker/machine/releases)
* [docker-compose](https://github.com/docker/compose/releases)
* [dive (docker layer stats)](https://github.com/wagoodman/dive)
* [dlayer (docker layer stats)](https://github.com/wercker/dlayer)
* [drone (drone-cli)](https://github.com/drone/drone-cli)
* [AWS awscli (v2)](https://aws.amazon.com/cli/)
* [AWS gimme-aws-creds](https://github.com/Nike-Inc/gimme-aws-creds)
* [AWS ecs-cli](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ECS_CLI_installation.html)
* [AWS eksctl](https://github.com/weaveworks/eksctl)
* [Azure azure-cli](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli)
* [Linode linode-cli](https://www.linode.com/products/cli/)
* [terraform](https://www.terraform0io/downloads) (not supported in Focal/20.04 or below)
* [Terraform-switcher tfswitch](https://github.com/warrensbox/terraform-switcher)
* [vault](https://www.vaultproject.io/downloads) (not supported in Focal/20.04 or below)
* [vagrant](https://www.vagrantup.com/) (not supported in Focal/20.04 or below)
* [Hammer](http://deb.theforeman.org/)
* [github-cli](https://cli.github.com/)

Unfortunately Hashicorp no longer supports Ubuntu Focal/20.04 since it went
EOL in May 2025.  So any Hashicorp tools will be removed from the install list
if we're running under Ubuntu Focal/20.04

### Install subset of tools

Build a list of the tools to install with the following syntax - set the variable **cloud_tools** to the list of desired tools by name above.  The list should be comma-delimited, inside square-brackets.
```
ansible-playbook -K -i hosts cloud_tools.yml -l localhost --extra-vars '{cloud_tools: [ awscli, eksctl, kubectl ] }'
```

