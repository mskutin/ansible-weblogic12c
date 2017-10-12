# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "bento/centos-7.2"
  config.vm.network "private_network", ip: "192.168.56.14"
  config.vm.hostname = "wls12c-r2-1.private"
  config.hostmanager.enabled = true
  config.hostmanager.ignore_private_ip = false
  config.vm.provider "virtualbox" do |vb|
      vb.memory = "6144"
      vb.cpus = 2
      vb.name = "Weblogic12cR2-1"
  end
	config.vm.provision "ansible" do |ansible|
      ansible.playbook = "weblogic-fmw-domain.yml"
      ansible.inventory_path = "./hosts"
      ansible.limit = 'all'
      # ansible.verbose = "v"
  end
end
