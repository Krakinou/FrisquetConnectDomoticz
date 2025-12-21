"""Constantes pour intégration Frisquet-Connect """

HOST="fcutappli.frisquet.com"
AUTH_API="/api/v1/authentifications"
SITE_API="/api/v1/sites"
ORDRES_API="/api/v1/ordres"

C_TAMB="1"
C_CONS_CONF="2"
C_CONS_RED="3"
C_CONS_HG="4"

MODE_ECS = [
{ "nom" : "Stop",       "ecs_out": "5", "ecs_in":0,  "nValue":0},
{ "nom" : "Eco+ Timer", "ecs_out": "4", "ecs_in":10, "nValue":1},
{ "nom" : "Eco+",       "ecs_out": "3", "ecs_in":20, "nValue":1},
{ "nom" : "Eco Timer",  "ecs_out": "2", "ecs_in":30, "nValue":1},
{ "nom" : "Eco",        "ecs_out": "1", "ecs_in":40, "nValue":1},
{ "nom" : "Max",        "ecs_out": "0", "ecs_in":50, "nValue":1}
]
