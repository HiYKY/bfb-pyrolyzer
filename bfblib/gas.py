import chemics as cm


class Gas:
    """
    Gas or gas mixture properties.

    Attributes
    ----------
    p : float
        Pressure [Pa]
    sp : list
        Species representing gas or gas mixture.
    tk : float
        Temperature [K]
    x : list
        Mole fraction of gas or gas mixture.
    mw : float
        Molecular weight [g/mol]
    mu : float
        Viscosity [µP]
    rho : float
        Density [kg/m³]
    """

    def __init__(self, sp, x, p, tk, eq='herning'):
        self.sp = sp
        self.x = x
        self.p = p
        self.tk = tk
        self._eq = eq
        self._n = len(sp)
        self._calc_mw()
        self._calc_rho()
        self._calc_mu()

    def _calc_mw(self):
        """
        Calculate molecular weight [g/mol] based on number of gas species.
        """
        if self._n == 1:
            mw = cm.mw(self.sp[0])
        else:
            mws = []
            for i in range(self._n):
                mw = cm.mw(self.sp[i])
                mws.append(mw)
            mw = cm.mw_mix(mws, self.x)
        self.mw = mw

    def _calc_rho(self):
        """
        Calculate gas density [kg/m³].
        """
        rho = cm.rhog(self.mw, self.p, self.tk)
        self.rho = rho

    def _calc_mu(self):
        """
        Calculate gas viscosity [µP] based on number of gas species.
        """
        if self._n == 1:
            mu = cm.mu_gas(self.sp[0], self.tk)
            self.mu = mu
        else:
            mws = []
            mus = []

            for i in range(self._n):
                mw = cm.mw(self.sp[i])
                mu = cm.mu_gas(self.sp[i], self.tk)
                mws.append(mw)
                mus.append(mu)

            if self._eq == 'graham':
                mu = cm.mu_graham(mus, self.x)
            elif self._eq == 'herning':
                mu = cm.mu_herning(mus, mws, self.x)
            else:
                raise ValueError(f'Viscosity equation `{self._eq}` not available.')
            self.mu = mu
