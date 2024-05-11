Algoritmo BoletadePago
	Definir  Nombre,CI,Cargo,TipodeEmpresa Como Cadena
	Definir añodeingreso,añoactual,AñosdeTrabajo como entero
	Definir BonoAlimentacion,numBasico,BonoTransporte,BonoAntiguedad,ValesdeConsumo,SalarioDominical,SalarioMinimoNacional,TotaldeIngresos,AFP,liquido Como Real
	Escribir "Nombre"
	leer Nombre
	escribir "ci"
	leer ci
	Escribir "haber basico"
	Leer numBasico
	Escribir "año de ingreso"
	leer añodeingreso
	Escribir "año de actual"
	leer añoactual
	Si añodeingreso>0 y añoactual>0 Entonces
		AñosdeTrabajo<-(añoactual-añodeingreso)
		Escribir "Su antiguedad es de: ",AñosdeTrabajo
	SiNo
		escribir "no trabaja usted"
	Fin Si
	Escribir "tipo de empresa"
	leer TipodeEmpresa
	SalarioMinimoNacional<-2362
	BonoAlimentacion<-60
	BonoTransporte<-157.5
	ValesdeConsumo<-88
	Escribir "Domingos que trabajo"
	Leer numDominical
	Si numDominical>0 Entonces
		SalarioDominical<-(numDominical*numBasico/30)*2
		Escribir "el bono dominical es: ",SalarioDominical
	SiNo
		Escribir "0"
	Fin Si
	
	Si AñosdeTrabajo>0 y AñosdeTrabajo<=2 Entonces
		BonoAntiguedad<-(numBasico*0)*3*(SalarioMinimoNacional)
	SiNo
		Si AñosdeTrabajo>2 y AñosdeTrabajo<=5 Entonces
			BonoAntiguedad<-(numBasico/100*5)*3*(SalarioMinimoNacional)
		SiNo
			Si AñosdeTrabajo>5 y AñosdeTrabajo<=8 Entonces
				BonoAntiguedad<-(numBasico/100*11)*3*(SalarioMinimoNacional)
			SiNo
				Si AñosdeTrabajo>8 y AñosdeTrabajo<=11 Entonces
					BonoAntiguedad<-(numBasico/100*18)*3*(SalarioMinimoNacional)
				SiNo
					Si AñosdeTrabajo>11 y AñosdeTrabajo<=15 Entonces
					BonoAntiguedad<-(numBasico/100*26)*3*(SalarioMinimoNacional)
					SiNo
						Si AñosdeTrabajo>15 y AñosdeTrabajo<=20 Entonces
						BonoAntiguedad<-(numBasico/100*34)*3*(SalarioMinimoNacional)
						SiNo
							Si AñosdeTrabajo>20 y AñosdeTrabajo<=25 Entonces
								BonoAntiguedad<-(numBasico/100*42)*3*(SalarioMinimoNacional)
							SiNo
								Si AñosdeTrabajo>25 Entonces
								BonoAntiguedad<-(numBasico/100*50)*3*(SalarioMinimoNacional)
								SiNo
									escribir "no tiene bono antiguedad"
								Fin Si
							Fin Si
						Fin Si
					Fin Si
				Fin Si
			Fin Si
		Fin Si
	Fin Si
	Escribir "su bono antiguedad es: ",BonoAntiguedad
	liquido<-SalarioDominical+BonoAlimentacion+BonoTransporte+BonoAntiguedad+ValesdeConsumo
	Escribir "su TotaldeIngresos es: ",liquido
	AFP<-liquido*0.1271
	escribir "---------BOLETA DE PAGO-----------"
	escribir "nombre es: ", Nombre
	Escribir "CI: ", ci
	Escribir "haber basico: ",numBasico
	Escribir "tipo de empresa: ",TipodeEmpresa
	Escribir "bono dominical: ",SalarioDominical
	Escribir "bono antiguedad: ",BonoAntiguedad
	Escribir "TotAl de ingresos: ",liquido
	Escribir "AFP: ",AFP
FinAlgoritmo