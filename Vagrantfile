# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

def from_env_or_default(key, default)
  value = ENV[key]
  return value ? value : default
end


HOSTNAME = from_env_or_default("VAGRANT_HOSTNAME", "local.chats")
MEMORY = from_env_or_default("VAGRANT_MEMORY", 4096)
CPUS = from_env_or_default("VAGRANT_CPUS", 1)
SYNCED_SOURCE = from_env_or_default("VAGRANT_SYNCED_SOURCE", "src/")
SYNCED_TARGET = from_env_or_default("VAGRANT_SYNCED_TARGET", "/var/www")


Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "ubuntu/trusty64"
  # config.vm.box = "ubuntu/xenial64"
  config.vm.hostname = HOSTNAME
  config.vm.network "private_network", ip: "192.168.50.4"
  config.ssh.forward_agent = true
  # config.vm.synced_folder SYNCED_SOURCE, SYNCED_TARGET, type: "nfs", mount_options:['nolock,vers=3,udp,noatime,actimeo=1']
  # config.vm.synced_folder '.', '/vagrant', disabled: true

  # ENV['LC_ALL']="ru_RU.UTF-8"

  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "provision/playbook.yml"
    #
    # To debug run ANSIBLE_EXTRA_ARGS='-vvvv --tags=tag-to-debug' vagrant provision
    extra_ansible_args = ENV["ANSIBLE_EXTRA_ARGS"]
    if extra_ansible_args
      ansible.raw_arguments = extra_ansible_args.split(' ')
    end
  end

  config.vm.provider "virtualbox" do |v|
    v.memory = MEMORY
    v.cpus = CPUS
  end
end
