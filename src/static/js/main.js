

function confirmDelete(){
    const ok = confirm("Are You Sure? ") //a pop up
    if(!ok){
        event.preventDefault()
    }
}


const errorSpan = document.querySelector('.error');
if(errorSpan){
    setTimeout(()=>{
        errorSpan.parentNode.removeChild(errorSpan)
    },4000); 
}

function saveUser(user){
    let email = document.getElementById('email').value;
    localStorage.setItem("email", email)
    alert(user.firstname);
}