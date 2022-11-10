/*==============================================================*/
/* DBMS name:      Sybase SQL Anywhere 12                       */
/* Created on:     10-11-2022 18:42:43                          */
/*==============================================================*/


if exists(select 1 from sys.sysforeignkey where role='FK_ANSWERS_RELATIONS_QUESTION') then
    alter table ANSWERS
       delete foreign key FK_ANSWERS_RELATIONS_QUESTION
end if;

if exists(select 1 from sys.sysforeignkey where role='FK_POLL_RELATIONS_USERS') then
    alter table POLL
       delete foreign key FK_POLL_RELATIONS_USERS
end if;

if exists(select 1 from sys.sysforeignkey where role='FK_POLL_RELATIONS_TESTS') then
    alter table POLL
       delete foreign key FK_POLL_RELATIONS_TESTS
end if;

if exists(select 1 from sys.sysforeignkey where role='FK_POLL_RELATIONS_PATIENTS') then
    alter table POLL
       delete foreign key FK_POLL_RELATIONS_PATIENTS
end if;

if exists(select 1 from sys.sysforeignkey where role='FK_QUESTION_RELATIONS_TESTS') then
    alter table QUESTIONS
       delete foreign key FK_QUESTION_RELATIONS_TESTS
end if;

drop index if exists ANSWERS.ANSWERS_PK;

drop table if exists ANSWERS;

drop index if exists PATIENTS.RELATIONSHIP_6_FK;

drop index if exists PATIENTS.RELATIONSHIP_1_FK;

drop index if exists PATIENTS.PATIENTS_PK;

drop table if exists PATIENTS;

drop index if exists POLL.RELATIONSHIP_5_FK;

drop index if exists POLL.POLL_PK;

drop table if exists POLL;

drop index if exists QUESTIONS.RELATIONSHIP_7_FK;

drop index if exists QUESTIONS.QUESTIONS_PK;

drop table if exists QUESTIONS;

drop index if exists TESTS.RELATIONSHIP_2_FK;

drop index if exists TESTS.TESTS_PK;

drop table if exists TESTS;

drop index if exists USERS.USERS_PK;

drop table if exists USERS;

/*==============================================================*/
/* Table: ANSWERS                                               */
/*==============================================================*/
create table ANSWERS 
(
   IDANSWER             integer                        not null,
   IDQUESTION           integer                        null,
   POINTS               integer                        null,
   TEXT                 char(100)                      null,
   OBSERVATIONS         char(100)                      null,
   constraint PK_ANSWERS primary key (IDANSWER)
);

/*==============================================================*/
/* Index: ANSWERS_PK                                            */
/*==============================================================*/
create unique index ANSWERS_PK on ANSWERS (
IDANSWER ASC
);

/*==============================================================*/
/* Table: PATIENTS                                              */
/*==============================================================*/
create table PATIENTS 
(
   IDPATIENT            char(10)                       not null,
   RUN                  integer                        null,
   DV                   char(50)                       null,
   FATHER_NAME          char(50)                       null,
   MOTHER_NAME          char(50)                       null,
   GENDER               char(20)                       null,
   BIRTHDAY             char(50)                       null,
   OBSERVATIONS         char(100)                      null,
   DELETED_AT           char(50)                       null,
   constraint PK_PATIENTS primary key (IDPATIENT)
);

/*==============================================================*/
/* Index: PATIENTS_PK                                           */
/*==============================================================*/
create unique index PATIENTS_PK on PATIENTS (
IDPATIENT ASC
);

/*==============================================================*/
/* Index: RELATIONSHIP_1_FK                                     */
/*==============================================================*/
create index RELATIONSHIP_1_FK on PATIENTS (
IDUSER ASC
);

/*==============================================================*/
/* Index: RELATIONSHIP_6_FK                                     */
/*==============================================================*/
create index RELATIONSHIP_6_FK on PATIENTS (
IDPATIENT ASC
);

