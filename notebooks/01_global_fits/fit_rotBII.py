import warnings
warnings.filterwarnings("ignore")
import SMEFT19

SMEFT19.SMEFTglob.gl.make_measurement()

Nx = 3
Ny = 3

def fit(num):
    
    xmin = -0.08
    xmax = 0.08
    ymin = -0.025
    ymax = 0.025
    xmargin = 0.02*(xmax-xmin)
    ymargin = 0.02*(ymax-ymin)
    ix = num % Nx
    iy = num // Ny
    x = (xmin-xmargin) + ix/Nx * ((xmax+xmargin) - (xmin-xmargin))
    y = (ymin-ymargin) + iy/Ny * ((ymax+ymargin) - (ymin-ymargin))
    lf = SMEFT19.likelihood_fits([-0.12, x, y, -0.076, 0.851], SMEFT19.scenarios.rotBII)
    return [lf[fit] for fit in ['likelihood_lfu_fcnc.yaml', 'likelihood_rd_rds.yaml', 'likelihood_lfv.yaml', 'global']]

with open('likelihood_rotBII_RK.dat', 'at') as fRK, open('likelihood_rotBII_RD.dat', 'at') as fRD, open('likelihood_rotBII_LFV.dat', 'at') as fLFV, open('likelihood_rotBII_global.dat', 'at') as fglobal:
    for i in range(0, Nx*Ny):
        lg = fit(i)
        if i%Nx == Ny-1:
            sep = '\n'
        else:
            sep = '\t'
        for j, f in enumerate([fRK, fRD, fLFV, fglobal]):
            f.write(f'{lg[j]}{sep}')
            f.flush()
        print(i)
