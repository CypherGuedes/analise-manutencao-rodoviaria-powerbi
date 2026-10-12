"""Auditoria básica dos CSVs exportados. Executar da raiz: python scripts/auditar_dados.py"""
import csv
from pathlib import Path
from collections import Counter
ROOT=Path(__file__).resolve().parents[1]
path=ROOT/'dados'/'levantamentos-tratados.csv'
with path.open(encoding='utf-8-sig',newline='') as f:rows=list(csv.DictReader(f,delimiter=';'))
print('Registros tratados:',len(rows))
print('Contratos:',dict(Counter(r['Contrato'] for r in rows)))
print('Classes:',dict(Counter(r['Classificação ICM'] for r in rows)))
issues=[]
for i,r in enumerate(rows,2):
 try:
  ini=float(r['km inicial']);fim=float(r['km final']);ip=float(r['IP']);ic=float(r['IC']);icm=float(r['ICM']);ext=float(r['Extensão segmento (km)'])
  if fim<=ini or abs(ext-(fim-ini))>0.001:issues.append((i,'extensão'))
  if abs(icm-(0.7*ip+0.3*ic))>0.011:issues.append((i,'ICM'))
 except (ValueError,KeyError,TypeError):issues.append((i,'valores numéricos'))
print('Ocorrências na auditoria:',len(issues))
for issue in issues[:30]:print(issue)
