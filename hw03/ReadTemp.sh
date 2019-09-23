#!/bin/bash
#Zachary Forster CM1646
#09/18/19

#This file reads two i2c tmp101 sensors and averages their values in F then prints the value

# Read forever
config-pin P9_24 i2c
config-pin P9_26 i2c


while [ "1" = "1" ]; do
        TEMP=`i2cget -y 1 0x48`
        TEMPF=$(((($TEMP *9)/5)+32)) 
        TEMP2=`i2cget -y 1 0x49`
        TEMPF2=$(((($TEMP2 *9)/5)+32)) 
        TEMPAVG=$((($TEMPF +$TEMPF2)/2))
        echo -ne "${TEMPAVG}"
        sleep 1.0
        # Return to the start of the line, but not the next line
        echo -ne "\\r"
        
done


