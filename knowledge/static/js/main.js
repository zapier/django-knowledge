
$(document).ready(function() {
  return $('input.question-search.unclicked').on('click', function() {
    return $(this).val('').removeClass('unclicked');
  });
});
