-- Importação para Tabela Cadastro (1 CSV)
COPY Cadastro (
    Registro_ANS, 
    CNPJ, 
    Razao_Social, 
    Nome_Fantasia, 
    Logradouro, 
    Numero, 
    Complemento, 
    Bairro, 
    Cidade, 
    UF, 
    CEP, 
    DDO, 
    Telefone, 
    Fax, 
    Endereco_eletronico, 
    Representante, 
    Cargo_Representante, 
    Regiao_de_Comercializacao, 
    Data_Registro_ANS
)
FROM '/caminho/para/arquivo/cadastro.csv'
WITH (
    FORMAT csv,
    ENCODING 'UTF8',
    HEADER TRUE,
    DELIMITER ';'
);

-- Importação para Tabela Financeiro (8 CSVs semestrais)
-- Função para importar múltiplos arquivos com prefixo
CREATE OR REPLACE FUNCTION importar_financeiro()
RETURNS VOID AS $$
DECLARE
    arquivos TEXT[] := ARRAY[
        '/caminho/para/financeiro_semestre1.csv',
        '/caminho/para/financeiro_semestre2.csv',
        '/caminho/para/financeiro_semestre3.csv',
        '/caminho/para/financeiro_semestre4.csv',
        '/caminho/para/financeiro_semestre5.csv',
        '/caminho/para/financeiro_semestre6.csv',
        '/caminho/para/financeiro_semestre7.csv',
        '/caminho/para/financeiro_semestre8.csv'
    ];
    arquivo TEXT;
BEGIN
    FOREACH arquivo IN ARRAY arquivos LOOP
        COPY Financeiro (
            DATA, 
            REG_ANS, 
            CD_CONTA_CONTABIL, 
            DESCRICAO, 
            VL_SALDO_INICIAL, 
            VL_SALDO_FINAL
        )
        FROM arquivo
        WITH (
            FORMAT csv,
            ENCODING 'UTF8',
            HEADER TRUE,
            DELIMITER ';'
        );
    END LOOP;
END;
$$ LANGUAGE plpgsql;

-- Chamada da função para importação
SELECT importar_financeiro();
