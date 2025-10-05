Vagrant.configure("2") do |config|
  config.vm.box = "debian/bookworm64"
  
  # 网络设置
  config.vm.network "forwarded_port", guest: 5000, host: 5000
  
  # 共享文件夹
  config.vm.synced_folder ".", "/vagrant"
  
  #  provisioning - 确保文件存在后再执行
  config.vm.provision "shell", inline: <<-SHELL
    echo "=== 开始设置 Flask 应用 ==="
    echo "检查 auto_flask.sh 文件..."
    
    if [ -f "/vagrant/auto_flask.sh" ]; then
        echo "找到 auto_flask.sh，设置执行权限..."
        chmod +x /vagrant/auto_flask.sh
        echo "执行 auto_flask.sh..."
        /vagrant/auto_flask.sh
    else
        echo "错误: /vagrant/auto_flask.sh 文件未找到"
        echo "当前目录内容:"
        ls -la /vagrant/
    fi
    
    echo "=== 设置过程完成 ==="
  SHELL
end