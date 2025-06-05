create sequence id_usuario;
create sequence id_publicacao;

create table usuario_gs (
   id          int primary key not null,
   nome        varchar(30) not null,
   email       varchar(45) not null,
   senha    varchar(45) not null
);

create table publicacao_gs (
   id              int primary key not null,
   titulo          varchar(30) not null,
   conteudo        varchar(90) not null,
   data_publicacao date not null,
   id_usuario      int
);

alter table publicacao_gs
   add constraint fk_usuario_publicacao foreign key ( id_usuario )
      references usuario_gs ( id )

create table comentario_gs (
   id              int primary key not null,
   conteudo        varchar(90) not null,
   data_comentario date not null,
   id_usuario      int,
   id_publicacao   int
);

alter table comentario_gs
   add constraint fk_usuario_comentario foreign key ( id_usuario )
      references usuario_gs ( id )

alter table comentario_gs
   add constraint fk_publicacao_comentario foreign key ( id_publicacao )
      references publicacao_gs ( id )

create table area_risco_gs (
   id         int primary key not null,
   endereco   varchar(50) not null,
   tipo_risco varchar(30) not null,
   data       date not null,
   id_usuario int
);

alter table area_risco_gs
   add constraint fk_usuario_area_risco foreign key ( id_usuario )
      references usuario_gs ( id )

create table jogo_gs (
   id         int primary key not null,
   pontos     int not null,
   id_usuario int
);

alter table jogo_gs
   add constraint fk_usuario_jogo foreign key ( id_usuario )
      references usuario_gs ( id )

DROP SEQUENCE id_usuario;
DROP SEQUENCE id_publicacao;

-- DROP TABLE jogo_gs;
-- DROP TABLE area_risco_gs;
-- DROP TABLE comentario_gs;
-- DROP TABLE publicacao_gs;
-- DROP TABLE usuario_gs;

SELECT * FROM usuario_gs;