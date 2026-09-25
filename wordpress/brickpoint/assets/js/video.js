(function(){document.addEventListener('DOMContentLoaded',function(){
if(window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches){
document.querySelectorAll('video[autoplay]').forEach(function(v){v.removeAttribute('autoplay');v.pause&&v.pause();});
}
});})();
