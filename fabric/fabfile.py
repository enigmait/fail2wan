from fabric.api import *


env.use_ssh_config = True
env.hosts = open('hosts.list', 'r').readlines()

def ban(jail, ip='null'):
    """ Bans a specific IP address """
    run("sudo /usr/bin/fail2ban-client set %s banip %s" % (jail, ip))

def unban(jail, ip='null'):
    """ Unban an IP address """
    run("sudo /usr/bin/fail2ban-client set %s unbanip %s" % (jail, ip))

def whitelist(jail, ip='null'):
    """ Add IP to Whitelist """
    run("sudo /usr/bin/fail2ban-client set %s addignoreip %s" % (jail, ip))

def unwhitelist(jail, ip='null'):
    """ Remote IP from whitelist """
    run("sudo /usr/bin/fail2ban-client set %s delignoreip %s" % (jail, ip))

def status(jail=''):
    """ Gets the status of a jail """
    run("sudo /usr/bin/fail2ban-client status %s" % jail)
