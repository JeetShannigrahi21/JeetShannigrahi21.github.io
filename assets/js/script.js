document.querySelectorAll('a[href^="#"]').forEach(a=>{
  a.addEventListener('click',e=>{
    const href=a.getAttribute('href'); if(!href||href==='#') return;
    const t=document.querySelector(href); if(t){e.preventDefault();t.scrollIntoView({behavior:'smooth',block:'start'});history.pushState(null,'',href);}
  });
});
const y=document.getElementById('year'); if (y) y.textContent=new Date().getFullYear();
