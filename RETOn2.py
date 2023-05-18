
#RETO N°2

nombre = "ingrese el nombre del estudiante"

Nombre = input("Ingrese el nombre")
Asignatura = input("Ingrese la asignatura")
NotaLAB1 = float(input("Ingrese la nota del laboratorio 1"))
NotaLAB2 = float(input("Ingrese la nota del laboratorio 2"))

Nota_PON1 = float(NotaLAB1*0.30)
type(Nota_PON1)
Nota_PON2 = float(NotaLAB2*0.70)
type(Nota_PON2)
Nota_FINAL = float(Nota_PON1 + Nota_PON2)


Nota_FINAL = "Nota_final"

Consulta = {"Nombre":Nombre
            ,"Asignatura":Asignatura
            ,"Nota 1":NotaLAB1
            ,"Nota 2":NotaLAB2
            ,"Promedio final":round(Nota_FINAL, 1)}
print(Consulta)


#Forma funcinal

estudiante = input("Ingrese el nombre del estudiante")
asignatura = input("Ingrese el nombre de la asignatura")
Nota1 = float(input("Ingrese la nota del laboratorio N°1:"))
Nota2 = float(input("Ingrese la nota del laboratorio N°2:"))




#Tambien se podria round: promedio.1 para redondear a un decimal despues de la coma.