
# This suppresses about 80% of the deprecation warnings from python 3.7.
import warnings
with warnings.catch_warnings():
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    import os
    import testinfra.utils.ansible_runner
    # EXAMPLE_1: make the linter fail by importing an unused module
    # Hint: From now on, try running molecule test --destroy never
    import pytest

# Define which packages to skip based on Ubuntu version
SKIP_PACKAGES_BY_RELEASE = {
    "20.04": {"vault", "terraform", "vagrant"},
    # Add more if needed, e.g.:
    # "18.04": {"vault", "terraform", "helm"},
}

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.fixture(scope="module")
def ubuntu_release(host):
    return host.system_info.release


@pytest.mark.parametrize("name", [
    "kubeadm",
    "kubectl",
    "azure-cli",
    "helm",
    # "ruby-hammer-cli",
    # "ruby-hammer-cli-foreman",
    "vault",
    "vagrant",
    "terraform",
    "gh",
])

def test_packages(host, name, ubuntu_release):
    skipped = set()
    all_variables = host.ansible.get_variables()

    # Merge all skipped packages for versions <= current release
    for version, packages in SKIP_PACKAGES_BY_RELEASE.items():
        if ubuntu_release <= version:
            skipped |= packages

    if name in skipped:
        pytest.skip(f"{name} is not expected on Ubuntu <= {ubuntu_release}")

    # Skip if the tool is not in the cloud_tools list
    tool_name = os.path.basename(name)
    if tool_name not in all_variables.get('cloud_tools', []):
        pytest.skip(f"{tool_name} is not in cloud_tools list to install")

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

    # Skip if the tool is not in the cloud_tools list
    tool_name = os.path.basename(name)
    if tool_name not in all_variables.get('cloud_tools', []):
        pytest.skip(f"{tool_name} is not in cloud_tools list to install")

    assert f.is_file
    assert f.user == all_variables['username']
    assert f.group == all_variables['groupname']


# pipx installs packages to /root/.local/.share... for 24.04+
# but to /usr/local/bin for lower than 24.04
@pytest.mark.parametrize("name", [
    '/root/.local/share/pipx/venvs/gimme-aws-creds/bin/gimme-aws-creds',
    '/root/.local/share/pipx/venvs/linode-cli/bin/linode-cli',
])

def test_pipx_files_24(host, name, ubuntu_release):
    skipped = set()
    all_variables = host.ansible.get_variables()
    f = host.file(name)

    if float(ubuntu_release) <= 24.04:
        pytest.skip(f"Skipping {name} for Ubuntu {ubuntu_release} (requires >= 24.04)")

    # Skip if the tool is not in the cloud_tools list
    tool_name = os.path.basename(name)
    if tool_name not in all_variables.get('cloud_tools', []):
        pytest.skip(f"{tool_name} is not in cloud_tools list to install")

    # Merge all skipped packages for versions <= current release
    for version, packages in SKIP_PACKAGES_BY_RELEASE.items():
        if ubuntu_release <= version:
            skipped |= packages

    if os.path.basename(name) in skipped:
        pytest.skip(f"{name} is not expected on Ubuntu <= {ubuntu_release}")

    assert f.is_file
    assert f.user == all_variables['username']
    assert f.group == all_variables['groupname']


# pipx installs packages to /root/.local/.share... for 24.04+
# but to /usr/local/bin for lower than 22.04
# These are root:root
@pytest.mark.parametrize("name", [
    '/usr/local/bin/gimme-aws-creds',
    '/usr/local/bin/linode-cli',
])

def test_pipx_files_old(host, name, ubuntu_release):
    skipped = set()
    all_variables = host.ansible.get_variables()

    if float(ubuntu_release) >= 22.04:
        pytest.skip(f"Skipping {name} for Ubuntu {ubuntu_release} (requires <= 22.04)")

    # Merge all skipped packages for versions <= current release
    for version, packages in SKIP_PACKAGES_BY_RELEASE.items():
        if ubuntu_release <= version:
            skipped |= packages

    if os.path.basename(name) in skipped:
        pytest.skip(f"{name} is not expected on Ubuntu <= {ubuntu_release}")

    # Skip if the tool is not in the cloud_tools list
    tool_name = os.path.basename(name)
    if tool_name not in all_variables.get('cloud_tools', []):
        pytest.skip(f"{tool_name} is not in cloud_tools list to install")

    f = host.file(name)

    assert f.is_file
    assert f.user == 'root'
    assert f.group == 'root'


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
    '/usr/bin/glasskube',
    '/usr/bin/k9s',
    '/usr/local/bin/skaffold',
    '/usr/sbin/helm',
    '/usr/bin/dive',
    '/usr/local/bin/ecs-cli',
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

def test_files_root(host, name, ubuntu_release):
    skipped = set()
    all_variables = host.ansible.get_variables()

    # Merge all skipped packages for versions <= current release
    for version, packages in SKIP_PACKAGES_BY_RELEASE.items():
        if ubuntu_release <= version:
            skipped |= packages

    if os.path.basename(name) in skipped:
        pytest.skip(f"{name} is not expected on Ubuntu <= {ubuntu_release}")

    # Skip if the tool is not in the cloud_tools list
    tool_name = os.path.basename(name)
    if tool_name not in all_variables.get('cloud_tools', []):
        pytest.skip(f"{tool_name} is not in cloud_tools list to install")

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

    # Skip if the tool is not in the cloud_tools list
    if 'Kui' not in all_variables.get('cloud_tools', []):
        pytest.skip("Kui is not in cloud_tools list to install")

    assert f.is_directory
    assert f.user == all_variables['username']
    assert f.group == all_variables['groupname']


@pytest.mark.parametrize("directory", [
    '/usr/local/share/kubetools',
])

def test_dirs_root(host, directory):
    all_variables = host.ansible.get_variables()
    f = host.file(directory)

    # Skip if neither kubectx nor kubens is in the cloud_tools list
    kubetools = ['kubectx', 'kubens']
    if not any(tool in all_variables.get('cloud_tools', []) for tool in kubetools):
        pytest.skip("Neither kubectx nor kubens is in cloud_tools list to install")

    assert f.is_directory
    assert f.user == 'root'
    assert f.group == 'root'


@pytest.mark.parametrize("symlink", [
    '/usr/local/bin/kubectx',
    '/usr/local/bin/kubens',
    '/usr/local/bin/Kui',
])

def test_symlink(host, symlink):
    all_variables = host.ansible.get_variables()
    f = host.file(symlink)

    # Skip if the tool is not in the cloud_tools list
    tool_name = os.path.basename(symlink)
    if tool_name not in all_variables.get('cloud_tools', []):
        pytest.skip(f"{tool_name} is not in cloud_tools list to install")

    assert f.is_symlink


@pytest.mark.parametrize("symlink", [
    '/root/.local/bin/gimme-aws-creds',
    '/root/.local/bin/linode-cli',
])

def test_symlink_24(host, symlink, ubuntu_release):
    all_variables = host.ansible.get_variables()
    f = host.file(symlink)

    # Skip if the tool is not in the cloud_tools list
    tool_name = os.path.basename(symlink)
    if tool_name not in all_variables.get('cloud_tools', []):
        pytest.skip(f"{tool_name} is not in cloud_tools list to install")

    if float(ubuntu_release) >= 22.04:
        pytest.skip(f"Skipping {tool_name} for Ubuntu {ubuntu_release} (requires <= 22.04)")

    assert f.is_symlink

