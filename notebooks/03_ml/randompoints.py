import warnings
warnings.filterwarnings("ignore")
import SMEFT19
import numpy as np

SMEFT19.SMEFTglob.gl.make_measurement()

bf = [-0.10766202, -0.12670602, 0.6409892]
lh0 = SMEFT19.likelihood_global(bf, SMEFT19.scenarios.rotBIII)
#cov = np.array([[0.5*(0.07**2+0.03**2), 0.5*(-0.07**2+0.03**2), 0], [0.5*(-0.07**2+0.03**2), 0.5*(0.07**2+0.03**2), 0], [0, 0, 0.5**2]])

print('random points')
with open('../data/random.dat', 'at') as f:
    #f.write(f'C_1,C_3,beta^q,likelihood\n')
    for i in range(1000):
        #C1 = -0.3+0.3*np.random.random()
        #C3 = -0.3+0.3*np.random.random()
        #bq = 3*np.random.random()
        C1 = np.random.normal(bf[0], np.abs(bf[0])*0.20)
        C3 = np.random.normal(bf[1], np.abs(bf[1])*0.20)
        bq = np.random.normal(bf[2], np.abs(bf[2])*0.20)
        lh = SMEFT19.likelihood_global([C1, C3, bq], SMEFT19.scenarios.rotBIII)
        f.write(f'{C1},{C3},{bq},{lh}\n')
        if lh - lh0 > np.log(np.random.random()):
            lh0 = lh
            bf = [C1, C3, bq]
        #x = np.random.multivariate_normal(bf, cov)
        #lh = SMEFT19.likelihood_global(x, SMEFT19.scenarios.rotBIII)
        #f.write(f'{x[0]},{x[1]},{x[2]},{lh}\n')
        if i%10==0:
            f.flush()
