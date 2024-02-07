#!/usr/bin/node
$(document).ready(function () {
  const header = $('header');

  if (header.hasClass('red')) {
    header.removeClass('green');
  } else if (header.hasClass('green')) {
    header.removeClass('red');
  } else {
    header.addClass('red');
  }

  header.click(function () {
    if (header.addClass('red')) {
      header.removeClass('red');
      header.addClass('green');
    }
  });
});
