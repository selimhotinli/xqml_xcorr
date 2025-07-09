import numpy as np
import healpy as hp

# ############## Some necessary choices ###############
nside = 8
bool_thresh = 0.5
npixtot = hp.nside2npix(nside)
fwhm = 0.5e-1 # 
pixwin = True

# ############## Initialise xqml class ###############
lmin = 2
lmax = nside*3-1
dell = 1


# ############## Generate White Noise (not used yet) ###############
muKarcmin = 0.1
pixvar = Karcmin2var(muKarcmin*1e-6, nside)
varmap = ones((nstokes * npix)) * pixvar
NoiseVar = np.diag(varmap)