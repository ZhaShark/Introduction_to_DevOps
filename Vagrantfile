Vagrant.configure("2") do |config|
  config.vm.box = "debian/bookworm64"
  
  config.vm.network "forwarded_port", guest: 5000, host: 5000
  
  config.vm.provision "shell", inline: <<-SHELL
	echo "== Starting =="
	cd /vagrant
	chmod +x auto_flask.sh
	./auto_flask.sh
  SHELL
end