/*==============================================================*/
/* Table: POLL                                                  */
/*==============================================================*/
create table POLL 
(
   IDPOLL               integer                        not null,
   IDTEST               integer                        null,
   IDPATIENT            char(10)                       null,
   IDUSER               integer                        null,
   RESULT               integer                        null,
   constraint PK_POLL primary key (IDPOLL)
);

/*==============================================================*/
/* Index: POLL_PK                                               */
/*==============================================================*/
create unique index POLL_PK on POLL (
IDPOLL ASC
);

/*==============================================================*/
/* Index: RELATIONSHIP_5_FK                                     */
/*==============================================================*/
create index RELATIONSHIP_5_FK on POLL (
IDTEST ASC
);

/*==============================================================*/
/* Table: QUESTIONS                                             */
/*==============================================================*/
create table QUESTIONS 
(
   IDQUESTION           integer                        not null,
   IDTEST               integer                        null,
   QUESTIONS            char(100)                      null,
   DESCRIPTIONS         char(10)                       null,
   DELETED_AT           char(50)                       null,
   constraint PK_QUESTIONS primary key (IDQUESTION)
);

/*==============================================================*/
/* Index: QUESTIONS_PK                                          */
/*==============================================================*/
create unique index QUESTIONS_PK on QUESTIONS (
IDQUESTION ASC
);

/*==============================================================*/
/* Index: RELATIONSHIP_7_FK                                     */
/*==============================================================*/
create index RELATIONSHIP_7_FK on QUESTIONS (
IDQUESTION ASC
);

/*==============================================================*/
/* Table: TESTS                                                 */
/*==============================================================*/
create table TESTS 
(
   IDTEST               integer                        not null,
   NAME                 char(50)                       null,
   CUT_POINT            integer                        null,
   MAX_POINT            integer                        null,
   OBSERVATIONS         char(100)                      null,
   constraint PK_TESTS primary key (IDTEST)
);

/*==============================================================*/
/* Index: TESTS_PK                                              */
/*==============================================================*/
create unique index TESTS_PK on TESTS (
IDTEST ASC
);

/*==============================================================*/
/* Index: RELATIONSHIP_2_FK                                     */
/*==============================================================*/
create index RELATIONSHIP_2_FK on TESTS (
IDTEST ASC
);

/*==============================================================*/
/* Table: USERS                                                 */
/*==============================================================*/
create table USERS 
(
   IDUSER               integer                        not null,
   RUN                  integer                        null,
   DV                   char(50)                       null,
   FATHER_NAME          char(50)                       null,
   MOTHER_NAME          char(50)                       null,
   GENDER               char(20)                       null,
   BIRTHDAY             char(50)                       null,
   PASSWORD             varchar(50)                    null,
   EMAIL                char(50)                       null,
   DELETED_AT           char(50)                       null,
   constraint PK_USERS primary key (IDUSER)
);

/*==============================================================*/
/* Index: USERS_PK                                              */
/*==============================================================*/
create unique index USERS_PK on USERS (
IDUSER ASC
);

alter table ANSWERS
   add constraint FK_ANSWERS_RELATIONS_QUESTION foreign key (IDQUESTION)
      references QUESTIONS (IDQUESTION)
      on update restrict
      on delete restrict;

alter table POLL
   add constraint FK_POLL_RELATIONS_USERS foreign key (IDUSER)
      references USERS (IDUSER)
      on update restrict
      on delete restrict;

alter table POLL
   add constraint FK_POLL_RELATIONS_TESTS foreign key (IDTEST)
      references TESTS (IDTEST)
      on update restrict
      on delete restrict;

alter table POLL
   add constraint FK_POLL_RELATIONS_PATIENTS foreign key (IDPATIENT)
      references PATIENTS (IDPATIENT)
      on update restrict
      on delete restrict;

alter table QUESTIONS
   add constraint FK_QUESTION_RELATIONS_TESTS foreign key (IDTEST)
      references TESTS (IDTEST)
      on update restrict
      on delete restrict;

