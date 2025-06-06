-- Sequencies
create sequence id_usuario;
create sequence id_publicacao;
create sequence id_comentario;
create sequence id_area_risco;
create sequence id_jogo;

-- Tables
create table usuario_gs (
   id    int primary key not null,
   nome  varchar(30) not null,
   email varchar(45) not null,
   senha varchar(60) not null
);

create table publicacao_gs (
   id              int primary key not null,
   titulo          varchar(30) not null,
   conteudo        varchar(90) not null,
   data_publicacao date not null,
   id_usuario      int
);
-- publicacao_gs
insert into publicacao_gs (id, titulo, conteudo, data_publicacao, id_usuario) values ( id_publicacao.nextval, 1, 1 ); commit;
insert into publicacao_gs (id, titulo, conteudo, data_publicacao, id_usuario) values ( id_publicacao.nextval, 2, 2 ); commit;
insert into publicacao_gs (id, titulo, conteudo, data_publicacao, id_usuario) values ( id_publicacao.nextval, 1, 3 ); commit;
insert into publicacao_gs (id, titulo, conteudo, data_publicacao, id_usuario) values ( id_publicacao.nextval, 2, 4 ); commit;
insert into publicacao_gs (id, titulo, conteudo, data_publicacao, id_usuario) values ( id_publicacao.nextval, 3, 5 ); commit;

create table comentario_gs (
   id              int primary key not null,
   conteudo        varchar(90) not null,
   data_comentario date not null,
   id_usuario      int,
   id_publicacao   int
);

create table area_risco_gs (
   id         int primary key not null,
   endereco   varchar(50) not null,
   tipo_risco varchar(30) not null,
   data       date not null,
   id_usuario int
);

create table jogo_gs (
   id         int primary key not null,
   pontos     int not null,
   id_usuario int
);

-- Alters Table
alter table publicacao_gs
   add constraint fk_usuario_publicacao foreign key ( id_usuario )
      references usuario_gs ( id )

alter table comentario_gs
   add constraint fk_usuario_comentario foreign key ( id_usuario )
      references usuario_gs ( id )

alter table comentario_gs
   add constraint fk_publicacao_comentario foreign key ( id_publicacao )
      references publicacao_gs ( id )

alter table area_risco_gs
   add constraint fk_usuario_area_risco foreign key ( id_usuario )
      references usuario_gs ( id )

alter table jogo_gs
   add constraint fk_usuario_jogo foreign key ( id_usuario )
      references usuario_gs ( id )

-- Inserts
-- usuario_gs
insert into usuario_gs (id, nome, email, senha) values ( id_usuario.nextval, 'Ana', 'ana@gmail.com', '123' ); commit;
insert into usuario_gs (id, nome, email, senha) values ( id_usuario.nextval, 'Caio', 'caio@gmail.com', '123' ); commit;
insert into usuario_gs (id, nome, email, senha) values ( id_usuario.nextval, 'Kevyn', 'kevyn@gmail.com', '123' ); commit;
insert into usuario_gs (id, nome, email, senha) values ( id_usuario.nextval, 'Lucas', 'lucas@gmail.com', '123' ); commit;
insert into usuario_gs (id, nome, email, senha) values ( id_usuario.nextval, 'Genésio', 'genesio@gmail.com', '123' ); commit;



-- comentario_gs
-- area_risco_gs
-- jogo_gs
insert into jogo_gs (id, pontos, id_usuario) values ( id_jogo.nextval, 1, 1 ); commit;
insert into jogo_gs (id, pontos, id_usuario) values ( id_jogo.nextval, 2, 2 ); commit;
insert into jogo_gs (id, pontos, id_usuario) values ( id_jogo.nextval, 1, 3 ); commit;
insert into jogo_gs (id, pontos, id_usuario) values ( id_jogo.nextval, 2, 4 ); commit;
insert into jogo_gs (id, pontos, id_usuario) values ( id_jogo.nextval, 3, 5 ); commit;

-- Consultas


drop sequence id_usuario;
drop sequence id_publicacao;
drop sequence id_comentario;
drop sequence id_area_risco;
drop sequence id_jogo;

DROP TABLE jogo_gs;
DROP TABLE area_risco_gs;
DROP TABLE comentario_gs;
DROP TABLE publicacao_gs;
DROP TABLE usuario_gs;
