// JS code copied from Stripe 
var stripe = Stripe('pk_test_51I8jgAFD24ixF7QTckHP0lc3vwYLcpcNYAYgW1rRGehHKbua3httWQLkiIcwOGgcuPDNe0lBWGR5dwuhyXF9rNhe00ObhaMZDc');
var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var client_secret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripe_public_key);
var elements = elements.create('card');
cart.mount('#card-element');

// Validation errors
cardElement.on('change', function(event) {
  var displayError = document.getElementById('card-errors');
  if (event.error) {
    displayError.textContent = event.error.message;
  } else {
    displayError.textContent = '';
  }
});