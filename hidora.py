#!/usr/bin/python
import sys, os, time, socket

# Restart Hidora
def restart():
   python = sys.executable
   os.execl(python, python, * sys.argv)
   curdir = os.getcwd()

# Variables for outputs used by various commands
prompt_wordlist  = "[*] Wordlist location: "
prompt_hostname  = "[*] Target IP or Hostname: "
prompt_username  = "[*] Target user: "
prompt_emailadd  = "[*] Target email address: "
prompt_smtpport	 = "[*] Target port (25,587,465): "
prompt_weburl    = "[*] URL to visit via proxy:"
prompt_proxyport = "[*] Target port (8080, 9050):"

# Clear everything on-screen
os.system("clear")             

# Hidora information scnreen
banner = '''
***********************************************************************
*                            H I D O R A                              *
*             A wrapper for the Hydra brute-forcing tool              *
*                                                                     *
* Supported Commands:                                                 *
* ------------------------------------------------------------------- *
* SSH      | SMTP     | SMB        | MySQL     | TeamSpeak | IRC      *
* Telnet(s)| IMAP(S)  | FTP(S)     | Posgres   | Asterisk  | XMPP     *
* VNC      | POP3(S)  | HTTP(S)    | Firebird  | SIP       | LDAP2(S) *
* RDP      | SNMP     | HTTP-Proxy | MSSQL     | VMware    | LDAP3(S) *
***********************************************************************
'''
print banner

# Requesting input from user then confirmation of command entered
hidora = raw_input("[*] Hidora > ")
print "[!] Loading %s module..." % (hidora)

# Protocol specific commands that call prompt_* variables from the top of the script
# for outputting messages to the user requesting data (hostname, wordlists etc.)
# os.system commands are then used to submit shell commands for Hydra

if hidora == 'VNC' or hidora == 'vnc':
  host = raw_input("%s" % (prompt_hostname))
  word = raw_input("%s" % (prompt_wordlist))
  os.system("hydra -V -P %s -e n -t 1 %s vnc -V" % (word, host))
    
elif hidora == 'SMB' or hidora == 'smb':
  user = raw_input("%s" % (prompt_username))
  host = raw_input("%s" % (prompt_hostname))
  word = raw_input("%s" % (prompt_wordlist))
  os.system("hydra -V -l %s -P %s %s smb" % (user, word, host))
  sys.exit()

elif hidora == 'FTP' or hidora == 'ftp':
  user = raw_input("%s" % (prompt_username))
  host = raw_input("%s" % (prompt_hostname))
  word = raw_input("%s" % (prompt_wordlist))
  os.system("hydra -V -l %s -P %s %s ftp" % (user, word, host))
  sys.exit()

elif hidora == 'FTPS' or hidora == 'ftps':
  user = raw_input("%s" % (prompt_username))
  host = raw_input("%s" % (prompt_hostname))
  word = raw_input("%s" % (prompt_wordlist))
  os.system("hydra -V -l %s -P %s %s ftps" % (user, word, host))
  sys.exit()
  
elif hidora == 'SMTP' or hidora == 'smtp':
  email = raw_input("%s" % (prompt_emailadd))
  host = raw_input("%s" % (prompt_hostname))
  port = raw_input("%s" % (prompt_smtpport))
  word = raw_input("%s" % (prompt_wordlist))
  os.system("hydra -V -l %s -P %s -s %s %s smtp" % (email, word, port, host))
  sys.exit()

elif hidora == 'IMAP' or hidora == 'imap':
  email = raw_input("%s" % (prompt_emailadd))
  host = raw_input("%s" % (prompt_hostname))
  word = raw_input("%s" % (prompt_wordlist))
  os.system("hydra -V -l %s -P %s %s imap" % (email, word, host))
  sys.exit()

elif hidora == 'IMAPS' or hidora == 'imaps':
  email = raw_input("%s" % (prompt_emailadd))
  host = raw_input("%s" % (prompt_hostname))
  word = raw_input("%s" % (prompt_wordlist))
  os.system("hydra -V -l %s -P %s %s imaps" % (email, word, host))
  sys.exit()

elif hidora == 'POP3' or hidora == 'pop3':
  email = raw_input("%s" % (prompt_emailadd))
  host = raw_input("%s" % (prompt_hostname))
  word = raw_input("%s" % (prompt_wordlist))
  os.system("hydra -V -l %s -P %s %s pop3" % (email, word, host))
  sys.exit()

