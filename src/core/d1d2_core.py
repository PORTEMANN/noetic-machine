"""D1+D2 — Ligne de vortex remplie, dispersion des modes longitudinaux.
Chantier dev libre hors programme 2027. Methode : deplacement du coeur X(z,t).
Axes : (0: z axial, 1: x, 2: y). Kinetic only on x,y => straight z-line dynamics.
psi = condensat hote (vortex), chi = composante de remplissage (cœur massif).
Unites : xi, tau comme e44. Immiscibilite : gab**2 > gaa*gbb.
"""
import numpy as np, time, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def build_linear(Nz, Nxy, dt, damp):
    kz = 2*np.pi*np.fft.fftfreq(Nz)
    kx = 2*np.pi*np.fft.fftfreq(Nxy)
    k2 = kz[:,None,None]**2 + kx[None,:,None]**2 + kx[None,None,:]**2
    return np.exp(-(1j+damp)*k2*dt/2.0)   # (1j+damp): damp=0 => unitaire temps reel

def _gauss_seed(Nz, Nxy, sig):
    zz, xx, yy = np.indices((Nz, Nxy, Nxy), dtype=float)
    c = (Nxy-1)/2.0
    return np.exp(-((xx-c)**2+(yy-c)**2)/(2*sig**2))

def _soft_core(Nz, Nxy, u):
    zz, xx, yy = np.indices((Nz, Nxy, Nxy), dtype=float)
    c = (Nxy-1)/2.0
    r2 = (xx-c)**2+(yy-c)**2
    return r2/(r2+u**2)

def init_state(Nz, Nxy, u_core, chi_frac, sig_chi, sig_seed=2.5):
    """psi : vortex axial droit (noyau doux, phase autour de l'axe).
    chi : tube gaussien centre, fraction chi_frac de la densite du coeur."""
    zz, xx, yy = np.indices((Nz, Nxy, Nxy), dtype=float)
    c = (Nxy-1)/2.0
    theta = np.arctan2(yy-c, xx-c)
    psi = np.sqrt(_soft_core(Nz, Nxy, u_core)) * np.exp(1j*theta)
    chi = np.sqrt(chi_frac)*_gauss_seed(Nz, Nxy, sig_chi)*np.exp(0j*theta)
    return psi.astype(np.complex128), chi.astype(np.complex128)

def _kinetic_half(psi, lin):
    return np.fft.ifftn(np.fft.fftn(psi)*lin)   # cinetique 3D complete (k2 inclut kz)

def soft_wall(Nz, Nxy, R0, V0, p=8):
    """Paroi douce cylindrique : V0*(r/R0)^p, confine le condensat, centre la ligne."""
    zz, xx, yy = np.indices((Nz, Nxy, Nxy), dtype=float)
    c = (Nxy-1)/2.0
    r = np.sqrt((xx-c)**2+(yy-c)**2)
    return V0*(r/R0)**p

def step_psi(psi, lin, dt, damp, gaa, gab, chid2, mu_a, Vtrap=None):
    p2 = np.abs(psi)**2
    V = gaa*p2 + gab*chid2 - mu_a
    if Vtrap is not None: V = V + Vtrap
    psi *= np.exp(-(1j+damp)*V*dt/2)
    psi = _kinetic_half(psi, lin); psi = _kinetic_half(psi, lin)
    p2 = np.abs(psi)**2
    V = gaa*p2 + gab*chid2 - mu_a
    if Vtrap is not None: V = V + Vtrap
    psi *= np.exp(-(1j+damp)*V*dt/2)
    return psi

def step_chi(chi, lin, dt, damp, gbb, gab, psid2, mu_b, Vtrap=None):
    c2 = np.abs(chi)**2
    V = gbb*c2 + gab*psid2 - mu_b
    if Vtrap is not None: V = V + Vtrap
    chi *= np.exp(-(1j+damp)*V*dt/2)
    chi = _kinetic_half(chi, lin); chi = _kinetic_half(chi, lin)
    c2 = np.abs(chi)**2
    V = gbb*c2 + gab*psid2 - mu_b
    if Vtrap is not None: V = V + Vtrap
    chi *= np.exp(-(1j+damp)*V*dt/2)
    return chi

