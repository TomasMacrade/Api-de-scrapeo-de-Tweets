-- Create Tablas

 CREATE TABLE Candidatos (
 ID int,
 Nombre Varchar(100),
 Apellido Varchar(100),
 Espacio int,
 Usuario Varchar (100)
 );

Create Table Tweets(
ID_Candidato int,
Texto Varchar(10000),
Rt int,
Citas int,
Likes int,
FechaHora TIMESTAMP,
URL Varchar(10000)
);

Create Table Espacio(
ID int,
Nombre Varchar(1000),
Nombre_Corto Varchar(10)
);

-- Insert Tabla Candidatos y Espacio

-- FIT = 0
-- LLA = 1
-- FdT = 2
-- JxC = 3

insert into Candidatos (ID,
 Nombre ,
 Apellido ,
 Espacio ,
 Usuario)
Values (0,'Nicolas','Del Caño', 0,'NicolasdelCano'),
(1,'Victoria','Villarruel',1,'VickyVillarruel'),
(2,'Maria Eugenia','Vidal',3,'mariuvidal' ),
(3,'Axel','Kicillof',2,'Kicillofok'),
(4,'Ramiro','Marra',1,'RAMIROMARRA'),
(5,'Jose Luis','Espert',1,'jlespert'),
(6,'Patricia','Bullrich',3,'PatoBullrich'),
(7,'Horacio','Larreta',3,'horaciorlarreta'),
(8,'Juan','Grabois',2,'JuanGrabois'),
(9,'Sergio Tomás','Massa',2,'SergioMassa'),
(10,'Myriam','Bregman',0,'myriambregman'),
(11,'Gabriel','Solano',0,'Solanopo');

insert into Espacio (ID,Nombre,Nombre_Corto)
Values (0,'Frente de Izquierda','FIT'),
(1,'La Libertad Avanza','LLA'),
(2,'Frente de Todos','FdT'),
(3,'Juntos por el cambio','JxC');




