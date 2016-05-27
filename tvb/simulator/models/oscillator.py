# -*- coding: utf-8 -*-
#
#
#  TheVirtualBrain-Scientific Package. This package holds all simulators, and
# analysers necessary to run brain-simulations. You can use it stand alone or
# in conjunction with TheVirtualBrain-Framework Package. See content of the
# documentation-folder for more details. See also http://www.thevirtualbrain.org
#
# (c) 2012-2013, Baycrest Centre for Geriatric Care ("Baycrest")
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License version 2 as published by the Free
# Software Foundation. This program is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public
# License for more details. You should have received a copy of the GNU General
# Public License along with this program; if not, you can download it here
# http://www.gnu.org/licenses/old-licenses/gpl-2.0
#
#
#   CITATION:
# When using The Virtual Brain for scientific publications, please cite it as follows:
#
#   Paula Sanz Leon, Stuart A. Knock, M. Marmaduke Woodman, Lia Domide,
#   Jochen Mersmann, Anthony R. McIntosh, Viktor Jirsa (2013)
#       The Virtual Brain: a simulator of primate brain network dynamics.
#   Frontiers in Neuroinformatics (7:10. doi: 10.3389/fninf.2013.00010)

"""
Oscillator models.

"""

from .base import Model, LOG, numpy, basic, arrays, numexpr


