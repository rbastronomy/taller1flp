/*==============================================================*/
/* DBMS name:      ORACLE Version 11g                           */
/* Created on:     30-10-2022 23:29:53                          */
/*==============================================================*/
/*==============================================================*/
/* Table: PERSONAS                                              */
/*==============================================================*/
create table PERSONAS 
(
   RUN                  INTEGER              not null,
   NAME                 CHAR(50)             not null,
   LAST_NAME            CHAR(50)             not null,
   ADRESS               CHAR(100)            not null,
   PHONE                INTEGER              not null,
   EMAIL                CHAR(100)            not null,
   constraint AK_IDENTIFIER_1_PERSONAS unique (RUN)
);

/*==============================================================*/
/* Table: PREGUNTAS                                             */
/*==============================================================*/
create table PREGUNTAS 
(
   IDPREGUNTAS          INTEGER              not null,
   DES                  CHAR(100)            not null,
   VAL                  INTEGER              not null,
   constraint PK_PREGUNTAS primary key (IDPREGUNTAS)
);

/*==============================================================*/
/* Table: RELATIONSHIP_1                                        */
/*==============================================================*/
create table RELATIONSHIP_1 
(
   RUN                  INTEGER              not null,
   IDPREGUNTAS          INTEGER              not null,
   RESPUESTA            INTEGER              not null,
   constraint PK_RELATIONSHIP_1 primary key (RUN, IDPREGUNTAS)
);

/*==============================================================*/
/* Index: RELATIONSHIP_3_FK                                     */
/*==============================================================*/
create index RELATIONSHIP_3_FK on RELATIONSHIP_1 (
   RUN ASC
);

/*==============================================================*/
/* Index: RELATIONSHIP_2_FK                                     */
/*==============================================================*/
create index RELATIONSHIP_2_FK on RELATIONSHIP_1 (
   IDPREGUNTAS ASC
);

alter table RELATIONSHIP_1
   add constraint FK_RELATION_RELATIONS_PREGUNTA foreign key (IDPREGUNTAS)
      references PREGUNTAS (IDPREGUNTAS);

alter table RELATIONSHIP_1
   add constraint FK_RELATION_RELATIONS_PERSONAS foreign key (RUN)
      references PERSONAS (RUN);

