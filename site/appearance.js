(() => {
 'use strict';
 const root=document.documentElement;
 const current=()=>root.dataset.appearance==='persona'?'persona':'calm';
 const apply=value=>{
   root.dataset.appearance=value==='persona'?'persona':'calm';
   document.querySelectorAll('[data-appearance]').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.appearance===current())));
   document.querySelector('meta[name="theme-color"]')?.setAttribute('content',current()==='persona'?'#111116':'#5146dc');
 };
 try{apply(localStorage.getItem('course-appearance'));}catch{apply('calm');}
 document.querySelectorAll('[data-appearance-slot]').forEach(slot=>{
   slot.innerHTML='<div class="appearance-picker" role="group" aria-label="Appearance"><button type="button" data-appearance="calm" title="Calm appearance">Calm</button><button type="button" data-appearance="persona" title="Persona inspired appearance">Persona</button></div>';
 });
 apply(current());
 document.addEventListener('click',event=>{
   const button=event.target.closest('[data-appearance]');if(!button)return;
   apply(button.dataset.appearance);
   try{localStorage.setItem('course-appearance',current());}catch{}
 });
 window.addEventListener('storage',event=>{if(event.key==='course-appearance')apply(event.newValue);});
})();
