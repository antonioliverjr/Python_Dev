create schema `movies_controll` default character set utf8mb4 ;

create table movies_controll.types(
	id int primary key auto_increment,
    type_name varchar(15) not null
);

create table movies_controll.movies(
	id int primary key auto_increment,
    type int not null,
    name varchar(30) not null,
    total_ep int null,
    atual_ep int null,
    last_view date default(current_date),
    foreign key (type) references types(id)
);

insert into movies_controll.types (type_name) values('Serie');
insert into movies_controll.types (type_name) values('Filme');

insert into movies_controll.movies (type,name,total_ep,atual_ep)
values(1, 'Friends', 10, 1);

insert into movies_controll.movies (type,name)
values(2, 'Avengers');

update movies_controll.movies set last_view = '2022-02-28' where id=1;

insert into movies_controll.movies (type,name,total_ep,atual_ep)
values(1, 'Todo mundo odeia o Cris', 20, 1);

insert into movies_controll.movies (type,name)
values(2, '1917');

insert into movies_controll.movies (type,name)
values(2, '300');

delete from movies_controll.movies where id=4;

insert into movies_controll.movies (type,name)
values(2, '1917');

