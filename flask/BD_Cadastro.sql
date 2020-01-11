--criando database
IF  NOT EXISTS (SELECT * FROM sys.databases WHERE name = N'SICAD')
    BEGIN
        CREATE DATABASE SICAD
    END;
GO

use SICAD --usar a base de dados criada
GO

-- criando a tabela alunos
if not exists (select * from INFORMATION_SCHEMA.TABLES
where TABLE_NAME = 'T_ALUNO')
	begin
		create table T_ALUNO
			(
			ID integer identity(1,1) constraint pk_ID_ALUNO primary key,
			NOME varchar(255) not null,
			ENDERECO varchar(255) not null,
			DT_NASC varchar(10) not null,
			GENERO varchar(15) not null,
			OBJ_GRAD varchar(1000) not null,
			EMAIL varchar(100) not null,
			USUARIO varchar(50) not null,
			SENHA varchar(10) not null
			)
	end
GO
