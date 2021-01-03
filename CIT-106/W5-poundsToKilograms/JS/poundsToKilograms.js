function convert2Kilos() {
    try {
        //INPUT
        var pounds = parseFloat(document.getElementById('pounds').value);
        //PROCESSING
        var kilos = pounds * 0.453592;
        var roundedKilos = Math.round(kilos * 10) / 10;
        //OUTPUT
        var returnMessage = pounds + " Pounds = " + roundedKilos + " Kilograms";
        document.getElementById('output').innerHTML = returnMessage;
    }
    catch(err){
        throw "Could not process users input";
    }
}