def vortex_positions(psi, prev=None):
    """Position du vortex par slice z : enroulement de phase sur plaquettes 2D,
    puis intersection des contours Re(psi)=0 et Im(psi)=0 (interp. lineaire).
    prev : (Xp, Yp) positions precedentes -> choisit la plaquette la plus proche
    (continuite temporelle, supprime la gigue inter-cellules)."""
    Nz, Nxy, _ = psi.shape
    th = np.angle(psi)
    def wrap(a): return (a+np.pi)%(2*np.pi)-np.pi
    t00 = th[:, :-1, :-1]; t10 = th[:, 1:, :-1]
    t11 = th[:, 1:, 1:];    t01 = th[:, :-1, 1:]
    w = np.rint((wrap(t10-t00)+wrap(t11-t10)+wrap(t01-t11)+wrap(t00-t01))/(2*np.pi))
    c = (Nxy-1)/2.0
    X = np.full(Nz, np.nan); Y = np.full(Nz, np.nan)
    for z in range(Nz):
        idx = np.argwhere(np.abs(w[z]) > 0.5)
        if len(idx) == 0:
            continue
        if prev is not None and not np.isnan(prev[0][z]):
            refx, refy = prev[0][z], prev[1][z]
        else:
            refx, refy = c, c
        i, j = idx[np.argmin((idx[:,0]-refx)**2 + (idx[:,1]-refy)**2)]
        # coins de la plaquette
        f = psi[z]
        f00 = f[i, j]; f10 = f[i+1, j]; f01 = f[i, j+1]
        # interpolation lineaire : f(u,v) ~ f00 + u(f10-f00) + v(f01-f00), u,v in [0,1]
        # resoudre Re=0 et Im=0
        A = np.array([[f10.real-f00.real, f01.real-f00.real],
                      [f10.imag-f00.imag, f01.imag-f00.imag]])
        b = -np.array([f00.real, f00.imag])
        try:
            uv = np.linalg.solve(A, b)
        except np.linalg.LinAlgError:
            uv = np.array([0.5, 0.5])
        if not (0 <= uv[0] <= 1 and 0 <= uv[1] <= 1):
            uv = np.clip(uv, 0.0, 1.0)
        X[z] = i + uv[0]; Y[z] = j + uv[1]
    return X, Y

def core_position(psi, r_mask=None):
    """X(z),Y(z) = barycentre du deficit de densite, masque circulaire interieur
    pour exclure la paroi de confinement."""
    Nz, Nxy, _ = psi.shape
    zz, xx, yy = np.indices((Nz, Nxy, Nxy), dtype=float)
    c = (Nxy-1)/2.0
    if r_mask is None:
        r_mask = 0.5*Nxy
    rm = np.sqrt((xx-c)**2+(yy-c)**2) <= r_mask
    w = np.clip(1.0 - np.abs(psi)**2, 0.0, None)*rm
    W = w.sum(axis=(1,2)) + 1e-12
    X = (w*xx).sum(axis=(1,2))/W
    Y = (w*yy).sum(axis=(1,2))/W
    return X, Y, W

def fill_profile(psi, chi, rmax=6.0):
    """Profil radial moyen de |chi|^2 autour du coeur instantane."""
    Nz, Nxy, _ = psi.shape
    zz, xx, yy = np.indices((Nz, Nxy, Nxy), dtype=float)
    X, Y, W = core_position(psi)
    Xz = X[:,None,None]; Yz = Y[:,None,None]
    r = np.sqrt((xx-Xz)**2+(yy-Yz)**2)
    cd2 = np.abs(chi)**2
    bins = np.arange(0, rmax+1.0, 1.0)
    prof = np.zeros(len(bins)-1)
    for i in range(len(bins)-1):
        m = (r>=bins[i])&(r<bins[i+1])
        prof[i] = cd2[m].mean() if m.any() else 0.0
    return bins[:-1]+0.5, prof

def measure_dispersion(Xt, Yt, dz, dt_samp, nk_max=4):
    """Xt,Yt : (nt, Nz) series temporelles du coeur. Retourne omega(k_n) par fit sinusoidal.
    k_n = 2 pi n / L.  On somme les puissances X+iY pour chaque n."""
    nt, Nz = Xt.shape
    Z = Xt + 1j*Yt
    klist = []
    omlist = []
    for n in range(1, nk_max+1):
        # mode spatial n (moyenne sur t)
        phi = 2*np.pi*n*np.arange(Nz)/Nz
        amp = (Z*np.exp(-1j*phi[None,:])).mean(axis=1)   # (nt,) complexe
        # spectre temporel : FFT complexe (signal chiral, un seul sens de rotation)
        amp = amp - amp.mean()
        # zero-padding x8 pour affiner la grille frequentielle
        nfft = 8*nt
        A = np.fft.fft(amp, n=nfft)
        om_full = 2*np.pi*np.fft.fftfreq(nfft, d=dt_samp)
        pos = om_full > 0
        A = np.abs(A)[pos]; om = om_full[pos]
        i = np.argmax(A)
        klist.append(2*np.pi*n/(Nz*dz))
        omlist.append(om[i])
    return np.array(klist), np.array(omlist)

def kelvin_theory(k, u_core, lnC=np.log(1.126)):
    """Dispersion de Kelvin attendue : omega = k^2 * [ln(1/(k u)) + lnC] / 2.
    Unites : kappa=rho_s=hbar=m=1 => vortex unit. Omega_K = (k^2/2)(ln(1/(k u))+C)."""
    with np.errstate(divide='ignore'):
        val = 0.5*k**2*(np.log(1.0/(k*u_core)) + lnC)
    return val
