<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" xmlns:tal="http://xml.zope.org/namespaces/tal">
<head>
  <title>Login - Pyramid tutorial</title>
  <meta http-equiv="Content-Type" content="text/html;charset=UTF-8"/>
  <meta name="keywords" content="python web application" />
  <meta name="description" content="pyramid web application" />
  <link rel="shortcut icon" href="static/favicon.ico" />
  <link rel="stylesheet" href="static/pylons.css" type="text/css" media="screen" charset="utf-8" />
 
</head>
<body>
  <div id="wrap">
    <div id="top-small">
      <div class="top-small align-center">
        <div>
	
	  <img width="220" height="50" alt="pyramid" src="static/pyramid-small.png" />
        </div>
      </div>
    </div>
    <div id="middle">
      <div class="middle align-right">
        <div id="left" class="app-welcome align-left">
          <b>Login</b> 
	 
	  <a href="/">Anar a la Home Page</a>
	  
	  <br/>
          % if message:
            ${message}
          % endif
        </div>
        <div id="right" class="app-welcome align-right"></div>
      </div>
    </div>
    <div id="bottom">
      <div class="bottom">
        <form action="${url}" method="post">
          <input type="hidden" name="came_from" value="${came_from}"/>
          <input type="text" name="login" value="${login}"/><br/>
          <input type="password" name="password"
                 value="${password}"/><br/>
          <input type="submit" name="form.submitted" value="Log In"/>
        </form>
      </div>
    </div>
  </div>
  <div id="footer">
    <div class="footer">Copyleft Institut Lacetània 2013.</div>
  </div>
</body>
</html>
