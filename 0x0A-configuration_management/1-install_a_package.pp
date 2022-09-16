# install flask using puppet

package { 'puppet-flask':
    ensure   => '2.1.0',
    provider => 'pip3',
}
