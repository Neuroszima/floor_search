$(document).ready(function () {
   menu_elements = $('.menu_element_container');

   for (var i = 0; i<menu_elements.length; i++) {
       menu_elements[i].addEventListener('click', function () {
           location.href = 'http://127.0.0.1:8000/' + this.id;
       })
   }
});