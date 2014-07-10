# -*- encoding: utf-8 -*-
from django.db import models
from student.models import Student
from person.models import Person
from classroom.models import Grade, ClassRoom
from location.models import School, Country, Department
from exercise.models import Unit, Exercise, Result, Subject, Area
from teacher.models import Teacher
from django.shortcuts import render_to_response
from django.template import RequestContext
import json
from datetime import datetime
import random

def resultados(request):
	read = open('resultados.json', 'r')
	diccionario = json.load(read)
	read.close()
	alumnos = 0
	docentes = 0
	for v in diccionario:
		try:
 			g = Grade.objects.get(name=5)
 		except Grade.DoesNotExist:
 			g = Grade(name=5)
 			g.save()

 		try:
 			a = Area.objects.get(name="Naturaleza")
 		except Area.DoesNotExist:
 			a = Grade(name="Naturaleza")
 			a.save()

		try:
			sub = Subject.objects.get(name=v.get('area'), area=a) 		 		 				
		except Area.DoesNotExist:
 			sub = Subject(name=v.get('area'), area=a)
			sub.save()

		try:
			u = Unit.objects.get(letter=v.get('topic'),grade=g,subject=sub)
		except Unit.DoesNotExist:
 			u = Unit(letter=v.get('topic'),grade=g,subject=sub)
			u.save()

		try:
			e = Exercise.objects.get(cuasimodo_exercise_id=v.get('exercise_id'), grade=g,unit=u)
		except Exercise.DoesNotExist:
 			e = Exercise(cuasimodo_exercise_id=v.get('exercise_id'), grade=g,unit=u)
			e.save()

		serial = v.get('serial')
		if v.get('is_teacher') == "1":
			is_teacher = True
		else:
			is_teacher = False

		try:
			p = Person.objects.get(serial=serial)
		except Person.DoesNotExist:
			trim_serial = serial[:4]
			if is_teacher:
				if serial is not "" and trim_serial is not "test":
					docentes += 1
				p = Teacher(serial=serial)
			else:
				if serial is not "" and trim_serial is not "test":
					alumnos += 1
				p = Student(serial=serial)
			p.save()

		points = v.get('points',0.0)
		if points == "":
			points = 0.0
		points = float(points)

		time = v.get('time',0.0)
		if time == "":
			time = 0.0
		time = float(time)
		answer = v.get('answers',"")
		created = v.get('created',None)
		try:
			r = Result.objects.get(id=v.get('id'))
		except:
			r = Result(id=v.get('id'),points=points, answer=answer, exercise=e, person=p, time_elapsed=time, created=created)
			r.save()

	return render_to_response('index.html', {'docentes':docentes, 'alumnos':alumnos}, context_instance = RequestContext(request))




