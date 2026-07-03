/*
============================================
Expense Tracker - script.js
Author: ChatGPT
============================================
*/

// Runs when the page is loaded
document.addEventListener("DOMContentLoaded", function () {

    console.log("Expense Tracker Loaded Successfully!");

    // Get the transaction type dropdown
    const typeSelect = document.querySelector("select[name='type']");

    if (typeSelect) {

        // Function to change dropdown background color
        function updateTypeColor() {

            if (typeSelect.value === "income") {
                typeSelect.style.backgroundColor = "#d4edda";
                typeSelect.style.color = "#155724";
            } else {
                typeSelect.style.backgroundColor = "#f8d7da";
                typeSelect.style.color = "#721c24";
            }

        }

        // Apply color when page loads
        updateTypeColor();

        // Change color whenever the user selects a different option
        typeSelect.addEventListener("change", updateTypeColor);
    }

});


/*
============================================
Delete Confirmation
============================================
*/

function confirmDelete() {

    return confirm(
        "Are you sure you want to delete this transaction?"
    );

}