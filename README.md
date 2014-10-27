fail2wan
========

A python/fabric style wrapper around fail2ban

Requirements:
 - *fail2ban* must be installed and be available from /usr/bin/fail2ban-client
 - In the *fabric* directory, create a file called hosts.list with the list 
   of hosts, one per line. Remember to include localhost in the file
 - On each target host: 
     - Ensure that the ssh public key of the user is added to authorized_hosts
     - Add a *NOPASSWD: /usr/bin/fail2ban-client* for the user in /etc/sudoers
