from premise import NewDatabase
from parameters_experiment_1 import BWDATABASE, BWDATABASE_VERSION, BWPROJECT
import brightway2 as bw

bw.projects.set_current(BWPROJECT)

ndb = NewDatabase(
    scenarios=[
        {
            "model": "remind",
            "pathway": "SSP2-Base",
            "year": 2020,
        },  # IAM model REMIND, scenario "Current Nationally-determined Contributions", year 2020
    ],
    source_db=BWDATABASE,  # name of the ecoinvent 3.8 in the BW2 project
    source_version=BWDATABASE_VERSION,
    key="tUePmX_S5B8ieZkkM7WUU2CnO8SmShwmAeWK9x2rTFo=",  # decryption key. Ask romain.sacchi(at)psi.ch to get it.
)

ndb.write_db_to_brightway()
