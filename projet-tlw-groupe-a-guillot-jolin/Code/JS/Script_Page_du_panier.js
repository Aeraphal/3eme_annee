/*reset*/
let questions = ["Adresse","Ville","Pays","Tel","Mail","Prenom","Nom","Date"]

function reset1(){
    for (const question of questions) {
        document.getElementById(question).value = "";
    }
}