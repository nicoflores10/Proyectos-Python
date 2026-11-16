import sqlite3


conexion=sqlite3.connect("GestionGanadera.db")
cursor=conexion.cursor()

def ingresar_campo():
	desc_campo=input("Descripción del campo(Sierra-Llano):")
	largo_campo=int(input("Largo del campo en metros:"))
	ancho_campo=int(input("Ancho del campo en metros:"))
	sup_campo=largo_campo*ancho_campo
	localidad_campo=input("localidad en la que está ubicada el campo:")
	direccion_campo=int(input("dirección calle(numero) donde esta ubicada la entrada al campo:"))
	propietario_campo=input("nombre y apellido del propietario del campo o la persona con la que hablamos:")
	telefono_campo=int(input("número de teléfono del propietario del campo o la persona con la que hablamos:"))
	email_campo=input("email del propietario del campo o la persona con la que hablamos:")
	inicioactlaboral_campo=input("fecha de cuando empezamos a trabajar en ese campo(dd/mm/aaaa):")

	desea_campo=int(input("¿Desea guardar los cambios?(Si-1,No-0):"))
	if desea_campo==1:
		cursor.execute("INSERT INTO CAMPOS VALUES(NULL,?,?,?,?,?,?,?,?)",(desc_campo,sup_campo,localidad_campo,direccion_campo,propietario_campo,telefono_campo,email_campo,inicioactlaboral_campo))
		conexion.commit()
	else:
		print("Datos borrados")

def ingresar_potrero():
	desc_pot=input("Descripción del potrero o referencia:")
	largo_pot=int(input("Largo del potrero en metros:"))
	ancho_pot=int(input("Ancho del potrero en metros:"))
	sup_pot=largo_pot*ancho_pot
	cargaanimal_pot=float(input("cantidad de animales por unidad de superficie:"))
	volpasto_pot=float(input("Volumen del pasto(m2):"))
	nrocamp_pot=int(input("numero de campo donde se encuentra:"))

	desea_pot=int(input("¿Desea guardar los cambios?(Si-1,No-0):"))
	if desea_pot==1:
		cursor.execute("INSERT INTO POTRERO VALUES(NULL,?,?,?,?,?)",(desc_pot,sup_pot,cargaanimal_pot,volpasto_pot,nrocamp_pot))
		conexion.commit()
	else:
		print("Datos borrados")

def ingresar_parcela():
	desc_par=input("Descripción del lote o referencia:")
	largo_par=int(input("Largo del potrero en metros:"))
	ancho_par=int(input("Ancho del potrero en metros:"))
	sup_par=largo_par*ancho_par
	pastimp_par=int(input("El pasto esta plantado-1, El pasto crecio de forma silvestre-0:"))
	trabtier_par=input("¿Podemos trabajar la tierra?(S-N):")
	ciclpast_par=int(input("¿Pasto creciendo(0) o Listo para que las vacas pasten(1)?:"))
	referencia_par=input("referencia sobre las parcelas para saber:")
	nropot_par=int(input("numero de potrero donde se encuentra:"))
	nrocamp_par=int(input("numero de campo donde se encuentra:"))
	desea_parce=int(input("¿Desea guardar los cambios?(Si-1,No-0):"))
	if desea_parce==1:
		cursor.execute("INSERT INTO PARCELA VALUES(NULL,?,?,?,?,?,?,?,?)",(desc_par,sup_par,pastimp_par,trabtier_par,ciclpast_par,referencia_par,nropot_par,nrocamp_par))
		conexion.commit()
	else:
		print("Datos borrados")

def ingresar_animales():
	nropadre_ani=int(input("ID_animal del padre del animal que se está cargando:"))
	nromadre_ani=int(input("ID_animal del madre del animal que se está cargando:"))
	fecnac_ani=input("Fecha de nacimiento del animal:")
	cat_ani=int(input("Categoria animal:"))
	catvie_ani=int(input("Categoria vientre:"))
	sex_ani=int(input("Macho(1) o Hembra(0):"))
	nropar_ani=int(input("Nro de parcela. Es la ubicación en la que esta el animal:"))

	desea_ani=int(input("¿Desea guardar los cambios?(Si-1,No-0):"))
	if desea_ani==1:
		cursor.execute("INSERT INTO ANIMAL VALUES(NULL,?,?,?,?,?,?,?)",(nropadre_ani,nromadre_ani,fecnac_ani,cat_ani,catvie_ani,sex_ani,nropar_ani))
		conexion.commit()
	else:
		print("Datos borrados")

def ingresar_gestiones():
	nroani_gest=int(input("Nro Animal.Vaca a la que se le realizo el seguimiento:"))
	fecseg_gest=input("Fecha en la que se realizó el seguimiento:")
	while True:
		estado_gest=int(input("Estado de la vaca(1-10):"))
		if estado_gest>10:
			print("Opción invalida")
		else:
			break
	obser_gest=input("Observaciones sobre la vaca:")
	peso_gest=int(input("Peso de la vaca al nacer:"))
	inse_gest=input("Vaca inseminada?(S-N):")
	desea_ges=int(input("¿Desea guardar los cambios?(Si-1,No-0):"))
	if desea_ges==1:
		cursor.execute("INSERT INTO SEGUIMIENTO VALUES(NULL,?,?,?,?,?,?)",(nroani_gest,fecseg_gest,estado_gest,obser_gest,peso_gest,inse_gest))
		conexion.commit()
	else:
		print("Datos borrados")

