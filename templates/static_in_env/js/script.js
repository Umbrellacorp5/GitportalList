// al darle al botón, si los datos coínciden redirecciona a página asistí, en caso de que los datos estén incorrectos poner un mensaje de error

const usuario ="a";
const contra = "a";

document.getElementById("btnLoginIP").addEventListener("click", function iniciarSesion() {
     if(usuario === document.getElementById("inputUsuarioIP").value && contra === document.getElementById("inputContraseñaIP").value){
        window.location.replace ("/templates/asistencia.html");
        alert("correcto")
      }
      else{
        alert("incorrecto")
      }
})
