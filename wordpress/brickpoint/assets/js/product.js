(function(){document.addEventListener('DOMContentLoaded',function(){
document.querySelectorAll('.bp-thumbs img').forEach(function(th){
th.style.cursor='pointer';
th.addEventListener('click',function(){
var main=document.querySelector('.bp-product-img');
if(main){var s=main.src;main.src=th.src;th.src=s;}
});
});
});})();
