const nav = document.querySelector('nav');
let prevScrollpos = window.pageYOffset;

window.addEventListener('scroll', ()=>{
	let currentScrollpos = window.pageYOffset;

	if(prevScrollpos < currentScrollpos){
		nav.classList.add('hide');
	}else{
	  nav.classList.remove('hide');  
	}
	prevScrollpos = currentScrollpos;
})