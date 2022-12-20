import brightway2 as bw
from pathlib import Path
from .parameters_experiment_1 import BWDATABASE, BWPROJECT

PATH_BASE = Path(__file__)
PATH = PATH_BASE.parent.parent.parent / "databases/ecoinvent38/datasets/"
# PATH = "/home/glarrea/databases/ecoinvent38/datasets"
print("this is the path222", Path(__file__))
print("this is the path", PATH)

def setup():
    bw.projects.set_current(BWPROJECT)
    bw.bw2setup()
    db = bw.SingleOutputEcospold2Importer(
                db_name=BWDATABASE, dirpath=PATH)
    db.apply_strategies()
    db.write_database()
    print("SETUP COMPLETED")