class Generic2dOscillator(Model):
    r"""
    The Generic2dOscillator model is a generic dynamic system with two state
    variables. The dynamic equations of this model are composed of two ordinary
    differential equations comprising two nullclines. The first nullcline is a
    cubic function as it is found in most neuron and population models; the
    second nullcline is arbitrarily configurable as a polynomial function up to
    second order. The manipulation of the latter nullcline's parameters allows
    to generate a wide range of different behaviours.

    Equations:

    .. math::
                \dot{V} &= d \, \tau (-f V^3 + e V^2 + g V + \alpha W + \gamma I), \\
                \dot{W} &= \dfrac{d}{\tau}\,\,(c V^2 + b V - \beta W + a),

    See:


        .. [FH_1961] FitzHugh, R., *Impulses and physiological states in theoretical
            models of nerve membrane*, Biophysical Journal 1: 445, 1961.

        .. [Nagumo_1962] Nagumo et.al, *An Active Pulse Transmission Line Simulating
            Nerve Axon*, Proceedings of the IRE 50: 2061, 1962.

        .. [SJ_2011] Stefanescu, R., Jirsa, V.K. *Reduced representations of
            heterogeneous mixed neural networks with synaptic coupling*.
            Physical Review E, 83, 2011.

        .. [SJ_2010]	Jirsa VK, Stefanescu R.  *Neural population modes capture
            biologically realistic large-scale network dynamics*. Bulletin of
            Mathematical Biology, 2010.

        .. [SJ_2008_a] Stefanescu, R., Jirsa, V.K. *A low dimensional description
            of globally coupled heterogeneous neural networks of excitatory and
            inhibitory neurons*. PLoS Computational Biology, 4(11), 2008).


    The model's (:math:`V`, :math:`W`) time series and phase-plane its nullclines
    can be seen in the figure below.

    The model with its default parameters exhibits FitzHugh-Nagumo like dynamics.

    +---------------------------+
    |  Table 1                  |
    +--------------+------------+
    |  EXCITABLE CONFIGURATION  |
    +--------------+------------+
    |Parameter     |  Value     |
    +==============+============+
    | a            |     -2.0   |
    +--------------+------------+
    | b            |    -10.0   |
    +--------------+------------+
    | c            |      0.0   |
    +--------------+------------+
    | d            |      0.02  |
    +--------------+------------+
    | I            |      0.0   |
    +--------------+------------+
    |  limit cycle if a is 2.0  |
    +---------------------------+


    +---------------------------+
    |   Table 2                 |
    +--------------+------------+
    |   BISTABLE CONFIGURATION  |
    +--------------+------------+
    |Parameter     |  Value     |
    +==============+============+
    | a            |      1.0   |
    +--------------+------------+
    | b            |      0.0   |
    +--------------+------------+
    | c            |     -5.0   |
    +--------------+------------+
    | d            |      0.02  |
    +--------------+------------+
    | I            |      0.0   |
    +--------------+------------+
    | monostable regime:        |
    | fixed point if Iext=-2.0  |
    | limit cycle if Iext=-1.0  |
    +---------------------------+


    +---------------------------+
    |  Table 3                  |
    +--------------+------------+
    |  EXCITABLE CONFIGURATION  |
    +--------------+------------+
    |  (similar to Morris-Lecar)|
    +--------------+------------+
    |Parameter     |  Value     |
    +==============+============+
    | a            |      0.5   |
    +--------------+------------+
    | b            |      0.6   |
    +--------------+------------+
    | c            |     -4.0   |
    +--------------+------------+
    | d            |      0.02  |
    +--------------+------------+
    | I            |      0.0   |
    +--------------+------------+
    | excitable regime if b=0.6 |
    | oscillatory if b=0.4      |
    +---------------------------+


    +---------------------------+
    |  Table 4                  |
    +--------------+------------+
    |  GhoshetAl,  2008         |
    |  KnocketAl,  2009         |
    +--------------+------------+
    |Parameter     |  Value     |
    +==============+============+
    | a            |    1.05    |
    +--------------+------------+
    | b            |   -1.00    |
    +--------------+------------+
    | c            |    0.0     |
    +--------------+------------+
    | d            |    0.1     |
    +--------------+------------+
    | I            |    0.0     |
    +--------------+------------+
    | alpha        |    1.0     |
    +--------------+------------+
    | beta         |    0.2     |
    +--------------+------------+
    | gamma        |    -1.0    |
    +--------------+------------+
    | e            |    0.0     |
    +--------------+------------+
    | g            |    1.0     |
    +--------------+------------+
    | f            |    1/3     |
    +--------------+------------+
    | tau          |    1.25    |
    +--------------+------------+
    |                           |
    |  frequency peak at 10Hz   |
    |                           |
    +---------------------------+


    +---------------------------+
    |  Table 5                  |
    +--------------+------------+
    |  SanzLeonetAl  2013       |
    +--------------+------------+
    |Parameter     |  Value     |
    +==============+============+
    | a            |    - 0.5   |
    +--------------+------------+
    | b            |    -10.0   |
    +--------------+------------+
    | c            |      0.0   |
    +--------------+------------+
    | d            |      0.02  |
    +--------------+------------+
    | I            |      0.0   |
    +--------------+------------+
    |                           |
    |  intrinsic frequency is   |
    |  approx 10 Hz             |
    |                           |
    +---------------------------+

    NOTE: This regime, if I = 2.1, is called subthreshold regime.
    Unstable oscillations appear through a subcritical Hopf bifurcation.


    .. figure :: img/Generic2dOscillator_01_mode_0_pplane.svg
    .. _phase-plane-Generic2D:
        :alt: Phase plane of the generic 2D population model with (V, W)

        The (:math:`V`, :math:`W`) phase-plane for the generic 2D population
        model for default parameters. The dynamical system has an equilibrium
        point.

    .. #Currently there seems to be a clash between traits and autodoc, autodoc
    .. #can't find the methods of the class, the class specific names below get
    .. #us around this...
    .. automethod:: Generic2dOscillator.__init__
    .. automethod:: Generic2dOscillator.dfun

    """

    _ui_name = "Generic 2d Oscillator"
    ui_configurable_parameters = ['tau', 'a', 'b', 'c', 'I', 'd', 'e', 'f', 'g', 'alpha', 'beta', 'gamma']

    #Define traited attributes for this model, these represent possible kwargs.
    tau = arrays.FloatArray(
        label=r":math:`\tau`",
        default=numpy.array([1.0]),
        range=basic.Range(lo=1.0, hi=5.0, step=0.01),
        doc="""A time-scale hierarchy can be introduced for the state
        variables :math:`V` and :math:`W`. Default parameter is 1, which means
        no time-scale hierarchy.""",
        order=1)

    I = arrays.FloatArray(
        label=":math:`I_{ext}`",
        default=numpy.array([0.0]),
        range=basic.Range(lo=-5.0, hi=5.0, step=0.01),
        doc="""Baseline shift of the cubic nullcline""",
        order=2)

    a = arrays.FloatArray(
        label=":math:`a`",
        default=numpy.array([-2.0]),
        range=basic.Range(lo=-5.0, hi=5.0, step=0.01),
        doc="""Vertical shift of the configurable nullcline""",
        order=3)

    b = arrays.FloatArray(
        label=":math:`b`",
        default=numpy.array([-10.0]),
        range=basic.Range(lo=-20.0, hi=15.0, step=0.01),
        doc="""Linear slope of the configurable nullcline""",
        order=4)

    c = arrays.FloatArray(
        label=":math:`c`",
        default=numpy.array([0.0]),
        range=basic.Range(lo=-10.0, hi=10.0, step=0.01),
        doc="""Parabolic term of the configurable nullcline""",
        order=5)

    d = arrays.FloatArray(
        label=":math:`d`",
        default=numpy.array([0.02]),
        range=basic.Range(lo=0.0001, hi=1.0, step=0.0001),
        doc="""Temporal scale factor. Warning: do not use it unless
        you know what you are doing and know about time tides.""",
        order=13)

    e = arrays.FloatArray(
        label=":math:`e`",
        default=numpy.array([3.0]),
        range=basic.Range(lo=-5.0, hi=5.0, step=0.0001),
        doc="""Coefficient of the quadratic term of the cubic nullcline.""",
        order=6)

    f = arrays.FloatArray(
        label=":math:`f`",
        default=numpy.array([1.0]),
        range=basic.Range(lo=-5.0, hi=5.0, step=0.0001),
        doc="""Coefficient of the cubic term of the cubic nullcline.""",
        order=7)

    g = arrays.FloatArray(
        label=":math:`g`",
        default=numpy.array([0.0]),
        range=basic.Range(lo=-5.0, hi=5.0, step=0.5),
        doc="""Coefficient of the linear term of the cubic nullcline.""",
        order=8)

    alpha = arrays.FloatArray(
        label=r":math:`\alpha`",
        default=numpy.array([1.0]),
        range=basic.Range(lo=-5.0, hi=5.0, step=0.0001),
        doc="""Constant parameter to scale the rate of feedback from the
            slow variable to the fast variable.""",
        order=9)

    beta = arrays.FloatArray(
        label=r":math:`\beta`",
        default=numpy.array([1.0]),
        range=basic.Range(lo=-5.0, hi=5.0, step=0.0001),
        doc="""Constant parameter to scale the rate of feedback from the
            slow variable to itself""",
        order=10)

    # This parameter is basically a hack to avoid having a negative lower boundary in the global coupling strength.
    gamma = arrays.FloatArray(
        label=r":math:`\gamma`",
        default=numpy.array([1.0]),
        range=basic.Range(lo=-1.0, hi=1.0, step=0.1),
        doc="""Constant parameter to reproduce FHN dynamics where
               excitatory input currents are negative.
               It scales both I and the long range coupling term.""",
        order=13)

    #Informational attribute, used for phase-plane and initial()
    state_variable_range = basic.Dict(
        label="State Variable ranges [lo, hi]",
        default={"V": numpy.array([-2.0, 4.0]),
                 "W": numpy.array([-6.0, 6.0])},
        doc="""The values for each state-variable should be set to encompass
            the expected dynamic range of that state-variable for the current
            parameters, it is used as a mechanism for bounding random initial
            conditions when the simulation isn't started from an explicit
            history, it is also provides the default range of phase-plane plots.""",
        order=11)

    #    variables_of_interest = arrays.IntegerArray(
    #        label = "Variables watched by Monitors.",
    #        range = basic.Range(lo = 0.0, hi = 2.0, step = 1.0),
    #        default = numpy.array([0], dtype=numpy.int32),
    #        doc = """This represents the default state-variables of this Model to be
    #        monitored. It can be overridden for each Monitor if desired. The
    #        corresponding state-variable indices for this model are :math:`V = 0`
    #        and :math:`W = 1`""",
    #        order = 7)

    variables_of_interest = basic.Enumerate(
        label="Variables watched by Monitors",
        options=["V", "W"],
        default=["V", ],
        select_multiple=True,
        doc="""This represents the default state-variables of this Model to be
                                        monitored. It can be overridden for each Monitor if desired. The
                                        corresponding state-variable indices for this model are :math:`V = 0`
                                        and :math:`W = 1`.""",
        order=12)


    def __init__(self, **kwargs):
        """
        May need to put kwargs back if we can't get them from trait...

        """

        LOG.info("%s: initing..." % str(self))

        super(Generic2dOscillator, self).__init__(**kwargs)

        #self._state_variables = ["V", "W"]
        self._nvar = 2
        self.cvar = numpy.array([0], dtype=numpy.int32)

        LOG.debug("%s: inited." % repr(self))


    def dfun(self, state_variables, coupling, local_coupling=0.0, ev=numexpr.evaluate):
        r"""
        The two state variables :math:`V` and :math:`W` are typically considered
        to represent a function of the neuron's membrane potential, such as the
        firing rate or dendritic currents, and a recovery variable, respectively.
        If there is a time scale hierarchy, then typically :math:`V` is faster
        than :math:`W` corresponding to a value of :math:`\tau` greater than 1.

        The equations of the generic 2D population model read

        .. math::
                \dot{V} &= d \, \tau (-f V^3 + e V^2 + g V + \alpha W + \gamma I), \\
                \dot{W} &= \dfrac{d}{\tau}\,\,(c V^2 + b V - \beta W + a),

        where external currents :math:`I` provide the entry point for local,
        long-range connectivity and stimulation.

        """

        V = state_variables[0, :]
        W = state_variables[1, :]

        #[State_variables, nodes]
        c_0 = coupling[0, :]

        tau = self.tau
        I = self.I
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        e = self.e
        f = self.f
        g = self.g
        beta = self.beta
        alpha = self.alpha
        gamma = self.gamma

        lc_0 = local_coupling * V

        # Pre-allocate the result array then instruct numexpr to use it as output.
        # This avoids an expensive array concatenation
        derivative = numpy.empty_like(state_variables)

        ev('d * tau * (alpha * W - f * V**3 + e * V**2 + g * V + gamma * I + gamma *c_0 + lc_0)', out=derivative[0])
        ev('d * (a + b * V + c * V**2 - beta * W) / tau', out=derivative[1])


        return derivative



