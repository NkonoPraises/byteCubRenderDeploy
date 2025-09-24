const mobileMenuButton = document.querySelector('.mobile-menu-toggle');
const primaryNavigation = document.querySelector('#primary-navigation');

mobileMenuButton.addEventListener('click', () => {
  const visibility = primaryNavigation.getAttribute('data-visible');

  if (visibility === "false") {
    primaryNavigation.setAttribute('data-visible', true);
    mobileMenuButton.setAttribute('aria-expanded', true);
  } else if (visibility === "true") {
    primaryNavigation.setAttribute('data-visible', false);
    mobileMenuButton.setAttribute('aria-expanded', false);
  }
})