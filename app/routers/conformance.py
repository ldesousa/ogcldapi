from typing import Optional

import fastapi
from fastapi import Request
from utils import utils

from config import *
from rdflib.namespace import DCTERMS, RDF
from api.conformance import ConformanceRenderer

router = fastapi.APIRouter()
g = utils.g


@router.get("/conformance")
def conformance(request: Request,
                _view: Optional[str] = None,
                _profile: Optional[str] = None,
                _format: Optional[str] = None,
                _mediatype: Optional[str] = None,
                version: Optional[str] = None
                ):
    # q = """
    #     PREFIX dcterms: <http://purl.org/dc/terms/>
    #     PREFIX ogcapi: <https://data.surroundaustralia.com/def/ogcapi/>
    #
    #     SELECT *
    #     WHERE {
    #         ?uri a ogcapi:ConformanceTarget ;
    #            dcterms:title ?title
    #     }
    #     """
    print("ahe")
    conformance_classes = []
    for s in g.subjects(predicate=RDF.type, object=OGCAPI.ConformanceTarget):
        uri = str(s)
        for o in g.objects(subject=s, predicate=DCTERMS.title):
            title = str(o)
        conformance_classes.append((uri, title))
    print("C_classes", conformance_classes)
    return ConformanceRenderer(request, conformance_classes).render()
