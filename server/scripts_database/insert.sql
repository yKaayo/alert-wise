-- usuario_gs
insert into usuario_gs (
   id,
   nome,
   email,
   senha
) values ( id_usuario.nextval,
           'Ana',
           'ana@gmail.com',
           '123' );

commit;
insert into usuario_gs (
   id,
   nome,
   email,
   senha
) values ( id_usuario.nextval,
           'Caio',
           'caio@gmail.com',
           '123' );

commit;
insert into usuario_gs (
   id,
   nome,
   email,
   senha
) values ( id_usuario.nextval,
           'Kevyn',
           'kevyn@gmail.com',
           '123' );

commit;
insert into usuario_gs (
   id,
   nome,
   email,
   senha
) values ( id_usuario.nextval,
           'Lucas',
           'lucas@gmail.com',
           '123' );

commit;
insert into usuario_gs (
   id,
   nome,
   email,
   senha
) values ( id_usuario.nextval,
           'Genésio',
           'genesio@gmail.com',
           '123' );

commit;
-- usuario_gs - Fim

-- publicacao_gs
insert into publicacao_gs (
   id,
   conteudo,
   data_publicacao,
   id_usuario
) values ( id_publicacao.nextval,
           'O nível do rio Itajaí-Açu subiu 12 metros em 24h, deixando centenas de desabrigados. A Defesa Civil trabalha no resgate de famílias isoladas.'
           ,
           current_date,
           1 );

commit;
insert into publicacao_gs (
   id,
   conteudo,
   data_publicacao,
   id_usuario
) values ( id_publicacao.nextval,
           'Terremoto de 6.7 graus atingiu o norte do Chile hoje de madrugada. Até o momento foram registrados danos em edificações antigas, mas sem vítimas fatais.'
           ,
           current_date,
           2 );

commit;
insert into publicacao_gs (
   id,
   conteudo,
   data_publicacao,
   id_usuario
) values ( id_publicacao.nextval,
           'Furacão Maria segue em direção às Pequenas Antilhas com ventos de 220km/h. Autoridades locais já iniciaram evacuação de áreas costeiras.'
           ,
           current_date,
           3 );

commit;
insert into publicacao_gs (
   id,
   conteudo,
   data_publicacao,
   id_usuario
) values ( id_publicacao.nextval,
           '6º ano consecutivo de seca extrema no sertão da Bahia. Reservatórios estão com apenas 8% da capacidade e agricultores perderam toda a safra.'
           ,
           current_date,
           4 );

commit;
insert into publicacao_gs (
   id,
   conteudo,
   data_publicacao,
   id_usuario
) values ( id_publicacao.nextval,
           'Incêndios florestais já consumiram mais de 500 mil hectares no sul da Austrália. Fumaça atinge Sydney e qualidade do ar está crítica.'
           ,
           current_date,
           5 );

commit;
-- publicacao_gs - Fim

-- comentario_gs
insert into comentario_gs (
   id,
   conteudo,
   data_comentario,
   id_usuario,
   id_publicacao
) values ( id_comentario.nextval,
           'Ótima observação sobre essa área de risco! A prefeitura deveria tomar providências.',
           current_date,
           1,
           1 );

commit;
insert into comentario_gs (
   id,
   conteudo,
   data_comentario,
   id_usuario,
   id_publicacao
) values ( id_comentario.nextval,
           'Parabéns pela pontuação alta! Alguma dica para melhorar meu desempenho?',
           current_date,
           2,
           2 );

commit;
insert into comentario_gs (
   id,
   conteudo,
   data_comentario,
   id_usuario,
   id_publicacao
) values ( id_comentario.nextval,
           'Essa informação é crucial para nossa comunidade. Obrigado por compartilhar!',
           current_date,
           3,
           3 );

commit;
insert into comentario_gs (
   id,
   conteudo,
   data_comentario,
   id_usuario,
   id_publicacao
) values ( id_comentario.nextval,
           'Você poderia informar quando essa situação foi registrada?',
           current_date,
           4,
           1 );

commit;
insert into comentario_gs (
   id,
   conteudo,
   data_comentario,
   id_usuario,
   id_publicacao
) values ( id_comentario.nextval,
           'Muito útil essa publicação, me ajudou a identificar um risco perto de casa!',
           current_date,
           5,
           4 );

commit;
-- comentario_gs - Fim

-- area_risco_gs
insert into area_risco_gs (
   id,
   endereco,
   tipo_risco,
   data,
   id_usuario
) values ( 1,
           'Rua das Encostas, 123 - Morro Alto',
           'Deslizamento',
           to_date('2023-05-15','YYYY-MM-DD'),
           1 );

commit;
insert into area_risco_gs (
   id,
   endereco,
   tipo_risco,
   data,
   id_usuario
) values ( 2,
           'Avenida Rio Grande, 456 - Centro',
           'Inundação',
           to_date('2023-06-20','YYYY-MM-DD'),
           2 );

commit;
insert into area_risco_gs (
   id,
   endereco,
   tipo_risco,
   data,
   id_usuario
) values ( 3,
           'Praça da Matriz, s/n - Centro Histórico',
           'Estrutural',
           to_date('2023-07-10','YYYY-MM-DD'),
           3 );

commit;
insert into area_risco_gs (
   id,
   endereco,
   tipo_risco,
   data,
   id_usuario
) values ( 4,
           'Rua das Flores, 789 - Jardim Primavera',
           'Incêndio',
           to_date('2023-08-05','YYYY-MM-DD'),
           4 );

commit;
insert into area_risco_gs (
   id,
   endereco,
   tipo_risco,
   data,
   id_usuario
) values ( 5,
           'Travessa da Ladeira, 321 - Vila Esperança',
           'Desabamento',
           to_date('2023-09-12','YYYY-MM-DD'),
           5 );

commit;
-- area_risco_gs - Fim

-- jogo_gs
insert into jogo_gs (
   id,
   pontos,
   id_usuario
) values ( id_jogo.nextval,
           1,
           1 );

commit;
insert into jogo_gs (
   id,
   pontos,
   id_usuario
) values ( id_jogo.nextval,
           2,
           2 );

commit;
insert into jogo_gs (
   id,
   pontos,
   id_usuario
) values ( id_jogo.nextval,
           1,
           3 );

commit;
insert into jogo_gs (
   id,
   pontos,
   id_usuario
) values ( id_jogo.nextval,
           2,
           4 );

commit;
insert into jogo_gs (
   id,
   pontos,
   id_usuario
) values ( id_jogo.nextval,
           3,
           5 );

commit;
-- jogo_gs - Fim