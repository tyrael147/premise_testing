from src.bw2setup import setup
from src.premisetest import import_premise
from src.lca_test import test_lca
from src.parameters_experiment_1 import BWPROJECT, BWDATABASE, BWDATABASE_VERSION

def go():
    setup()
    import_premise(bw_project=BWPROJECT,database_name=BWDATABASE, database_version=BWDATABASE_VERSION)
    test_lca()

if __name__ == "__main__":
    go()
