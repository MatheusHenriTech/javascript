const long=document.getElementById("long")
const lati=document.getElementById("lati")

if(navigator.geolocation){

    navigator.geolocation.getCurrentPosition(mostrarLocalização,erroLocalização)

}else{
    console.log("Geolocalização não suportada")
}

function mostrarLocalização(pos){
    long.innerHTML=pos.coords.longitude
    lati.innerHTML=pos.coords.latitude
}

function erroLocalização(){
    console.log("Erro ao obter a localização")
}

