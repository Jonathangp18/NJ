$(document).ready(function(){
    tablaPersonas = $("#tablaPersonas").DataTable({
        
        //Para cambiar el lenguaje a español
    "language": {
            "lengthMenu": "Mostrar _MENU_ registros",
            "zeroRecords": "No se encontraron resultados",
            "info": "Mostrando registros del _START_ al _END_ de un total de _TOTAL_ registros",
            "infoEmpty": "Mostrando registros del 0 al 0 de un total de 0 registros",
            "infoFiltered": "(filtrado de un total de _MAX_ registros)",
            "sSearch": "Buscar:",
            "oPaginate": {
                "sFirst": "Primero",
                "sLast":"Último",
                "sNext":"Siguiente",
                "sPrevious": "Anterior"
             },
             "sProcessing":"Procesando...",
        }
    });
    
    
    $(document).on("click", ".btnAbrir", function(){
    $("#formPersonas").trigger("reset");
    $(".modal-header").css("background-color", "rgb(42, 224, 26)");
    $(".modal-header").css("color", "white");
    $(".modal-title").text("¿Seguro que deseas abrir la vacante?");            
    $("#modalCRUD").modal("show");  
    fila = $(this).closest("tr");
    nombre = fila.find('td:eq(0)').text(); 
    $("#nombre").val(nombre);  
    id=null;
    opcion = 1; //alta

    }); 

    $(document).on("click", ".btnpostu", function(){
        $("#formPersonas7").trigger("reset");
        $(".modal-header7").css("background-color", "#87CEFA");
        $(".modal-header7").css("color", "white");
        $(".modal-title7").text("Postulantes");            
        $("#modalCRUD7").modal("show");  
        fila = $(this).closest("tr");
        Pendientes = fila.find('td:eq(3)').text(); 
        Entrevistados = fila.find('td:eq(4)').text(); 
        Aceptados = fila.find('td:eq(5)').text(); 
        Rechazados = fila.find('td:eq(6)').text(); 
        $("#pendientess").val(Pendientes);
        $("#entrevistados").val(Entrevistados); 
        $("#aceptados").val(Aceptados); 
        $("#rechazadoss").val(Rechazados);   
        id=null;
        opcion = 1; //alta
    
        }); 
    

$(document).on("click", "#btAbrir", function(){
    fila = $(this).closest("tr");
    nombre = fila.find('td:eq(0)').text(); 
    var nombre1 = $("#nombre").val();
    var texto = {"vacante": nombre1}
    console.log(nombre);
    
    $.ajax({
        url: '/openvac',
        method: 'POST',
        headers:{
            'Content-type':'application/json'
        },
        dataType: 'text',
        data: JSON.stringify(texto),
        success: function(data){
     
            window.location.reload();
        

        }
    });
    console.log("hola");
    $("#modalCRUD").modal("hide");
    $("#modalCRUD3").modal("show");  
     
     //alta
});
    

var fila; //capturar la fila para editar o borrar el registro

$(document).on("click", ".btnwarning", function(){
    fila = $(this).closest("tr");
    nombre = fila.find('td:eq(0)').text(); 
    $("#nombre6").val(nombre); 
    window.location.href = "/edit?id="+nombre
    id=null;
    opcion = 1; //alta

}); 
//botón EDITAR    
$(document).on("click", ".btnEdita", function(){
    fila = $(this).closest("tr");
    id = parseInt(fila.find('td:eq(0)').text());
    nombre = fila.find('td:eq(1)').text();
    pais = fila.find('td:eq(2)').text();
    edad = parseInt(fila.find('td:eq(3)').text());
    $("#nombre").val(nombre);
    $("#pais").val(pais);
    $("#edad").val(edad);
    opcion = 2; //editar
    
    $(".modal-header").css("background-color", "#122548");
    $(".modal-header").css("color", "white");
    $(".modal-title").text("Editar Persona");            
    $("#modalCRUD").modal("show");  
    
});

//botón BORRAR
$(document).on("click", ".btnBorrar", function(){
    $("#formPersonas2").trigger("reset");
    $(".modal-header2").css("background-color", "#ff4500");
    $(".modal-header2").css("color", "white");
    $(".modal-title2").text("¿Seguro que deseas cerrar la vacante?");            
    $("#modalCRUD2").modal("show");  
    fila = $(this).closest("tr");
    nombre = fila.find('td:eq(0)').text(); 
    $("#nombre2").val(nombre); 
    id=null;
    opcion = 1; //alta
});





$(document).on("click", "#btnCerrar", function(){
    fila = $(this).closest("tr");
    nombre = fila.find('td:eq(0)').val();
    var nombre1 = $("#nombre2").val();
    var texto = {"vacante": nombre1}
    console.log(nombre);
    
    $.ajax({
        url: '/closevac',
        method: 'POST',
        headers:{
            'Content-type':'application/json'
        },
        dataType: 'text',
        data: JSON.stringify(texto),
        success: function(data){
            window.location.reload();

        }
    });
    console.log("hola");
    $("#modalCRUD2").modal("hide"); 
    $("#modalCRUD3").modal("show");  
     //alta
});
/*var boton = document.getElementById('btnCerrar');
 boton.addEventListener("click", function(){
    fila = $(this).closest("tr");
    nombre = fila.find('td:eq(0)').text();
    var nm = "Becario de TI";
    var texto = {"vacante" : nm};
    console.log(texto);
    $.ajax({
        url: '/closevac',
        method: 'POST',
        headers:{
            'Content type':'application/json'
        },
        dataType: 'text',
        data: JSON.stringify(texto),
        success: function(texto){
            alert(texto);
        }
    });


 });*/

$(document).on("click", ".btnvac", function(){    
    $("#formPersonas4").trigger("reset");
    $(".modal-header4").css("background-color", "#122548");
    $(".modal-header4").css("color", "white");
    $(".modal-title4").text("Editar vacante o ver postulantes");            
    $("#modalCRUD4").modal("show");  
    fila = $(this).closest("tr");
    nombre = fila.find('td:eq(0)').text(); 
    nombre2 = fila.find('td:eq(2)').text(); 
    $("#nombre3").val(nombre); 
    $("#nombre4").val(nombre2); 
       
});
$(document).on("click", ".btnguardar", function(){
    var nombre1 = $("#nombre3").val();
    var nombre2 = $("#nombre4").val();
    var texto = {"vacante": nombre1, "Id": nombre2}
    $.ajax({
        url: '/editvac',
        method: 'POST',
        headers:{
            'Content-type':'application/json'
        },
        dataType: 'text',
        data: JSON.stringify(texto),
        success: function(data){
            window.location.reload();

        }
    });  
    $("#modalCRUD4").modal("hide");
    $("#modalCRUD3").modal("show"); 
    

                 
});

$(document).on("click", ".btndash", function(){
    console.log("dentro")
    $("#modalCRUD3").modal("show");
    
});

$(document).on("click", "#winner", function(){
    console.log("dentro")
    $("#modalCRUD3").modal("show");
    
});

$(document).on("click", ".btnpost", function(){ 
    $("#modalCRUD4").modal("hide");
    $("#modalCRUD3").modal("show");                 
});

$("#formPersonas2").submit(function(e){
    e.preventDefault();    
    fila = $(this).closest("tr");
    nombre = fila.find('td:eq(0)').text();
    var nm = "Becario de TI";
    var texto = {"vacante" : nm};
    console.log(texto);
    $.ajax({
        url: '/closevac',
        method: 'POST',
        headers:{
            'Content type':'application/json'
        },
        dataType: 'text',
        data: JSON.stringify(texto),
        success: function(texto){
            alert(texto);
        }
    });
    $("#modalCRUD").modal("hide");    
    
}); 


$(document).on("click", "#closee", function(){
    var texto = {"vacante" : "prueba"};
    $.ajax({
        url: '/skipp',
        method: 'POST',
        headers:{
            'Content-type':'application/json'
        },
        dataType: 'text',
        data: JSON.stringify(texto),
        success: function(texto){
            $("#modalCRUD5").modal("hide"); 
            $("#modalCRUD6").modal("hide");
        }
    });        

  });

  $(document).on("click", ".modall-btn", function(){
    $("#modalCRUD5").modal("hide");
    $("#modalCRUD6").modal("hide");  
    $("#modalCRUD3").modal("show");  
    
  });

var estatus = document.getElementById('estatus')
var nombre = document.getElementById('nombre').style.backgroundColor = "#122548"
$(".nombre").css("background-color", "#122548");

var win = $("#win").val();

if(win == "cerrada"){
    $("#modalCRUD5").modal("show");
}

if(win == "cerradanoprimero"){
    $("#modalCRUD6").modal("show");
}

for(i=0; i<200; i++) {
    // Random rotation
    var randomRotation = Math.floor(Math.random() * 360);
    // Random width & height between 0 and viewport
    var randomWidth = Math.floor(Math.random() * Math.max(document.documentElement.clientWidth, window.innerWidth || 0));
    var randomHeight =  Math.floor(Math.random() * Math.max(document.documentElement.clientHeight, window.innerHeight || 0));
    
    // Random animation-delay
    var randomAnimationDelay = Math.floor(Math.random() * 10);
    console.log(randomAnimationDelay)
  
    // Random colors
    var colors = ['#0CD977', '#FF1C1C', '#FF93DE', '#5767ED', '#FFC61C', '#8497B0']
    var randomColor = colors[Math.floor(Math.random() * colors.length)];
  
    // Create confetti piece
    var confetti = document.createElement('div');
    confetti.className = 'confetti';
    confetti.style.top=randomHeight + 'px';
    confetti.style.left=randomWidth + 'px';
    confetti.style.backgroundColor=randomColor;
    confetti.style.transform='skew(15deg) rotate(' + randomRotation + 'deg)';
    confetti.style.animationDelay=randomAnimationDelay + 's';
    document.getElementById("confetti-wrapper").appendChild(confetti);
  }

});

var man = $("#man").val();
if(man == 2){
    $("#modalCRUD55").modal("show");  
    
}

$(document).on("click", "#btncerrarrr", function(){           
    
    var texto = {"vacante" : "prueba"}; 
    $.ajax({
        url: '/sumsession',
        method: 'POST',
        headers:{
            'Content-type':'application/json'
        },
        dataType: 'text',
        data: JSON.stringify(texto),
        success: function(texto){
            $("#modalCRUD55").modal("hide"); 
        }
    }); 
});