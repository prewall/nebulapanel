#!/usr/bin/python
import cgi
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
    <h1 class="page-header"> Python <small>Setup</small></h1>
        <p>Welcome to <font color=blue> PreWall </font> installation wizard. </p>
  <hr>

  <blockquote class="blockquote-reverse">
        <p> <b>Note: </b>This is a <mark>beta program</mark> and please proceed all changes with causion.</p>
  </blockquote>

<hr>
<table class="table">
</thead>
  <tbody>
    <tr>
      <th scope="row">USERNAME</th>
      <td>%s</td>
    </tr>
    <tr>
      <th scope="row">HOSTNAME</th>
      <td>%s</td>
    </tr>
   <tr>
      <th scope="row">INTERFACE</th>
      <td>%s</td>
    </tr>
  <tr>
      <th scope="row">CLUSTER NAME</th>
      <td>%s</td>
    </tr>
   <tr>
      <th scope="row">ClUSTER MASTER</th>
      <td>%s</td>
    </tr>
  </tbody>
</table>
<hr>

<a href="../cgi-bin/status.py" class="btn btn-success" role="button">PROCEED</a> | <a href="javascript:history.back()" class="btn btn-warning" role="button">BACK</a>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="../js/jquery-3.3.1.slim.min.js"</script>
    <script src="../js/popper.min.js"</script>
    <script src="../js/bootstrap.min.js"</script>
  </body>
</html>

"""
username = form["username"].value
server = form["server"].value
interface = form["interface"].value
clustername = form["clustername"].value
masterip = form["masterip"].value

print(html % (username, server, interface, clustername, masterip))
