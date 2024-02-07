#!/usr/bin/node
document.addEventListener('DOMContentLoaded', function () {
  $(document).ready(function () {
    const divAdd = $('DIV#add_item');
    const divRemove = $('DIV#remove_item');
    const divClear = $('DIV#clear_list');
    divAdd.click(function () {
      const item = '<li>Item</li>';
      $('UL.my_list').append(item);
    });
    divRemove.click(function () {
      $('UL.my_list li:last').remove();
    });
    divClear.click(function () {
      $('UL.my_list').empty();
    });
  });
});
