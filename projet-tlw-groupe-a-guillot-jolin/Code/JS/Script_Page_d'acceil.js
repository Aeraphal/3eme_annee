
    
        
/*fonction des filtres*/
function filtres_prix (){
    max=document.getElementById("filtre_max").valueAsNumber;
    min=document.getElementById("filtre_min").valueAsNumber;
    for (monstre of monstres) {
        if ((min>monstre.maximum_price)||(max<monstre.minimum_price)||(max<min)){
            document.getElementById(monstre.id).style.display = 'none';

        }
        
        else{
            document.getElementById(monstre.id).style.display = '';
        }  
        }
    }
