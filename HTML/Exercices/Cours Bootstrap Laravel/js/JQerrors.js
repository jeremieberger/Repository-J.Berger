    $(function () {
      $('form').submit(function(event) {
        if (this.checkValidity() == false) {
          event.preventDefault()
          event.stopPropagation()
        }
        $(this).addClass("was-validated")
      })
    })