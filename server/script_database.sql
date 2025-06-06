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
   conteudo        VARCHAR(150) not null,
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

-- Alters Table
alter table publicacao_gs
   add constraint fk_usuario_publicacao foreign key ( id_usuario )
      references usuario_gs ( id );

alter table comentario_gs
   add constraint fk_usuario_comentario foreign key ( id_usuario )
      references usuario_gs ( id );

alter table comentario_gs
   add constraint fk_publicacao_comentario foreign key ( id_publicacao )
      references publicacao_gs ( id );

alter table area_risco_gs
   add constraint fk_usuario_area_risco foreign key ( id_usuario )
      references usuario_gs ( id );

alter table jogo_gs
   add constraint fk_usuario_jogo foreign key ( id_usuario )
      references usuario_gs ( id );

-- Inserts
-- usuario_gs
insert into usuario_gs (id, nome, email, senha) values ( id_usuario.nextval, 'Ana', 'ana@gmail.com', '123' ); commit;
insert into usuario_gs (id, nome, email, senha) values ( id_usuario.nextval, 'Caio', 'caio@gmail.com', '123' ); commit;
insert into usuario_gs (id, nome, email, senha) values ( id_usuario.nextval, 'Kevyn', 'kevyn@gmail.com', '123' ); commit;
insert into usuario_gs (id, nome, email, senha) values ( id_usuario.nextval, 'Lucas', 'lucas@gmail.com', '123' ); commit;
insert into usuario_gs (id, nome, email, senha) values ( id_usuario.nextval, 'Genésio', 'genesio@gmail.com', '123' ); commit;

-- publicacao_gs
insert into publicacao_gs (id, conteudo, data_publicacao, id_usuario) values ( id_publicacao.nextval, 'O nível do rio Itajaí-Açu subiu 12 metros em 24h, deixando centenas de desabrigados. A Defesa Civil trabalha no resgate de famílias isoladas.', CURRENT_DATE, 1); commit;
insert into publicacao_gs (id, conteudo, data_publicacao, id_usuario) values ( id_publicacao.nextval, 'Terremoto de 6.7 graus atingiu o norte do Chile hoje de madrugada. Até o momento foram registrados danos em edificações antigas, mas sem vítimas fatais.', CURRENT_DATE, 2); commit;
insert into publicacao_gs (id, conteudo, data_publicacao, id_usuario) values ( id_publicacao.nextval, 'Furacão Maria segue em direção às Pequenas Antilhas com ventos de 220km/h. Autoridades locais já iniciaram evacuação de áreas costeiras.', CURRENT_DATE, 3); commit;
insert into publicacao_gs (id, conteudo, data_publicacao, id_usuario) values ( id_publicacao.nextval, '6º ano consecutivo de seca extrema no sertão da Bahia. Reservatórios estão com apenas 8% da capacidade e agricultores perderam toda a safra.', CURRENT_DATE, 4); commit;
insert into publicacao_gs (id, conteudo, data_publicacao, id_usuario) values ( id_publicacao.nextval, 'Incêndios florestais já consumiram mais de 500 mil hectares no sul da Austrália. Fumaça atinge Sydney e qualidade do ar está crítica.', CURRENT_DATE, 5); commit;

-- comentario_gs
insert into comentario_gs (id, conteudo, data_comentario, id_usuario, id_publicacao) values ( id_comentario.nextval, 'Incêndios florestais já consumiram mais de 500 mil hectares no sul da Austrália. Fumaça atinge Sydney e qualidade do ar está crítica.', CURRENT_DATE, 5); commit;

-- area_risco_gs

-- jogo_gs
insert into jogo_gs (id, pontos, id_usuario) values ( id_jogo.nextval, 1, 1 ); commit;
insert into jogo_gs (id, pontos, id_usuario) values ( id_jogo.nextval, 2, 2 ); commit;
insert into jogo_gs (id, pontos, id_usuario) values ( id_jogo.nextval, 1, 3 ); commit;
insert into jogo_gs (id, pontos, id_usuario) values ( id_jogo.nextval, 2, 4 ); commit;
insert into jogo_gs (id, pontos, id_usuario) values ( id_jogo.nextval, 3, 5 ); commit;

-- Querys
-- 1. Listar as publicações com o nome, conteúdo e data de publicação ordenando pela data mais recente
SELECT usuario_gs.nome as Nome, publicacao_gs.conteudo as Texto, publicacao_gs.data_publicacao as Data_De_Publicacao FROM usuario_gs
LEFT JOIN publicacao_gs ON usuario_gs.id = publicacao_gs.id_usuario
ORDER BY publicacao_gs.data_publicacao DESC;

-- 2. Listar os usuários com o nome, email e a quantidade total de pontos no jogo e ordenando por quem tem mais pontos
select usuario_gs.nome AS Usuarios, usuario_gs.email AS Email, SUM(jogo_gs.pontos) AS Pontos_Totais
from usuario_gs
LEFT JOIN jogo_gs ON usuario_gs.id = jogo_gs.id_usuario
GROUP BY usuario_gs.id, usuario_gs.nome, usuario_gs.email
ORDER BY 3 DESC;

-- 3. Listar as publicações com o nome do autor, conteúdo e a quantidade total de comentários, ordenando pela quantidade de comentários
SELECT usuario_gs.nome AS Autor, publicacao_gs.conteudo AS Publicacao, 
       COUNT(comentario_gs.id) AS Total_Comentarios
FROM publicacao_gs
JOIN usuario_gs ON publicacao_gs.id_usuario = usuario_gs.id
LEFT JOIN comentario_gs ON publicacao_gs.id = comentario_gs.id_publicacao
GROUP BY usuario_gs.nome, publicacao_gs.conteudo
ORDER BY total_comentarios DESC;

-- 4. Calcula a média de pontos dos usuários em um jogo e filtrando apenas aqueles com média superior a 1 pontos
SELECT usuario_gs.nome AS Nome, AVG(jogo_gs.pontos) AS Media_De_Pontos
FROM jogo_gs
JOIN usuario_gs ON jogo_gs.id_usuario = usuario_gs.id
GROUP BY usuario_gs.nome
HAVING AVG(jogo_gs.pontos) > 1
ORDER BY Media_De_Pontos DESC;

-- 5. Listar todos


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

-- Select
SELECT * FROM usuario_gs;
SELECT * FROM publicacao_gs;
SELECT * FROM jogo_gs;

