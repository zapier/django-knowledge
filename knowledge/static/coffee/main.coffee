$(document).ready ->

    $('input.question-search.unclicked').on 'click', ->
        $(@).val('').removeClass('unclicked')