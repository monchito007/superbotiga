<html>
	<head>
		<title>Benvinguda SUPERBOTIGA Simple Shop</title>
	</head>
   <body>
		<h1>Benvinguda SUPERBOTIGA SimpleShop</h1>
		
    % if logged_in:
        <p id="usuari-box">Usuari: <b>${logged_in}</b> | [<a href="/logout">Sortir</a>]</p>
    % else:
	<p id="usuari-box">[<a href="/login">Identifica't</a>]</p>
	
    % endif
        <ul>
        <li><h2><a href=${request.route_url('llista_productes')} >Veure productes botiga</a></h2></li>
        <li><h2><a href=${request.route_url('productes')} >Realitzar comanda</a></h2></li>
        <li><h2><a href=${request.route_url('llistat_comandes')} >Veure llistat de comandes</a></h2></li>
        
        
        
        
        </ul>
		
	
	</body>
</html>
