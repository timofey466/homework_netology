create table if not exists songer(
id serial primary key,
title varchar(40) unique
);

CREATE TABLE IF NOT EXISTS songer_alb(
	Id serial PRIMARY KEY , 
	alb_id integer REFERENCES albom(Id),
	songer_id integer REFERENCES songer(Id)
);

create table if not exists albom(
  Id serial primary key,
  title varchar(40) not null ,
  years integer not null
);

create table if not exists song(
  second_id integer references albom(Id),
  Id serial primary key,
  title varchar(40) not null ,
  times numeric 
);

create table if not exists generals (
  Id serial primary key,
  title varchar(30) not null
);

CREATE TABLE IF NOT EXISTS gen_songer(
	Id serial PRIMARY KEY,
	songer_id integer REFERENCES songer(Id) ,
	general_id integer REFERENCES generals(Id)
);

CREATE TABLE IF NOT EXISTS songer_alb(
	Id serial PRIMARY KEY , 
	alb_id integer REFERENCES albom(Id),
	songer_id integer REFERENCES songer(Id)
);

CREATE TABLE IF NOT EXISTS playlist(
	Id serial PRIMARY KEY,
	title varchar(40) NOT NULL ,
	year_old integer NOT NULL
	);

CREATE TABLE IF NOT EXISTS song_in_playlist(
	Id serial PRIMARY KEY,
	song_id integer REFERENCES song(Id),
	playlist integer REFERENCES playlist(Id)
	);



















































