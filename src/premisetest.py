from premise import NewDatabase
import brightway2 as bw


def import_premise(bw_project, database_name, database_version):
# def import_premise():
    bw.projects.set_current(bw_project)

    ndb = NewDatabase(
        scenarios=[
            {
                "model": "remind",
                "pathway": "SSP2-Base",
                "year": 2020,
            },  # IAM model REMIND, scenario "Current Nationally-determined Contributions", year 2
        ],
        source_db=database_name,  # name of the ecoinvent 3.8 in the BW2 project
        source_version=database_version,
        key="tUePmX_S5B8ieZkkM7WUU2CnO8SmShwmAeWK9x2rTFo=",  # decryption key. Ask romain.sacchi(at)psi.ch to get it.
    )

    ndb.write_db_to_brightway()
    print("PREMISE INSTALLED")