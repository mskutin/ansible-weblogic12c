## Weblogic12c Admin Server, Node Manager and Managed Server Vagrantbox with Ansible provisioner

>Ansible playbook for deploy and create a WebLogic 12c Domain with Oracle Fusion Middleware Infrastructure automatically

[![asciicast](https://asciinema.org/a/141978.png)](https://asciinema.org/a/141978?t=1&speed=40?size=small)
Special credits to @abessifi and @cvezalis.

### Prerequisites:
- [Vagrant 1.9.5](https://www.vagrantup.com/docs/installation/) + [Vagrant Hostmanager](https://github.com/devopsgroup-io/vagrant-hostmanager)
- [Ansible 2.3.0](http://docs.ansible.com/ansible/latest/intro.html)
- Oracle Weblogic 12c
- Oracle JDK 1.8.66

### Configuration
- Place Weblogic distributive to `roles/fmw-software/files/fmw_12.2.1.2.0_infrastructure.jar`
- Place JDK distributive to `roles/linux-jdk/files/jdk-8u66-linux-x64.tar.gz`

> Update the `infra-vars.yml` if required
```yml
# JDK installer and target folder
jdk_installation_archive: 'jdk-8u66-linux-x64.tar.gz'
jdk_folder: '{{ oracle_base }}/jdk1.8.0_66'

# fmw installer
mw_installer: 'fmw_12.2.1.2.0_infrastructure.jar'
```

### Installation
```bash
$ vagrant up --provision
```

Access Weblogic web interface at http://192.168.56.14:7001/console using `weblogic/welcome1` credentials.

Playbook includes the following roles:
- linux-wls
    - This role configures the Linux system with requirements to run the WebLogic domain.
- linux-jdk
    - This role configures the Linux system with JDK 8
- fmw-software
    - This role installs the the Weblogic 12c
- fmw-domain
    - This role creates and configures a Domain with Fusion Middleware software
- node-manager
    - This role configures and starts the Nodemanager. It also configures systemd to start automatically the nodemanager after restart
- start-admin-server
    - This starts the Admin server using nodemanager for the first time. Creates some initial configuration like boot.properties file
- fmw-managed-server
    - This role creates and starts a managed server