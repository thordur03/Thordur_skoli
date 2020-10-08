-- drop database if exists Verkefni1A;

create database Verkefni1A;

use Verkefni1A;



-- Dæmi 1

-- drop table if exists Nemandi;
create table Nemandi
(
kennitala char(10) primary key,
nafn varchar(75),
skoli varchar(45),
virkur boolean
);
select * from Nemandi;

insert into Nemandi(kennitala,nafn,skoli,virkur)values(2810032910,"Þórður Ingi","Tækniskólinn-Hát",True);
insert into Nemandi(kennitala,nafn,skoli,virkur)values(0111048900,"Pálína puðra","Tækniskólinn-Haf",False);
insert into Nemandi(kennitala,nafn,skoli,virkur)values(0202038090,"Pésípas Pútur","Tækniskólinn-haf",True);
insert into Nemandi(kennitala,nafn,skoli,virkur)values(1312988909,"Jónas Aparingur","Tækniskólinn-Skó",True);
insert into Nemandi(kennitala,nafn,skoli,virkur)values(3101038750,"Kalli Þakálfur","Tækniskólinn-hát",False);





-- Dæmi 2






-- drop table if exists Eigandi;
create table Eigandi
(
	kennitala int,
    fornafn varchar(30),
    eftirnafn varchar(30),
    faedingardagur date,
    netfang varchar(75),
    kennitala char(10),
    constraint eigandi_PK primary key(kennitala)
);

insert into Eigandi(kennitala,fornafn,eftirnafn,faedingardagur,netfang)values("5000","Jón","Jónson","1995-09-26","jon@gmail.com");
insert into Eigandi(kennitala,fornafn,eftirnafn,faedingardagur,netfang)values("6000","Geur","palsen","1986-02-01","geggi@gmail.com");
insert into Eigandi(kennitala,fornafn,eftirnafn,faedingardagur,netfang)values("7000","Jón","Ingimarsson","1989-12-29","jonni@gmail.com");
insert into Eigandi(kennitala,fornafn,eftirnafn,faedingardagur,netfang)values("8000","Ron","weeler","1967-02-25","ron@gmail.com");
insert into Eigandi(kennitala,fornafn,eftirnafn,faedingardagur,netfang)values("9000","Palli","póstsson","1998-07-28","pals@gmail.com");

select * from Eigandi;



-- Dæmi 3
create table Fyrirtæki(
	kennitala char(10),
    constraint nafn  primary key,
    heimilisfang varchar(40),
    framkvaendarstjori varchar(30),
    simi char(7),
    netfang(25),
    vefur(100),
    lysing varchar(255)
);

-- daemi 4
-- drop table if exist Bill 
create table Bill
(
	fastanumer char(10),
    tegund char(20),
    argerd char(10),
    litur char(15),
    sjalfskiptur boolean,
    orkugjafi char(10),
    KennitalaEiganda char(10),
    constraint bill_PK primary key(fastanumer),
	constraint bill_eigandi_FK foreign key(kennitalaEiganda) references Eigandi(kennitala)
);


insert into Bill(fastanumer,tegund,argerd,litur,sjalfskiptur,orkugjafi,KennitalaEiganda)values("ZQL45","Telsa","2020","svartur",true,"Bensín","5000");
insert into Bill(fastanumer,tegund,argerd,litur,sjalfskiptur,orkugjafi,KennitalaEiganda)values("IS291","Kia","2000","grár",true,"Bensín","5000");
insert into Bill(fastanumer,tegund,argerd,litur,sjalfskiptur,orkugjafi,KennitalaEiganda)values("ABC28","Toyota","2010","hvítur",false,"Dísel","6000");
insert into Bill(fastanumer,tegund,argerd,litur,sjalfskiptur,orkugjafi,KennitalaEiganda)values("ISL88","Ford","2008","blár",false,"Bensín","6000");
insert into Bill(fastanumer,tegund,argerd,litur,sjalfskiptur,orkugjafi,KennitalaEiganda)values("JB007","Toyota","1990","svartur",true,"Dísel","7000");
insert into Bill(fastanumer,tegund,argerd,litur,sjalfskiptur,orkugjafi,KennitalaEiganda)values("XX001","Ferrari","1986","rauður",false,"Bensín","8000");
insert into Bill(fastanumer,tegund,argerd,litur,sjalfskiptur,orkugjafi,KennitalaEiganda)values("MZP99","Tesla","2019","hvítur",true,"Rafmagn","9000");
insert into Bill(fastanumer,tegund,argerd,litur,sjalfskiptur,orkugjafi,KennitalaEiganda)values("TU807","Renault","2015","grár",false,"Rafmagn","9000");

select * from Bill;


