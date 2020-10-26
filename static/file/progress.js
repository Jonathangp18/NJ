var i = 1;
$('.progress .circle').removeClass().addClass('circle active');
$('.progress .bar').removeClass().addClass('bar');

  $('.progress .circle:nth-of-type(' + i + ')').addClass('active');//te los deja en azul
  
  $('.progress .circle:nth-of-type(' + (i-1) + ')').removeClass('active').addClass('done');//te lo pinta de verde
  
  $('.progress .circle:nth-of-type(' + (i-1) + ') .label').html('&#10003;');//te pone la paloma
  
  $('.progress .bar:nth-of-type(' + (i-1) + ')').addClass('active');
  
  $('.progress .bar:nth-of-type(' + (i-2) + ')').removeClass('active').addClass('done');
  
  i++;
  
  if (i==0) {
    $('.progress .bar').removeClass().addClass('bar');
    $('.progress div.circle').removeClass().addClass('circle');
    i = 1;
  };