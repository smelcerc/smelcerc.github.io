function whichShoes() {
    try {
        //INPUT
        var weather = (document.getElementById('weatherInput').value).toLowerCase();
        //PROCESSING
        if (weather == "sunny") {
            var shoe = "SANDLES";
        }
        else if (weather == "raining") {
            var shoe = "SHOES"
        }
        else if (weather == "snowing") {
            var shoe = "BOOTS";
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