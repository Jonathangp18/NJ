$( document ).ready(function() {
    $('#ready').css('display', 'block').addClass('fadeIn');
  
    setTimeout(function(){
     $('.r2')
      .addClass('slideInUp');
    }, 300);
    setTimeout(function(){
     $('.r3')
      .addClass('slideInUp');
    }, 600);
    setTimeout(function(){
     $('.r1')
      .addClass('slideInUp');
    }, 900);
  
  });