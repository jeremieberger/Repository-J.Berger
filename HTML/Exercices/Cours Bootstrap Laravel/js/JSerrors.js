    <div class="container">
      <br>
      <form id="form" novalidate>
        <div class="form-group">
          <label for="nom">Nom</label>
          <input type="text" class="form-control" id="nom" placeholder="Nom" required>
          <div class="invalid-feedback">
            Veuillez entrer un nom
          </div>
        </div>
        <div class="form-group">
          <label for="prenom">Prénom</label>
          <input type="text" class="form-control" id="prenom" placeholder="Prénom" required>
          <div class="invalid-feedback">
            Veuillez entrer un prénom
          </div>
        </div>
        <div class="form-group">
          <label for="prenom">Age</label>
          <input type="number" class="form-control" id="age" value="20" min="20" max="80" required>
          <div class="invalid-feedback">
            Veuillez entrer un nombre compris entre 20 et 80
          </div>
        </div>
        <button class="btn" type="submit">Envoyer</button>
      </form>
    </div>
    <script>
    (function() {
      "use strict"
      window.addEventListener("load", function() {
        var form = document.getElementById("form")
        form.addEventListener("submit", function(event) {
          if (form.checkValidity() == false) {
            event.preventDefault()
            event.stopPropagation()
          }
          form.classList.add("was-validated")
        }, false)
      }, false)
    }())
    </script>