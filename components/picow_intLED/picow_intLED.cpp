#include "esphome/core/log.h"
#include "picow_intLED.h"

namespace esphome {
namespace picow_intLED {

static const char *TAG = "picow_intLED.binary_output";

void PicoWIntLed::setup(){

}

void PicoWIntLed::write_state(bool state){

}

void PicoWIntLed::dump_config() {
    ESP_LOGCONFIG(TAG, "picow_intLed binary output");
}

} //namespace picow_intLED
} //namespace esphome
