create table usuario_gs (
   id    int primary key not null,
   nome  varchar(30) not null,
   email varchar(45) not null,
   senha varchar(60) not null
);

create table publicacao_gs (
   id              int primary key not null,
   conteudo        varchar(150) not null,
   data_publicacao date not null,
   id_usuario      int
);

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