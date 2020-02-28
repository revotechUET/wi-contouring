import numpy as np
import gstools as gs
from pykrige.ok import OrdinaryKriging


def kriging_fill_grid(input):
    """
    conditioning data:
        input['x'] (array)
        input['y'] (array)
        input['z'] (array)

    grid definition for output field
        input['x_start']
        input['x_stop']
        input['x_step']
        input['y_start']
        input['y_stop']
        input['y_step']
    """
    if len(input['x']) == len(input['y']) == len(input['z']): 
        XI = np.arange(input['x_start'], input['x_stop'], input['x_step'])
        YI = np.arange(input['y_start'], input['y_stop'], input['y_step'])

        cov_model = gs.Gaussian(
            dim=2, len_scale=1, anis=0.2, angles=-0.5, var=0.5, nugget=0.1
        )
        pk_kwargs = cov_model.pykrige_kwargs
        OK = OrdinaryKriging(input['x'], input['y'], input['z'], **pk_kwargs)
        ZI, ss = OK.execute("grid", XI, YI)
        return ZI
    else:
        return None

# conditioning data


