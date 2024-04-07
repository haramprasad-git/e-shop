function sign_up(){
    var inputs = document.querySelectorAll('.input_form_sign');
  document.querySelectorAll('.ul_tabs > li')[0].className=""; 
  document.querySelectorAll('.ul_tabs > li')[1].className="active";
  document.getElementsByName('action')[0].setAttribute('value', 'signup');
  for (let i = 0, elems = document.getElementsByClassName('signup_req'), len = elems.length; i < len; i++) {
    elems[i].setAttribute('required', '')
  }
    
    for(var i = 0; i < inputs.length ; i++  ) {
  inputs[i].setAttribute('autocomplete', 'off')    
  if(i == 3  ){
  
  }else{  
  document.querySelectorAll('.input_form_sign')[i].className = "input_form_sign d_block";
  }
  } 
  
  setTimeout( function(){
  for(var d = 0; d < inputs.length ; d++  ) {
   document.querySelectorAll('.input_form_sign')[d].className = "input_form_sign d_block active_inp";  
     }
  
  
   },100 );
   document.querySelector('.link_forgot_pass').style.opacity = "0";
     document.querySelector('.link_forgot_pass').style.top = "-5px";
     document.querySelector('.btn_sign').innerHTML = "SIGN UP";    
    
    setTimeout(function(){
      document.querySelector('.link_forgot_pass').className = "link_forgot_pass d_none";
    },450);
  
  }
  
  
  
  function log_in(){
    var inputs = document.querySelectorAll('.input_form_sign');
  document.querySelectorAll('.ul_tabs > li')[0].className = "active"; 
  document.querySelectorAll('.ul_tabs > li')[1].className = "";
  document.getElementsByName('action')[0].setAttribute('value', 'login');
  // document.getElementsByName('email')[0].style.marginTop = "2em"
    
    for(var i = 0; i < inputs.length ; i++  ) {
  switch(i) {
      case 1:
   console.log(inputs[i].name);
          break;
      case 3:
   console.log(inputs[i].name);
      default: 
  document.querySelectorAll('.input_form_sign')[i].className = "input_form_sign d_block";
  }
  } 
  
  setTimeout( function(){
  for(var d = 0; d < inputs.length ; d++  ) {
  switch(d) {
      case 1:
   console.log(inputs[d].name);
          break;
      case 3:
   console.log(inputs[d].name);
  
      default:
   document.querySelectorAll('.input_form_sign')[d].className = "input_form_sign d_block";  
   document.querySelectorAll('.input_form_sign')[3].className = "input_form_sign d_block active_inp";  
  
     }
    }
   },100 );
    
    setTimeout(function(){
  document.querySelector('.link_forgot_pass').className = "link_forgot_pass d_block";
  
   },500);
  
    setTimeout(function(){
  
   document.querySelector('.link_forgot_pass').style.opacity = "1";
     document.querySelector('.link_forgot_pass').style.top = "5px";
      
  
  for(var d = 0; d < inputs.length ; d++  ) {
  
  switch(d) {
      case 1:
   console.log(inputs[d].name);
          break;
      case 3:
   console.log(inputs[d].name);
  
           break;
      default:
   document.querySelectorAll('.input_form_sign')[d].className = "input_form_sign";  
  }
    }
     },1500);
     document.querySelector('.btn_sign').innerHTML = "LOG IN";    
  }
  
  
  window.onload =function(){
    document.querySelector('.cont_centrar').className = "cont_centrar cent_active";
  }
  if (window.location.href.includes('#up')) {
    sign_up()
  }