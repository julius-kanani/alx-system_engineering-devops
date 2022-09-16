# install flask using puppet

package { 'puppet-flask':
    ensure   => '2.1.0',
    name     => 'flask',
    provider => 'pip3',
}
