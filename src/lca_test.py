import brightway2 as bw
from .parameters_experiment_1 import BWPROJECT,BWDATABASE

def test_lca():
    bw.projects.set_current(BWPROJECT)
    db = bw.Database("ecoinvent_remind_SSP2-Base_2020")
    act = db.random()
    method = bw.methods.random()
    LCA = bw.LCA({act:1},method=method)
    LCA.lci()
    LCA.lcia()
    print(f"THE SCORE OF TEST IS {LCA.score}")