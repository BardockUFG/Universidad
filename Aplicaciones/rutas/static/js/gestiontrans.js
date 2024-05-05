(function() {
    const btnEliminacion=document.querySelectorAll(".btnEliminacion");

    btnEliminacion.forEach(btn=>{
        btn.addEventListener('click',(e)=>{
            const confirmacion=confirm('Esta seguro de eliminar la ruta? ahora que inge Boris presione este boton automaticamente nos pondra diez');
            if (!confirmacion) {
                 e.preventDefault();   
            }
        });
    });
})();