elif hidora == 'POP3S' or hidora == 'pop3s':
  email = raw_input("%s" % (prompt_emailadd))
  host = raw_input("%s" % (prompt_hostname))
  word = raw_input("%s" % (prompt_wordlist))
  os.system("hydra -V -l %s -P %s %s pop3s" % (email, word, host))
  sys.exit()

elif hidora == 'SSH' or hidora == 'ssh':
  user = raw_input("%s" % (prompt_username))
  host = raw_input("%s" % (prompt_hostname))
  word = raw_input("%s" % (prompt_wordlist))
  os.system("hydra -V -t 4 -l %s -P %s %s ssh" % (user, word, host))
  sys.exit()

elif hidora == 'Telnet' or hidora == 'telnet':
  user = raw_input("%s" % (prompt_username))
  host = raw_input("%s" % (prompt_hostname))
  word = raw_input("%s" % (prompt_wordlist))
  os.system("hydra -V -l %s -P %s %s telnet" % (user, word, host))
  sys.exit()

elif hidora == 'Telnets' or hidora == 'telnets':
  user = raw_input("%s" % (prompt_username))
  host = raw_input("%s" % (prompt_hostname))
  word = raw_input("%s" % (prompt_wordlist))
  os.system("hydra -V -l %s -P %s %s telnets" % (user, word, host))
  sys.exit()
 
elif hidora == 'SNMP' or hidora == 'snmp':
  user = raw_input("%s" % (prompt_username))
  host = raw_input("%s" % (prompt_hostname))
  word = raw_input("%s" % (prompt_wordlist))
  os.system("hydra -V -l %s -P %s -m r %s snmp" % (user, word, host))
  sys.exit()

elif hidora == 'MySQL' or hidora == 'mysql':
  user = raw_input("%s" % (prompt_username))
  host = raw_input("%s" % (prompt_hostname))
  word = raw_input("%s" % (prompt_wordlist))
  os.system("hydra -t 5 -V -l %s -e ns -P %s %s mysql" % (user, word, host))

elif hidora == 'Firebird' or hidora == 'firebird':
  user = raw_input("%s" % (prompt_username))
  host = raw_input("%s" % (prompt_hostname))
  word = raw_input("%s" % (prompt_wordlist))
  os.system("hydra -t 5 -V -l %s -e ns -P %s %s firebird" % (user, word, host))

elif hidora == 'Posgres' or hidora == 'posgres':
  user = raw_input("%s" % (prompt_username))
  host = raw_input("%s" % (prompt_hostname))
  word = raw_input("%s" % (prompt_wordlist))
  os.system("hydra -t 5 -V -l %s -e ns -P %s %s posgres" % (user, word, host))
  
elif hidora == 'MSSQL' or hidora == 'mssql':
  user = raw_input("%s" % (prompt_username))
  host = raw_input("%s" % (prompt_hostname))
  word = raw_input("%s" % (prompt_wordlist))
  os.system("hydra -t 5 -V -l %s -e ns -P %s %s mssql" % (user, word, host))

elif hidora == 'HTTP' or hidora == 'http':
  user = raw_input("%s" % (prompt_username))
  host = raw_input("%s" % (prompt_hostname))
  word = raw_input("%s" % (prompt_wordlist))
  os.system("hydra -V -m / -l %s -P %s %s http-get" % (user, word, host))
  sys.exit()
	
elif hidora == 'HTTPS' or hidora == 'https':
  user = raw_input("%s" % (prompt_username))
  host = raw_input("%s" % (prompt_hostname))
  word = raw_input("%s" % (prompt_wordlist))
  os.system("hydra -V -m / -l %s -P %s %s https-get" % (user, word, host))
  sys.exit()

elif hidora == 'SOCKS5' or hidora == 'socks5':
  user = raw_input("%s" % (prompt_username))
  host = raw_input("%s" % (prompt_hostname))
  port = raw_input("%s" % (prompt_proxyport))
  word = raw_input("%s" % (prompt_wordlist))
  os.system("hydra -V -l %s -P %s %s -s %s socks5" % (user, word, host, port))
  sys.exit()

elif hidora == 'HTTP-Proxy' or hidora == 'http-proxy':
  user = raw_input("%s" % (prompt_username))
  host = raw_input("%s" % (prompt_hostname))
  word = raw_input("%s" % (prompt_wordlist))
  url  = raw_input("%s" % (prompt_weburl))
  os.system("hydra -V -l %s -P %s -m %s %s http-proxy" % (user, word, url, host))
  sys.exit()

