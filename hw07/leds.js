#!/usr/bin/env node
// Blinks various LEDs
const Blynk = require('blynk-library');
const b = require('bonescript');
const util = require('util');

const LED0 = 'USR3';
const button = 'P9_25';
b.pinMode(LED0, b.OUTPUT);
b.pinMode(button, b.INPUT);

const LED1 = 'P9_14';
b.pinMode(LED1, b.OUTPUT);

const AUTH = 'FmLWNg6Aoe9RqHEcN6BYib0CRRo1PREH';


var blynk = new Blynk.Blynk(AUTH);

var v0 = new blynk.VirtualPin(0);
var v10 = new blynk.WidgetLED(10);
var v11 = new blynk.VirtualPin(11);

v0.on('write', function(param) {
    console.log('V0:', param[0]);
    b.digitalWrite(LED0, param[0]);
});

v11.on('write', function(param) {
    var pwmVal = param[0]/1023;
    console.log('V11:', pwmVal);
    b.analogWrite(LED1, pwmVal);
});

v10.setValue(0);    // Initiallly off

b.attachInterrupt(button, toggle, b.CHANGE);

function toggle(x) {
    console.log("V10: ", x.value);
    x.value ? v10.turnOff() : v10.turnOn();
}
