# SSH client configuration with puppet

file_line {
  'passAuth':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => '   PasswordAuthentication no'
  ;
  'keyLocation':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => '   IdentityFile ~/.ssh/school'
}
