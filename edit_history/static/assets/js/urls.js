(function() {  
  var $form = $("#new_url_form");

  var urlExists = function(url,success,failure)
  {
      return $.ajax({
        type: 'OPTIONS',
        url : url
      }).always(function(response) {
        if (response.status != 404) {
          success.apply();
        } else {
          failure.apply()
        }

      });
  };

  var submitForm = function() {
    var url = $form.find("#id_title").val();
    $.post($form.attr("action"),$form.serialize()).always(function() {
      NProgress.done();
    });
  };

  var handleError = function() {
    $("#content .flash").html('<div class="alert alert-danger alert-dismissible" role="alert"><button type="button" class="close" data-dismiss="alert"><span aria-hidden="true">&times;</span><span class="sr-only">Close</span></button><strong>Error!</strong> The url you entered does not seem to be valid.</div>');
    NProgress.done();
  };

  $form.submit(function(e) {
    e.preventDefault();
    var url = $form.find("#id_title").val();
    if(url.length) {
      NProgress.start();
      urlExists(url,submitForm,handleError);
    }
    
  });
}).apply();
