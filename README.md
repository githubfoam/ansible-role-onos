onos
=========

Ansible Role: [![Ansible Role](https://img.shields.io/ansible/role/d/32836.svg?style=plastic)](https://galaxy.ansible.com/githubfoam/onos)  
Ansible Role: [![Ansible Role](https://img.shields.io/ansible/role/32836.svg)](https://galaxy.ansible.com/githubfoam/onos)  


Travis (.com) branch:
[![Build Status](https://travis-ci.com/githubfoam/ansible-role-onos.svg?branch=badges)](https://travis-ci.com/githubfoam/ansible-role-onos)  
Travis (.com) molecule testinfra branch:
[![Build Status](https://travis-ci.com/githubfoam/ansible-role-onos.svg?branch=molecule-testinfra)](https://travis-ci.com/githubfoam/ansible-role-onos)  
Travis (.com) test branch:
[![Build Status](https://travis-ci.com/githubfoam/ansible-role-onos.svg?branch=test)](https://travis-ci.com/githubfoam/ansible-role-onos)  
Travis (.com) dev branch:
[![Build Status](https://travis-ci.com/githubfoam/ansible-role-onos.svg?branch=dev)](https://travis-ci.com/githubfoam/ansible-role-onos)  


[![Docker Automated build](https://img.shields.io/docker/automated/dockerfoam/onos.svg?style=plastic)](https://hub.docker.com/r/dockerfoam/onos/)  
[![Docker Pulls](https://img.shields.io/docker/pulls/dockerfoam/onos.svg?style=plastic)](https://hub.docker.com/r/dockerfoam/onos/)  
[![Docker Stars](https://img.shields.io/docker/stars/dockerfoam/onos.svg?style=plastic)](https://hub.docker.com/r/dockerfoam/onos/)

[![GitHub search hit counter](https://img.shields.io/github/search/githubfoam/ansible-role-onos/goto.svg)](https://github.com/githubfoam/ansible-role-onos)  
[![GitHub](https://img.shields.io/github/license/githubfoam/ansible-role-onos.svg?style=plastic)](https://github.com/githubfoam/ansible-role-onos)

~~~~
----------------

Playbook
----------------

molecule testinfra branch:

    - MOLECULE_SCENARIO=ubuntu1604
    - MOLECULE_SCENARIO=ubuntu1804
    - MOLECULE_SCENARIO=ubuntu1810
    - MOLECULE_SCENARIO=ubuntu1904
    
File:

    - hosts: servers
      roles:
         - { role: githubfoam.onos }

Command:

             - $ ansible-galaxy install --roles-path . githubfoam.onos


License
-------

GNU General Public License v3.0

Author Information
------------------

An optional section for the role authors

release watch
~~~~

java watch
~~~~
Installation of the JDK on Linux Platforms
https://docs.oracle.com/en/java/javase/13/install/installation-jdk-linux-platforms.html#GUID-737A84E4-2EFF-4D38-8E60-3E29D1B884B8

Oracle JDK 13 Certified System Configurations
Ubuntu Linux  19.04  	18.04 LTS
https://www.oracle.com/technetwork/java/javase/documentation/jdk13certconfig-5567436.html

~~~~
