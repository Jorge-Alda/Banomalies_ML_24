import SMEFT19
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from flavio.statistics.functions import pull
import warnings
from flavio.statistics.functions import pull, delta_chi2, pvalue

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    SMEFT19.SMEFTglob.gl.make_measurement()

def fit_I(x):
    return -SMEFT19.likelihood_global(x, SMEFT19.scenarios.rotBI)

bf_I, v_I, d_I, L_I = SMEFT19.ellipse.minimum(fit_I, [-0.13, 0, 0.851])

SMEFT19.ellipse.save(bf_I, v_I, d_I, L_I, '../data/ellipses/rotBI.yaml', name='Mass Rotation fit, Scenario I',
                     fit='rotBI')
L0 = fit_I(np.zeros(dim))

with open('results_01.txt', 'wt') as f:
    f.write(f'Best fit point: {str(bf_I)}\n')
    f.write(f'Delta Chi2: {2*L_I}\n')
    f.write(f'Pull: {pull(2*abs(Lmin-L0), 3)}')