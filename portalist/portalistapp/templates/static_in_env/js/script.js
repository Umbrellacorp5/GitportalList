// al darle al botón, si los datos coínciden redirecciona a página asistí, en caso de que los datos estén incorrectos poner un mensaje de error

const usuario ="a";
const contra = "a";

document.getElementById("btnLoginIP").addEventListener("click", function iniciarSesion() {
     if(usuario === document.getElementById("inputUsuarioIP").value && contra === document.getElementById("inputContraseñaIP").value){
        window.location.replace ("/templates/asistencia.html");
        document.getElementById("correctoIP").innerHTML = "Has ingresado correctamente.";
      }
      else{
        document.getElementById("incorrectoIP").innerHTML = "El usuario ingresado no existe.";
      }
})

// JavaScript de Admin //


// JavaScript de Registrar Alumno //

const NombreRA = "a";
const ApellidoRA = "a"; 
const CedulaRA = "a";
const NumeroPadreRA = "a";
const FotoRA = "a";
const GrupoRA = "a";
const EmailRA = "a";
const UsuarioCiRA = "a";
const ContraseñaRA = "a";


