var btn_generate = document.getElementById("btn_generate_key");
var inp_key = document.getElementById("inp_key");

// Function to generate random api key from characters
function generete_key() {
  var characters = "abcdefghijklmnopqrstuvwyxz0123456789";
  var key = "";

  for (var i = 0; i < 26; i++) {
    var random_number = Math.floor(Math.random() * characters.length);
    key += characters[random_number];
  }

  return key;
}

// when generate btn clicks run this
btn_generate.addEventListener("click", function (e) {
  e.preventDefault();

  var key = generete_key();
  inp_key.value = key;
});
