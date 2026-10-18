const header=document.querySelector('.site-header');
const onScroll=()=>header.classList.toggle('scrolled',scrollY>30);
addEventListener('scroll',onScroll,{passive:true});onScroll();
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{threshold:.12});
document.querySelectorAll('main h1,main h2,main p,main figure,.frame,.gallery img,.cutout').forEach((el,i)=>{el.classList.add('reveal');el.style.transitionDelay=(i%4)*70+'ms';io.observe(el)});
