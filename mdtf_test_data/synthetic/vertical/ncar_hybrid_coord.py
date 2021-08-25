""" Module for generating synthetic datasets """

___all__ = [
    "ncar_hybrid_coord",
]

import cftime
import xarray as xr
import numpy as np
from mdtf_test_data.util.rectilinear import construct_rect_grid
import mdtf_test_data.generators as generators

from mdtf_test_data.synthetic.time import generate_monthly_time_axis
from mdtf_test_data.synthetic.time import generate_daily_time_axis
from mdtf_test_data.synthetic.time import generate_hourly_time_axis


def ncar_hybrid_coord():
    """Generates NCAR CAM2 hybrid vertical coordinate

    Returns
    -------
    xarray.DataArray
        NCAR vertical hybrid coordinate, a, and b coefficients
    """

    lev = np.array(
        [
            2.501651,
            4.187496,
            6.66766,
            10.099201,
            14.551163,
            19.943806,
            26.002806,
            32.250471,
            38.050216,
            42.70557,
            46.240154,
            49.511782,
            53.014888,
            56.765857,
            60.782212,
            65.082732,
            69.687527,
            74.618127,
            79.897583,
            85.550576,
            91.603545,
            98.084766,
            105.024556,
            112.455371,
            120.411924,
            128.931421,
            138.053706,
            147.821421,
            158.280234,
            169.479033,
            181.470176,
            194.309746,
            208.057754,
            222.778457,
            238.540693,
            255.418164,
            273.489746,
            292.839941,
            313.559268,
            335.744541,
            359.499453,
            384.935117,
            412.17043,
            441.332715,
            472.55834,
            505.993262,
            541.793789,
            580.127324,
            621.173066,
            665.12291,
            712.182383,
            762.571445,
            816.525625,
            858.699883,
            886.368125,
            912.162773,
            935.873203,
            957.301758,
            976.266953,
            992.556094,
        ]
    )

    hyam = np.array(
        [
            2.501651e-03,
            4.187496e-03,
            6.667660e-03,
            1.009920e-02,
            1.455116e-02,
            1.994381e-02,
            2.600281e-02,
            3.225047e-02,
            3.805022e-02,
            4.270557e-02,
            4.624015e-02,
            4.951178e-02,
            5.301489e-02,
            5.676586e-02,
            6.078221e-02,
            6.508273e-02,
            6.968753e-02,
            7.461813e-02,
            7.989758e-02,
            8.555058e-02,
            9.160354e-02,
            9.808477e-02,
            1.050246e-01,
            1.124554e-01,
            1.204119e-01,
            1.289314e-01,
            1.380537e-01,
            1.478214e-01,
            1.582802e-01,
            1.694790e-01,
            1.746796e-01,
            1.726401e-01,
            1.696388e-01,
            1.664251e-01,
            1.629841e-01,
            1.592996e-01,
            1.553543e-01,
            1.511300e-01,
            1.466068e-01,
            1.417635e-01,
            1.365776e-01,
            1.310247e-01,
            1.250790e-01,
            1.187125e-01,
            1.118957e-01,
            1.045965e-01,
            9.678086e-02,
            8.841227e-02,
            7.945159e-02,
            6.985690e-02,
            5.958334e-02,
            4.858288e-02,
            3.680412e-02,
            2.759706e-02,
            2.155681e-02,
            1.592557e-02,
            1.074934e-02,
            6.071232e-03,
            1.930966e-03,
            -1.648308e-09,
        ]
    )

    hybm = np.array(
        [
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.006791,
            0.02167,
            0.038419,
            0.056353,
            0.075557,
            0.096119,
            0.118135,
            0.14171,
            0.166953,
            0.193981,
            0.222922,
            0.25391,
            0.287091,
            0.32262,
            0.360663,
            0.401397,
            0.445013,
            0.491715,
            0.541721,
            0.595266,
            0.652599,
            0.713989,
            0.779722,
            0.831103,
            0.864811,
            0.896237,
            0.925124,
            0.951231,
            0.974336,
            0.992556,
        ]
    )

    lev_attrs = {
        "long_name": "hybrid level at midpoints (1000*(A+B))",
        "units": "level",
        "positive": "down",
        "standard_name": "atmosphere_hybrid_sigma_pressure_coordinate",
        "formula_terms": "a: hyam b: hybm p0: P0 ps: PS",
    }

    dset_out = xr.Dataset()

    dset_out["hyam"] = xr.DataArray(
        hyam,
        dims={"lev": lev},
        coords={"lev": (lev)},
        attrs={"long_name": "hybrid A coefficient at layer midpoints"},
    )

    dset_out["hybm"] = xr.DataArray(
        hybm,
        dims={"lev": lev},
        coords={"lev": (lev)},
        attrs={"long_name": "hybrid B coefficient at layer midpoints"},
    )

    dset_out["lev"] = xr.DataArray(
        lev, dims={"lev": lev}, coords={"lev": (lev)}, attrs=lev_attrs
    )

    return dset_out