def ingresar_categorias():
	descat=input("Ingrese una descripcion:")
	desea_cat=int(input("¿Desea guardar los cambios?(Si-1,No-0):"))
	if desea_cat==1:
		cursor.execute("INSERT INTO CATEGORIA_ANIMAL VALUES(NULL,?)",(descat))
		conexion.commit()
	else:
		print("Datos borrados")

def ingresar_subcategorias():
	descvien=input("Ingrese alguna descripcion:")
	nrocate=int(input("Ingrese numero de categoria:"))
	desea_vien=int(input("¿Desea guardar los cambios?(Si-1,No-0):"))
	if desea_vien==1:
		cursor.execute("INSERT INTO CLAS_VACA_VIENTRE VALUES(NULL,?,?)",(descvien,nrocate))
		conexion.commit()
	else:
		print("Datos borrados")

while True:
	print("------------------------------------------------------------")
	print("                 MENU DE GESTIÓN GANADERA                   ")
	print("1_ Gestiones")
	print("2_ Listados")
	print("0_ Salir")
	print("------------------------------------------------------------")
	op_menu_prin=int(input("Ingrese la opción que usted desee:"))

	if op_menu_prin==0:
		print("Muchas gracias por usar nuestro sistema")
		break

	if op_menu_prin>2:
		print("Ingresar una opción valida")

	if op_menu_prin==1:
		while True:
			print("------------------------------------------------------------")
			print("                      MENU DE GESTIONES                     ")
			print("1_ Campo")
			print("2_ Potrero")
			print("3_ Parcela")
			print("4_ Animales")
			print("5_ Gestiones")
			print("6_ Categorias")
			print("7_ Subcategorias")
			print("0_ Volver al MP")
			print("------------------------------------------------------------")

			op_menu_gest=int(input("Ingrese la opción que usted desee:"))

			if op_menu_gest==0:
				break

			if op_menu_gest>7:
				print("Ingresar una opción valida")

			if op_menu_gest==1:
				while True:
					print("------------------------------------")
					print("               CAMPOS               ")
					print("1_ Crear nuevo registro")
					print("2_ Modificar un registro")
					print("3_ Eliminar un registro")
					print("4_ Mostrar registro")
					print("0_ Volver al menu de gestiones")
					print("------------------------------------")

					menu_gest_cam=int(input("Ingrese la opción que usted desee:"))

					if menu_gest_cam==0:
						break

					if menu_gest_cam>4:
						print("Ingresar una opción valida")

					if menu_gest_cam==1:
						ingresar_campo()

					if menu_gest_cam==2:
						cursor.execute("SELECT * FROM CAMPOS")
						modi=cursor.fetchall()
						nrocam=int(input("Ingrese el numero de campo a modificar:"))
						print("----------------------------")
						print("1_Descripción")
						print("2_Superficie")
						print("3_Localidad")
						print("4_Dirección")
						print("5_Propietarios")
						print("6_Teléfono")
						print("7_Email")
						print("8_Inicio de acta laboral")
						print("0_ Salir")
						print("----------------------------")
						ing=int(input("Ingrese la opcion que desea modificar:"))

						while True:
							if ing>7:
								print("opcion invalida")
							if ing==0:
								break
							if ing==1:
								desc_campo=input("Ingrese el cambio:")
								cursor.execute("UPDATE CAMPOS SET descripcion=? WHERE nro_campo LIKE ?",(desc_campo,nrocam))
								conexion.commit()
								print("MODIFICADO")
							if ing==2:
								sup_campo=int(input("Ingrese la superficie:"))
								cursor.execute("UPDATE CAMPOS SET superficie=? WHERE nro_campo LIKE ?",(sup_campo,nrocam))
								conexion.commit()
								print("MODIFICADO")
							if ing==3:
								localidad_campo=input("Ingrese la localidad:")
								cursor.execute("UPDATE CAMPOS SET localidad=? WHERE nro_campo LIKE ?",(localidad_campo,nrocam))
								conexion.commit()
								print("MODIFICADO")
							if ing==4:
								direccion_campo=int(input("Ingrese la direccion:"))
								cursor.execute("UPDATE CAMPOS SET direccion=? WHERE nro_campo LIKE ?",(direccion_campo,nrocam))
								conexion.commit()
								print("MODIFICADO")
							if ing==5:
								sup_campo=input("Ingrese el propietario:")
								cursor.execute("UPDATE CAMPOS SET propietario=? WHERE nro_campo LIKE ?",(propietario_campo,nrocam))
								conexion.commit()
								print("MODIFICADO")
							if ing==6:
								telefono_campo=int(input("Ingrese el telefono:"))
								cursor.execute("UPDATE CAMPOS SET telefono=? WHERE nro_campo LIKE ?",(telefono_campo,nrocam))
								conexion.commit()
								print("MODIFICADO")
							if ing==7:
								email_campo=input("Ingrese el email:")
								cursor.execute("UPDATE CAMPOS SET email=? WHERE nro_campo LIKE ?",(email_campo,nrocam))
								conexion.commit()
								print("MODIFICADO")
							if ing==8:
								inicioactlaboral_campo=input("Ingrese inicio de acta laboral(dd/mm/aaaa):")
								cursor.execute("UPDATE CAMPOS SET inicio_act_laboral=? WHERE nro_campo LIKE ?",(inicioactlaboral_campo,nrocam))
								conexion.commit()
								print("MODIFICADO")

					if menu_gest_cam==3:
						cam=int(input("Ingrese el numero de campo a eliminar:"))
						cursor.execute("SELECT * FROM CAMPOS")
						ven=cursor.fetchall()
						cursor.execute("DELETE FROM CAMPOS WHERE nro_campo=?",(cam,))
						conexion.commit()
						print("eliminado")

					if menu_gest_cam==4:
						while True:
							print("------------------------------------")
							print("          MOSTRAR REGISTRO          ")
							print("1_ Buscar Registro")
							print("2_ Mostar todos los registros")
							print("0_ Volver")
							print("------------------------------------")

							inn=int(input("Ingrese la opción que usted desea:"))
							if inn>2:
								print("opción invalida")
							if inn==0:
								break
							if inn==1:
								nrocamp=int(input("Ingrese el numero de campo para buscar:"))
								cursor.execute("SELECT * FROM CAMPOS")
								modi=cursor.fetchall()
								TT=0
								eia=0
								while True:
									try:
										if nrocamp==modi[TT][0]:
											print("------------------------------------------------------------------------------")
											print("|{:^20}|{:^14}|{:^14}|{:^14}|{:^12}|{:^14}|{:^14}|{:^14}||{:^20}|".format("Numero de campo","Descripción","Superficie","Localidad","Dirección","Propietario","Telefono","Email","Inicio acta laboral"))
											print("|{:^20}|{:^14}|{:^14}|{:^15}|{:^10}|{:^14}|{:^14}|{:^14}||{:^20}|".format(modi[TT][0],modi[TT][1],modi[TT][2],modi[TT][3],modi[TT][4],modi[TT][5],modi[TT][6],modi[TT][7],modi[TT][8]))
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
												ingresar_campo()
											else:
												pass
											
											break
									
									except TypeError:
										pass
							if inn==2:
								cursor.execute("SELECT * FROM CAMPOS")
								modi=cursor.fetchall()
								TT=0
								eia=0
								while True:
									try:
										print("------------------------------------------------------------------------------")
										print("|{:^20}|{:^14}|{:^14}|{:^14}|{:^12}|{:^14}|{:^14}|{:^14}||{:^20}|".format("Numero de campo","Descripción","Superficie","Localidad","Dirección","Propietario","Telefono","Email","Inicio acta laboral"))
										print("|{:^20}|{:^14}|{:^14}|{:^15}|{:^10}|{:^14}|{:^14}|{:^14}||{:^20}|".format(modi[TT][0],modi[TT][1],modi[TT][2],modi[TT][3],modi[TT][4],modi[TT][5],modi[TT][6],modi[TT][7],modi[TT][8]))
										print("------------------------------------------------------------------------------")
										TT+=1
										eia=100
										
										break
									
									except TypeError:
										pass


			if op_menu_gest==2:
				while True:
					print("------------------------------------")
					print("              POTRERO               ")
					print("1_ Crear nuevo registro")
					print("2_ Modificar un registro")
					print("3_ Eliminar un registro")
					print("4_ Mostrar registro")
					print("0_ Volver al menú de gestiones")
					print("------------------------------------")

					menu_gest_pot=int(input("Ingrese la opción que usted desee:"))

					if menu_gest_pot==0:
						break

					if menu_gest_pot>4:
						print("Ingresar una opción valida")

					if menu_gest_pot==1:
						ingresar_potrero()
						
					if menu_gest_pot==2:
						cursor.execute("SELECT * FROM POTRERO")
						list_potre=cursor.fetchall()
						cc=0
						potri=int(input("Ingrese el numero de potrero a modificar:"))

						if potri==list_potre[cc][0]:
							print("----------------------------")
							print("1_Descripción del potrero")
							print("2_Superficie del potrero")
							print("3_Carga animal")
							print("4_Volumen pasto")
							print("0_ Salir")
							print("----------------------------")
							ing=int(input("Ingrese la opcion que desea modificar:"))

							while True:
								if ing>4:
									print("opcion invalida")
								if ing==0:
									break					
								if ing==1:
									descri=input("Ingrese la descripcion:")
									cursor.execute("UPDATE POTRERO SET descripcion_potrero=? WHERE nro_potrero LIKE ?",(descri,potri))
									conexion.commit()
									print("MODIFICADO")
									break
								if ing==2:
									supi=int(input("Ingrese la superficie:"))
									cursor.execute("UPDATE POTRERO SET sup_potrero=? WHERE nro_potrero LIKE ?",(supi,potri))
									conexion.commit()
									print("MODIFICADO")
									break				
								if ing==3:
									carani=int(input("Ingrese carga animal:"))
									cursor.execute("UPDATE POTRERO SET carga_animal=? WHERE nro_potrero LIKE ?",(carani,potri))
									conexion.commit()
									print("MODIFICADO")
									break
								if ing==4:
									volpas=int(input("Ingrese volumen del pasto:"))
									cursor.execute("UPDATE POTRERO SET volumen_pasto=? WHERE nro_potrero LIKE ?",(volpas,potri))
									conexion.commit()
									print("MODIFICADO")
									break

					if menu_gest_pot==3:
						pot=int(input("Ingrese el numero de potrero a eliminar:"))
						cursor.execute("SELECT * FROM POTRERO")
						ven=cursor.fetchall()
						cursor.execute("DELETE FROM POTRERO WHERE nro_potrero=?",(pot,))
						conexion.commit()
						print("eliminado")

					if menu_gest_pot==4:
						while True:
							print("------------------------------------")
							print("          MOSTRAR REGISTRO          ")
							print("1_ Buscar Registro")
							print("2_ Mostar todos los registros")
							print("0_ Volver")
							print("------------------------------------")

							inn=int(input("Ingrese la opción que usted desea:"))
							if inn>2:
								print("opción invalida")
							if inn==0:
								break
							if inn==1:
								nropot=int(input("Ingrese el numero de potrero para buscar:"))
								cursor.execute("SELECT * FROM POTRERO")
								modi=cursor.fetchall()
								TT=0
								eia=0
								while True:
									try:
										if nropot==modi[TT][0]:
											print("------------------------------------------------------------------------------")
											print("|{:^14}|{:^18}|{:^10}|{:^14}|{:^13}|{:^14}|".format("Nro de potrero","Descripción","Superficie","Carga Animal","Volumen Pasto","Nro de Campo"))
											print("|{:^14}|{:^18}|{:^10}|{:^14}|{:^13}|{:^14}|".format(modi[TT][0],modi[TT][1],modi[TT][2],modi[TT][3],modi[TT][4],modi[TT][5]))
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
												ingresar_potrero()
											else:
												pass
											
											break
									
									except TypeError:
										pass
							if inn==2:
								cursor.execute("SELECT * FROM POTRERO")
								modi=cursor.fetchall()
								TT=0
								eia=0
								while True:
									try:										
										print("------------------------------------------------------------------------------")
										print("|{:^14}|{:^18}|{:^10}|{:^14}|{:^13}|{:^14}|".format("Nro de potrero","Descripción","Superficie","Carga Animal","Volumen Pasto","Nro de Campo"))
										print("|{:^14}|{:^18}|{:^10}|{:^14}|{:^13}|{:^14}|".format(modi[TT][0],modi[TT][1],modi[TT][2],modi[TT][3],modi[TT][4],modi[TT][5]))
										print("------------------------------------------------------------------------------")
										TT+=1
										
										if br==len(modi):
											if eia >= 100:
												break
											break
								
									except TypeError:
										pass

			if op_menu_gest==3:
				while True:
					print("------------------------------------")
					print("              PARCELA               ")
					print("1_ Crear nuevo registro")
					print("2_ Modificar un registro")
					print("3_ Eliminar un registro")
					print("4_ Mostrar registro")
					print("0_ Volver al menú de gestiones")
					print("------------------------------------")

					menu_gest_parce=int(input("Ingrese la opción que usted desee:"))

					if menu_gest_parce==0:
						break

					if menu_gest_parce>4:
						print("Ingresar una opción valida")

					if menu_gest_parce==1:
						ingresar_parcela()

					if menu_gest_parce==2:
						cursor.execute("SELECT * FROM PARCELA")
						list_parce=cursor.fetchall()
						cc=0
						parce=int(input("Ingrese el numero de parcela a modificar:"))

						if parce==list_parce[cc][0]:
							print("----------------------------")
							print("1_Descripción")
							print("2_Superficie")
							print("3_Pastura Implantada")
							print("4_Trabajar Tierra")
							print("5_Ciclo del Pasto")
							print("6_Referencia")
							print("0_ Salir")
							print("----------------------------")
							ing=int(input("Ingrese la opcion que desea modificar:"))

							while True:
								if ing>6:
									print("opcion invalida")
								if ing==0:
									break					
								if ing==1:
									descri=input("Ingrese la descripcion:")
									cursor.execute("UPDATE PARCELA SET descripcion_lote=? WHERE nro_lote LIKE ?",(descri,parce))
									conexion.commit()
									print("MODIFICADO")
									break
								if ing==2:
									supi=int(input("Ingrese la superficie:"))
									cursor.execute("UPDATE PARCELA SET sup_lote=? WHERE nro_lote LIKE ?",(supi,parce))
									conexion.commit()
									print("MODIFICADO")
									break				
								if ing==3:
									pasim=int(input("Ingrese pastura implantada:"))
									cursor.execute("UPDATE PARCELA SET pastura_implantada=? WHERE nro_lote LIKE ?",(pasim,parce))
									conexion.commit()
									print("MODIFICADO")
									break
								if ing==4:
									tietr=int(input("Ingrese tierra trabajada(S-N):"))
									cursor.execute("UPDATE PARCELA SET trabajar_tierra=? WHERE nro_lote LIKE ?",(tietr,parce))
									conexion.commit()
									print("MODIFICADO")
									break
								if ing==5:
									cicpas=int(input("Pasto creciendo(0) o Listo para que las vacas pasten(1):"))
									cursor.execute("UPDATE PARCELA SET ciclo_pasto=? WHERE nro_lote LIKE ?",(cicpas,parce))
									conexion.commit()
									print("MODIFICADO")
									break
								if ing==6:
									ref=int(input("Ingrese referencia sobre las parcelas para saber:"))
									cursor.execute("UPDATE PARCELA SET referencia=? WHERE nro_lote LIKE ?",(ref,parce))
									conexion.commit()
									print("MODIFICADO")
									break

					if menu_gest_parce==3:
						par=int(input("Ingrese el numero de parcela a eliminar:"))
						cursor.execute("SELECT * FROM PARCELA")
						ven=cursor.fetchall()
						cursor.execute("DELETE FROM PARCELA WHERE nro_lote=?",(par,))
						conexion.commit()
						print("eliminado")

					if menu_gest_parce==4:
						while True:
							print("------------------------------------")
							print("          MOSTRAR REGISTRO          ")
							print("1_ Buscar Registro")
							print("2_ Mostar todos los registros")
							print("0_ Volver")
							print("------------------------------------")
							inn=int(input("Ingrese la opción que usted desea:"))
							if inn>2:
								print("opción invalida")
							if inn==0:
								break
							if inn==1:
								nrolot=int(input("Ingrese el numero de parcela para buscar:"))
								cursor.execute("SELECT * FROM PARCELA")
								modi=cursor.fetchall()
								TT=0
								eia=0
								while True:
									try:
										if nrolot==modi[TT][0]:
											print("------------------------------------------------------------------------------")
											print("|{:^8}|{:^14}|{:^10}|{:^18}|{:^15}|{:^14}|{:^14}|{:^11}|{:^9}|".format("Nro Lote","Descripción","Superficie","Pastura Implantada","Trabajar Tierra","Ciclo Pasto","Referencia","Nro Potrero","Nro Campo"))
											print("|{:^8}|{:^14}|{:^10}|{:^18}|{:^15}|{:^14}|{:^14}|{:^11}|{:^9}|".format(modi[TT][0],modi[TT][1],modi[TT][2],modi[TT][3],modi[TT][4],modi[TT][5],modi[TT][6],modi[TT][7],modi[TT][8]))
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
												ingresar_parcela()
											else:
												pass
											
											break
									
									except TypeError:
										pass

			if op_menu_gest==4:
				while True:
					print("------------------------------------")
					print("              ANIMALES              ")
					print("1_ Crear nuevo registro")
					print("2_ Modificar un registro")
					print("3_ Eliminar un registro")
					print("4_ Mostrar registro")
					print("0_ Volver al menú de gestiones")
					print("------------------------------------")

					menu_gest_ani=int(input("Ingrese la opción que usted desee:"))

					if menu_gest_ani==0:
						break

					if menu_gest_ani>4:
						print("Ingresar una opción valida")

					if menu_gest_ani==1:
						ingresar_animales()

					if menu_gest_ani==2:
						cursor.execute("SELECT * FROM ANIMAL")
						list_animal=cursor.fetchall()
						cc=0
						idani=int(input("Ingrese el numero del animal a modificar:"))

						if idani==list_animal[cc][0]:
							print("----------------------------")
							print("1_Numero de padre")
							print("2_Numero de madre")
							print("3_Fecha de nacimiento")
							print("4_Categoria")
							print("5_Categoria vientre")
							print("6_Sexo")
							print("0_ Salir")
							print("----------------------------")
							ing=int(input("Ingrese la opcion que desea modificar:"))

							while True:
								if ing>6:
									print("opcion invalida")
								if ing==0:
									break					
								if ing==1:
									nropad=input("Ingrese la ID del padre:")
									cursor.execute("UPDATE ANIMAL SET nro_padre=? WHERE nro_animal LIKE ?",(nropad,idani))
									conexion.commit()
									print("MODIFICADO")
									break
								if ing==2:
									nromad=int(input("Ingrese ID de la madre:"))
									cursor.execute("UPDATE ANIMAL SET nro_madre=? WHERE nro_animal LIKE ?",(nromad,idani))
									conexion.commit()
									print("MODIFICADO")
									break				
								if ing==3:
									fecnac=int(input("Ingrese fecha de nacimiento(dd/mm/aaaa):"))
									cursor.execute("UPDATE ANIMAL SET fecha_nac=? WHERE nro_animal LIKE ?",(fecnac,idani))
									conexion.commit()
									print("MODIFICADO")
									break
								if ing==4:
									cat=int(input("Ingrese Categoria:"))
									cursor.execute("UPDATE ANIMAL SET categoria=? WHERE nro_animal LIKE ?",(cat,idani))
									conexion.commit()
									print("MODIFICADO")
									break
								if ing==5:
									catvi=int(input("Ingrese Categoria vientre:"))
									cursor.execute("UPDATE ANIMAL SET categoria_vientre=? WHERE nro_animal LIKE ?",(catvi,idani))
									conexion.commit()
									print("MODIFICADO")
									break
								if ing==6:
									sex=int(input("Ingrese el sexo Macho(1), Hembra(0):"))
									cursor.execute("UPDATE ANIMAL SET sexo=? WHERE nro_animal LIKE ?",(sex,idani))
									conexion.commit()
									print("MODIFICADO")
									break

					if menu_gest_ani==3:
						ani=int(input("Ingrese el numero de animal a eliminar:"))
						cursor.execute("SELECT * FROM ANIMAL")
						ven=cursor.fetchall()
						cursor.execute("DELETE FROM ANIMAL WHERE nro_animal=?",(ani,))
						conexion.commit()
						print("eliminado")

					if menu_gest_ani==4:
						while True:
							print("------------------------------------")
							print("          MOSTRAR REGISTRO          ")
							print("1_ Buscar Registro")
							print("2_ Mostar todos los registros")
							print("0_ Volver")
							print("------------------------------------")
							inn=int(input("Ingrese la opción que usted desea:"))
							if inn>2:
								print("opción invalida")
							if inn==0:
								break
							if inn==1:
								nroani=int(input("Ingrese el numero de animal para buscar:"))
								cursor.execute("SELECT * FROM ANIMAL")
								modi=cursor.fetchall()
								TT=0
								eia=0
								while True:
									try:
										if nroani==modi[TT][0]:
											print("------------------------------------------------------------------------------")
											print("|{:^10}|{:^9}|{:^9}|{:^18}|{:^9}|{:^17}|{:^4}|{:^11}|".format("Nro Animal","Nro Padre","Nro Madre","Fecha Nacimiento","Categoria","Categoria Vientre","Sexo","Nro Parcela"))
											print("|{:^10}|{:^9}|{:^9}|{:^18}|{:^9}|{:^17}|{:^4}|{:^11}|".format(modi[TT][0],modi[TT][1],modi[TT][2],modi[TT][3],modi[TT][4],modi[TT][5],modi[TT][6],modi[TT][7]))
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
												ingresar_animales()
											else:
												pass
											
											break
									
									except TypeError:
										pass

			if op_menu_gest==5:
				while True:
					print("------------------------------------")
					print("             GESTIONES              ")
					print("1_ Crear nuevo registro")
					print("2_ Modificar un registro")
					print("3_ Eliminar un registro")
					print("4_ Mostrar registro")
					print("0_ Volver al menú de gestiones")
					print("------------------------------------")

					menu_gest_ges=int(input("Ingrese la opción que usted desee:"))

					if menu_gest_ges==0:
						break

					if menu_gest_ges>4:
						print("Ingresar una opción valida")

					if menu_gest_ges==1:
						ingresar_gestiones()

					if menu_gest_ges==2:
						cursor.execute("SELECT * FROM SEGUIMIENTO")
						list_seguimiento=cursor.fetchall()
						cc=0
						nroseg=int(input("Ingrese el numero del animal a modificar:"))

						if nroseg==list_seguimiento[cc][0]:
							print("----------------------------")
							print("1_Nro animal")
							print("2_Fecha seguimiento")
							print("3_Estado")
							print("4_Observacion")
							print("5_Peso")
							print("6_Inseminada")
							print("0_ Salir")
							print("----------------------------")
							ing=int(input("Ingrese la opcion que desea modificar:"))

							while True:
								if ing>6:
									print("opcion invalida")
								if ing==0:
									break					
								if ing==1:
									nroanim=int(input("Ingrese el numero animal:"))
									cursor.execute("UPDATE SEGUIMIENTO SET nro_animal=? WHERE nro_seguimiento LIKE ?",(nroanim,nroseg))
									conexion.commit()
									print("MODIFICADO")
									break
								if ing==2:
									fecseg=input("Ingrese fecha de seguimiento(dd/mm/aaaa):")
									cursor.execute("UPDATE SEGUIMIENTO SET fecha_seguimiento=? WHERE nro_seguimiento LIKE ?",(fecseg,nroseg))
									conexion.commit()
									print("MODIFICADO")
									break				
								if ing==3:
									estad=int(input("Ingrese estado(1-10):"))
									cursor.execute("UPDATE SEGUIMIENTO SET estad=? WHERE nro_seguimiento LIKE ?",(estad,nroseg))
									conexion.commit()
									print("MODIFICADO")
									break
								if ing==4:
									obs=input("Ingrese Observaciones:")
									cursor.execute("UPDATE SEGUIMIENTO SET observaciones=? WHERE nro_seguimiento LIKE ?",(obs,nroseg))
									conexion.commit()
									print("MODIFICADO")
									break
								if ing==5:
									pes=int(input("Ingrese peso:"))
									cursor.execute("UPDATE SEGUIMIENTO SET peso=? WHERE nro_seguimiento LIKE ?",(pes,nroseg))
									conexion.commit()
									print("MODIFICADO")
									break
								if ing==6:
									inse=int(input("Ingrese si esta inseminada o no(S-N):"))
									cursor.execute("UPDATE SEGUIMIENTO SET inseminada=? WHERE nro_seguimiento LIKE ?",(inse,nroseg))
									conexion.commit()
									print("MODIFICADO")
									break

					if menu_gest_ges==3:
						segui=int(input("Ingrese el numero de seguimiento a eliminar:"))
						cursor.execute("SELECT * FROM SEGUIMIENTO")
						ven=cursor.fetchall()
						cursor.execute("DELETE FROM SEGUIMIENTO WHERE nro_seguimiento=?",(segui,))
						conexion.commit()
						print("eliminado")

					if menu_gest_ges==4:
						while True:
							print("------------------------------------")
							print("          MOSTRAR REGISTRO          ")
							print("1_ Buscar Registro")
							print("2_ Mostar todos los registros")
							print("0_ Volver")
							print("------------------------------------")

							inn=int(input("Ingrese la opción que desee:"))

							if inn>2:
								print("Opción no valida")
							if inn==0:
								break
							if inn==1:
								nrosegui=int(input("Ingrese el numero de animal para buscar:"))
								cursor.execute("SELECT * FROM SEGUIMIENTO")
								modi=cursor.fetchall()
								TT=0
								eia=0
								while True:
									try:
										if nrosegui==modi[TT][0]:
											print("------------------------------------------------------------------------------")
											print("|{:^15}|{:^10}|{:^17}|{:^6}|{:^25}|{:^4}|{:^10}|".format("Nro seguimiento","Nro animal","Fecha seguimiento","estado","observaciones","Peso","Inseminada"))
											print("|{:^15}|{:^10}|{:^17}|{:^6}|{:^25}|{:^4}|{:^10}|".format(modi[TT][0],modi[TT][1],modi[TT][2],modi[TT][3],modi[TT][4],modi[TT][5],modi[TT][6]))
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
												ingresar_gestiones()
											else:
												pass
											
											break
									
									except TypeError:
										pass
							if inn==2:
								pass

			if op_menu_gest == 6:
				while True:
					print("------------------------------------")
					print("             CATEGORIAS             ")
					print("1_ Crear nuevo registro")
					print("2_ Modificar un registro")
					print("3_ Eliminar un registro")
					print("4_ Mostrar registro")
					print("0_ Volver al menú de gestiones")
					print("------------------------------------")

					menu_gest_cat=int(input("Ingrese la opción que usted desee:"))

					if menu_gest_cat==0:
						break

					if menu_gest_cat>4:
						print("Ingresar una opción valida")

					if menu_gest_cat==1:
						ingresar_categorias()

					if menu_gest_cat==2:
						cursor.execute("SELECT * FROM CATEGORIA_ANIMAL")
						list_cate=cursor.fetchall()
						cc=0
						idcat=int(input("Ingrese el numero del animal a modificar:"))

						if idcat==list_cate[cc][0]:
							print("----------------------------")
							print("1_Numero de categoria")
							print("2_Descripción")
							print("0_Salir")
							print("----------------------------")
							ing=int(input("Ingrese la opcion que desea modificar:"))

							while True:
								if ing>2:
									print("opcion invalida")
								if ing==0:
									break					
								if ing==1:
									nrocateg=input("Ingrese el numero de categoria:")
									cursor.execute("UPDATE CATEGORIA_ANIMAL SET nro_categoria=? WHERE nro_categoria LIKE ?",(idcat,nrocateg))
									conexion.commit()
									print("MODIFICADO")
									break
								if ing==2:
									des=input("Ingrese la descripcion:")
									cursor.execute("UPDATE CATEGORIA_ANIMAL SET descripcion=? WHERE nro_categoria LIKE ?",(idcat,des))
									conexion.commit()
									print("MODIFICADO")
									break

					if menu_gest_cat==3:
						cate=int(input("Ingrese el numero de categoria a eliminar:"))
						cursor.execute("SELECT * FROM CATEGORIA_ANIMAL")
						ven=cursor.fetchall()
						cursor.execute("DELETE FROM CATEGORIA_ANIMAL WHERE nro_categoria=?",(cate,))
						conexion.commit()
						print("eliminado")

					if menu_gest_cat==4:
						while True:
							print("------------------------------------")
							print("          MOSTRAR REGISTRO          ")
							print("1_ Buscar Registro")
							print("2_ Mostar todos los registros")
							print("0_ Volver")
							print("------------------------------------")

							nrocat=int(input("Ingrese el numero de categoria para buscar:"))
							cursor.execute("SELECT * FROM CATEGORIA_ANIMAL")
							modi=cursor.fetchall()
							TT=0
							eia=0
							while True:
								try:
									if nrocat==modi[TT][0]:
										print("------------------------------------------------------------------------------")
										print("|{:^15}|{:^20}|".format("Nro categoria","descripcion"))
										print("|{:^15}|{:^20}|".format(modi[TT][0],modi[TT][1]))
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
											ingresar_categorias()
										else:
											pass
										
										break
								
								except TypeError:
									pass

			if op_menu_gest == 7:
				while True:
					print("------------------------------------")
					print("            SUBCATEGORIAS           ")
					print("1_ Crear nuevo registro")
					print("2_ Modificar un registro")
					print("3_ Eliminar un registro")
					print("4_ Mostrar registro")
					print("0_ Volver al menú de gestiones")
					print("------------------------------------")

					menu_gest_cat=int(input("Ingrese la opción que usted desee:"))

					if menu_gest_cat==0:
						break

					if menu_gest_cat>4:
						print("Ingresar una opción valida")

					if menu_gest_cat==1:
						ingresar_subcategorias()

					if menu_gest_cat==2:
						cursor.execute("SELECT * FROM CLAS_VACA_VIENTRE")
						list_subcate=cursor.fetchall()
						cc=0
						idsubcat=int(input("Ingrese el numero del animal a modificar:"))

						if idsubcat==list_subcate[cc][0]:
							print("----------------------------")
							print("1_Descripción")
							print("2_Numero de categoria")
							print("0_Salir")
							print("----------------------------")
							ing=int(input("Ingrese la opcion que desea modificar:"))

							while True:
								if ing>2:
									print("opcion invalida")
								if ing==0:
									break					
								if ing==1:
									nrocateg=input("Ingrese el numero de categoria:")
									cursor.execute("UPDATE CATEGORIA_ANIMAL SET desc_vientre=? WHERE nro_vientre LIKE ?",(idcat,idsubcat))
									conexion.commit()
									print("MODIFICADO")
									break
								if ing==2:
									des=input("Ingrese la descripcion:")
									cursor.execute("UPDATE CATEGORIA_ANIMAL SET nro_categoria=? WHERE nro_vientre LIKE ?",(idcat,idsubcat))
									conexion.commit()
									print("MODIFICADO")
									break

					if menu_gest_cat==3:
						subcate=int(input("Ingrese el numero de categoria a eliminar:"))
						cursor.execute("SELECT * FROM CLAS_VACA_VIENTRE")
						ven=cursor.fetchall()
						cursor.execute("DELETE FROM CLAS_VACA_VIENTRE WHERE nro_vientre=?",(subcate,))
						conexion.commit()
						print("eliminado")

					if menu_gest_cat==4:
						while True:
							print("------------------------------------")
							print("          MOSTRAR REGISTRO          ")
							print("1_ Buscar Registro")
							print("2_ Mostar todos los registros")
							print("0_ Volver")
							print("------------------------------------")

							inn=int(input("ingrese opcion:"))
							if inn==1:
								nrocat=int(input("Ingrese el numero de categoria para buscar:"))
								cursor.execute("SELECT * FROM CLAS_VACA_VIENTRE")
								modi=cursor.fetchall()
								TT=0
								eia=0
								while True:
									try:
										if nrocat==modi[TT][0]:
											print("------------------------------------------------------------------------------")
											print("|{:^15}|{:^20}|{:^20}|".format("Nro vientre","descripcion","Nro categoria"))
											print("|{:^15}|{:^20}|{:^20}|".format(modi[TT][0],modi[TT][1],modi[TT][2]))
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
												ingresar_subcategorias()
											else:
												pass
											
											break
									
									except TypeError:
										pass





			
	if op_menu_prin==2:
		while True:
			print("------------------------------------------------------------")
			print("                      MENU DE LISTADOS                      ")
			print("1_ Vacas X Categoria")
			print("2_ Vacas X Subcategoria")
			print("3_ Vacas X Parcela")
			print("4_ Vacas X Genero")
			print("5_ Categoria X Potrero")
			print("6_ Categoria X Campo")
			print("7_ Carga Animal X Potrero")
			print("8_ Potrero X Tierra Trabajable")
			print("0_ Volver al MP")
			print("------------------------------------------------------------")

			op_menu_list=int(input("Ingrese la opción que usted desee:"))

			if op_menu_list>10:
				print("Opción no valida")
			if  op_menu_list==0:
				break
			if op_menu_list==1:
				cursor.execute('''
					SELECT * 
					FROM ANIMAL A
					JOIN CATEGORIA_ANIMAL CA ON A.categoria=CA.nro_categoria
					''')
				listado_vacxcat=cursor.fetchall()
				conexion.close()
				
				ttt=0
				for fila in listado_vacxcat:
					print("------------------------------------------------------------------------------")
					print("|{:^9}|{:^8}|".format("Categoria","Cantidad"))
					print("|{:^9}|{:^8}|".format(listado_vacxcat[ttt][8],listado_vacxcat[ttt][1]))
					print("------------------------------------------------------------------------------")
					
					ttt+=1
					eia=100
				'''cursor.execute("SELECT * FROM ANIMAL")
				mido=cursor.fetchall()
				br=0
				eia=0

				while True:
					try:
						print("------------------------------------------------------------------------------")
						print("|{:^9}|{:^8}|".format("Categoria","Cantidad"))
						print("|{:^9}|{:^8}|".format(mido[br][4],mido[br][1]))
						print("------------------------------------------------------------------------------")
						br+=1
						eia=100
						
						br+=1
							
						break
						
					except TypeError:
						pass'''
				
			if op_menu_list==2:
				cursor.execute('''SELECT * FROM CLAS_VACA_VIENTRE''')
				listado_vacxsubcat=cursor.fetchall()
				ttt=0

				for fila in listado_vacxsubcat:
					print(fila)
					print("------------------------------------------------------------------------------")
					print("|{:^9}|{:^8}|".format("Categoria","Cantidad"))
					print("|{:^9}|{:^8}|".format(listado_vacxsubcat[ttt][0],listado_vacxsubcat[ttt][2]))
					print("------------------------------------------------------------------------------")
					
					ttt+=1
					eia=100

			if op_menu_list==3:
				cursor.execute('''
					SELECT * 
					FROM CAMPOS C
					JOIN POTRERO P ON C.nro_campo=P.nro_campo
					JOIN PARCELA P1 ON P.nro_potrero=P1.nro_potrero
					''')
					
				listado_vacxpar=cursor.fetchall()
				ttt=0

				cursor.execute('''
					SELECT * 
					FROM ANIMAL A
					JOIN CATEGORIA_ANIMAL CA ON A.categoria=CA.nro_categoria
					''')
				listado_vacxcat=cursor.fetchall()
				
				for fila in listado_vacxpar:
					print(fila)
					print("------------------------------------------------------------------------------")
					print("|{:^9}|{:^8}|{:^9}|{:^9}|{:^9}|".format("Categoria","Cantidad","Parcela","Potrero","Campo"))
					print("|{:^9}|{:^8}|{:^9}|{:^9}|{:^9}|".format(listado_vacxcat[ttt][8],listado_vacxcat[ttt][1],listado_vacxpar[ttt][15],listado_vacxpar[ttt][9],listado_vacxpar[ttt][0]))
					print("------------------------------------------------------------------------------")
					
					eia=100
					break
				