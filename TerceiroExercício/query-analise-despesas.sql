-- Query para as 10 operadoras com maiores despesas no último trimestre
WITH UltimoTrimestre AS (
    SELECT 
        c.Registro_ANS,
        c.Razao_Social,
        SUM(f.VL_SALDO_FINAL) AS Total_Despesas
    FROM Financeiro f
    JOIN Cadastro c ON f.REG_ANS = c.Registro_ANS
    WHERE 
        f.DESCRICAO = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR'
        AND f.DATA >= DATE_TRUNC('quarter', CURRENT_DATE - INTERVAL '1 quarter')
        AND f.DATA < DATE_TRUNC('quarter', CURRENT_DATE)
    GROUP BY 
        c.Registro_ANS, 
        c.Razao_Social
    ORDER BY 
        Total_Despesas DESC
    LIMIT 10
),

-- Query para as 10 operadoras com maiores despesas no último ano
UltimoAno AS (
    SELECT 
        c.Registro_ANS,
        c.Razao_Social,
        SUM(f.VL_SALDO_FINAL) AS Total_Despesas
    FROM Financeiro f
    JOIN Cadastro c ON f.REG_ANS = c.Registro_ANS
    WHERE 
        f.DESCRICAO = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR'
        AND f.DATA >= DATE_TRUNC('year', CURRENT_DATE - INTERVAL '1 year')
        AND f.DATA < DATE_TRUNC('year', CURRENT_DATE)
    GROUP BY 
        c.Registro_ANS, 
        c.Razao_Social
    ORDER BY 
        Total_Despesas DESC
    LIMIT 10
)

-- Resultados
SELECT 
    'Último Trimestre' AS Periodo,
    Registro_ANS,
    Razao_Social,
    Total_Despesas
FROM UltimoTrimestre

UNION ALL

SELECT 
    'Último Ano' AS Periodo,
    Registro_ANS,
    Razao_Social,
    Total_Despesas
FROM UltimoAno
ORDER BY 
    Periodo, 
    Total_Despesas DESC;
