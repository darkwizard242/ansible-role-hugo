import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hugo_binary_exists(host):
    assert host.file('/usr/local/bin/hugo').exists


def test_hugo_binary_file(host):
    assert host.file('/usr/local/bin/hugo').is_file


def test_hugo_binary_which(host):
    assert host.check_output('which hugo') == '/usr/local/bin/hugo'
