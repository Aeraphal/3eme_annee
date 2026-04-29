let produit_id = new URLSearchParams(window.location.search).get("id")
let template_n = document.querySelector('#t_nmonstre');
/*let template_i = document.querySelector('#t_imonstre');*/
let template_l = document.querySelector('#t_lmonstre');
var d1 = document.querySelector("#t1");
/*var d2 = document.querySelector("#t2");*/
var d3 = document.querySelector("#t3");

/*function Firsttime(){*/
    for (const  monstre of monstres) { 
        if (monstre.id_p ==produit_id){   
            let clone_n = document.importNode(template_n.content, true);
        /* let clone_i = document.importNode(template_i.content, true);*/
            let clone_l = document.importNode(template_l.content, true);

            newContent1 = clone_n.firstElementChild.innerHTML 
            .replace(/{{nom_du_monstre}}/g, monstre.race);
            clone_n.firstElementChild.innerHTML = newContent1
            d1.appendChild(clone_n);

            document.getElementById("p7").innerHTML = monstre.minimum_price ;
            

            let img = new Image();   // Crée un nouvel élément Image
            img.src = monstre.image;
            var canvas = document.querySelector("canvas");
            var ctx =canvas.getContext("2d");
            ctx.drawImage(
                img,100,100
            )

            

            /*var image = document.getElementById("image_monstre");
            image.src = monstre.image;*/
            document.getElementById(monstre.id).checked = true
        
        /*
            newContent2 = clone_i.firstElementChild.innerHTML 
            .replace(/{{image}}/g, monstre.image);
            clone_i.firstElementChild.innerHTML = newContent2
            d2.appendChild(clone_i);
        */
            newContent3 = clone_l.firstElementChild.innerHTML 
            .replace(/{{level}}/g, monstre.level);        
            clone_l.firstElementChild.innerHTML = newContent3
            d3.appendChild(clone_l);
        }
    }
/*}*/
/* Tableau pour les prix des armes et des armures */


/* Update des images et position de ceux ci */



class armesjs {
    constructor(
        Image,
        Level,
        Id_arme,
        Id,
        price) {
            this.image =Image;
            this.level = Level;
            this.id_arme = Id_arme;
            this.id = Id;
            this.price = price;
        }
}

class armuresjs {
    constructor(
        Image,
        Level,
        Id_armure,
        Id,
        price) {
            this.image =Image;
            this.level = Level;
            this.id_armure = Id_armure;
            this.id = Id;
            this.price = price;
        }
}

Arc = new armesjs("../../Code/Images/Arc_2.png",4,1,"Arc",1400)
Baton = new armesjs("../../Code/Images/Baton_2.png",8,2,"Baton",12500)
Epee = new armesjs("../../Code/Images/Epee_2.png",4,3,"Epee",1650)


Bottes = new armuresjs("../../Code/Images/Bottes.png",2,1,"Bottes",550)
Boucle_doreille = new armuresjs("../../Code/Images/boucle_doreille.png",7,2,"Boucle_doreille",3500)
Cornes = new armuresjs("../../Code/Images/Cornes.png",12,3,"Cornes",24000)
Epaulettes = new armuresjs("../../Code/Images/Epaulettes.png",3,4,"Epaulettes",650)
Masque = new armuresjs("../../Code/Images/Masque.png",9,5,"Masque",13750)


let armes_tab =[Arc,Baton,Epee]
let armures_tab =[Bottes,Boucle_doreille,Cornes,Epaulettes,Masque]

function draw(){
    var canvas = document.querySelector("canvas");
    var ctx =canvas.getContext("2d");
    for (monstre of monstres) {
        if (document.getElementById(monstre.id).checked){
            let img = new Image();  
            img.src = monstre.image;
            
            ctx.drawImage(
                img,100,100
            )
        }
    }
    for (armes of armes_tab){
        if (document.getElementById(armes.id).checked){
            let img = new Image();  
            img.src = armes.image;
            
            ctx.drawImage(
                img,80,175,100,100
            )
        }
    }
    for (armures of armures_tab){
        if (document.getElementById(armures.id).checked){
            let img = new Image();  
            img.src = armures.image;
            if (armures.id_armure == 1){
                ctx.drawImage(
                    img,130,250,80,80
                )
            }
            if (armures.id_armure == 2){
                ctx.drawImage(
                    img,78,120,100,100
                )
            }
            if (armures.id_armure == 5){
                if(document.getElementById("Goblin").checked){
                    ctx.drawImage(
                        img,115,100,140,130
                    )
                }
                else{
                    ctx.drawImage(
                        img,100,110,160,140
                    )
                }
            }

            if (armures.id_armure == 3){
                ctx.drawImage(
                    img,110,90,100,100
                )
            }
            if (armures.id_armure == 4){
                if(document.getElementById("Goblin").checked){
                    ctx.drawImage(
                        img,175,160,80,80
                    )
                }
                else{
                    ctx.drawImage(
                        img,175,190,80,80
                    )
                }
                
            }
        
                
            
        }
    }  
}     


function price_and_other(){
    var prix=0;
    for (monstre of monstres) {
        if (document.getElementById(monstre.id).checked){
            document.getElementById("p1").innerHTML = monstre.id;
            document.getElementById("p2").innerHTML = "Level:" + monstre.level ;
            prix=prix+Number(monstre.minimum_price)
        }
    }
    console.log(prix)
    for (armes of armes_tab){
        if (document.getElementById(armes.id).checked){
            prix=prix+Number(armes.price)
        }
    }
    for (armures of armures_tab){
        if (document.getElementById(armures.id).checked){
            prix=prix+Number(armures.price)
        }
    }
    nbproduit = document.getElementById('number').value;
    if (Number(nbproduit)>10){
        prix =prix*Number(nbproduit)*90/100
    }
   else{
    prix =prix*Number(nbproduit)
   }
    document.getElementById("p7").innerHTML = prix;

}

function reset2(){
    for (monstre of monstres) {
        if(monstre.id_p ==produit_id){
            document.getElementById(monstre.id).checked = true; 
        }
        else    {
            document.getElementById(monstre.id).checked = false; 
        }  
    }

    for (armes of armes_tab){
        document.getElementById(armes.id).checked = false;
    }
    
    for (armures of armures_tab){
        document.getElementById(armures.id).checked = false;
    }
    document.getElementById('number').value = 1;

    /*clear the canvas*/

}
localStorage.setItem("nb_produit",0)
function addpanier(){
    const mob="";
    const arme="";
    let armure="" ;
    const cout =document.getElementById("p7").Value;
    const quantité= document.getElementById('number').value;

    for (monstre of monstres) {
        if (document.getElementById(armes.id).checked){
            mob = monstre.id
        }
    }
    for (armes of armes_tab){
        if (document.getElementById(armes.id).checked){
            arme=armes.id;
        }
    }
    for (armures of armures_tab){
        if (document.getElementById(armures.id).checked){
            armure = armure+ armures.id;
        }
    }

    let produit={
        nom_monstre:mob,
        nom_arme:arme,
        noms_armures:armure,
        nombre_de_monstre:quantité,
        prix_du_lot:cout,
    }
    localStorage.setItem("produit1","produit")

}