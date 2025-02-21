import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import output
from esphome.const import CONF_ID

# Declare the component in ESPHome's namespace
picow_intLED = cg.esphome_ns.namespace('picow_intLED')
PicoWIntLed = picow_intLED_ns.class_(
    "PicoWIntLed", output.BinaryOutput, cg.Component
)

# Define configuration schema for the component
CONFIG_SCHEMA = output.BINARY_OUTPUT_SCHEMA.extend(
    {
        # Define the 'id' field for the component (used in YAML)
        cv.Required(CONF_ID): cv.declare_id(PicoWIntLed),
    }
).extend(cv.COMPONENT_SCHEMA)

# Register the component in ESPHome
async def setup(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await output.register_output(var, config)
    await cg.register_component(var, config)