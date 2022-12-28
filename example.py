from objects import *

schema_name = "test_schema"
db_entry = {
    "entity_id": 1,
    "identifier": "WMT",
    "description": "Walmart Inc.",
    "attribute_1": [
        {
            "attribute_1_id": 1,
            "identifier": "WMT",
            "attribute_1_subsidiary_1": [
                {
                    "attributes_1_subsidiary_1_id": 1,
                    "identifier": "z_42E8ME0198_MO_OS_SamsClubNetSalesincludingFuel_4",
                    "description": "Sam's Club net sales (including fuel), mm",
                },
            ],
        }
    ],
    "attributes_2": [
        {
            "attributes_2_id": 1,
            "identifier": 1,
            "description": 1,
        }
    ],
    "attributes_3": [
        {
            "attributes_3_id": 1,
            "identifier": 1,
            "description": 1,
        }
    ],
}

en = Entity()
en.create_schema(schema_name, db_entry)
