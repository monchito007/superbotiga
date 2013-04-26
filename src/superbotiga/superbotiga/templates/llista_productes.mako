<html>
	<head>
		<title>Llista de productes Simple Shop</title>
	</head>
   <body>
      <h1>Llista de productes - ${projecte}</h1>
    % if logged_in:
        <p id="usuari-box">Usuari: <b>${logged_in}</b> | [<a href="/logout">Sortir</a>]</p>
    % else:
	<p id="usuari-box">[<a href="/login">Identifica't</a>]</p>	
    % endif
      <form action="comandes" method="post">
			<table border='1'>
				<tr>
				    <td><b>ID</b></td>
				    <td><b>Nom</b></td>
				    <td><b>Stock</b></td>
				    <td><b>Preu</b></td>
					
				</tr>
				% for prod in dades_productes:
				<tr>
				    <td>${dades_productes[prod]['id']}</td>
				    <td>${prod}</td>
				    <td>${dades_productes[prod]['stock']} Kg</td>
				    <td>${dades_productes[prod]['preu']} €/Kg</td>
				</tr>
				% endfor
				<tr>
				    <td colspan=4 align="center"><a href=${request.route_url('home')}>Tornar</a></td>
				</tr>
			</table>
	</form>
   </body>
</html>
