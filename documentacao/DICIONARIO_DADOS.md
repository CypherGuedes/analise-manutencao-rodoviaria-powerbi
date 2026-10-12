# Dicionário de dados

## LEVANTAMENTOS e LEVANTAMENTOS_TRATADOS

- `Contrato`: identificador contratual.
- `Rodovia`: código da rodovia.
- `Sentido`: direção da pista ou sentido único.
- `km inicial`, `km final`: limites do segmento.
- `Data do levantamento`: data da vistoria.
- `Panelas`, `Remendos`, `Trincamento`, `Roçada`, `Drenagem`, `Sinalização`: avaliações qualitativas dos itens observados.
- `IP`: índice de pavimentação.
- `IC`: índice de conservação.
- `Latitude`, `Longitude`: coordenadas geográficas do segmento.
- `SegmentoID`: chave de identificação do segmento na base tratada.
- `Mês referência`: período mensal da observação.
- `Extensão segmento (km)`: diferença entre km final e km inicial.
- `ICM`: índice combinado na base tratada.
- `Classificação ICM`: Bom, Regular, Ruim ou Péssimo.

## CONTRATOS

`Contrato`, `Empresa`, `Rodovia`, `km inicial`, `km final`, `Pista`, `Extensão contratual (km)`.

## PARAMETROS_ICM

Registra os pesos dos índices e os intervalos de classificação. Fonte de verdade para revisão de regras de negócio.

## LOG_TRATAMENTO

Registro de verificações e correções aplicadas durante o tratamento. Consulte a aba correspondente para rastreabilidade.
