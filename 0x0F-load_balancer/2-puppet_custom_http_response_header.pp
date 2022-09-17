# puppet manifest to install nginx with custom header
exec { 'apt-get-update':
  command => '/usr/bin/apt-get update',
}
exec { 'apt-get-upgrade':
  command => '/usr/bin/apt-get upgrade',
}

package { 'nginx':
  ensure  => installed,
  require => [ Exec['apt-get-update'], Exec['apt-get-upgrade'] ],
}

file_line { 'add header':
  ensure  => 'present',
  path    => '/etc/nginx/sites-available/default',
  after   => 'listen [::]:80 default_server;',
  line    => "add_header X-Served-By ${hostname};",
  require => Package['nginx'],
}

file { '/etc/nginx/html/index.html':
  content => 'Holberton School',
  require => Package['nginx'],
}

file { '/etc/nginx/html/404.html':
  content => 'Ceci n\'est pas une page',
  require => Package['nginx'],
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
