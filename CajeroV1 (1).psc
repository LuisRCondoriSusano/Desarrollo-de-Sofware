Algoritmo Cajero
	definir haytarjeta, pin, idioma, accion Como Entero //variables para la interfaz y manejo del codigo
	definir retiro,saldo,estracto como entero //valores manejados como enteros
	definir deposito Como Real //deposito al saldo
	definir transferencia como real
	definir cuentadestino Como Real 
	definir montotransferencia Como Real
	
	escribir "---Mercantil Santa cruz---"
	escribir " "
	escribir " "
	escribir "Introduce tu tarjeta -->"
	escribir "1--Con tarjeta"
	escribir "2--Sin Tarjte"
	leer haytarjeta
	saldo=Aleatorio(10,10000)  //generamos un saldo aleatorio no definido previamente
	pin=aleatorio (1000,9999)
	si haytarjeta=1
		escribir "Digita tu pin: " pin
		escribir "Selecciona un idioma"
		escribir "1--Español"
		escribir "2--English"
		//Menu
		leer idioma
		Si idioma =1 Entonces
			escribir "--------INTERFAZ--------"
			escribir "1.Retirar dinero"
			Escribir "2.Depositar dinero"
			escribir "3.Hacer una transferencia"
			escribir "4.Consultar Saldo"
			escribir "5.Salir"
			leer accion
			//retiro
			si accion =1
				escribir "Digita la cantidad a retirar:"
				Leer retiro
				estracto=saldo-retiro //estracto es el residuo despues de retirar el dinero
				
				Si estracto<0//si el retiro es mayor al saldo condiciona la accion
					escribir "Esta accion no se puede realizar "
				SiNo
					Si estracto>0//si el retiro es mayor al saldo condiciona la accion
						escribir "Tu accion se esta ejecutando"
						escribir "|"
						escribir "|"
						escribir "v"
						escribir "Tu saldo actual es de: " estracto " Bs"
					FinSi
					
				Fin Si
			SiNo
				//deposito
				Si accion=2
					Escribir "Introduce la cantidad a depositar: "
					Leer deposito
					saldo = saldo + deposito
					Escribir "Depositaste: ", deposito " Bs"
					Escribir "Tu saldo actual es: " saldo " Bs"
				Sino
					//transferencia
					Si accion=3
						escribir "Introduce el numero de la cuenta de destino"
						Leer cuentadestino
						escribir "Digita el monto en Bs"
						leer montotransferencia
						//condicionamos segun el monto y el saldo
						Si montotransferencia>saldo
							escribir "Fondos insuficientes"
							
						SiNo
							Si montotransferencia<saldo
								estracto=saldo-montotransferencia
								escribir "Ya se realizo la transferencia con exito"
								Escribir "Tu saldo actual es de " estracto " Bs" 
							FinSi
							
						FinSi
					SiNo
						//Consulta de saldo
						Si accion=4
							escribir "Tu saldo actual es " saldo " Bs"
						SiNo
							//Salir
							Si accion=5
								escribir "Hasta luego"
							FinSi
						FinSi
					FinSi
				FinSi
			FinSi
		SiNo
			Si idioma=2 Entonces
				Escribir "--------INTERFACE--------"
				Escribir "1.Withdraw money"
				Escribir "2.Deposit money"
				Escribir "3.Make a transfer"
				Escribir "4.Check balance"
				Escribir "5.Exit"
				leer accion
				//withdrawal
				Si accion = 1
					Escribir "Enter the amount to withdraw:"
					Leer retiro
					estracto = saldo - retiro //estracto is the remainder after withdrawing money
					
					Si estracto < 0 //if the withdrawal is greater than the balance, condition the action
						Escribir "This action cannot be performed "
					SiNo
						Si estracto > 0 //if the withdrawal is greater than the balance, condition the action
							Escribir "Your action is being processed"
							Escribir "|"
							Escribir "|"
							Escribir "v"
							Escribir "Your current balance is: " estracto " Bs"
						FinSi
					FinSi
				SiNo
					//deposit
					Si accion = 2
						Escribir "Enter the amount to deposit: "
						Leer deposito
						saldo = saldo + deposito
						Escribir "You have deposited: " , deposito " Bs"
						Escribir "Your current balance is: " saldo " Bs"
					Sino
						//transfer
						Si accion = 3
							Escribir "Enter the destination account number"
							Leer cuentadestino
							Escribir "Enter the amount in Bs"
							Leer montotransferencia
							//condition based on the amount and the balance
							Si montotransferencia > saldo
								Escribir "Insufficient funds"
							SiNo
								Si montotransferencia < saldo
									estracto = saldo - montotransferencia
									Escribir "Transfer successful"
									Escribir "Your current balance is: " estracto " Bs"  
								FinSi
							FinSi
						SiNo
							//Check balance
							Si accion = 4
								Escribir "Your current balance is " saldo " Bs"
							SiNo
								//Exit
								Si accion = 5
									Escribir "Goodbye"
								FinSi
							FinSi
						FinSi
					FinSi
				FinSi
			FinSi
		FinSi
	Sino 
		Si haytarjeta=2
			escribir "Vuelve a intentarlo :("
		FinSi
	Fin si
	
	
	
	
	
FinAlgoritmo