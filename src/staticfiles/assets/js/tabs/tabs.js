function openTab(evt, tabName) {
  // Declare all variables
  var i, tabcontent, tablinks;

  // Get all elements with class="tabcontent" and hide them
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }

  // Get all elements with class="tablinks" and remove the class "active"
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }
// Show the current tab, and add an "active" class to the button that opened the tab
  document.getElementById(tabName).style.display = "block";
  evt.currentTarget.className += " active";
}


function openTaba(evt, tabName) {
  // Declare all variables
  var j, tabcontenta, tablinksa;

  
  // section 2

  // Show the current tab, and add an "active" class to the button that opened the tab
  document.getElementById(tabName).style.display = "block";
  evt.currentTarget.className += " activea";

   // Get all elements with class="tabcontent" and hide them
  tabcontenta = document.getElementsByClassName("tabcontenta");
  for (j = 0; j < tabcontenta.length; j++) {
    tabcontenta[j].style.display = "none";
  }

  // Get all elements with class="tablinks" and remove the class "active"
  tablinksa = document.getElementsByClassName("tablinksa");
  for (j = 0; j < tablinksa.length; j++) {
    tablinksa[j].className = tablinksa[j].className.replace(" activea", "");
  }

  // Show the current tab, and add an "active" class to the button that opened the tab
  document.getElementById(tabName).style.display = "block";
  evt.currentTarget.className += " activea";

}

function openTabb(evt, tabName) {
  // Declare all variables

  var k, tabcontentb, tablinksb;


   // section 3

  // Show the current tab, and add an "active" class to the button that opened the tab
  document.getElementById(tabName).style.display = "block";
  evt.currentTarget.className += " activeb";

   // Get all elements with class="tabcontent" and hide them
  tabcontentb = document.getElementsByClassName("tabcontentb");
  for (k = 0; k < tabcontentb.length; k++) {
    tabcontentb[k].style.display = "none";
  }

  // Get all elements with class="tablinks" and remove the class "active"
  tablinksb = document.getElementsByClassName("tablinksb");
  for (k = 0; k < tablinksb.length; k++) {
    tablinksb[k].className = tablinksb[k].className.replace(" activeb", "");
  }

  // Show the current tab, and add an "active" class to the button that opened the tab
  document.getElementById(tabName).style.display = "block";
  evt.currentTarget.className += " activeb";
}