elif hidora == 'RDP' or hidora == 'rdp':
  user = raw_input("%s" % (prompt_username))
  host = raw_input("%s" % (prompt_hostname)) 
  word = raw_input("%s" % (prompt_wordlist))
  os.system("hydra -V -f -t 1 -l %s -P %s %s rdp" % (user, word, host))
  sys.exit()

elif hidora == 'Cisco' or hidora == 'cisco':
  host = raw_input("%s" % (prompt_hostname))
  word = raw_input("%s" % (prompt_wordlist))
  os.system("hydra -V -P %s %s cisco" % (word, host))
  sys.exit()
	
elif hidora == 'TeamSpeak' or hidora == 'teamspeak':
  user = raw_input("%s" % (prompt_username))
  host = raw_input("%s" % (prompt_hostname))
  word = raw_input("%s" % (prompt_wordlist))
  os.system("hydra -V -l %s -P %s %s teamspeak" % (user, word, host))
  sys.exit()

elif hidora == 'VMware' or hidora == 'vmware':
  user = raw_input("%s" % (prompt_username))
  host = raw_input("%s" % (prompt_hostname))
  word = raw_input("%s" % (prompt_wordlist))
  os.system("hydra -V -l %s -P %s %s vmauthd" % (user, word, host))
  sys.exit()

elif hidora == 'Asterisk' or hidora == 'asterisk':
  user = raw_input("%s" % (prompt_username))
  host = raw_input("%s" % (prompt_hostname))
  word = raw_input("%s" % (prompt_wordlist))
  os.system("hydra -V -l %s -P %s %s asterik" % (user, word, host))
  sys.exit()

elif hidora == 'SIP' or hidora == 'sip':
  user = raw_input("%s" % (prompt_username))
  host = raw_input("%s" % (prompt_hostname))
  word = raw_input("%s" % (prompt_wordlist))
  os.system("hydra -V -l %s -P %s %s sip" % (user, word, host))
  sys.exit()
	
elif hidora == 'IRC' or hidora =='irc':
  user = raw_input("%s" % (prompt_username))
  host = raw_input("%s" % (prompt_hostname))
  word = raw_input("%s" % (prompt_wordlist))
  os.system("hydra -V -l %s -P %s %s irc" % (user, word, host))
  sys.exit()

elif hidora == 'XMPP' or hidora == 'xmpp':
  user = raw_input("%s" % (prompt_username))
  host = raw_input("%s" % (prompt_hostname))
  word = raw_input("%s" % (prompt_wordlist))
  os.system("hydra -V -l %s -P %s %s xmpp" % (user, word, host))
  sys.exit()

elif hidora == 'LDAP2' or hidora == 'ldap2':
  user = raw_input("%s" % (prompt_username))
  host = raw_input("%s" % (prompt_hostname))
  word = raw_input("%s" % (prompt_wordlist))
  os.system("hydra -V -l %s -P %s %s ldap2" % (user, word, host))
  sys.exit()

elif hidora == 'LDAP2S' or hidora == 'ldap2s':
  user = raw_input("%s" % (prompt_username))
  host = raw_input("%s" % (prompt_hostname))
  word = raw_input("%s" % (prompt_wordlist))
  os.system("hydra -V -l %s -P %s %s ldap2s" % (user, word, host))
  sys.exit()

elif hidora == 'LDAP3' or hidora == 'ldap3':
  user = raw_input("%s" % (prompt_username))
  host = raw_input("%s" % (prompt_hostname))
  word = raw_input("%s" % (prompt_wordlist))
  os.system("hydra -V -l %s -P %s %s ldap3" % (user, word, host))
  sys.exit()

elif hidora == 'LDAP3S' or hidora == 'ldap3s':
  user = raw_input("%s" % (prompt_username))
  host = raw_input("%s" % (prompt_hostname))
  word = raw_input("%s" % (prompt_wordlist))
  os.system("hydra -V -l %s -P %s %s ldap3S" % (user, word, host))
  sys.exit()

# Quit Hidora command
elif hidora == 'Quit' or hidora == 'quit':
  print "\n[!] Quitting..."
  sys.exit()
	
# If command is not recognised, script restarts
else:
  print "\n[!] Input not recognised..."
  time.sleep(1)
  restart()
