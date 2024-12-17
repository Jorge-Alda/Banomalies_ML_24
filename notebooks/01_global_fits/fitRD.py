import flavio
import numpy as np
from scenarios import rotBIII
import warnings
warnings.simplefilter("ignore")

bf1 = [-0.1023464, -0.11863709, 0.9034919 ]

rd_exp = flavio.combine_measurements('Rtaul(B->Dlnu)')
rds_exp = flavio.combine_measurements('Rtaul(B->D*lnu)')

def likelihood_global(x, func):
    rd_np = flavio.np_prediction('Rtaul(B->Dlnu)', func(x))
    rds_np = flavio.np_prediction('Rtaul(B->D*lnu)', func(x))
    return (rd_np-rd_exp.central_value)**2/rd_exp.error_left**2 + (rds_np-rds_exp.central_value)**2/rds_exp.error_left**2

def lh_C1C3(num: int) -> float:
    xmin = -0.3
    xmax = 0.0
    ymin = -0.3
    ymax = 0.0
    xmargin = 0.02*(xmax-xmin)
    ymargin = 0.02*(ymax-ymin)
    ix = num % 50
    iy = num // 50
    x = (xmin-xmargin) + ix/50 * ((xmax+xmargin) - (xmin-xmargin))
    y = (ymin-ymargin) + iy/50 * ((ymax+ymargin) - (ymin-ymargin))
    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        try:
            lg = likelihood_global([x, y, bf1[2]], rotBIII)
        except:
            return -100
        return max(lg, -100)

def lh_C1beta(num: int) -> float:
    xmin = -0.3
    xmax = 0.0
    ymin = 0.0
    ymax = 3.2
    xmargin = 0.02*(xmax-xmin)
    ymargin = 0.02*(ymax-ymin)
    ix = num % 50
    iy = num // 50
    x = (xmin-xmargin) + ix/50 * ((xmax+xmargin) - (xmin-xmargin))
    y = (ymin-ymargin) + iy/50 * ((ymax+ymargin) - (ymin-ymargin))
    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        try:
            lg = likelihood_global([x, bf1[1], y], rotBIII)
        except:
            return -100
        return max(lg, -100)
    
def lh_C3beta(num: int) -> float:
    xmin = -0.3
    xmax = 0.0
    ymin = 0.0
    ymax = 3.2
    xmargin = 0.02*(xmax-xmin)
    ymargin = 0.02*(ymax-ymin)
    ix = num % 50
    iy = num // 50
    x = (xmin-xmargin) + ix/50 * ((xmax+xmargin) - (xmin-xmargin))
    y = (ymin-ymargin) + iy/50 * ((ymax+ymargin) - (ymin-ymargin))
    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        try:
            lg = likelihood_global([bf1[0], x, y], rotBIII)
        except:
            return -100
        return max(lg, -100)

start = 0
print('C1 C3')
with open('likelihoodRD_rotBIII_C1C3.dat', 'at') as f:
    for i in range(start, 50*50):
        lg = lh_C1C3(i)
        if i%50 == 49:
            sep = '\n'
        else:
            sep = '\t'
        f.write(f'{lg}{sep}')
        f.flush()
        print(i)
        
start = 0

print('C1 betaq')

with open('likelihoodRD_rotBIII_C1beta.dat', 'at') as f:
    for i in range(start, 50*50):
        lg = lh_C1beta(i)
        if i%50 == 49:
            sep = '\n'
        else:
            sep = '\t'
        f.write(f'{lg}{sep}')
        f.flush()
        print(i)
        
start = 0


print('C3 betaq')

with open('likelihoodRD_rotBIII_C3beta.dat', 'at') as f:
    for i in range(start, 50*50):
        lg = lh_C3beta(i)
        if i%50 == 49:
            sep = '\n'
        else:
            sep = '\t'
        f.write(f'{lg}{sep}')
        f.flush()
        print(i)