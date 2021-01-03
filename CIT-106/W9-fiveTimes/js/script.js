function fiveTimes() {
    //input
    var i;
    var returnMessage = '';
    
    //processing
    for (i = 1; i <= 12; i++) {
        var answer = 5 * i;
        returnMessage += '5 x ' + i + ' = ' + answer + '<br>';
    }

    //output
    document.getElementById('output').innerHTML = returnMessage;

}