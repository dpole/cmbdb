"""Data base of CMB experiemnts
"""
import os.path as op
import pandas as pd
import yaml

this_dir = op.split(__file__)[0]
with open(op.join(this_dir, 'experiments.yaml'), 'r') as f:
    exps = yaml.safe_load(f)

cmbdb = []

for exp, conf in exps.items():
    tmp = (pd.DataFrame([conf]).set_index(['meta'])
                               .apply(pd.Series.explode)
                               .reset_index(drop=True)
          )

    for key, item in conf['meta'].items():
        tmp[key] = item

    tmp['experiment'] = exp
    cmbdb.append(tmp)

cmbdb = pd.concat(cmbdb)
