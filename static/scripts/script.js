
function addOnClickRedirect(){
    // toate fisierele care au fost uploadate de catre user
    var fisiere = document.getElementsByTagName("td")

    for (const fisier of fisiere){
        fisier.addEventListener("click", function(e){
            let newUrl = window.location.href + "/" + e.currentTarget.innerText
            // redirectionez pagina catre link-ul de download 
            
            window.location.replace(newUrl)
        })
    }
}

addOnClickRedirect()
