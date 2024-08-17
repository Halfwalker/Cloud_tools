# ansible-cloud_tools

![Build Status](http://bondi.local:3001/api/badges/Halfwalker/ansible-cloud_tools/status.svg)

This is a role to install a useful set of tools for dealing with cloud type things.

### Install latest ansible with :
```
sudo apt install --no-install-recommends software-properties-common
sudo add-apt-repository ppa:ansible/ansible
sudo apt install --no-install-recommends ansible
```

### Optional : Set a github user/token var to avoid rate-limiting

Github may sometimes rate-limit non-authenticated access, which can cause the playbook to fail.  If you don't already have one, you can [Create a personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) for github.  Then set the **vault_github_auth** variable in your ansible vault as follows `ansible-vault edit group_vars/all/vault`
```
# github access tokens
vault_github_auth:
  name: my_github_username
  token: 3457blahblah34985735987blahblah5908734
```

### Install all tools with playbook.yml

```
- hosts: all
  gather_facts: true

  roles:
    - { role: ansible-cloud_tools, tags: 'cloud' }
```

Then run playbook with something like

```
ansible-playbook -K -i hosts playbook.yml -l localhost
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
* [Terraform](https://www.terraform.io/downloads) (not supported in Bionic/18.04)
* [Terraform-switcher](https://github.com/warrensbox/terraform-switcher)
* [vault](https://www.vaultproject.io/downloads) (not supported in Bionic/18.04)
* [vagrant](https://www.vagrantup.com/) (not supported in Bionic/18.04)
* [Hammer](http://deb.theforeman.org/)
* [github-cli](https://cli.github.com/)

### Install subset of tools

Define a `cloud_tools` variable to list all the tools desired in the playbook

```
- hosts: all
  gather_facts: true

  vars:
    cloud_tools:
      - minikube
      - kind
      - kubernetes
      - skaffold

  roles:
    - { role: ansible-cloud_tools, tags: 'cloud' }
```

Then run playbook with something like

```
ansible-playbook -K -i hosts playbook.yml -l localhost
```

That will install just the tools listed in the playbook.  Or, you can override it right on the command-line ...

Build a list of the tools to install with the following syntax - set the variable **cloud_tools** to the list of desired tools by name above.  The list should be comma-delimited, inside square-brackets.
```
ansible-playbook -K -i hosts playbook.yml -l localhost --extra-vars '{cloud_tools: [ awscli, eksctl, kubectl ] }'
```

