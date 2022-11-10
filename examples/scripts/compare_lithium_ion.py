#
# Compare lithium-ion battery models
#
import pybamm

pybamm.set_logging_level("INFO")
# load models
models = [
    pybamm.lithium_ion.SPM(),
    pybamm.lithium_ion.SPM({"particle": "uniform profile"}),
    # pybamm.lithium_ion.BasicDFN(),
    # pybamm.lithium_ion.DFN(),
    # pybamm.lithium_ion.NewmanTobias(),
]

# create and run simulations
sims = []
for model in models:
    sim = pybamm.Simulation(
        model,
        # parameter_values=pybamm.ParameterValues("Ai2020"),
        solver=pybamm.CasadiSolver(),  # root_method="lm"),
    )
    sim.solve([0, 3600])
    sims.append(sim)

# plot
pybamm.dynamic_plot(
    sims,
    [
        "Average negative particle concentration [mol.m-3]",
        "Average positive particle concentration [mol.m-3]",
    ],
)
