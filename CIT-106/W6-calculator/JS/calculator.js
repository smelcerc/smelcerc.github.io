function doMath() {
    try {
        //INPUT
        var number1 = parseFloat(document.getElementById('number1').value);
        var operator = document.getElementById('operatorList').value;
        var number2 = parseFloat(document.getElementById('number2').value);
        var answer = parseFloat(document.getElementById('answer').value);
        
        //PROCESSING
        var realAnswer;
        var returnMessage;

        switch (operator){
            case "+":
                realAnswer = number1 + number2;
                break;
            case "-":
                realAnswer = number1 - number2;
                break;
            case "*":
                realAnswer = number1 * number2;
                break;
            case "/":
                realAnswer = number1 / number2;
                break;
        }

        if (answer == realAnswer){
            returnMessage = "Correct! 🏆";
        }
        else {
            returnMessage = "Incorrect 😢";
        }
        
        //OUTPUT
        document.getElementById('output').innerHTML = returnMessage;
    }
    catch(err){
        throw "Could not process users input";
    }
}