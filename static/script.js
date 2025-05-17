const form = document.getElementById('expense-form');
const nameInput = document.getElementById('expense-name');
const amountInput = document.getElementById('expense-amount');
const expenseList = document.getElementById('expense-list');
const totalDisplay = document.getElementById('total');

let total = 0;

form.addEventListener('submit', function(e) {
  e.preventDefault();

  const name = nameInput.value;
  const amount = parseFloat(amountInput.value);

  if (!name || !amount || amount <= 0) {
    alert("Please enter a valid expense name and amount.");
    return;
  }

  // Add to the list
  const li = document.createElement('li');
  li.innerHTML = `${name} <span>₹${amount.toFixed(2)}</span>`;
  expenseList.appendChild(li);

  // Update total
  total += amount;
  totalDisplay.textContent = total.toFixed(2);

  // Clear inputs
  nameInput.value = '';
  amountInput.value = '';
});




  
 


