alter table publicacao_gs
   add constraint fk_usuario_publicacao
      foreign key ( id_usuario )
         references usuario_gs ( id );

alter table comentario_gs
   add constraint fk_usuario_comentario
      foreign key ( id_usuario )
         references usuario_gs ( id );

alter table comentario_gs
   add constraint fk_publicacao_comentario
      foreign key ( id_publicacao )
         references publicacao_gs ( id );

alter table area_risco_gs
   add constraint fk_usuario_area_risco
      foreign key ( id_usuario )
         references usuario_gs ( id );

alter table jogo_gs
   add constraint fk_usuario_jogo
      foreign key ( id_usuario )
         references usuario_gs ( id );