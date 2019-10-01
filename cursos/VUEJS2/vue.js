new Vue({
  el: '#eventos',
  data: {
    contador: 0,
    x: 0,
    y: 0,
    contadorUno: 0,
    contadorDos: 0
  },
  methods: {
    sumarUno: function(){
      this.contador +=1;
    },
    restarUno: function(){
       this.contador -=1;
    },
    alerta: function(mensaje){
      // no le pasamos nada. Ponemos "e" por
      // poner un nombra y poder asignarlo
        alert(mensaje);
    },
    mostrarUbicacion: function(e){
      this.x = e.clientX;
      this.y = e.clientY;
    },
    sumar: function(){
      this.contadorUno++;
    },
    sumarDos: function(cantidad){
      this.contadorDos += cantidad;
    }
  }
})
