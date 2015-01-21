from fabric.api import *


env.use_ssh_config = True
env.hosts = open('hosts.list', 'r').readlines()

def ban(jail, ip='null'):
    """ Bans a specific IP address """
    run("sudo /usr/bin/fail2ban-client set %s banip %s" % (jail, ip))
    
def bantime(jail, time='600'):
    """ Set the ban time on a jail """
    run("sudo /usr/bin/fail2ban-client set %s bantime %s" % (jail, time))

def maxretry(jail, time='6'):
    """ Set the ban time on a jail """
    run("sudo /usr/bin/fail2ban-client set %s maxretry %s" % (jail, time))

def idle(jail, idlemode='off'):
    """ Idle or Unidle a jail """
    run("sudo /usr/bin/fail2ban-client set %s idle %s" % (jail, idlemode))

def unban(jail, ip='null'):
    """ Unban an IP address """
    run("sudo /usr/bin/fail2ban-client set %s unbanip %s" % (jail, ip))

def whitelist(jail, ip='null'):
    """ Add IP to Whitelist """
    run("sudo /usr/bin/fail2ban-client set %s addignoreip %s" % (jail, ip))

def unwhitelist(jail, ip='null'):
    """ Remote IP from whitelist """
    run("sudo /usr/bin/fail2ban-client set %s delignoreip %s" % (jail, ip))

def start(jail=''):
    """ Starts a jail """
    run("sudo /usr/bin/fail2ban-client start %s" % jail)

def stop(jail=''):
    """ Stops a jail """
    run("sudo /usr/bin/fail2ban-client stop %s" % jail)

def status(jail=''):
    """ Gets the status of a jail """
    run("sudo /usr/bin/fail2ban-client status %s" % jail)

def ping():
    """ Gets the status of a jail """
    run("sudo /usr/bin/fail2ban-client ping")



