/* activate scrollspy menu */
$('body').scrollspy({
  target: '#main-nav',
  offset: 52
});

$('.blog-side img').addClass('img-responsive')

var $doc = $('html, body');
$('a').click(function() {
    $doc.animate({
        scrollTop: $( $.attr(this, 'href') ).offset().top
    }, 500);
    return false;
});
