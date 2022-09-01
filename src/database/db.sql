CREATE TABLE IF NOT EXISTS clientes(
    nome CHAR(50) NOT NULL,
    telefone VARCHAR(15) NOT NULL,
    negocio VARCHAR(50),
    email VARCHAR(50),
    mensagem VARCHAR(200),
    PRIMARY KEY('telefone')
);

