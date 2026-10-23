const header=document.querySelector('.site-header');
const onScroll=()=>header.classList.toggle('scrolled',scrollY>30);
addEventListener('scroll',onScroll,{passive:true});onScroll();
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{threshold:.12});
document.querySelectorAll('main h1,main h2,main p,main figure,.frame,.gallery img,.cutout').forEach((el,i)=>{el.classList.add('reveal');el.style.transitionDelay=(i%4)*70+'ms';io.observe(el)});

/* Contact button: copy the email address instead of opening a mail app */
document.querySelectorAll('.contact[data-email]').forEach(b=>{
  b.addEventListener('click',async e=>{
    e.preventDefault();
    const email=b.dataset.email,label=b.textContent;let ok=false;
    try{await navigator.clipboard.writeText(email);ok=true}
    catch(_){const t=document.createElement('textarea');t.value=email;t.style.cssText='position:fixed;opacity:0';document.body.appendChild(t);t.select();try{ok=document.execCommand('copy')}catch(_){}t.remove()}
    b.textContent=ok?'Email copied!':email;
    setTimeout(()=>{b.textContent=label},2500);
  });
});
