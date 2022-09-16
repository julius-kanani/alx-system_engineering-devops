# install Flask python package

exec { 'install flask':
  command => 'pip3 install flask==2.1.0'
}

package { 'flask':
  ensure  => 'installed',
  require => Exec['install flask']
}
