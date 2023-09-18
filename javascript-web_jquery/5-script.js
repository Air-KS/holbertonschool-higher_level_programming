/* global $ */
$(document).ready(function () {
  $('#add_item').click(function () {
    // Compte combiebn d'élément <li> sont déjà présent
    let itemCount = $('.my_list li').length;

    // Ajoute +1 pour obtenir numéro de l'élément
    itemCount++;

    // ajoute le nouvel élement avec le numero
    $('.my_list').append('<li>Item ' + itemCount + '</li>');
  });
});

/*
$(document).ready(function () {
  $('#add_item').click(function () {
    $('.my_list').append('<li>Item</li>');
  })
});
*/
