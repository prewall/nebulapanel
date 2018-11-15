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
    <h1 class="page-header"> OPENNEBULA <small>Packages</small></h1>
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

<table class="table table-hover">
  <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">Package</th>
      <th scope="col">Version/Status</th>
      <th scope="col">License</th>
      <th scope="col">Last Modified</th>
      <th scope="col">Add/Remove</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">1</th>
      <td>Opennebula Sunstone</td>
      <td>%s</td>
      <td>%s</td>
      <td>%s</td>
      <td>FORBIDDEN</td>
    </tr>
    <tr>
      <th scope="row">2</th>
      <td>Opennebula Server</td>
      <td>%s</td>
      <td>%s</td>
      <td>%s</td>
      <td>FORBIDDEN</td>
    </tr>
	<tr>
      <th scope="row">3</th>
      <td>VIM</td>
      <td>%s</td>
      <td>%s</td>
      <td>%s</td>
      <td><form method=POST action="../cgi-bin/pkg.py"> <button name="serviceb" value="vim" type=submit class="btn btn-%s">%s</button> </form> </td>
    </tr>
	<tr>
      <th scope="row">4</th>
      <td>Libvirt</td>
      <td>%s</td>
      <td>%s</td>
      <td>%s</td>
      <td>FORBIDDEN</td>
    </tr>
  </tbody>
</table>

<hr>


    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="../js/jquery-3.3.1.slim.min.js"></script>
    <script src="../js/popper.min.js"></script>
    <script src="../js/bootstrap.min.js"></script>
  </body>
</html>

"""
filepath = "pkg.tmp"
filepathi = "pkghtml.tmp"

vimb = "danger"
vimbb = "REMOVE"

os.system('sudo rm -rf pkg*')
os.system('sudo touch pkg.tmp pkghtml.tmp ')
os.system('sudo chmod 777 pkg.tmp pkghtml.tmp ')

pkg1 = os.popen('sudo rpm -qi opennebula-sunstone | head -n2 | grep Version | cut -c 15-20').read()
pkg2 = os.popen('sudo rpm -qi opennebula | head -n2 | grep Version | cut -c 15-20').read()
pkg3 = os.popen('sudo rpm -qi vim-enhanced | head -n10 | grep Version | cut -c 15-20').read()
pkg4 = os.popen('sudo rpm -qi libvirt | head -n10 | grep Version | cut -c 15-20').read()
lic1 = os.popen('sudo rpm -qi opennebula-sunstone | head -n8 | grep License | cut -c 15-20').read()
lic2 = os.popen('sudo rpm -qi opennebula | head -n8 | grep License | cut -c 15-20').read()
lic3 = os.popen('sudo rpm -qi vim-enhanced | head -n10 | grep License | cut -c 15-20').read()
lic4 = os.popen('sudo rpm -qi libvirt | head -n10 | grep License | cut -c 15-20').read()
lm1 = os.popen('sudo rpm -qi opennebula-sunstone | head -n10 | grep "Install Date" | cut -c 15-42').read()
lm2 = os.popen('sudo rpm -qi opennebula | head -n10 | grep "Install Date" | cut -c 15-42').read()
lm3 = os.popen('sudo rpm -qi vim-enhanced | head -n10 | grep "Install Date" | cut -c 15-42').read()
lm4 = os.popen('sudo rpm -qi libvirt | head -n10 | grep "Install Date" | cut -c 15-42').read()

os.system('sudo lscpu > pkg.tmp')

def pcStatus():
	msg = os.popen('cat lscpuhtml.tmp').read()
	print(html % (pkg1, lic1, lm1, pkg2, lic2, lm2, pkg3, lic3, lm3, vimb, vimbb, pkg4, lic4, lm4))

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
