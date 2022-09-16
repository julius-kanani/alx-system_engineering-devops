# install Flask python package

exec { 'apt-get update':
  command => '/usr/bin/apt-get update'
}

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Exec['apt-get update']
}
