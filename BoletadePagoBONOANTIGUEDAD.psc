Algoritmo BoletadePago
	Definir  Nombre,CI,Cargo,TipodeEmpresa Como Cadena
	Definir a�odeingreso,a�oactual,A�osdeTrabajo como entero
	Definir BonoAlimentacion,numBasico,BonoTransporte,BonoAntiguedad,ValesdeConsumo,SalarioDominical,SalarioMinimoNacional,TotaldeIngresos,AFP,liquido Como Real
	Escribir "Nombre"
	leer Nombre
	escribir "ci"
	leer ci
	Escribir "haber basico"
	Leer numBasico
	Escribir "a�o de ingreso"
	leer a�odeingreso
	Escribir "a�o de actual"
	leer a�oactual
	Si a�odeingreso>0 y a�oactual>0 Entonces
		A�osdeTrabajo<-(a�oactual-a�odeingreso)
		Escribir "Su antiguedad es de: ",A�osdeTrabajo
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
	
	Si A�osdeTrabajo>0 y A�osdeTrabajo<=2 Entonces
		BonoAntiguedad<-(numBasico*0)*3*(SalarioMinimoNacional)
	SiNo
		Si A�osdeTrabajo>2 y A�osdeTrabajo<=5 Entonces
			BonoAntiguedad<-(numBasico/100*5)*3*(SalarioMinimoNacional)
		SiNo
			Si A�osdeTrabajo>5 y A�osdeTrabajo<=8 Entonces
				BonoAntiguedad<-(numBasico/100*11)*3*(SalarioMinimoNacional)
			SiNo
				Si A�osdeTrabajo>8 y A�osdeTrabajo<=11 Entonces
					BonoAntiguedad<-(numBasico/100*18)*3*(SalarioMinimoNacional)
				SiNo
					Si A�osdeTrabajo>11 y A�osdeTrabajo<=15 Entonces
					BonoAntiguedad<-(numBasico/100*26)*3*(SalarioMinimoNacional)
					SiNo
						Si A�osdeTrabajo>15 y A�osdeTrabajo<=20 Entonces
						BonoAntiguedad<-(numBasico/100*34)*3*(SalarioMinimoNacional)
						SiNo
							Si A�osdeTrabajo>20 y A�osdeTrabajo<=25 Entonces
								BonoAntiguedad<-(numBasico/100*42)*3*(SalarioMinimoNacional)
							SiNo
								Si A�osdeTrabajo>25 Entonces
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