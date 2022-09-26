# Setup nginx server

package { 'nginx':
  ensure     => 'installed',
}

file { '/var/www/html/index.nginx-debian.html':
  content => 'Hello World!',
}

file_line { 'redirect_me':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
