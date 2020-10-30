function discount() {
    
    //INPUT
    let now = new Date();
    let dayOfWeek = now.getDay();
    let subtotal = parseFloat(document.getElementById('subtotal').value);
    
    //PROCESSING
    let tax = subtotal * .06;

    if (subtotal > 50 && (dayOfWeek == 2 || dayOfWeek == 3)){
       let discount = subtotal * .1;
       subtotal = subtotal - discount;
    }

    let total = subtotal + tax;

    //OUTPUT
    let returnMessage = "$" + total;

    document.getElementById('output').innerHTML = returnMessage;

}