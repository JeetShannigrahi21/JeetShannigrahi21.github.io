document.querySelectorAll('a[href^="#"]').forEach(a=>{
  a.addEventListener('click',e=>{
    const href=a.getAttribute('href'); if(!href||href==='#') return;
    const t=document.querySelector(href); if(t){e.preventDefault();t.scrollIntoView({behavior:'smooth',block:'start'});history.pushState(null,'',href);}
  });
});
const y=document.getElementById('year'); if (y) y.textContent=new Date().getFullYear();

const visitorEl=document.getElementById('visitor-count');
if(visitorEl){
  const endpoint='https://api.countapi.xyz/hit/jeetshannigrahi21.github.io/visits';
  fetch(endpoint)
    .then(r=>r.ok?r.json():Promise.reject())
    .then(data=>{
      if(typeof data.value==='number'){
        visitorEl.textContent=data.value.toLocaleString('en-US');
      }else{
        visitorEl.textContent='—';
      }
    })
    .catch(()=>{visitorEl.textContent='—';});
}
