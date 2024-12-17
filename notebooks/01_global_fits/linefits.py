import warnings
warnings.simplefilter('ignore')
import SMEFT19
import numpy as np
import pandas as pd

def lines_scenarioIII():
    bf = [-0.10, -0.12, 0.90]

    likelihhod_C1 = [{'C1': C1} | SMEFT19.likelihood_fits([C1, bf[1], bf[2]], SMEFT19.scenarios.rotBIII) for C1 in np.linspace(-0.3, 0, 50)]
    pd.DataFrame(likelihhod_C1).to_csv('likelihoodC1.dat', index=False)

    likelihhod_C3 = [{'C3': C3} | SMEFT19.likelihood_fits([bf[0], C3, bf[2]], SMEFT19.scenarios.rotBIII) for C3 in np.linspace(-0.3, 0, 50)]
    pd.DataFrame(likelihhod_C3).to_csv('likelihoodC3.dat', index=False)

    likelihhod_bq = [{'bq': bq} | SMEFT19.likelihood_fits([bf[0], bf[1], bq], SMEFT19.scenarios.rotBIII) for bq in np.linspace(0, 3.0, 50)]
    pd.DataFrame(likelihhod_bq).to_csv('likelihoodbq.dat', index=False)

def lines_scenarioI():
    bf = [-0.11, 0, 0.78]

    likelihhod_C = [{'C': C1} | SMEFT19.likelihood_fits([C1, bf[1], bf[2]], SMEFT19.scenarios.rotBI) for C1 in np.linspace(-0.3, 0, 50)]
    pd.DataFrame(likelihhod_C).to_csv('likelihoodC_scI.dat', index=False)

    likelihhod_bl = [{'bl': C3} | SMEFT19.likelihood_fits([bf[0], C3, bf[2]], SMEFT19.scenarios.rotBI) for C3 in np.linspace(-0.02, 0.02, 50)]
    pd.DataFrame(likelihhod_bl).to_csv('likelihoodbl_scI.dat', index=False)

    likelihhod_bq = [{'bq': bq} | SMEFT19.likelihood_fits([bf[0], bf[1], bq], SMEFT19.scenarios.rotBI) for bq in np.linspace(0, 3.0, 50)]
    pd.DataFrame(likelihhod_bq).to_csv('likelihoodbq_scI.dat', index=False)

def lines_scenarioII():
    bf = [-0.12, 0.07, 0, -0.076, 0.851]

    likelihhod_C = [{'C': C} | SMEFT19.likelihood_fits([C, bf[1], bf[2], bf[3], bf[4]], SMEFT19.scenarios.rotBII) for C in np.linspace(-0.3, 0, 50)]
    pd.DataFrame(likelihhod_C).to_csv('likelihoodC_scII.dat', index=False)

    likelihhod_al = [{'al': al} | SMEFT19.likelihood_fits([bf[0], al, bf[2], bf[3], bf[4]], SMEFT19.scenarios.rotBII) for al in np.linspace(-0.15, 0.15, 50)]
    pd.DataFrame(likelihhod_al).to_csv('likelihoodal_scII.dat', index=False)

    likelihhod_bl = [{'bl': bl} | SMEFT19.likelihood_fits([bf[0], bf[1], bl, bf[3], bf[4]], SMEFT19.scenarios.rotBII) for bl in np.linspace(-0.02, 0.02, 50)]
    pd.DataFrame(likelihhod_bl).to_csv('likelihoodbl_scII.dat', index=False)

    likelihhod_aq = [{'aq': aq} | SMEFT19.likelihood_fits([bf[0], bf[1], bf[2], aq, bf[4]], SMEFT19.scenarios.rotBII) for aq in np.linspace(-0.15, 0.15, 50)]
    pd.DataFrame(likelihhod_aq).to_csv('likelihoodaq_scII.dat', index=False)

    likelihhod_bq = [{'bq': bq} | SMEFT19.likelihood_fits([bf[0], bf[1], bf[2], bf[3], bq], SMEFT19.scenarios.rotBII) for bq in np.linspace(0, 3.0, 50)]
    pd.DataFrame(likelihhod_bq).to_csv('likelihoodbq_scII.dat', index=False)

print('Start Scenario II')
lines_scenarioII()
