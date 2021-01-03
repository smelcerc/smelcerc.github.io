function alarm() {
    
    var returnMessage = "";

    //INPUT
    var now = new Date();
    var month = now.getMonth();
    var dayOfMonth = now.getDate();
    var dayOfWeek = now.getDay();
    var getUP;
    
    //PROCESSING
    if (dayOfWeek > 0 && dayOfWeek < 6){
        if ((month == 0 && dayOfMonth == 1) || (month == 6 && dayOfMonth == 4) || (month == 11 && dayOfMonth == 25)){
            getUP = false;
        }
        getUP = true;
    }else{
        getUP = false;
    }

    //OUTPUT
    if (getUP == true){
        returnMessage = "Get up!";
    }else{
        returnMessage = "Sleep in";
    }

    document.getElementById('output').innerHTML = returnMessage;

}