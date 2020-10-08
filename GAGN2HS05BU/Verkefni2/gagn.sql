-- -----------------------------------------------------
-- 					  Namsferill
-- -----------------------------------------------------
-- drop database if exists Namsferill;
create database Namsferill default character set utf8;
use Namsferill ;


-- -----------------------------------------------------
-- 						Afangar
-- -----------------------------------------------------
create table Afangar 
(
  afangaNumer char(15) not null,
  afangaHeiti varchar(75) not null,
  einingar tinyint(4) null default '5',
  constraint afangi_PK primary key(afangaNumer),
  constraint name_NQ unique(afangaHeiti asc)
);


-- -----------------------------------------------------
-- 						Skolar
-- -----------------------------------------------------
create table Skolar 
(
  skolaNumer int(11) not null auto_increment,
  skolaheiti varchar(75) null default null,
  constraint skoli_PK primary key(skolaNumer)
);


-- -----------------------------------------------------
-- 					  Undirskolar
-- -----------------------------------------------------
create table Undirskolar
(
  undirskolaNumer int(11) not null auto_increment,
  heiti varchar(75) not null,
  skolaNumer int(11) not null,
  constraint deild_PK primary key(undirskolaNumer),
  constraint deild_skoli_FK foreign key(skolaNumer) references Skolar(skolaNumer)
);


-- -----------------------------------------------------
-- 						Brautir
-- -----------------------------------------------------
create table Brautir 
(
  brautarNumer int(11) not null auto_increment,
  heitiBrautar varchar(75) null default null,
  tilheyrir int(11) not null,
  constraint braut_PK primary key(brautarNumer),
  constraint braut_undirskoli_FK foreign key(tilheyrir) references Undirskolar(undirskolaNumer)
);


-- -----------------------------------------------------
-- 						AfangarBrauta
-- -----------------------------------------------------
create table AfangaFrambod
(
  brautarNumer int(11) not null,
  afangaNumer char(15) not null,
  onnAfanga tinyint null default null,
  skylda boolean default True,
  constraint afangar_brauta_PK primary key(brautarNumer, afangaNumer),
  constraint frambod_afangi_FK foreign key (afangaNumer) references Afangar (afangaNumer),
  constraint frambod_namsleid_FK foreign key (brautarNumer) references Brautir(brautarNumer)
);


-- -----------------------------------------------------
-- 						Undanfarar
-- -----------------------------------------------------
create table Undanfarar 
(
  undanfaraNumer char(15) not null,
  afangaNumer char(15) not null,
  tegund char(1) null default '1',	-- 1 = undanfari, 2 = má taka með, 3 = verður að taka með.
  primary key (afangaNumer, undanfaraNumer),
  constraint afangi_afangi_FK foreign key (afangaNumer) references Afangar(afangaNumer),
  constraint undanfari_afangi_FK foreign key (undanfaraNumer) references Afangar(afangaNumer)
);
