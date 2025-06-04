create sequence id_usuario;
create sequence id_publicacao;

create table usuario_gs (
   id          int primary key not null,
   nome        varchar(30) not null,
   email       varchar(45) not null,
   local_atual varchar(45) not null
)

create table publicacao_gs (
   id              int primary key not null,
   titulo          varchar(30) not null,
   conteudo        text not null,
   data_publicacao datetime not null,
   id_usuario      int
)

alter table publicacao_gs
   add constraint fk_usuario_publicacao foreign key ( id_usuario )
      references usuario_gs ( id_usuario )

create table comentario_gs (
   id              int primary key not null,
   conteudo        text not null,
   data_comentario datetime not null,
   id_usuario      int,
   id_publicacao   int
)

alter table comentario_gs
   add constraint fk_usuario_comentario foreign key ( id_usuario )
      references usuario_gs ( id_usuario )

alter table comentario_gs
   add constraint fk_publicacao_comentario foreign key ( id_publicacao )
      references publicacao_gs ( id_publicacao )

create table area_risco_gs (
   id         int primary key not null,
   endereco   varchar(50) not null,
   tipo_risco varchar(30) not null,
   date       datetime not null,
   id_usuario int
)

alter table area_risco_gs
   add constraint fk_usuario_area_risco foreign key ( id_usuario )
      references usuario_gs ( id_usuario )

create table jogo_gs (
   id     int primary key not null,
   pontos int not NULL,
   id_usuario int
)

alter table jogo_gs
   add constraint fk_usuario_jogo foreign key ( id_usuario )
      references usuario_gs ( id_usuario )