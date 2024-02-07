#!/usr/bin/node
$(document).ready(function () {
  const header = $('#update_header');
  header.click(function () {
    header.html('New Header!!!');
  });
});
