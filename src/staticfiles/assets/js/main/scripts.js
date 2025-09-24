let body = document.querySelector("body");
let open = document.querySelector(".open");
// let open_2=document.querySelector(".account-2")
// let items = document.querySelector(".account-items");
// let open_cat=document.querySelector(".open-cat");
// let open_cat2=document.querySelector(".category-2");
// let open_sort = document.querySelector(".sort");
// let open_filter = document.querySelector(".filter");
// let close_filter=document.querySelector(".close-filter")
const menuIcon = document.querySelector('.menu-icon');
const leftContainer = document.querySelector('.left-container');
// const backBtn = document.getElementById('back-btn');
const midContainer = document.querySelector('.mid-container');
const nav = document.querySelector('nav');
let prevScrollpos = window.pageYOffset;
let search = document.querySelector(".search-2");
let back = document.querySelector(".search-back")

// opens and closes the search field on smaller screens 
	search.onclick=function(){
			document.querySelector(".search-bar").classList.toggle('activate');
		}
	back.onclick=function(){
			document.querySelector(".search-bar").classList.toggle('activate');
		}

// Hides nav bar on scroll
window.addEventListener('scroll', ()=>{
	let currentScrollpos = window.pageYOffset;

	if(prevScrollpos < currentScrollpos){
		nav.classList.add('hide');
	}else{
	  nav.classList.remove('hide');  
	}
	prevScrollpos = currentScrollpos;
})

// open and close accounts

open.addEventListener('click', ()=>{
	body.classList.toggle("active");
	
})

// open_2.addEventListener('click', ()=>{
// 	body.classList.toggle("active");
	
// })




// Function to open sidebar
function openSidebar() {
  leftContainer.classList.toggle('show');
  document.body.classList.toggle('sidebar-open');
  document.body.classList.toggle('no-scroll'); // Prevent scrolling
}

// Function to close sidebar
function closeSidebar() {
  leftContainer.classList.remove('show');
  document.body.classList.remove('sidebar-open');
  document.body.classList.remove('no-scroll');
}

// Show sidebar
menuIcon.addEventListener('click', openSidebar);

// // Hide sidebar
// backBtn.addEventListener('click', closeSidebar);

window.addEventListener('scroll', function() {
	const header = document.querySelector('.nav-1');
	const navBar = document.querySelector('.nav-2');
	const currentScrollPos = window.pageYOffset;
	const prevScrollPos = window.scrollY || document.documentElement.scrollTop; 

	if (prevScrollPos > currentScrollPos) {
		// Scrolling up
		header.classList.remove('hidden');
		navBar.classList.remove('hidden');
		if(leftContainer){
			leftContainer.classList.remove('move-up')
		}
		
	} else {
		// Scrolling down
		header.classList.add('hidden');
		navBar.classList.add('hidden');
		if(leftContainer){
			leftContainer.classList.add('move-up')
		}
		
	}

	// Update the previous scroll position for the next iteration
	window.scrollY = currentScrollPos; 
});

// Simple animation for the whatsapp community button
document.querySelectorAll('.whatsapp-button').forEach(button => {
	
	button.addEventListener('mouseout', function() {
		if (!this.classList.contains('whatsapp-button-floating')) {
			this.style.transform = 'translateY(0)';
			this.style.boxShadow = '0 5px 15px rgba(37, 211, 102, 0.3)';
		}
	});
});


