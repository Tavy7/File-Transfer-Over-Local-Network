user = ""
user = JSON.parse(window.localStorage.getItem('user'))

window.addEventListener('keydown', (e) => {
    if (e.which == 13) {
        var inputValue = document.getElementsByTagName('input')[0].value

        if (user == null){
            user = inputValue
        }

        document.getElementsByClassName('login')[0].style.display='none'

        window.localStorage.setItem('user', JSON.stringify(user))
        newUrl = window.location.href + user
        window.location.replace(newUrl)
    }
})

window.onload = function(){
    console.log(user)
    if (user != null){
        // daca a existat acces pe aplicatie
        document.getElementsByClassName('login')[0].style.display='none'
    
        let addr = window.location.href
        if (addr.includes('redirect')){
            return
        }
            
        // username-ul
        let match = addr.substring(addr.length - user.length, addr.length)

        // daca user exista dar inca e pe adresa de baza
        if (user != match){
            newUrl = window.location.href
            if (newUrl[newUrl.length - 1] != '/'){
                newUrl += '/'
            } 

            newUrl += user
            window.location.replace(newUrl)
       }
    }
}