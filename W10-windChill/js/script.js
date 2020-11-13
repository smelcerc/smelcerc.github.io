function doInputOutput() {
    //input
    var temperature = parseFloat(document.getElementById('temperature').value);
    var windspeed = parseFloat(document.getElementById('windspeed').value);
    var returnMessage;
   
    //processing
    if (temperature > 50 || windspeed < 3) {
        returnMessage = temperature + '<br> We do not calculate wind chill if the temperature is above 50 or the windspeed is below 3';
    } else {
        returnMessage = windChill(temperature, windspeed); 
    }

    //output
    document.getElementById('output').innerHTML = returnMessage;
}

function windChill(tempF, speed) {
    var windChill = 35.74 + (0.6215 * tempF) - (35.75 * (Math.pow(speed, 0.16))) + (0.4275 * tempF * (Math.pow(speed, 0.16)));
    return windChill;
}