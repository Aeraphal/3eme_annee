/*Bouton retour en haut*/
window.addEventListener("scroll", function(){
    document.getElementById('boutonback').style.visibility = 'visible';
    let P =window.pageYOffset
    if (P==0){document.getElementById('boutonback').style.visibility = 'hidden';}
    })

/*mise en commun du footer et header*/
fetch("./header.fakehtml")
    .then(data => data.text())
    .then(html =>document.getElementById('h1').innerHTML = html);


fetch("./footer.fakehtml")
    .then(data => data.text())
    .then(html =>document.getElementById('f1').innerHTML = html);

/*Classes*/
class monsterjs {
    constructor(
        Image,
        Level,
        Id_produit,
        Id,
        Race,
        Maximum_price,
        Minimum_price) {
            this.image =Image;
            this.level = Level;
            this.id_p = Id_produit;
            this.id = Id;
            this.race = Race;
            this.maximum_price = Maximum_price;
            this.minimum_price = Minimum_price;
        }
}

Goblin= new monsterjs("../../Code/Images/Goblin_retouche.png",5,1,"Goblin","Goblin",450,150);
Loup_Garou= new monsterjs("../../Code/Images/Loupgarou.png",25,2,"Loup_Garou","Loup_Garou",1200,250);
Naga= new monsterjs ("../../Code/Images/Naga.png",15,3,"Naga","Naga",1500,200)
/*Ghoul= new monster("../../Code/Images/Yoru_MoonGain.png",10,4,"Ghoul","Ghoul",350,50)
Ogre= new monster("../../Code/Images/Yoru_MoonGain.png",35,5,"Ogre","Ogre",15000,500)
Gargouille= new monster("../../Code/Images/Yoru_MoonGain.png",20,6,"Gargouille","Gargouille",1200,150)
*/

let monstres = [Goblin,Loup_Garou,Naga,]