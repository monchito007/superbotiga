<html>
	<head>
		<title>Comandes Simple Shop</title>
	</head>
   <body>
      <h1>${projecte}</h1>
      <!--<form action="${request.route_url('new')}" method="post">-->
      <form  method="post">
			<table border='1'>
				<tr>
					<td><b>ID</b></td>
					<td><b>Nom</b></td>
					<td><b>Stock</b></td>
					<td><b>Preu</b></td>
					<td><b>Quantitat (Kg)</b></td>
				</tr>
				% for prod in dades_productes.keys():
					<tr>
						<td>${dades_productes[prod]['id']}</td>
						<td>${prod}</td>
						<td>${dades_productes[prod]['stock']} Kg</td>
						<td>${dades_productes[prod]['preu']} €/Kg</td>
						<td>
						<select name=${prod} >
						% for i in range(0,dades_productes[prod]['stock']+1,1):
							% if i==0:
								<option value=${i} selected='true'>${i}</option>
							%else:
								<option value=${i} >${i}</option>
							%endif
							
						% endfor
						</td>
						</select>
					</tr>
				% endfor
					<tr>
						<td colspan=5><input type="submit" name="add" value="Realitzar comanda" class="button"></td>
					</tr>
			</table>
		</form>
   </body>
</html>
