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
    <h1 class="page-header"> OPENNEBULA <small>System Info  v1.0</small> </h1>
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
          <a class="dropdown-item" href="../cgi-bin/zfs.py">ZFS</a>
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

<p class="bg-info"><b>OS</b> :  %s</p>

<table class="table table-hover">
<thead>
    <tr>
    </tr>
  </thead>
<tbody>
    <tr>
      <td>%s</td>
    </tr>
</tbody>
</table>


<hr>


<input type="button" value="Refresh Page" onClick="location.href=location.href"> 

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="../js/jquery-3.3.1.slim.min.js"></script>
    <script src="../js/popper.min.js"></script>
    <script src="../js/bootstrap.min.js"></script>
  </body>
</html>

"""
filepath = "lscpu.tmp"
filepathi = "lscpuhtml.tmp"

os.system('sudo rm -rf lscp*')
os.system('sudo touch lscpu.tmp lscpuhtml.tmp ')
os.system('sudo chmod 777 lscpu.tmp lscpuhtml.tmp ')

osmsg = os.popen('sudo uname').read()
os.system('sudo lscpu > lscpu.tmp')

def pcStatus():
	msg = os.popen('cat lscpuhtml.tmp').read()
	print(html % (osmsg, msg))

#def pcHtml():
with open(filepath) as fp, open(filepathi, 'w') as fw:
   line = fp.readline()
   cnt = 1
   while line:
       #print("<p>{}</p>".format(line.strip()))
       fw.write("<p>" + str(line.strip()) + "</p>")
       line = fp.readline()
       cnt += 1
#	pcStatus()

pcStatus()
