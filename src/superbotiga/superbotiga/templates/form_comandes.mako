<html>
	<head>
		<title>Comandes Simple Shop</title>
	</head>
   <body>
		<h1>Comandes SimpleShop</h1>
		% if logged_in:
		    <p id="usuari-box">Usuari: <b>${logged_in}</b> | [<a href="/logout">Sortir</a>]</p>
		% else:
		    <p id="usuari-box">[<a href="/login">Identifica't</a>]</p>	
		% endif
		
		<table border='1'>
				<tr>
					<td><b>ID Comanda</b></td>
					<td><b>ID Client</b></td>
					<td><b>Pomes</b></td>
					<td><b>Peres</b></td>
					<td><b>Platans</b></td>
					<td><b>Taronges</b></td>
					<td><b>Llimones</b></td>
					<td><b>Pastanagues</b></td>
					<td><b>Raïm</b></td>
					<td><b>Preu</b></td>
				</tr>
				
				<tr>
					<td><b>${id_comanda}</b></td>
					<td><b>${id_client}</b></td>
					<td><b>${pomes} Kg.</b></td>
					<td><b>${peres} Kg.</b></td>
					<td><b>${platans} Kg.</b></td>
					<td><b>${taronges} Kg.</b></td>
					<td><b>${llimones} Kg.</b></td>
					<td><b>${pastanagues} Kg.</b></td>
					<td><b>${raim} Kg.</b></td>
					<td><b>${preu} €</b></td>
				</tr>
		</table>
		<br>
		<a href=${request.route_url('home')}>Inici</a>
		<br>
		<a href=${request.route_url('llistat_comandes')}>Veure Llistat de Comandes</a>
	</body>
</html>
