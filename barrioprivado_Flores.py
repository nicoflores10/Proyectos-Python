import sqlite3

conexion=sqlite3.connect("BarrioPrivado.db")
cursor=conexion.cursor()

def ingresar():
	while True:
		nya=input("Ingrese el nombre y apellido:")
		lot=int(input("Ingrese el numero de lote:"))
		mza=int(input("Ingrese el numero de manzana:"))
		cursor.execute("SELECT * FROM PROPIETARIOS WHERE Lote=? AND Manzana=?",(lot,mza))
		propp=cursor.fetchall()
		bd=0
		if len(propp)==0:
			fec_com=input("Ingrese fecha de compra(dd/mm/aaaa):")
			sup_cub=int(input("Superficie cubierta en m2:"))
			habit=int(input("Habitantes en casa:"))
			vehi=int(input("Cantidad de vehiculos:"))
			fec_vta=input("Ingrese fecha de venta(dd/mm/aaaa):")

			conf=input("Confirmar datos(S-N):")
			if conf=="S" or conf=="s":
				cursor.execute("INSERT INTO PROPIETARIOS VALUES(?,?,?,?,?,?,?,?)",(nya,lot,mza,fec_com,sup_cub,habit,vehi,fec_vta))
				conexion.commit()
				break
			else:
				print("Datos eliminados")
				break
		else:
			print("Ya creado, ingrese otro")


'''def ingresar():
	nya=input("Ingrese el nombre y apellido:")
	cursor.execute("SELECT * FROM PROPIETARIOS WHERE ")
	propp=cursor.fetchall()
	bd=0
	while True:
		lot=int(input("Ingrese el numero de lote:"))
		mza=int(input("Ingrese el numero de manzana:"))
		if mza==propp[bd][2]:
			if lot==propp[bd][1]:
				print("opción invalida")
			if lot!=propp[bd][1]:
				break
		bd +=1
		if bd==len(propp):
			break
	fec_com=input("Ingrese fecha de compra(dd/mm/aaaa):")
	sup_cub=int(input("Superficie cubierta en m2:"))
	habit=int(input("Habitantes en casa:"))
	vehi=int(input("Cantidad de vehiculos:"))
	fec_vta=input("Ingrese fecha de venta(dd/mm/aaaa):")

	conf=input("Confirmar datos(S-N):")
	if conf=="S" or conf=="s":
		cursor.execute("INSERT INTO PROPIETARIOS VALUES(?,?,?,?,?,?,?,?)",(nya,lot,mza,fec_com,sup_cub,habit,vehi,fec_vta))
		conexion.commit()
	else:
		print("Datos eliminados")'''

def ingresar_lot():
	while True:
		lote=int(input("Ingrese el numero del lote:"))
		manz=int(input("Ingrese el numero de manzana:"))
		cursor.execute("SELECT * FROM LOTES WHERE Lote=? AND Manzana=?",(lote,manz))
		lott=cursor.fetchall()
		bc=0
		if len(lott)==0:
			mts_fr=int(input("Ingrese los metros de frente:"))
			mts_fo=int(input("Ingrese los metros de fondo:"))
			luzpub=input("Tiene luz publica(S-N):")
			agupub=input("Tiene agua publica(S-N):")
			asfalto=input("Tiene asfalto(S-N):")
			esquina=input("Tiene esquina(S-N):")
					
			conf=input("Confirmar datos(S-N):")
			print("--------------------------------------------------")
			if conf=="S" or conf=="s":
				cursor.execute("INSERT INTO LOTES VALUES(?,?,?,?,?,?,?,?)",(lote,manz,mts_fr,mts_fo,luzpub,agupub,asfalto,esquina))
				conexion.commit()
				break
			else:
				print("Datos eliminados")
				break
		else:
			print("Ya creado, ingrese otro")

