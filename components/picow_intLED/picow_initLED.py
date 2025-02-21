import esphome.codegen as cg
from esphome.components import output

# Declare the component in ESPHome's namespace
picow_intLED = cg.esphome_ns.namespace('picow_intLED')

# Define configuration schema for the component
CONFIG_SCHEMA = cg.schema({
    # Define the 'id' field for the component (used in YAML)
    'id': cg.use_id(output.Output),
})

# Register the component in ESPHome
@cg.register_component
def setup(config):
    picow_intLED_obj = picow_intLED.picow_intLED()  # Create C++ object
    cg.add(picow_intLED_obj)  # Register component with ESPHome
    return picow_intLED_obj
