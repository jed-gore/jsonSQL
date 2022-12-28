from objects import *

schema_name = "test_schema"
db_map = {
    "entity_id": 0,
    "identifier": "",
    "description": "",
    "attribute_1": [
        {
            "attribute_1_id": 0,
            "identifier": "",
            "attribute_1_subsidiary_1": [
                {
                    "attributes_1_subsidiary_1_id": 0,
                    "identifier": "",
                    "description": "",
                },
            ],
        }
    ],
    "attributes_2": [
        {
            "attributes_2_id": 0,
            "identifier": "",
            "description": "",
        }
    ],
    "attributes_3": [
        {
            "attributes_3_id": 0,
            "identifier": "",
            "description": "",
        }
    ],
}

en = Entity()
en.create_schema(schema_name, db_map)
