const table = document.getElementById('menuItems')
var sumValue = 0
for (var i=0; i < table.rows.length; i++) {
    sumValue = sumValue + parseFloat(table.rows[i].cells[1].innerHTML);
}

document.getElementById('totalPrice').innerHTML = "$" + parseFloat(sumValue).toFixed(2);

let moneyCell = Array.prototype.slice.call(document.querySelectorAll(".currency"));
moneyCell.forEach(function(cell){
    cell.textContext = (+cell.textContext).toLocaleString('en-US', {style: 'currency', currency: 'USD'});
});