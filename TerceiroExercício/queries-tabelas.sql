-- Criação da tabela de Cadastro
CREATE TABLE Cadastro (
    Registro_ANS INT64 PRIMARY KEY NOT NULL,
    CNPJ INT64 NOT NULL,
    Razao_Social VARCHAR(255),
    Nome_Fantasia VARCHAR(255),
    Logradouro VARCHAR(255),
    Numero VARCHAR(50),
    Complemento VARCHAR(100),
    Bairro VARCHAR(100),
    Cidade VARCHAR(100),
    UF VARCHAR(2),
    CEP INT64,
    DDO FLOAT64,
    Telefone FLOAT64,
    Fax VARCHAR(50),
    Endereco_eletronico VARCHAR(255),
    Representante VARCHAR(255),
    Cargo_Representante VARCHAR(255),
    Regiao_de_Comercializacao FLOAT64,
    Data_Registro_ANS DATE
);

-- Criação da tabela Financeiro 
CREATE TABLE Financeiro (
    ID SERIAL PRIMARY KEY,
    DATA DATE,
    REG_ANS INT64 NOT NULL,
    CD_CONTA_CONTABIL INT64,
    DESCRICAO VARCHAR(255),
    VL_SALDO_INICIAL DECIMAL(18,2),
    VL_SALDO_FINAL DECIMAL(18,2),
    FOREIGN KEY (REG_ANS) REFERENCES Cadastro(Registro_ANS)
);