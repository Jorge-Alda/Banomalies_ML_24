import warnings
warnings.filterwarnings("ignore")
import SMEFT19
import numpy as np
import flavio
from wilson import Wilson

SMEFT19.SMEFTglob.gl.make_measurement()

bf = [-0.12,0.07,0.001,-0.076,0.85]
lh0 = SMEFT19.likelihood_global(bf, SMEFT19.scenarios.rotBII)
#cov = np.array([[0.5*(0.07**2+0.03**2), 0.5*(-0.07**2+0.03**2), 0], [0.5*(-0.07**2+0.03**2), 0.5*(0.07**2+0.03**2), 0], [0, 0, 0.5**2]])

print('random points')
with open('random_scII.dat', 'at') as f:
    point = [bf[i] for i in range(5)]
    #f.write(f'C,al,bl,aq,bq,likelihood,RD*,BKnunu\n')
    i = 0
    while i < 1000:
        C = np.random.normal(bf[0], np.abs(bf[0])*0.1)
        al = np.random.normal(bf[1], np.abs(bf[1])*0.1)
        bl = np.random.normal(bf[2], np.abs(bf[2])*0.1)
        aq = np.random.normal(bf[3], np.abs(bf[1])*0.1)
        bq = np.random.normal(bf[4], np.abs(bf[2])*0.5)
        lh = SMEFT19.likelihood_global([C, al, bl, aq, bq], SMEFT19.scenarios.rotBII)
        if lh - lh0 > np.log(np.random.random()):
            lh0 = lh
            bf = [C, al, bl, aq, bq]
            w = Wilson.from_wc(SMEFT19.scenarios.rotBII(bf).match_run(scale=48, eft='WET', basis='flavio'))
            rd = flavio.np_prediction('Rtaul(B->D*lnu)', w)
            bknunu = flavio.np_prediction('BR(B+->Knunu)', w) * 1e5
            f.write(f'{C},{al},{bl},{aq},{bq},{lh},{rd},{bknunu}\n')
            #x = np.random.multivariate_normal(bf, cov)
            #lh = SMEFT19.likelihood_global(x, SMEFT19.scenarios.rotBIII)
            #f.write(f'{x[0]},{x[1]},{x[2]},{lh}\n')
            f.flush()
