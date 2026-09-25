(function(){document.addEventListener('DOMContentLoaded',function(){
if(!('IntersectionObserver' in window))return;
var els=document.querySelectorAll('.reveal');
var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('visible');io.unobserve(e.target);}});},{threshold:.12});
els.forEach(function(el){io.observe(el);});
});})();
