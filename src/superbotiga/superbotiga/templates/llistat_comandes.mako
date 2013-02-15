<html>
	<head>
		<title>Comandes Simple Shop</title>
	</head>
   <body>
      <h1>Llistat Comandes - ${projecte}</h1>
      <a href='/'>Tornar</a><br><br>
      <form action="comandes" method="post">
			<table border='1'>
				<tr>
					<td><b>ID Comanda</b></td>
					<td><b>ID Client</b></td>
					<td><b>Pomes (Kg)</b></td>
					<td><b>Peres (Kg)</b></td>
					<td><b>Platans (Kg)</b></td>
					<td><b>Taronges (Kg)</b></td>
					<td><b>Llimones (Kg)</b></td>
					<td><b>Pastanagues (Kg)</b></td>
					<td><b>Raïm (Kg)</b></td>
					<td><b>Preu (€)</b></td>
				</tr>
				%if len(dict_comandes)==0:
				<tr>
					    <td colspan="10" align="center"><b>No hi han comandes a la llista</b></td>
				</tr>
				% endif
				
				% for id_comanda in dict_comandes.keys():
				    
					<tr>
					    <td>${dict_comandes[id_comanda]['id']}</td>
					    <td>${dict_comandes[id_comanda]['id_client']}</td>
					    <td>${dict_comandes[id_comanda]['pomes']}</td>
					    <td>${dict_comandes[id_comanda]['peres']}</td>
					    <td>${dict_comandes[id_comanda]['platans']}</td>
					    <td>${dict_comandes[id_comanda]['taronges']}</td>
					    <td>${dict_comandes[id_comanda]['llimones']}</td>
					    <td>${dict_comandes[id_comanda]['pastanagues']}</td>
					    <td>${dict_comandes[id_comanda]['raim']}</td>
					    <td>${dict_comandes[id_comanda]['preu']}</td>
					</tr>
				% endfor
			</table>
		</form>
		<a href='/'>Tornar</a>
   </body>
</html>