class Kuramoto(Model):
    r"""
    The Kuramoto model is a model of synchronization phenomena derived by
    Yoshiki Kuramoto in 1975 which has since been applied to diverse domains
    including the study of neuronal oscillations and synchronization.

    See:

        .. [YK_1975] Y. Kuramoto, in: H. Arakai (Ed.), International Symposium
            on Mathematical Problems in Theoretical Physics, *Lecture Notes in
            Physics*, page 420, vol. 39, 1975.

        .. [SS_2000] S. H. Strogatz. *From Kuramoto to Crawford: exploring the
            onset of synchronization in populations of coupled oscillators*.
            Physica D, 143, 2000.

        .. [JC_2011] J. Cabral, E. Hugues, O. Sporns, G. Deco. *Role of local
            network oscillations in resting-state functional connectivity*.
            NeuroImage, 57, 1, 2011.

    The :math:`\theta` variable is the phase angle of the oscillation.

    Dynamic equations:
        .. math::

                \dot{\theta}_{k} = \omega_{k} + \mathbf{\Gamma}(\theta_k, \theta_j, u_{kj}) + \sin(W_{\zeta}\theta)

    """

    _ui_name = "Kuramoto Oscillator"
    ui_configurable_parameters = ['omega']

    #Define traited attributes for this model, these represent possible kwargs.
    omega = arrays.FloatArray(
        label=r":math:`\omega`",
        default=numpy.array([1.0]),
        range=basic.Range(lo=0.01, hi=200.0, step=0.1),
        doc=""":math:`\omega` sets the base line frequency for the
            Kuramoto oscillator in [rad/ms]""",
        order=1)

    #Informational attribute, used for phase-plane and initial()
    state_variable_range = basic.Dict(
        label="State Variable ranges [lo, hi]",
        default={"theta": numpy.array([0.0, numpy.pi * 2.0]),
        },
        doc="""The values for each state-variable should be set to encompass
            the expected dynamic range of that state-variable for the current
            parameters, it is used as a mechanism for bounding random initial
            conditions when the simulation isn't started from an explicit
            history, it is also provides the default range of phase-plane plots.""",
        order=6)

    variables_of_interest = basic.Enumerate(
        label="Variables watched by Monitors",
        options=["theta"],
        default=["theta"],
        select_multiple=True,
        doc="""This represents the default state-variables of this Model to be
                            monitored. It can be overridden for each Monitor if desired. The Kuramoto
                            model, however, only has one state variable with and index of 0, so it
                            is not necessary to change the default here.""",
        order=7)



    def __init__(self, **kwargs):
        """
        May need to put kwargs back if we can't get them from trait...

        """

        LOG.info("%s: initing..." % str(self))

        super(Kuramoto, self).__init__(**kwargs)

        #self._state_variables = ["theta"]
        self._nvar = 1
        self.cvar = numpy.array([0], dtype=numpy.int32)

        LOG.debug("%s: inited." % repr(self))


    def dfun(self, state_variables, coupling, local_coupling=0.0,
             ev=numexpr.evaluate, sin=numpy.sin, pi2=numpy.pi * 2):
        r"""
        The :math:`\theta` variable is the phase angle of the oscillation.

        .. math::
            \dot{\theta}_{k} = \omega_{k} + \mathbf{\Gamma}(\theta_k, \theta_j, u_{kj}) + \sin(W_{\zeta}\theta)

        where :math:`I` is the input via local and long range connectivity,
        passing first through the Kuramoto coupling function,
        :py:class:tvb.simulator.coupling.Kuramoto.

        """

        theta = state_variables[0, :]
        #import pdb; pdb.set_trace()

        #A) Distribution of phases according to the local connectivity kernel
        local_range_coupling = numpy.sin(local_coupling * theta)

        # NOTE: To evaluate.
        #B) Strength of the interactions
        #local_range_coupling = local_coupling * numpy.sin(theta)

        I = coupling[0, :] + local_range_coupling

        if not hasattr(self, 'derivative'):
            self.derivative = numpy.empty((1,) + theta.shape)

        # phase update
        self.derivative[0] = self.omega + I

        # all this pi makeh me have great hungary, can has sum NaN?
        return self.derivative
