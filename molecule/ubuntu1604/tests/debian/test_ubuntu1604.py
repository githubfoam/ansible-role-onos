import os
import pytest
import testinfra.utils.ansible_runner

@pytest.mark.parametrize('pkg', [
  'software-properties-common',
  'oracle-java8-set-default',
  'curl',
  'oracle-java8-installer'
])
def test_pkg(host, pkg):
    package = host.package(pkg)
    assert package.is_installed