def ingresar_datos(request):

	countries = [
		("Uruguay"),
		("Argentina"),
		("Chile"),
		("Peru"),
		("Guatemala"),
		("Paraguay"),
		("Panama"),
	]
	departments = [
		("Montevideo", 1),
		("Canelones", 1),
		("Florida", 1),
		("San Jose", 1),
		("Flores", 1),
		("Colonia", 1),
		("Maldonado", 1),
		("Rocha", 1),
		("Treinta y Tres", 1),
		("Cerro Largo", 1),
		("Soriano", 1),
		("Rio Negro", 1),
		("Tacuarembo", 1),
		("Durazno", 1),
		("Rivera", 1),
		("Paysandu", 1),
		("Salto", 1),
		("Artigas", 1),
		("Lavalleja", 1),
		("Buenos Aires", 2),
		("Entre Rios", 2),
		("Cordoba", 2),
		("Mendoza", 2),
	]

	#school(id, number, name, department_id)
	schools = [
		(2, "Republica Argentina", 1),
		(279, "Julio Castro", 1),
		(5, "Jose Pedro Varela", 1),
		(11, "Abraham Lincoln", 1),
		(164, "Roger Ballet", 1),
		(6, "Estados Unidos", 1),
		(16, "Suecia", 1),
		(132, "Aurelia Viera", 1),
		(20, "-", 1),
		(74, "-", 1),
		(21, "Alemania", 1),
		(27, "-", 1),
		(32, "-", 1),
		(40, "Mexico", 1),
		(83, "-", 1),
		(36, "Belgica", 1)
	]

	#grade(id, name)
	grades = [
		(1),
		(2),
		(3),
		(4),
		(5),
		(6),
	]

	#classroom(code, class_letter, shift, grade, school_id)
	classrooms = [
		('qwer1','A','MORNING',5,1),
		('qwer2','B','MORNING',5,1),
		('qwer3','C','MORNING',5,1),
		('qwer4','A','MORNING',6,1),
		('qwer5','B','MORNING',6,1),
		('qwer6','C','MORNING',6,1),
		('awer1','D','EVENING',5,1),
		('awer2','E','EVENING',5,1),
		('awer3','F','EVENING',5,1),
		('awer4','D','EVENING',6,1),
		('awer5','E','EVENING',6,1),
		('awer6','F','EVENING',6,1),
		('qder1','A','MORNING',5,2),
		('qder2','B','MORNING',5,2),
		('qder3','C','MORNING',5,2),
		('qder4','A','MORNING',6,2),
		('qder5','B','MORNING',6,2),
		('qder6','C','MORNING',6,2),
		('adsr1','D','EVENING',5,2),
		('adsr2','E','EVENING',5,2),
		('adsr3','F','EVENING',5,2),
		('adsr4','D','EVENING',6,2),
		('adsr5','E','EVENING',6,2),
		('adsr6','F','EVENING',6,2),
		('qwsr1','A','MORNING',5,3),
		('qwsr2','B','MORNING',5,3),
		('qwsr3','C','MORNING',5,3),
		('qwsr4','A','MORNING',6,3),
		('qwsr5','B','MORNING',6,3),
		('qwsr6','C','MORNING',6,3),
		('awsr1','D','EVENING',5,3),
		('awsr2','E','EVENING',5,3),
		('awsr3','F','EVENING',5,3),
		('awsr4','D','EVENING',6,3),
		('awsr5','E','EVENING',6,3),
		('awsr6','F','EVENING',6,3),
		('qdsr1','A','MORNING',5,4),
		('qdsr2','B','MORNING',5,4),
		('qdsr3','C','MORNING',5,4),
		('qdsr4','A','MORNING',6,4),
		('qdsr5','B','MORNING',6,4),
		('qdsr6','C','MORNING',6,4),
		('addr1','D','EVENING',5,4),
		('addr2','E','EVENING',5,4),
		('addr3','F','EVENING',5,4),
		('addr4','D','EVENING',6,4),
		('addr5','E','EVENING',6,4),
		('addr6','F','EVENING',6,4),
		('qwdr1','A','MORNING',5,5),
		('qwdr2','B','MORNING',5,5),
		('qwdr3','C','MORNING',5,5),
		('qwdr4','A','MORNING',6,5),
		('qwdr5','B','MORNING',6,5),
		('qwdr6','C','MORNING',6,5),
		('awdr1','D','EVENING',5,5),
		('awdr2','E','EVENING',5,5),
		('awdr3','F','EVENING',5,5),
		('awdr4','D','EVENING',6,5),
		('awdr5','E','EVENING',6,5),
		('awdr6','F','EVENING',6,5),
		('qddr1','A','MORNING',5,6),
		('qddr2','B','MORNING',5,6),
		('qddr3','C','MORNING',5,6),
		('qddr4','A','MORNING',6,6),
		('qddr5','B','MORNING',6,6),
		('qddr6','C','MORNING',6,6),
		('addr1','D','EVENING',5,6),
		('addr2','E','EVENING',5,6),
		('addr3','F','EVENING',5,6),
		('addr4','D','EVENING',6,6),
		('addr5','E','EVENING',6,6),
		('addr6','F','EVENING',6,6),
		('qwdr1','A','MORNING',5,7),
		('qwdr2','B','MORNING',5,7),
		('qwdr3','C','MORNING',5,7),
		('qwdr4','A','MORNING',6,7),
		('qwdr5','B','MORNING',6,7),
		('qwdr6','C','MORNING',6,7),
		('awdr1','D','EVENING',5,7),
		('awdr2','E','EVENING',5,7),
		('awdr3','F','EVENING',5,7),
		('awdr4','D','EVENING',6,7),
		('awdr5','E','EVENING',6,7),
		('awdr6','F','EVENING',6,7),
		('qddr1','A','MORNING',5,8),
		('qddr2','B','MORNING',5,8),
		('qddr3','C','MORNING',5,8),
		('qddr4','A','MORNING',6,8),
		('qddr5','B','MORNING',6,8),
		('qddr6','C','MORNING',6,8),
		('addr1','D','EVENING',5,8),
		('addr2','E','EVENING',5,8),
		('addr3','F','EVENING',5,8),
		('addr4','D','EVENING',6,8),
		('addr5','E','EVENING',6,8),
		('addr6','F','EVENING',6,8),
	]

	#area(id, name, grade_id)
	areas =	[
		("Lenguas",5),
		("Matematicas",5),
		("Artística",5),
		("Naturaleza",5),
		("Social",5),
	]

	#area(id, name, area_id)
	subjects = [
		("Biología",4),
		("Química",4),
		("Física",4),
		("Geología",4),
		("Astronomía",4),
	]

	#area(id, letter, name, description, subject_id, available,grade)
	units = [
		("A","El agua como solvente","-",2,1,5),
		("B","La capilaridad","-",2,1,5),
		("C","La ósmosis","-",2,1,5),
		("D","La destilación y la electrólisis - Las sustancias simples y compuestas","-",2,1,5),
		("E","Los elementos químicos - Los metales y los no metales","-",2,1,5),
		("A","La refracción de la luz","-",3,1,5),
		("B","Imanes y brújulas","-",3,1,5),
		("C","Electricidad y energia","-",3,1,5),
		("D","Calor: Una forma de transferir energía","-",3,1,5),
		("E","Movimiento y gravedad","-",3,1,5),
		("A","Las aguas superficiales","-",4,1,5),
		("B","El clima","-",4,1,5),
		("C","Erosión eólica","-",4,1,5),
		("D","La isostasia","-",4,1,5),
		("E","Ciclo bioecológico","-",4,1,5),
		("A","El modelo corpuscular de la materia","-",2,1,6),
		("B","Las soluciones gaseosas","-",2,1,6),
		("C","La densidad como propiedad intensiva de los sistemas","-",2,1,6),
		("D","La conservación de la masa","-",2,1,6),
		

	]


	#lecture(id,cuasimodo_lecture_id,name,grade,unit,teacher_guide,img,lecture_type)
	lectures = [
		(1,"Portada",5,6,"","media/5f_A1.jpg","EXPERIMENT"),
		(2,"Misterio Luminoso",5,6,"<h3>MATERIALES:</h3> <ul> <li> <p>1 láser</br> El láser puede sustituirse por una linterna potente a la que se ha pegado una cartulina negra con una pequeña perforación, de modo de tener un haz delgado de luz.</p> </li> <li> <p>1 caja de cartón</br> La usaremos sólo si no fuera posible que el salón esté un poco oscurecido.</p> </li> <li> <p>1 tira de papel</br> En lugar de papel puede utilizarse una varita de incienso.</p> </li> <li>2 o 3 gotas de leche</li> </ul> <p> El salón debe estar un poco oscurecido; si no fuera posible, colocar el frasco dentro de una caja grande de cartón.<br/> Se trata de inducir la idea de que la luz viaja en línea recta en un medio homogéneo, pero cuando cambia de medio cambia la dirección en que se propaga (excepto cuando incide perpendicularmente a la superficie que separa los medios: en ese único caso no sufre desviación, pero igual se refracta.<br/> En el experimento se está comparando lo que le ocurre a la luz al pasar del aire al agua. Se agrega un poco de humo y una gota de leche, ya que al incorporar partículas en suspensión en cada medio estas reflejan la luz del láser de manera que se puede observar su trayectoria.<br/> Como la luz del láser puede dañar seriamente la vista, se recomienda una manipulación exclusiva del docente. </p>","media/5f_A2.jpg","EXPERIMENT"),
		(3,"¿Viste lo que ocurrió?",5,6,"","media/5f_A3.jpg","EXPERIMENT"),
		(4,"Veloz como el relámpago",5,6,"","media/5f_A4.jpg","LECTURE"),
		(5,"La velocidad de la luz y la refracción",5,6,"","media/5f_A5.jpg","LECTURE"),
		(6,"Los 'trucos' de la luz",5,6,"","media/5f_A6.jpg","LECTURE"),
		(7,"Las lentes",5,6,"","media/5f_A7.jpg","LECTURE"),
		(8,"Resumen",5,6,"","media/5f_A8.jpg","LECTURE"),
		(23,"Actividades escritas",5,6,"","media/5f_A23.jpg","BOOK_ACTIVITY"),
		(24,"Actividades escritas",5,6,"","media/5f_A24.jpg","BOOK_ACTIVITY"),
		(25,"Actividades escritas",5,6,"","media/5f_A25.jpg","BOOK_ACTIVITY"),
		(26,"Actividades escritas",5,6,"","media/5f_A26.jpg","BOOK_ACTIVITY"),
		(27,"Tareas",5,6,"","media/5f_A27.jpg","HOMEWORK"),
	]

	#exercise(number,...,type)
	exercises = [
		(9,"Ejercicio",5,6,"","TRUE_FALSE","media/5f_A9.jpg"),
		(10,"Ejercicio",5,6,"","TRUE_FALSE","media/5f_A10.jpg"),
		(12,"Ejercicio",5,6,"","TRUE_FALSE","media/5f_A12.jpg"),
		(13,"Ejercicio",5,6,"","TRUE_FALSE","media/5f_A13.jpg"),
		(14,"Ejercicio",5,6,"","TRUE_FALSE","media/5f_A14.jpg"),
		(15,"Ejercicio",5,6,"","MULTIPLE_CHOICE","media/5f_A15.jpg"),
		(16,"Ejercicio",5,6,"","TRUE_FALSE","media/5f_A16.jpg"),
		(17,"Ejercicio",5,6,"","TRUE_FALSE","media/5f_A17.jpg"),
		(18,"Ejercicio",5,6,"","FILL_BLANKS","media/5f_A18.jpg"),
		(19,"Ejercicio",5,6,"","FILL_BLANKS","media/5f_A19.jpg"),
		(20,"Ejercicio",5,6,"","TRUE_FALSE","media/5f_A20.jpg"),
		(21,"Ejercicio",5,6,"","TRUE_FALSE","media/5f_A21.jpg"),
		(22,"Ejercicio",5,6,"","CRUCIGRAMA","media/5f_A22.jpg"),
		

	]

	#teacher(id,name, last_name, date_of_birth, gender, serial, email, username, password)
	teachers = [
		["Teresa","Gonzalez","1967-06-12","FEMALE",None,"teregonzalez@hotmail.com","TereGonzalez","tere1234"],
		["Marta","Fernández","1987-08-22","FEMALE",None,"mfer85@hotmail.com","mfdez","mfdez1234"],
		["Susana","Maciel","1963-06-12","FEMALE",None,"sumaciel@hotmail.com","sumaciel","sulopez1234"],
		["Lorena","Lopez","1983-02-22","FEMALE",None,"lololopez@gmail.com","lololopez","lolopez1234"],
		["Ana","González","1972-08-22","FEMALE",None,"anagonz@hotmail.com","anagonz","sulopez1234"],
		["Vilma","Macías","1982-08-14","FEMALE",None,"vilmamacias@gmail.com","vilmamacias","sulopez1234"],
		["Paula","Pereira","1972-08-14","FEMALE",None,"paupereira@hotmail.com","paupereira","sulopez1234"],
		["Florencia","Fernández","1985-04-13","FEMALE",None,"flofer@gmail.com","flofer","sulopez1234"],
		["Elena","Rodríguez","1982-04-13","FEMALE",None,"elerod@hotmail.com","elerod","sulopez1234"],
		["Carolina","Banchero","1985-09-12","FEMALE",None,"carobanchero@gmail.com","carobanchero","sulopez1234"],
		["José","Cardozo","1985-02-12","MALE",None,"pepecardozo@hotmail.com","pepecardozo","sulopez1234"],
		["Nelly","Lopez","1985-03-16","FEMALE",None,"nellylo@gmail.com","nellylo","sulopez1234"],
		["Pedro","Hernández","1988-12-22","MALE",None,"pedroher@hotmail.com","pedroher","sulopez1234"],
		["Mariana","Britos","1975-05-12","FEMALE",None,"maribritos@gmail.com","maribritos","sulopez1234"],
		["Elizabeth","Rojo","1978-05-27","FEMALE",None,"elirojo@gmail.com","elirojo","sulopez1234"],
		["Paola","Garay","1985-06-17","FEMALE",None,"paogaray@hotmail.com","paogaray","sulopez1234"],
		["Julio","Alvez","1985-03-16","MALE",None,"julitoalvez@hotmail.com","julitoalvez","sulopez1234"],
	]



	#teacher(id,name, last_name, date_of_birth, gender, serial, classroom)
	students = [
		["Joaquín","González","2004-08-12","MALE",None,1],
		["Ana","González","2004-09-11","FEMALE",None,1],
		["Jonathan","Giménez","2004-09-12","MALE",None,1],
		["Rúben","Pereyra","2004-12-10","MALE",None,1],
		["Adrián","González","2004-09-11","	MALE",None,1],
		["Julio","Tucci","2004-09-12","MALE",None,1],
		["Mariana","López","2004-12-10","FEMALE",None,1],
		["Leonardo","Rodríguez","2004-08-12","MALE",None,1],
		["Leandro","González","2004-09-11","MALE",None,1],
		["Martina","Giménez","2004-09-12","FEMALE",None,1],
		["Gabriel","Pereira","2004-12-10","MALE",None,1],
		["Gabriela","López","2004-12-10","FEMALE",None,1],
		["Martín","Lugano","2004-12-10","MALE",None,1],
		["Federico","Fernandez","2004-12-10","MALE",None,1],
		["Federica","López","2004-12-10","FEMALE",None,1],
		["Felipe","Rodríguez","2004-05-10","MALE",None,2],
		["Tiago","Pereyra","2004-12-10","MALE",None,2],
		["Atilio","Arévalo","2004-05-10","MALE",None,2],
		["Bernardo","Fernandez","2004-12-10","MALE",None,2],
		["Franco","Rodríguez","2004-05-10","MALE",None,2],
		["Leonardo","López","2004-12-10","MALE",None,2],
		["Sofía","Britos","2004-05-10","FEMALE",None,2],
		["Joaquín","González","2004-08-12","MALE",None,2],
		["Ana","González","2004-09-11","FEMALE",None,2],
		["Jonathan","Giménez","2004-09-11","MALE",None,2],
		["Rúben","Pereyra","2004-12-10","MALE",None,2],
		["Fernando","González","2004-08-11","MALE",None,2],
		["Adrián","González","2004-09-11","	MALE",None,2],
		["Julio","Giménez","2004-09-12","MALE",None,2],
		["Mariana","López","2004-12-10","FEMALE",None,2],
		["Leonardo","Rodríguez","2004-08-12","MALE",None,2],
		["Leandro","González","2004-09-11","MALE",None,2],
		["Ana Laura","Giménez","2004-09-12","FEMALE",None,2],
		["Gabriel","Pereira","2004-05-10","MALE",None,2],
		["Gabriela","López","2004-12-10","FEMALE",None,2],
		["Martín","Lugano","2004-12-10","MALE",None,2],
		["Federico","Fernandez","2004-12-10","MALE",None,2],
		["Elena","López","2004-05-10","FEMALE",None,2],
		["Felipe","Rodríguez","2004-05-10","MALE",None,2],
		["Tiago","Pereyra","2004-12-10","MALE",None,2],
		["Leonardo","Fernandez","2004-12-10","MALE",None,2],
		["Franco","Rodríguez","2004-05-10","MALE",None,2],
		["Mario","López","2004-12-10","MALE",None,2],
		["Martina","Pereyra","2004-12-10","FEMALE",None,2],
		["Sofía","Giménez","2004-12-10","FEMALE",None,2],
		["Joaquín","González","2004-08-11","MALE",None,3],
		["Ana","González","2004-09-11","FEMALE",None,3],
		["Jonathan","Giménez","2004-09-11","MALE",None,3],
		["Rúben","Pereyra","2004-12-10","MALE",None,3],
		["Fernando","González","2004-08-11","MALE",None,3],
		["Adrián","González","2004-09-11","	MALE",None,3],
		["Julio","Tucci","2004-09-12","MALE",None,3],
		["Mariana","López","2004-05-10","FEMALE",None,3],
		["Leonardo","Rodríguez","2004-08-12","MALE",None,3],
		["Leandro","González","2004-09-11","MALE",None,3],
		["Martina","Giménez","2004-09-11","FEMALE",None,3],
		["Gabriel","Pereira","2004-05-10","MALE",None,3],
		["Gabriela","López","2004-05-10","FEMALE",None,3],
		["Martín","Lugano","2004-12-10","MALE",None,3],
		["Federico","Fernandez","2004-12-10","MALE",None,3],
		["Federica","López","2004-12-10","FEMALE",None,3],
		["Felipe","Rodríguez","2004-12-10","MALE",None,4],
		["Tiago","Pereyra","2004-12-10","MALE",None,4],
		["Atilio","Arévalo","2004-12-10","MALE",None,4],
		["Bernardo","Fernandez","2004-12-10","MALE",None,4],
		["Franco","Rodríguez","2004-12-10","MALE",None,4],
		["Leonardo","López","2004-12-10","MALE",None,4],
		["Ana Clara","Pereyra","2004-12-10","FEMALE",None,4],
		["Sofía","Giménez","2004-12-10","FEMALE",None,4],
		["Joaquín","González","2004-08-12","MALE",None,4],
		["Ana","González","2004-09-11","FEMALE",None,4],
		["Jonathan","Tucci","2004-09-12","MALE",None,4],
		["Rúben","Pereyra","2004-12-10","MALE",None,4],
		["Fernando","González","2004-08-12","MALE",None,4],
		["Adrián","González","2004-09-11","	MALE",None,4],
		["Julio","Giménez","2004-09-12","MALE",None,4],
		["Mariana","López","2004-12-10","FEMALE",None,4],
		["Leonardo","Rodríguez","2004-08-12","MALE",None,4],
		["Leandro","González","2004-09-11","MALE",None,4],
		["Ana Laura","Giménez","2004-09-12","FEMALE",None,4],
		["Gabriel","Pereira","2004-12-10","MALE",None,4],
		["Gabriela","López","2004-12-10","FEMALE",None,4],
		["Martín","Lugano","2004-12-10","MALE",None,4],
		["Federico","Fernandez","2004-12-10","MALE",None,4],
		["Elena","López","2004-12-10","FEMALE",None,4],
		["Felipe","Rodríguez","2004-12-10","MALE",None,4],
		["Tiago","Pereyra","2004-12-10","MALE",None,4],
		["Ana Clara","Arévalo","2004-12-10","MALE",None,4],
		["Leonardo","Britos","2004-12-10","MALE",None,4],
		["Franco","Rodríguez","2004-12-10","MALE",None,4],
		["Mario","López","2004-12-10","MALE",None,4],
		["Martina","Pereyra","2004-12-10","FEMALE",None,4],
		["Sofía","Britos","2004-12-10","FEMALE",None,4],
		["Joaquín","González","2004-08-12","MALE",None,5],
		["Ana","González","2004-09-11","FEMALE",None,5],
		["Jonathan","Giménez","2004-09-12","MALE",None,5],
		["Rúben","Pereyra","2004-12-10","MALE",None,5],
		["Fernando","González","2004-08-12","MALE",None,5],
		["Adrián","González","2004-09-11","	MALE",None,5],
		["Julio","Tucci","2004-09-12","MALE",None,5],
		["Mariana","López","2004-12-10","FEMALE",None,5],
		["Leonardo","Rodríguez","2004-08-12","MALE",None,5],
		["Leandro","González","2004-09-11","MALE",None,5],
		["Martina","Giménez","2004-09-12","FEMALE",None,5],
		["Gabriel","Pereira","2004-12-10","MALE",None,5],
		["Gabriela","López","2004-12-10","FEMALE",None,5],
		["Martín","Lugano","2004-12-10","MALE",None,5],
		["Federico","Fernandez","2004-12-10","MALE",None,5],
		["Federica","López","2004-12-10","FEMALE",None,5],
		["Felipe","Rodríguez","2004-12-10","MALE",None,6],
		["Tiago","Pereyra","2004-12-10","MALE",None,6],
		["Atilio","Arévalo","2004-12-10","MALE",None,6],
		["Bernardo","Fernandez","2004-12-10","MALE",None,6],
		["Franco","Rodríguez","2004-12-10","MALE",None,6],
		["Leonardo","López","2004-12-10","MALE",None,6],
		["Ana Clara","Pereyra","2004-12-10","FEMALE",None,6],
		["Sofía","Britos","2004-12-10","FEMALE",None,6],
		["Joaquín","González","2004-08-12","MALE",None,6],
		["Ana","González","2004-09-11","FEMALE",None,6],
		["Jonathan","Giménez","2004-09-12","MALE",None,6],
		["Rúben","Pereyra","2004-12-10","MALE",None,6],
		["Fernando","González","2004-08-12","MALE",None,6],
		["Adrián","González","2004-09-11","	MALE",None,6],
		["Julio","Giménez","2004-09-12","MALE",None,6],
		["Mariana","López","2004-12-10","FEMALE",None,6],
		["Leonardo","Rodríguez","2004-08-12","MALE",None,6],
		["Leandro","González","2004-09-11","MALE",None,6],
		["Ana Laura","Giménez","2004-09-12","FEMALE",None,6],
		["Gabriel","Pereira","2004-12-10","MALE",None,6],
		["Gabriela","López","2004-12-10","FEMALE",None,6],
		["Martín","Lugano","2004-12-10","MALE",None,6],
		["Federico","Fernandez","2004-12-10","MALE",None,6],
		["Elena","López","2004-12-10","FEMALE",None,6],
		["Felipe","Rodríguez","2004-12-10","MALE",None,6],
		["Tiago","Pereyra","2004-12-10","MALE",None,6],
		["Ana Clara","Arévalo","2004-12-10","MALE",None,6],
		["Leonardo","Fernandez","2004-12-10","MALE",None,6],
		["Franco","Rodríguez","2004-12-10","MALE",None,6],
		["Mario","López","2004-12-10","MALE",None,6],
		["Martina","Pereyra","2004-12-10","FEMALE",None,6],
		["Sofía","Giménez","2004-12-10","FEMALE",None,6],
		["Joaquín","González","2004-08-12","MALE",None,7],
		["Ana","González","2004-09-11","FEMALE",None,7],
		["Jonathan","Giménez","2004-09-12","MALE",None,7],
		["Rúben","Pereyra","2004-12-10","MALE",None,7],
		["Fernando","González","2004-08-12","MALE",None,7],
		["Adrián","González","2004-09-11","MALE",None,7],
		["Julio","Tucci","2004-09-12","MALE",None,7],
		["Mariana","López","2004-12-10","FEMALE",None,7],
		["Leonardo","Rodríguez","2004-08-12","MALE",None,7],
		["Leandro","González","2004-09-11","MALE",None,7],
		["Martina","Giménez","2004-09-12","FEMALE",None,7],
		["Gabriel","Pereira","2004-12-10","MALE",None,7],
		["Gabriela","López","2004-12-10","FEMALE",None,7],
		["Martín","Lugano","2004-12-10","MALE",None,7],
		["Federico","Fernandez","2004-12-10","MALE",None,7],
		["Federica","López","2004-12-10","FEMALE",None,7],
		["Felipe","Rodríguez","2004-12-10","MALE",None,8],
		["Tiago","Pereyra","2004-12-10","MALE",None,8],
		["Atilio","Arévalo","2004-12-10","MALE",None,8],
		["Bernardo","Fernandez","2004-12-10","MALE",None,8],
		["Franco","Rodríguez","2004-12-08","MALE",None,8],
		["Leonardo","López","2004-12-10","MALE",None,8],
		["Ana Clara","Pereyra","2004-12-10","FEMALE",None,8],
		["Sofía","Giménez","2004-02-08","FEMALE",None,8],
		["Joaquín","González","2004-08-12","MALE",None,8],
		["Ana","González","2004-09-11","FEMALE",None,8],
		["Jonathan","Tucci","2004-09-12","MALE",None,8],
		["Rúben","Pereyra","2004-02-10","MALE",None,8],
		["Fernando","González","2004-08-12","MALE",None,8],
		["Adrián","González","2004-09-11","	MALE",None,8],
		["Julio","Giménez","2004-09-12","MALE",None,8],
		["Mariana","López","2004-02-10","FEMALE",None,8],
		["Leonardo","Rodríguez","2004-08-12","MALE",None,8],
		["Leandro","González","2004-09-11","MALE",None,8],
		["Ana Laura","Giménez","2004-09-12","FEMALE",None,8],
		["Gabriel","Pereira","2004-12-08","MALE",None,8],
		["Gabriela","López","2004-02-08","FEMALE",None,8],
		["Martín","Lugano","2004-02-10","MALE",None,8],
		["Federico","Fernandez","2004-12-10","MALE",None,8],
		["Elena","López","2004-12-08","FEMALE",None,8],
		["Felipe","Rodríguez","2004-12-10","MALE",None,8],
		["Tiago","Pereyra","2004-12-08","MALE",None,8],
		["Ana Clara","Arévalo","2004-12-10","MALE",None,8],
		["Leonardo","Britos","2004-02-08","MALE",None,8],
		["Franco","Rodríguez","2004-12-08","MALE",None,8],
		["Mario","López","2004-02-10","MALE",None,8],
		["Martina","Pereyra","2004-12-10","FEMALE",None,8],
		["Sofía","Britos","2004-12-08","FEMALE",None,8],
	]

	for country in countries:
		try:
			c = Country.objects.get(name=country)
		except Country.DoesNotExist:
			c = Country(name=country)
			c.save()

	for department in departments:
		try:
			d = Department.objects.get(name=department[0])
		except Department.DoesNotExist:
			c = Country.objects.get(id=department[1])
			d = Department(name=department[0],country=c)
			d.save()

	for school in schools:
		try:
			s = School.objects.get(number=school[0], name=school[1])
		except School.DoesNotExist:
			d = Department.objects.get(id=school[2])
			s = School(number=school[0], name=school[1],department=d)
			s.save()

	for grade in grades:
		try:
			g = Grade.objects.get(name=grade)
		except Grade.DoesNotExist:
			g = Grade(name=grade)
			g.save()

	for area in areas:
		try:
			a = Area.objects.get(name=area[0])
		except Area.DoesNotExist:
			a = Area(name=area[0])
			a.save()

	for subject in subjects:
		try:
			s = Subject.objects.get(name=subject[0])
		except Subject.DoesNotExist:
			a = Area.objects.get(id=subject[1])
			s = Subject(name=subject[0], area=a)
			s.save()

	for unit in units:
		try:
			u = Unit.objects.get(letter=unit[0], name=unit[1])
		except Unit.DoesNotExist:
			s = Subject.objects.get(id=unit[3])
			g = Grade.objects.get(name=unit[5])
			u = Unit(letter=unit[0], name=unit[1], description=unit[2], subject=s, available=unit[4], grade=g)
			u.save()	

	for classroom in classrooms:
		try:
			c = ClassRoom.objects.get(code=classroom[0])
		except ClassRoom.DoesNotExist:
			g = Grade.objects.get(id=classroom[3])
			s = School.objects.get(id=classroom[4])
			c = ClassRoom(code=classroom[0], class_letter=classroom[1], shift=classroom[2], grade=g, school=s)
			c.save()

	for teacher in teachers:
		try:
			t = Teacher.objects.get(email=teacher[5])
		except Teacher.DoesNotExist:
			dob = datetime.strptime(teacher[2], '%Y-%m-%d').date()
			serial = teacher[4]
			while serial is None:
				serial = "test" + str(int(random.random() * 10000))
				try:
					t = Teacher.objects.get(serial=serial)
					serial = None
				except Teacher.DoesNotExist:
					teacher[4] = serial
			t = Teacher(name=teacher[0], last_name=teacher[1], date_of_birth=dob, gender=teacher[3], serial=teacher[4], email=teacher[5], nickname=teacher[6], password=teacher[7])
			t.save()

	for student in students:
 		try:
 			code = classrooms[student[5]][0]
 			c = ClassRoom.objects.get(code=code)
			s = Student.objects.get(serial=student[4])
		except Student.DoesNotExist:
			dob = datetime.strptime(student[2], '%Y-%m-%d').date()
			serial = student[4]
			while serial is None:
				serial = "test" + str(int(random.random() * 10000))
				try:
					s = Student.objects.get(serial=serial)
					serial = None
				except Student.DoesNotExist:
					student[4] = serial
			s = Student(name=student[0], last_name=student[1], date_of_birth=dob, gender=student[3], serial=student[4], class_room=c)
			s.save()

	#asignacion de teacher a classroom
	i = 0
	for teacher in teachers:
		c = ClassRoom.objects.get(code=classrooms[i][0])
		t = Teacher.objects.get(serial=teacher[4])
		c.teachers.add(t)
		i += 1
	

	return render_to_response('index.html', context_instance = RequestContext(request))

def borrar_tablas(request):

	return render_to_response('index.html', context_instance=RequestContext(request))