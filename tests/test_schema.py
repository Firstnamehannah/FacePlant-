from linkml_runtime.utils.schemaview import SchemaView

SCHEMA_PATH = "src/faceplant/schema/faceplant.yaml"

def test_schema_loads():
    sv = SchemaView(SCHEMA_PATH)
    assert sv.schema is not None
    
def test_expected_classes_exist():
    sv = SchemaView(SCHEMA_PATH)
    classes = sv.all_classes()
    # swap in your actual class names
    assert len(classes) > 0

def test_custom_types_have_uris():
    """Guards against the shaclgen/sqltablegen 'No URI for type' errors."""
    sv = SchemaView(SCHEMA_PATH)
    for name, t in sv.all_types().items():
        if t.typeof is None and t.uri is None:
            assert False, f"type '{name}' has neither a uri nor a typeof base"    