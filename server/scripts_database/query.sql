-- 1. Listar as publicações com o nome, conteúdo e data de publicação ordenando pela data mais recente
select usuario_gs.nome as nome,
       publicacao_gs.conteudo as texto,
       publicacao_gs.data_publicacao as data_de_publicacao
  from usuario_gs
  left join publicacao_gs
on usuario_gs.id = publicacao_gs.id_usuario
 order by publicacao_gs.data_publicacao desc;

-- 2. Listar os usuários com o nome, email e a quantidade total de pontos no jogo e ordenando por quem tem mais pontos
select usuario_gs.nome as usuarios,
       usuario_gs.email as email,
       sum(jogo_gs.pontos) as pontos_totais
  from usuario_gs
  left join jogo_gs
on usuario_gs.id = jogo_gs.id_usuario
 group by usuario_gs.id,
          usuario_gs.nome,
          usuario_gs.email
 order by 3 desc;

-- 3. Listar as publicações com o nome do autor, conteúdo e a quantidade total de comentários, ordenando pela quantidade de comentários
select usuario_gs.nome as autor,
       publicacao_gs.conteudo as publicacao,
       count(comentario_gs.id) as total_comentarios
  from publicacao_gs
  join usuario_gs
on publicacao_gs.id_usuario = usuario_gs.id
  left join comentario_gs
on publicacao_gs.id = comentario_gs.id_publicacao
 group by usuario_gs.nome,
          publicacao_gs.conteudo
 order by total_comentarios desc;

-- 4. Calcula a média de pontos dos usuários em um jogo e filtrando apenas aqueles com média superior a 1 pontos
select usuario_gs.nome as nome,
       avg(jogo_gs.pontos) as media_de_pontos
  from jogo_gs
  join usuario_gs
on jogo_gs.id_usuario = usuario_gs.id
 group by usuario_gs.nome
having avg(jogo_gs.pontos) > 1
 order by media_de_pontos desc;

-- 5. Listar todos os comentários com o nome do autor, conteúdo e a data do comentário, ordenando pela data mais recente
select usuario_gs.nome as autor,
       comentario_gs.conteudo as comentario,
       comentario_gs.data_comentario as data
  from comentario_gs
  join usuario_gs
on comentario_gs.id_usuario = usuario_gs.id
 order by comentario_gs.data_comentario desc;