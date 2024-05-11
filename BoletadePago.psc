Algoritmo BoletadePago
	Definir  Nombre,CI,Cargo,AñosdeAntiguedad,TipodeEmpresa Como Cadena
	Definir BonoAlimentacion,numBasico,BonoTransporte,ValesdeConsumo,SalarioDominical,TotaldeIngresos,AFP,liquido Como Real
	Escribir "Nombre"
	leer Nombre
	escribir "ci"
	leer ci
	Escribir "haber basico"
	Leer numBasico
	Escribir "Antiguedad"
	leer AñosdeAntiguedad
	Escribir "tipo de empresa"
	leer TipodeEmpresa
	BonoAlimentacion<-60
	BonoTransporte<-157.5
	ValesdeConsumo<-88
	Escribir "Domingos que trabajo"
	Leer numDominical
	Si numDominical>0 Entonces
		SalarioDominical<-(numDominical*numBasico/30)*2
		Escribir "el bono de es: ",SalarioDominical
	SiNo
		Escribir "0"
	Fin Si
	liquido<-SalarioDominical+BonoAlimentacion+BonoTransporte+ValesdeConsumo
	Escribir "su TotaldeIngresos es: ",liquido
	AFP<-liquido*0.1271
	escribir "nombre es: ", Nombre
	Escribir "CI: ", ci
	Escribir "haber basico: ",numBasico
	Escribir "tipo de empresa: ",TipodeEmpresaescribi
	Escribir "bonos dominical: ", SalarioDominical
	Escribir "Toal de ingresos: ",liquido
	Escribir "AFP: ",AFP
FinAlgoritmo
