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
    
    $(".modal-header").css("background-color", "#007bff");
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
    $(".modal-header4").css("background-color", "#4b8edb");
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
var estatus = document.getElementById('estatus')
var nombre = document.getElementById('nombre').style.backgroundColor = "#4b8edb"
$(".nombre").css("background-color", "#4b8edb");

});