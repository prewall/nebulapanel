#!/usr/bin/python
import cgi, os
form = cgi.FieldStorage()

print('Content-type: text/html')

html = """
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="../css/bootstrap.min.css">

    <title>Python Setup</title>
  </head>
  <body>
  <div class="container">
    <h1 class="page-header"> OPENNEBULA <small>Control Panel</small></h1>
  <hr>
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNavDropdown">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link" href="../home/index.html">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">About</a>
      </li>
        <li class="nav-item dropdown">
        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
          Controls
        </a>
        <div class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
          <a class="dropdown-item" href="../cgi-bin/status.py">Service Status</a>
          <a class="dropdown-item" href="#">Configuration</a>
          <a class="dropdown-item" href="#">ZFS</a>
          <a class="dropdown-item" href="../cgi-bin/packages.py">Manage Packages</a>
        </div>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="../cgi-bin/pcstatus.py">System Info</a>
      </li>
    </ul>
  </div>
</nav>
<hr>

  <blockquote class="blockquote-reverse">
	<p> Press <kbd>Back</kbd> and click <kbd> REFRESH </kbd> button.
  </blockquote>

<hr>
<table class="table">
<thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">SERVICE</th>
      <th scope="col">STATUS</th>
      <th scope="col">MANAGE</th>
    </tr>
  <tbody>
    <tr>
      <th scope="row">1</th>
      <td>Opennebula Server</td>
      <td>%s</td>
    </tr>
    <tr>
      <th scope="row">2</th>
      <td>Opennebula Web</td>
      <td>%s</td>
    </tr>
   <tr>
      <th scope="row">3</th>
      <td>Logstash</td>
      <td>%s</td>
	</tr>
  <tr>
      <th scope="row">4</th>
      <td>Libvirt</td>
      <td>%s</td>
	</tr>
  </tbody>
</table>
<hr>
<a href="../cgi-bin/status.py" class="btn btn-info" role="button">BACK</a>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="../js/jquery-3.3.1.slim.min.js"</script>
    <script src="../js/popper.min.js"</script>
    <script src="../js/bootstrap.min.js"</script>
  </body>
</html>

"""
ELASTICSEARCH = os.popen('systemctl status opennebula | head -3 | grep running | cut -c 20-26').read(7)
LOGSTASH = os.popen('systemctl status logstash | head -3 | grep running | cut -c 20-26').read(7)
KIBANA = os.popen('systemctl status opennebula-sunstone | head -3 | grep running | cut -c 20-26').read(7)
SURICATA = os.popen('systemctl status libvirtd | head -3 | grep running | cut -c 20-26').read(7)
#os.setuid('0')
srv = form["serviceb"].value


#print(html % (ELASTICSEARCH, LOGSTASH, KIBANA, SURICATA))

def esServiceStatus():
	if ELASTICSEARCH == "running" :
		ES = "running"
		lsServiceStatus(ES)
	else:
		ES = "stopped"
		lsServiceStatus(ES)

def lsServiceStatus(ES):
        if LOGSTASH == 'running' :
		LS = "running"
                kbServiceStatus(ES, LS)
        else:
		LS = "stopped"
		kbServiceStatus(ES, LS)

def kbServiceStatus(ES, LS):
        if KIBANA == 'running' :
		KB = "running"
                srServiceStatus(ES, LS, KB)
        else:
		KB = "stopped"
                srServiceStatus(ES, LS, KB)

def srServiceStatus(ES, LS, KB):
        if SURICATA == 'running' :
		SR = "running"
		printAll(ES, LS, KB, SR)
                
        else:
		SR = "stopped"
                printAll(ES, LS, KB, SR)

def printAll(ES, LS, KB, SR):
	#IM = print(form)
	print(html % (ES, LS, KB, SR))

def srvCheck():
	if "elstart" in srv:
		os.system('sudo systemctl start opennebula > /tmp/tmp')
		esServiceStatus()
	elif 'elstop' in srv:
		os.system('sudo systemctl stop opennebula > /tmp/tmp')
        	esServiceStatus()
	elif 'kbstart' in srv:
                os.system('sudo systemctl start opennebula-sunstone > /tmp/tmp')
                esServiceStatus()
	elif 'kbstop' in srv:
                os.system('sudo systemctl stop opennebula-suntone > /tmp/tmp')
                esServiceStatus()
	elif 'lsstart' in srv:
                os.system('sudo systemctl start logstash > /tmp/tmp')
                esServiceStatus()
	elif 'lsstop' in srv:
                os.system('sudo systemctl stop logstash > /tmp/tmp')
                esServiceStatus()
	elif 'srstart' in srv:
                os.system('sudo systemctl start libvirtd > /tmp/tmp')
                esServiceStatus()
	elif 'srstop' in srv:
                os.system('sudo systemctl stop libvirtd > /tmp/tmp')
                esServiceStatus()
	else:
		esServiceStatus()

srvCheck()
