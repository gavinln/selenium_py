# Install python and compiled modules for project
class python {
    case $operatingsystem {
        ubuntu: {
            # may need to install openbox for gui
            package {
                ["python-zmq", "python-pip"
                , "python-qt4"]:
                    ensure => installed;
            }
            exec { "pip-install-virtualenv":
                command => "pip install virtualenv",
                require => Package['python-pip']
            }
            exec { "virtualenv-create":
                command => "virtualenv --system-site-packages $HOME_DIR/unix",
                cwd => "$PROJ_DIR",
                require => Exec['pip-install-virtualenv']
            }
            exec { "pip-install-compiled":
                command => "$HOME_DIR/unix/bin/pip install -r $PROJ_DIR/puppet/requirements/compiled.txt",
                require => Exec['virtualenv-create']
            }
        }
    }
}
