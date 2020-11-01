function sumOdds() {

    //User input
    var number = parseFloat(document.getElementById('number').value);

    //Determains if the input number needs to be added sum
    var sum;
    if (number % 2 == 0) {
        sum = 0;
    } else {
        sum = number;
    }

    //Add all the odd numbers
    var i = 1
    while (i < number) {
        sum += i;
        i +=2;
    }

    //Output
    var returnMessage = sum;

    document.getElementById('output').innerHTML = returnMessage;
}