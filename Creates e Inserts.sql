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

-- Insert Tabla Candidatos

insert into Candidatos
Values (0,"Nicolas","Del Caño", "FIT","NicolasdelCano"),
(1,"Victoria","Villarruel","LLA","VickyVillarruel"),
(2,"Maria Eugenia","Vidal",""




