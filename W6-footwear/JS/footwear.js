function whichShoes() {
    try {
        //INPUT
        var weather = (document.getElementById('weather').value).toLowerCase();
        //PROCESSING
        if (weather == "hot") {
            var shoe = "sandals";
        }
        else if (weather == "rain") {
            var shoe = "galoshes"
        }
        else if (weather == "snow") {
            var shoe = "boots";
        }
        else {
            document.getElementById('output').innerHTML = "Please enter the weather";
            return;
        }
        var returnMessage = "The weather is " + weather.toUpperCase() + " so you should wear " + shoe + "!";
        //OUTPUT
        
        document.getElementById('output').innerHTML = returnMessage;
    }
    catch(err){
        throw "Could not process users input";
    }
}