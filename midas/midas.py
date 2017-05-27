import numpy as np


from scipy.optimize import least_squares

from midas.weights import x_weighted
from midas.fit import ssr


def estimate(y, yl, x):
    xw, w = x_weighted(x, 1., 5.)

    # First we do OLS to get initial parameters
    c = np.linalg.lstsq(np.concatenate([xw.reshape((len(xw), 1)), yl, np.ones((len(xw), 1))], axis=1), y)[0]

    print(c)

    f = lambda v: ssr(v, x.values, y.values, yl.values)

    opt_res = least_squares(f, np.concatenate([c[0:2], [1., 5.], c[2:]]))

    print(opt_res.x)