'''def ingresar_lot():
	lote=int(input("Ingrese el numero del lote:"))
	manz=int(input("Ingrese el numero de manzana:"))
	cursor.execute("SELECT * FROM LOTES WHERE Lote=? AND Manzana=?",(lote,manz))
	lott=cursor.fetchall()
	bc=0
	while True:
		if manz==lott[bc][1]:
			if lote==lott[bc][0]:
				print("opción invalida")
				lote=int(input("Ingrese el numero del lote:"))
				manz=int(input("Ingrese el numero de manzana:"))
			if lote!=lott[bc][0]:
				break
		bc +=1
		if bc==len(lott):
			break
	mts_fr=int(input("Ingrese los metros de frente:"))
	mts_fo=int(input("Ingrese los metros de fondo:"))
	luzpub=input("Tiene luz publica(S-N):")
	agupub=input("Tiene agua publica(S-N):")
	asfalto=input("Tiene asfalto(S-N):")
	esquina=input("Tiene esquina(S-N):")
			
	conf=input("Confirmar datos(S-N):")
	print("--------------------------------------------------")
	if conf=="S" or conf=="s":
		cursor.execute("INSERT INTO LOTES VALUES(?,?,?,?,?,?,?,?)",(lote,manz,mts_fr,mts_fo,luzpub,agupub,asfalto,esquina))
		conexion.commit()
	else:
		print("Datos eliminados")'''


