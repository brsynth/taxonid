from logging import (
    Logger,
    getLogger
)
from Bio import Entrez


def get_taxonid(org_name: str, logger: Logger = getLogger(__name__)) -> int:
    """Get taxon ID from NCBI taxonomy database

    :param org_name: Name of the organism
    :type org_name: str
    :param logger: Logger, defaults to getLogger(__name__)
    :type logger: Logger, optional
    :return: Taxon ID
    :rtype: int
    """
    # Provide your email address to NCBI
    Entrez.email = "your_email@example.com"

    # Search for the organism by its name
    handle = Entrez.esearch(db="taxonomy", term=org_name)
    record = Entrez.read(handle)

    if record["Count"] == "0":
        logger.error("No taxon ID found for {}".format(org_name))
        taxon_id = -1
    else:
        # Extract the taxon ID from the search result
        taxon_id = record["IdList"][0]

    logger.debug("Taxon ID for {} is {}".format(org_name, taxon_id))

    return int(taxon_id)
