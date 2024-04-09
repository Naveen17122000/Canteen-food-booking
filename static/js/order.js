document.addEventListener("DOMContentLoaded", function() {
    var selectedItems = []; 
    var itemsList = document.getElementById("items-list");
    var itemCheckboxes = document.querySelectorAll(".item-checkbox");
    var quantityInput = document.getElementById("quantity");


function handleItemSelection() {
    selectedItems = [];
    itemCheckboxes.forEach(function(itemCheckbox) {
        if (itemCheckbox.checked) {
            var itemId = itemCheckbox.value;
            var itemName = itemCheckbox.nextElementSibling.textContent.split(" - ")[0];
            var itemPrice = parseFloat(itemCheckbox.nextElementSibling.textContent.split(" - ")[1].slice(1));
            var quantity = parseInt(quantityInput.value);
            selectedItems.push({ id: itemId, name: itemName, price: itemPrice, quantity: quantity });
        }
    });
    updateItemsList();
    calculateTotalPrice();
}


    function updateItemsList() {
        if (!itemsList) return;
        itemsList.innerHTML = "";
        selectedItems.forEach(function(item) {
            var li = document.createElement("li");
            li.textContent = item.name + " (Quantity: " + item.quantity + ")";
            itemsList.appendChild(li);
        });
    }


    function calculateTotalPrice() {
        var totalPrice = selectedItems.reduce(function(acc, item) {
            return acc + (item.price * item.quantity);
        }, 0);
        var totalAmount = document.getElementById("total-amount");
        if (totalAmount) {
            totalAmount.textContent = "Total: $" + totalPrice.toFixed(2);
        }
    }

    if (itemCheckboxes) {
        itemCheckboxes.forEach(function(itemCheckbox) {
            itemCheckbox.addEventListener("change", function() {
                handleItemSelection();
            });
        });
    }


    if (quantityInput) {
        quantityInput.addEventListener("change", function() {
            handleItemSelection();
        });
    }
});
