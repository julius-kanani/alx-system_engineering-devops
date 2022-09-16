# Create a file in /tmp.

$folder = '/tmp'

file { $folder:
  ensure => 'directory'
}

file { '/tmp/school':
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
  require => File[$folder]
}
