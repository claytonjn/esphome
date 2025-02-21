// https://community.home-assistant.io/t/rpi-pico-w-onboard-temperature-sensor-and-onboard-led/564904/6
// C++ Code (picow_intLED.h)

#pragma once

#include "esphome/core/component.h"
#include "esphome/components/output/binary_output.h"

namespace esphome{
namespace picow_intLED {
    
// Custom binary output, for exposing binary states
class PicoWIntLed : public output::BinaryOutput, public Component {

    public:

    void setup() override {
        // This will be called by App.setup()
        
        pinMode(LED_BUILTIN, OUTPUT);
    }

    void write_state(bool state) override {
        digitalWrite(LED_BUILTIN, state);
    }

    void dump_config() override;
};

} //namespace picow_intLED
} //namespace esphome