while True:
	print("--------------------------------------------------------------")
	print("                      MENU BARRIO PRIVADO                     ")
	print("1_ Lotes")
	print("2_ Propietarios")
	print("3_ Costos")
	print("4_ Consumos")
	print("5_ Liquidación")
	print("0_ Salir del menú")
	print("--------------------------------------------------------------")

	op_menu_prin=int(input("Ingrese la opción que usted desee:"))

	if op_menu_prin==0:
		print("Gracias por usar el sistema😉")
		break

	if op_menu_prin==1:
		while True:
			print("--------------------------------------------------")
			print("                     LOTES                        ")
			print("1_ Alta")
			print("2_ Modificar")
			print("3_ Consulta")
			print("0_ Salir")
			print("--------------------------------------------------")
			ingr=int(input("Ingrese la opción:"))

			if ingr>3:
				print("Ingrese una opción valida")
			if ingr==0:
				break
			if ingr==1:
				print("--------------------------------------------------")
				print("                ALTA DE LOTES                     ")
				ingresar_lot()
				print("--------------------------------------------------")
				
			
			if ingr==2:
				cursor.execute("SELECT * FROM LOTES")
				moda=cursor.fetchall()
				bb=0
				manzi=int(input("Ingrese el numero de manzana:"))
				loti=int(input("Ingrese el numero de lote a modificar:"))

				if manzi==moda[bb][1]:
					if loti==moda[bb][0]:
						print("----------------------------")
						print("1_Metros de frente")
						print("2_Metros de fondo")
						print("3_Luz publica")
						print("4_Agua publica")
						print("5_Asfalto")
						print("6_Esquina")
						print("0_ Salir")
						print("----------------------------")
						ing=int(input("Ingrese la opcion que desea modificar:"))

						while True:
							if ing>6:
								print("opcion invalida")
							if ing==0:
								break					
							if ing==1:
								mtfr=int(input("Ingrese metros de frente:"))
								cursor.execute("UPDATE LOTES SET Mts_fren=? WHERE Lote LIKE ?",(mtfr,loti))
								conexion.commit()
								print("MODIFICADO")
								break
							if ing==2:
								mtfo=int(input("Ingrese metros de fondo:"))
								cursor.execute("UPDATE LOTES SET Mts_fon=? WHERE Lote LIKE ?",(mtfo,loti))
								conexion.commit()
								print("MODIFICADO")
								break				
							if ing==3:
								lp=input("Ingrese Luz publica(S-N):")
								cursor.execute("UPDATE LOTES SET Luz_pub=? WHERE Lote LIKE ?",(lp,loti))
								conexion.commit()
								print("MODIFICADO")
								break
							if ing==4:
								ap=input("Ingrese Agua publica(S-N):")
								cursor.execute("UPDATE LOTES SET Agua_pub=? WHERE Lote LIKE ?",(ap,loti))
								conexion.commit()
								print("MODIFICADO")
								break
							if ing==5:
								asfi=input("Ingrese si tiene asfalto(S-N):")
								cursor.execute("UPDATE LOTES SET Asfalto=? WHERE Lote LIKE ?",(asfi,loti))
								conexion.commit()
								print("MODIFICADO")
								break
							if ing==6:
								esq=input("Ingrese si tiene esquina(S-N):")
								cursor.execute("UPDATE LOTES SET Esquina=? WHERE Lote LIKE ?",(esq,loti))
								conexion.commit()
								print("MODIFICADO")
								break

					if loti!=moda[bb][0]:
						print("Lote no encontrado")
						des=input("Desea crearlo?(S-N):")
						if des=="S":
							ingresar_lot()

			if ingr==3:
				print("------------------------------------------------------------------------------")
				print("1_ Consulta por lote")
				print("2_ Consulta por manzana y lote")
				print("0_ Salir")
				print("------------------------------------------------------------------------------")
				ingrr=int(input("Ingrese la opción:"))
				
				while True:
					if ingrr==0:
						break

					if ingrr>2:
						print("Opcion invalida")
						
					if ingrr==1:
						manza=int(input("Ingrese el numero de manzana:"))
						lotee=int(input("Ingrese el numero de lote a consultar:"))
						cursor.execute("SELECT * FROM LOTES")
						mido=cursor.fetchall()
						br=0
						eia=0
						while True:
							try:
								if manza==mido[br][1]:
									if lotee==mido[br][0]:
										print("------------------------------------------------------------------------------")
										print("|{:^5}|{:^8}|{:^14}|{:^14}|{:^14}|{:^14}|{:^8}|{:^8}|".format("Lote","Manzana","Mt de frente","Mt de fondo","Luz publica","Agua publica","Asfalto","Esquina"))
										print("|{:^5}|{:^8}|{:^14}|{:^14}|{:^14}|{:^14}|{:^8}|{:^8}|".format(mido[br][0],mido[br][1],mido[br][2],mido[br][3],mido[br][4],mido[br][5],mido[br][6],mido[br][7]))
										print("------------------------------------------------------------------------------")
										br+=1
										eia=100
									else:
										br+=1

									if br==len(mido):
										if eia >= 100:
											break
											print("No se encuentra")
												
											preg=input("Desea crearlo?(S-N):")
											if preg=="S":
												ingresar()
											else:
												pass
												
											break
				
							except TypeError:
								pass

					if ingrr==2:
						mazi=int(input("Ingrese la manzana que desea ver:"))
						cursor.execute("SELECT * FROM LOTES")
						mido=cursor.fetchall()
						br=0
						eia=0
						while True:
							try:
								if mazi==mido[br][1]:
									print("------------------------------------------------------------------------------")
									print("|{:^5}|{:^8}|{:^14}|{:^14}|{:^14}|{:^14}|{:^8}|{:^8}|".format("Lote","Manzana","Mt de frente","Mt de fondo","Luz publica","Agua publica","Asfalto","Esquina"))
									print("|{:^5}|{:^8}|{:^14}|{:^14}|{:^14}|{:^14}|{:^8}|{:^8}|".format(mido[br][0],mido[br][1],mido[br][2],mido[br][3],mido[br][4],mido[br][5],mido[br][6],mido[br][7]))
									print("------------------------------------------------------------------------------")
									br+=1
									eia=100
								else:
									br+=1

								if br==len(mido):
									if eia >= 100:
										break
									print("No se encuentra")
									break
								
							except TypeError:
								pass

	if op_menu_prin==2:
		while True:
			print("--------------------------------------------------")
			print("                   PROPIETARIOS                   ")
			print("1_ Alta")
			print("2_ Consulta")
			print("3_ Modificar")
			print("4_ Baja")
			print("0_ Volver MP")
			print("--------------------------------------------------")

			op_prop=int(input("Ingrese la opción que desee:"))

			if op_prop==1:
				ingresar()

			if op_prop==2:
				while True:
					print("------------------------------------------------------------------------------")
					print("1_ Consulta por propietario")
					print("2_ Consulta por manzana")
					print("0_ Salir")
					print("------------------------------------------------------------------------------")

					inn=int(input("Ingrese la opción que usted desea:"))

					if inn==1:
						nya=input("Ingrese el nombre y apellido del propietario a buscar:")
						cursor.execute("SELECT * FROM PROPIETARIOS")
						modi=cursor.fetchall()
						TT=0
						eia=0
						while True:
							try:
								if nya==modi[TT][0]:
									print("------------------------------------------------------------------------------")
									print("|{:^20}|{:^14}|{:^14}|{:^14}|{:^14}|{:^14}|{:^14}|{:^14}|".format("Nombre y Apellido","Nro de Lote","Nro de Manzana","Fecha de compra","Superficie cubierta","Habitantes","Nro de vehiculos","Fecha de venta"))
									print("|{:^20}|{:^14}|{:^14}|{:^15}|{:^18}|{:^14}|{:^14}|{:^14}|".format(modi[TT][0],modi[TT][1],modi[TT][2],modi[TT][3],modi[TT][4],modi[TT][5],modi[TT][6],modi[TT][7]))
									print("------------------------------------------------------------------------------")
									TT+=1
									eia=100
								else:
									TT+=1

								if TT==len(modi):
									if eia >= 100:
										break
									print("No se encuentra")
									
									preg=input("Desea crearlo?(S-N):")
									if preg=="S":
										ingresar()
									else:
										pass
									
									break
							
							except TypeError:
								pass

					if inn==2:
						mazi=int(input("Ingrese la manzana que desea ver:"))
						cursor.execute("SELECT * FROM PROPIETARIOS")
						modi=cursor.fetchall()
						TT=0
						eia=0
						while True:
							try:
								if mazi==modi[TT][2]:
									print("------------------------------------------------------------------------------")
									print("|{:^20}|{:^14}|{:^14}|{:^14}|{:^14}|{:^14}|{:^14}|{:^14}|".format("Nombre y Apellido","Nro de Lote","Nro de Manzana","Fecha de compra","Superficie cubierta","Habitantes","Nro de vehiculos","Fecha de venta"))
									print("|{:^20}|{:^14}|{:^14}|{:^15}|{:^18}|{:^14}|{:^14}|{:^14}|".format(modi[TT][0],modi[TT][1],modi[TT][2],modi[TT][3],modi[TT][4],modi[TT][5],modi[TT][6],modi[TT][7]))
									print("------------------------------------------------------------------------------")
									TT+=1
									eia=100
								else:
									TT+=1

								if TT==len(modi):
									if eia >= 100:
										break
									print("No se encuentra")
									break
							
							except TypeError:
								pass

			if op_prop==3:
				cursor.execute("SELECT * FROM PROPIETARIOS")
				modi=cursor.fetchall()
				nya=input("Ingrese el nombre y apellido del propietario a modificar(Nombre y Apellido):")
				print("----------------------------")
				print("1_Fecha de compra")
				print("2_Superficie cubierta")
				print("3_Habitantes")
				print("4_Vehiculos")
				print("5_Fecha de venta")
				print("0_ Salir")
				print("----------------------------")
				ing=int(input("Ingrese la opcion que desea modificar:"))

				while True:
					if ing>7:
						print("opcion invalida")
					if ing==0:
						break					
					if ing==1:
						fec_com=input("Ingrese fecha de compra(dd/mm/aaaa):")
						cursor.execute("UPDATE PROPIETARIOS SET FecComp=? WHERE NomyApe LIKE ?",(fec_com,nya))
						conexion.commit()
						print("MODIFICADO")
					if ing==2:
						sup_cub=int(input("Superficie cubierta en m2:"))
						cursor.execute("UPDATE PROPIETARIOS SET SupCub=? WHERE NomyApe LIKE ?",(sup_cub,nya))
						conexion.commit()
						print("MODIFICADO")					
					if ing==3:
						habit=int(input("Habitantes en casa:"))
						cursor.execute("UPDATE PROPIETARIOS SET Habitantes=? WHERE NomyApe LIKE ?",(habit,nya))
						conexion.commit()
						print("MODIFICADO")
					if ing==4:
						vehi=int(input("Cantidad de vehiculos:"))
						cursor.execute("UPDATE PROPIETARIOS SET Vehiculos=? WHERE NomyApe LIKE ?",(vehi,nya))
						conexion.commit()
						print("MODIFICADO")
					if ing==5:
						fec_vta=input("Ingrese fecha de venta(dd/mm/aaaa):")
						cursor.execute("UPDATE PROPIETARIOS SET FecBaja=? WHERE NomyApe LIKE ?",(fec_vta,nya))
						conexion.commit()
						print("MODIFICADO")

			if op_prop==4:
				cursor.execute("SELECT * FROM PROPIETARIOS")
				ven=cursor.fetchall()
				nom=input("Ingrese el nombre del propietario a bajar:")
				cursor.execute("SELECT * FROM PROPIETARIOS WHERE NomyApe=?",(nom,))
				ven=cursor.fetchall()
				for c in range(len(ven)):
					ven=input("Fecha de venta(dd/mm/aaaa):")
					cursor.execute("DELETE FROM PROPIETARIOS WHERE FecBaja=?",(ven,))
					conexion.commit()
					print("eliminado")

	if op_menu_prin==3:
		while True:
			print("--------------------------------------------------")
			print("                     COSTOS                       ")
			print("1_ Alta")
			print("2_ Consulta")
			print("3_ Baja")
			print("0_ Volver MP")
			print("--------------------------------------------------")
			inn=int(input("Ingrese la opción que desee:"))

			if inn>3:
				print("Opcion invalida")
			if inn==0:
				break
			if inn==1:
				cursor.execute("SELECT * FROM COSTOS")
				propp=cursor.fetchall()
				bd=0
				
				nrolot=int(input("Ingrese el lote:"))
				nromanza=int(input("Ingrese la manzana:"))
				nomprop=input("ingrese el nombre del propietario:")
				fecha=input("Ingrese mes y año(mm/aaaa):")
				conluz=int(input("Ingrese el consumo de luz x kw:"))
				conag=int(input("Ingrese el consumo de agua x mt3:"))
				congas=int(input("Ingrese el consumo de gas x mt3:"))
				luzpubli=input("Luz publica(S-N):")
				aguapubli=input("Agua publica(S-N):")
				asfa=input("Asfalto(S-N):")
				coche=int(input("Cantidad de coches:"))

				conf=input("Confirmar datos(S-N):")
				print("--------------------------------------------------")
				if conf=="S" or conf=="s":
					cursor.execute("INSERT INTO COSTOS VALUES(?,?,?,?,NULL,?,?,?,?,?,?,?,NULL)",(nrolot,nromanza,nomprop,fecha,conluz,conag,congas,luzpubli,aguapubli,asfa,coche))
					conexion.commit()
				else:
					print("Datos eliminados")

				cursor.execute("SELECT * FROM CONSUMOS")
				consu=cursor.fetchall()
				c=0
				precio_segu=consu[c][0]
				precio_luz=consu[c][1]*conluz
				precio_agua=consu[c][2]*conag
				precio_gas=consu[c][3]*congas
				if luzpubli=="S" or luzpubli=="s":
					precio_luzpub=consu[c][4]
				else:
					precio_luzpub=0
				
				if aguapubli=="S" or aguapubli=="s":
					precio_aguapub=consu[c][5]
				else:
					precio_aguapub=0

				if asfa=="S" or asfa=="s":
					precio_asfa=consu[c][6]
				else:
					precio_asfa=0
				precio_cochera=consu[c][7]*coche
				precio_terreno=consu[c][8]

				cursor.execute("INSERT INTO LIQUIDACION VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)",(nrolot,nromanza,nomprop,fecha,precio_segu,precio_luz,precio_agua,precio_gas,precio_luzpub,precio_aguapub,precio_asfa,precio_cochera,precio_terreno))
				conexion.commit()

			if inn==2:
				loot=int(input("Ingrese el lote:"))
				man=int(input("Ingrese la manzana:"))
				cursor.execute("SELECT * FROM COSTOS WHERE NroLot = ? AND nromanza = ?",(loot,man))
				modi=cursor.fetchall()
				print(modi)
				TT=0
				eia=0
				if len(modi)==0:
					print("No se encuentra")
				else:
					print("------------------------------------------------------------------------------")
					print("|{:^20}|{:^14}|{:^14}|{:^14}|{:^14}|{:^14}|{:^14}|{:^14}|{:^14}|{:^14}|{:^14}|".format("Lote","Manzana","Nombre","Fecha","Consumo LuzXkw","Consumo aguaXmt3","Consumo gasXmt3","Luz Publica","Agua Publica","Asfalto","Autos"))
					print("|{:^20}|{:^14}|{:^14}|{:^15}|{:^14}|{:^14}|{:^14}|{:^14}|{:^14}|{:^14}|{:^14}|".format(modi[TT][0],modi[TT][1],modi[TT][2],modi[TT][3],modi[TT][5],modi[TT][6],modi[TT][7],modi[TT][8],modi[TT][9],modi[TT][10],modi[TT][11]))
					print("------------------------------------------------------------------------------")
					
			if inn==3:
				nom=input("Ingrese el nombre de propietario a eliminar:")
				cursor.execute("SELECT * FROM COSTOS")
				ven=cursor.fetchall()
				cursor.execute("DELETE FROM COSTOS WHERE NomProp=?",(nom,))
				conexion.commit()
				print("eliminado")
				

	if op_menu_prin==4:
		print("--------------------------------------------------")
		print("                    CONSUMOS                      ")
		print("1_ Consulta")
		print("2_ Modificar")
		print("0_ Volver MP")
		print("--------------------------------------------------")
		inn=int(input("Ingrese la opción que desee:"))

		if inn==7:
			consumos=[
				(30000,60,30,45,80000,40,70,10000,60000)
			]
			cursor.executemany("INSERT INTO CONSUMOS VALUES(?,?,?,?,?,?,?,?,?)",consumos)
			conexion.commit()
			print("CONSUMOS CARGADOS")

		if inn==1:
			cursor.execute("SELECT * FROM CONSUMOS")
			modi=cursor.fetchall()
			TT=0
			print("------------------------------------------------------------------------------")
			print("|{:^9}|{:^9}|{:^10}|{:^10}|{:^14}|{:^14}|{:^9}|{:^16}|{:^14}|".format("Seguridad","Luz x Kw","Agua x mt3","Gas x mt3","Luz publica","Agua publica","Asfalto","Alquiler cochera","Valor terreno"))
			print("|{:^9}|{:^9}|{:^10}|{:^10}|{:^14}|{:^14}|{:^9}|{:^16}|{:^14}|".format(modi[TT][0],modi[TT][1],modi[TT][2],modi[TT][3],modi[TT][4],modi[TT][5],modi[TT][6],modi[TT][7],modi[TT][8]))
			print("------------------------------------------------------------------------------")

		if inn==2:
			cursor.execute("SELECT * FROM CONSUMOS")
			modi=cursor.fetchall()
			tt=0
			print("----------------------------")
			print("1_Seguridad ${:}".format(modi[tt][0]))
			print("2_Luz x Kw ${:}".format(modi[tt][1]))
			print("3_Agua x mt3 ${:}".format(modi[tt][2]))
			print("4_Gas x mt3 ${:}".format(modi[tt][3]))
			print("5_Luz publica ${:}".format(modi[tt][4]))
			print("6_Agua publica ${:}".format(modi[tt][5]))
			print("7_Asfalto ${:}".format(modi[tt][6]))
			print("8_Alquiler cochera ${:}".format(modi[tt][7]))
			print("9_Valor terreno ${:}".format(modi[tt][8]))
			print("0_ Salir")
			print("----------------------------")
			ing=int(input("Ingrese el precio a modificar:"))

			while True:
				if ing>9:
					print("opcion invalida")
				if ing==0:
					break					
				if ing==1:
					seg=int(input("Ingrese el nevo precio:"))
					cursor.execute("UPDATE CONSUMOS SET Seguridad=?",(seg,))
					conexion.commit()
					print("MODIFICADO")
					break
				if ing==2:
					luzxkw=int(input("Ingrese el nevo precio:"))
					cursor.execute("UPDATE CONSUMOS SET Luz_x_Kw=?",(luzxkw,))
					conexion.commit()
					print("MODIFICADO")
					break
				if ing==3:
					agxmt3=int(input("Ingrese el nevo precio:"))
					cursor.execute("UPDATE CONSUMOS SET Agua_x_mt3=?",(agxmt3,))
					conexion.commit()
					print("MODIFICADO")
					break
				if ing==4:
					gasxmt3=int(input("Ingrese el nevo precio:"))
					cursor.execute("UPDATE CONSUMOS SET Gas_x_mt3=?",(gasxmt3,))
					conexion.commit()
					print("MODIFICADO")
					break
				if ing==5:
					luzpu=int(input("Ingrese el nevo precio:"))
					cursor.execute("UPDATE CONSUMOS SET Luz_publica=?",(luzpu,))
					conexion.commit()
					print("MODIFICADO")
					break
				if ing==6:
					aguapu=int(input("Ingrese el nevo precio:"))
					cursor.execute("UPDATE CONSUMOS SET Agua_publica=?",(aguapu,))
					conexion.commit()
					print("MODIFICADO")
					break
				if ing==7:
					asf=int(input("Ingrese el nevo precio:"))
					cursor.execute("UPDATE CONSUMOS SET Asfalto=?",(asf,))
					conexion.commit()
					print("MODIFICADO")
					break
				if ing==8:
					alqcoch=int(input("Ingrese el nevo precio:"))
					cursor.execute("UPDATE CONSUMOS SET Alquiler_cochera=?",(alqcoch,))
					conexion.commit()
					print("MODIFICADO")
					break
				if ing==9:
					valterr=int(input("Ingrese el nevo precio:"))
					cursor.execute("UPDATE CONSUMOS SET Valor_terreno=?",(valterr,))
					conexion.commit()
					print("MODIFICADO")
					break

	if op_menu_prin==5:
		while True:
			print("--------------------------------------------------")
			print("                    LIQUIDACION                   ")
			print("1_ Consulta")
			print("2_ Baja")
			print("0_ Salir")
			print("--------------------------------------------------")
			ingr=int(input("Ingrese la opción:"))

			if ingr>2:
				print("Opcion invalida")
			if ingr==0:
				break
			if ingr==1:
				loot=int(input("Ingrese el lote:"))
				man=int(input("Ingrese la manzana:"))
				cursor.execute("SELECT * FROM LIQUIDACION WHERE NroLote = ? AND NroManzana = ?",(loot,man))
				modi=cursor.fetchall()
				print(modi)
				TT=0
				eia=0
				if len(modi)==0:
					print("No se encuentra")
				else:
					print("------------------------------------------------------------------------------")
					print("|{:^20}|{:^14}|{:^14}|{:^14}|{:^14}|{:^14}|{:^14}|{:^14}|{:^14}|{:^14}|{:^14}|".format("Lote","Manzana","Nombre","Fecha","Seguridad","Consumo LuzXkw","Consumo aguaXmt3","Consumo gasXmt3","Luz Publica","Agua Publica","Asfalto","Autos","Terreno"))
					print("|{:^20}|{:^14}|{:^14}|{:^15}|{:^14}|{:^14}|{:^14}|{:^14}|{:^14}|{:^14}|{:^14}|".format(modi[TT][0],modi[TT][1],modi[TT][2],modi[TT][3],modi[TT][4],modi[TT][5],modi[TT][6],modi[TT][7],modi[TT][8],modi[TT][9],modi[TT][10],modi[TT][11],modi[TT][12]))
					print("------------------------------------------------------------------------------")
			if ingr==2:
				nom=input("Ingrese el nombre de propietario a eliminar:")
				cursor.execute("SELECT * FROM LIQUIDACION")
				ven=cursor.fetchall()
				cursor.execute("DELETE FROM LIQUIDACION WHERE NomPropie=?",(nom,))
				conexion.commit()
				print("eliminado")