# Metodologia e validação

## Cálculo do índice

`ICM = 0,7 × IP + 0,3 × IC`, conforme parâmetros da planilha tratada. O resultado aumenta com a piora da condição.

| Classe | Intervalo ICM |
|---|---|
| Bom | ICM < 30 |
| Regular | 30 <= ICM < 50 |
| Ruim | 50 <= ICM < 70 |
| Péssimo | ICM >= 70 |

## Cuidados de agregação

O percentual de extensão por classe deve usar a soma de `Extensão segmento (km)` no contexto filtrado. Verificar se o percentual crítico considera Ruim + Péssimo e se usa extensão ou contagem de segmentos. A média ICM pode ser simples ou ponderada; confirmar no DAX do PBIX antes de documentar como definitiva.

## Checklist de validação

1. Conferir quantidade de registros brutos, tratados e removidos no log.
2. Verificar tipos de dados, nulos, duplicidades por `SegmentoID` e mês e datas inválidas.
3. Conferir extensões positivas e limites contratuais.
4. Verificar pesos, classes e arredondamento de ICM.
5. Verificar comparações mensais para o mesmo conjunto de segmentos.
6. Confirmar filtros, medidas DAX e relacionamento de calendário.
7. Validar mapa, latitudes, longitudes e privacidade das fontes.
8. Confrontar cartões e tabela do painel com os resultados sob os mesmos filtros.

## Pontos de atenção na captura

O painel de junho de 2026 apresenta ICM médio 37,38 e 29,4% crítico. A evolução mostra CT-01/2025: 14,48 atual, 14,58 anterior, -0,09 de variação; CT-02/2025: 53,73 atual, 47,25 anterior, 6,49 de variação. Diferenças de 0,01 podem decorrer de arredondamento de valores subjacentes.
