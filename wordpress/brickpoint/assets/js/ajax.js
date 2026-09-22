(function(){
document.addEventListener('submit',function(e){
var f=e.target;
if(!f||!f.classList||!f.classList.contains('bp-quote-form'))return;
e.preventDefault();
var data=new FormData(f);data.append('action','brickpoint_quote');data.append('nonce',(window.BRICKPOINT&&BRICKPOINT.nonce)||'');
var btn=f.querySelector('[type=submit]');if(btn){btn.disabled=true;}
fetch((window.BRICKPOINT&&BRICKPOINT.ajaxUrl)||'/wp-admin/admin-ajax.php',{method:'POST',body:data,credentials:'same-origin'})
.then(function(r){return r.json();}).then(function(j){
var n=f.querySelector('.bp-form-note');if(n){n.textContent=(j&&j.data)||'';}
if(btn){btn.disabled=false;}
}).catch(function(){if(btn){btn.disabled=false;}});
});
})();
