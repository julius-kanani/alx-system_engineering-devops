# Install Nginx package
package {'nginx':
  ensure => installed,
}

# Enable and start Nginx service
service {'nginx':
  ensure => running,
  enable => true,
}

# Adjust the firewall to allow access to the Nginx service
exec {'ufw allow Nginx HTTP':
  command => 'ufw allow Nginx HTTP',
  path    => '/usr/sbin:/usr/bin:/sbin:/bin',
  unless  => 'ufw status | grep -q "Nginx HTTP"',
}

# Enable ufw if inactive
exec {'ufw enable':
  command => 'ufw enable',
  path    => '/usr/sbin:/usr/bin:/sbin:/bin',
  onlyif  => 'ufw status | grep -q "Status: inactive"',
}

# Create a new directory for the caesarus.tech website and set the appropriate permissions
file {'/var/www/caesarus.tech/html':
  ensure => directory,
  owner  => root,
  group  => root,
  mode   => '0755',
}

# Create an index.html file for the caesarus.tech website
file {'/var/www/caesarus.tech/html/index.html':
  ensure => file,
  content => 'Hello World!',
}

# Create a new configuration file for the caesarus.tech server block
file {'/etc/nginx/sites-available/caesarus.tech':
  ensure => file,
  content => "server {\n    listen 80;\n    listen [::]:80;\n\n    root /var/www/caesarus.tech/html;\n    index index.html;\n\n    server_name caesarus.tech 127.0.0.1 localhost 18.210.15.46;\n\n    location / {\n        try_files \$uri \$uri/ =404;\n    }\n\n    location /redirect_me {\n        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;\n    }\n\n    error_page 404 /custom_404_Page.html;\n}\n",
}

# Setup custom error 404 page.
file {'/var/www/caesarus.tech/html/custom_404_Page.html':
  ensure => file,
  content => "Ceci n'est pas une page",
}

# Create a symbolic link to enable the caesarus.tech server block configuration
file {'/etc/nginx/sites-enabled/caesarus.tech':
  ensure => link,
  target => '/etc/nginx/sites-available/caesarus.tech',
}

# Test the Nginx configuration
exec {'nginx -t':
  command => '/usr/sbin/nginx -t',
  path    => '/usr/sbin:/usr/bin:/sbin:/bin',
  require => File['/etc/nginx/sites-available/caesarus.tech'],
  unless  => '/usr/sbin/nginx -t | grep -q "syntax is ok"',
}

# If the configuration is valid, restart Nginx
Exec {'service nginx restart':
  command => '/usr/sbin/service nginx restart',
  path    => '/usr/sbin:/usr/bin:/sbin:/bin',
  require => Exec['nginx -t'],
}
