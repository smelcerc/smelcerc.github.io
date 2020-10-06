function doMath() {
    try {
        //INPUT
        var number1 = parseFloat(document.getElementById('number1').value);
        var operator = (document.getElementById('operatorList').value).toLowerCase();
        var number2 = parseFloat(document.getElementById('number2').value);
        //PROCESSING
        var answer = eval(number1 + operator + number2);
        //OUTPUT
        var returnMessage = number1 + " " + operator + " " + number2 + " = " + answer;
        document.getElementById('output').innerHTML = returnMessage;
    }
    catch(err){
        throw "Could not process users input";
    }
}