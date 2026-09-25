(function(){document.addEventListener('DOMContentLoaded',function(){
var t=document.getElementById('bpMenuToggle'),m=document.getElementById('bpMobileMenu');
if(!t||!m)return;
t.addEventListener('click',function(){var open=m.hasAttribute('hidden');if(open){m.removeAttribute('hidden');t.setAttribute('aria-expanded','true');document.body.style.overflow='hidden';}else{m.setAttribute('hidden','');t.setAttribute('aria-expanded','false');document.body.style.overflow='';}});
});})();
