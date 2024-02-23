
# This suppresses about 80% of the deprecation warnings from python 3.7.
import warnings
with warnings.catch_warnings():
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    import os
    import testinfra.utils.ansible_runner
    # EXAMPLE_1: make the linter fail by importing an unused module
    # Hint: From now on, try running molecule test --destroy never
    import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

@pytest.mark.parametrize("name", [
    "kubeadm",
    "kubectl",
    "azure-cli",
    "helm",
    # "ruby-hammer-cli",
    # "ruby-hammer-cli-foreman",
    "vault",
    "gh",
])

def test_packages(host, name):
    pkg = host.package(name)
    assert pkg.is_installed


## @pytest.mark.parametrize("name", [
##     ("/home/testing/.git-files-tracked"),
## ])
## 
## def test_contains(host, name):
##     all_variables = host.ansible.get_variables()
##     f = host.file(name)
##     # f = host.file(all_variables['git_repos_tracked'])
## 
##     assert f.exists
##     assert f.is_file
##     assert f.user == all_variables['username']
##     assert f.group == all_variables['groupname']
##     assert f.contains('/usr/local/bin/kubectx ahmetb/kubectx /usr/local/bin/kubectx --version')
##     assert f.contains('/usr/local/bin/eksctl weaveworks/eksctl /usr/local/bin/eksctl version')


@pytest.mark.parametrize("name", [
##    "/home/testing/.git-repos-tracked",
    '/usr/local/bin/eksctl',
    '/usr/local/bin/drone',
])

def test_files(host, name):
    all_variables = host.ansible.get_variables()
    f = host.file(name)

    assert f.is_file
    assert f.user == all_variables['username']
    assert f.group == all_variables['groupname']


# # These are owned by root:user-group
# @pytest.mark.parametrize("name", [
# ])

# def test_files_root_group(host, name):
#     all_variables = host.ansible.get_variables()
#     f = host.file(name)

#     assert f.is_file
#     assert f.user == 'root'
#     assert f.group == all_variables['groupname']


# These are root:root
@pytest.mark.parametrize("name", [
    '/usr/local/bin/dlayer',
    '/usr/bin/vault',
    '/usr/local/bin/minikube',
    '/usr/local/bin/kind',
    '/usr/bin/kubeadm',
    '/usr/bin/kubelet',
    '/usr/bin/kubectl',
    '/usr/local/bin/skaffold',
    '/usr/sbin/helm',
    '/usr/local/bin/docker-machine',
    '/usr/local/bin/docker-compose',
    '/usr/bin/dive',
    '/usr/local/bin/gimme-aws-creds',
    '/usr/local/bin/ecs-cli',
    '/usr/local/bin/linode-cli',
    '/usr/bin/az',
    # '/usr/bin/hammer',
    '/usr/bin/gh',
    '/etc/bash_completion.d/_kubectl',
    '/etc/bash_completion.d/_kubeadm',
    '/etc/bash_completion.d/_minikube',
    '/etc/bash_completion.d/_eksctl',
    '/etc/bash_completion.d/_kind',
    '/etc/bash_completion.d/_skaffold',
    '/usr/share/zsh/vendor-completions/_kubectl',
    '/usr/share/zsh/vendor-completions/_kubeadm',
    '/usr/share/zsh/vendor-completions/_minikube',
    '/usr/share/zsh/vendor-completions/_eksctl',
    '/usr/share/zsh/vendor-completions/_kind',
    '/usr/share/zsh/vendor-completions/_skaffold',
])

def test_files_root(host, name):
    f = host.file(name)

    assert f.is_file
    assert f.user == 'root'
    assert f.group == 'root'


@pytest.mark.parametrize("directory", [
    '/usr/local/share/Kui-linux-x64',
])

def test_dirs(host, directory):
    all_variables = host.ansible.get_variables()
    f = host.file(directory)

    assert f.is_directory
    assert f.user == all_variables['username']
    assert f.group == all_variables['groupname']

@pytest.mark.parametrize("directory", [
    '/usr/local/share/kubetools',
])

def test_dirs_root(host, directory):
    all_variables = host.ansible.get_variables()
    f = host.file(directory)

    assert f.is_directory
    assert f.user == 'root'
    assert f.group == 'root'



@pytest.mark.parametrize("symlink", [
    '/usr/local/bin/kubectx',
    '/usr/local/bin/kubens',
    '/usr/local/bin/Kui',
])

def test_symlink(host, symlink):
    f = host.file(symlink)

    assert f.is_symlink

