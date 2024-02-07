#!/usr/bin/node
$(document).ready(function () {
  const list = $('#add_item');
  list.click(function () {
    const item = '<li>Item</li>';
    $('UL.my_list').append(item);
  });
});
