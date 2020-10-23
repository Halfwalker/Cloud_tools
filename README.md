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
