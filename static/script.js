let totalPunti = 0;

function aggiungiPunti(valore) {
    totalPunti += valore;
    
    // Animazione numerica
    const elementoPunti = document.getElementById('punti');
    elementoPunti.innerText = totalPunti;
    
    // Effetto "pop" visivo
    elementoPunti.style.transform = "scale(1.2)";
    elementoPunti.style.color = "#15803d";
    
    setTimeout(() => {
        elementoPunti.style.transform = "scale(1)";
        elementoPunti.style.color = "#22c55e";
    }, 200);
}