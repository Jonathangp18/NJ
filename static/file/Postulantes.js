$(document).ready(function(){
    tablaPersonas = $("#tablaPersonas").DataTable({
       "columnDefs":[{
        "targets": -1
        
         
       }],
        
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
    
    $(document).on("click", ".btnEditar", function(){
    $("#formPersonas").trigger("reset");
    $(".modal-header").css("background-color", "#87CEFA");
    $(".modal-header").css("color", "white");
    $(".modal-title").text("¿Seguro que deseas responder?");            
    $("#modalCRUD").modal("show");  
    fila = $(this).closest("tr");
    nombre = fila.find('td:eq(11)').text(); 
    $("#nombre").val(nombre);  
    id=null;
    opcion = 1; //alta

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

$(document).on("click", "#btnGuardar", function(){
    console.log("dentro1")
    $("#modalCRUD").modal("hide");
    $("#modalCRUD80").modal("show");
    
});

$(document).on("click", "#btnGuardar2", function(){
    console.log("dentro1")
    $("#modalCRUD2").modal("hide");
    $("#modalCRUD80").modal("show");
    
});

//PARAALERTA DE COMENTARIO
$(document).on("click", ".btn80", function(){
    console.log("dentro1")
    $("#modalCRUD4").modal("hide");
    $("#modalCRUD80").modal("show");
    
});
//PARAALERTA DE editar
$(document).on("click", "#btn81", function(){
    console.log("dentro")
    $("#modalCRUD3").modal("hide");
    $("#modalCRUD80").modal("show");
    
});

$(document).on("click", ".btndash", function(){
    console.log("dentro")
    $("#modalCRUD80").modal("show");
    
});

$(document).on("click", ".btn900", function(){
    console.log("dentro")
    $("#modalCRUD88").modal("hide");
    $("#modalCRUD80").modal("show");
    
});


$(document).on("click", ".btnBorrar", function(){
    $("#formPersonas").trigger("reset");
    $(".modal-header").css("background-color", "#ff4500");
    $(".modal-header").css("color", "white");
    $(".modal-title").text("¿Seguro que deseas rechazar?");            
    $("#modalCRUD2").modal("show");  
    fila = $(this).closest("tr");
    nombre = fila.find('td:eq(11)').text(); 
    $("#nombre2").val(nombre);     
    id=null;
    opcion = 1; //alta
});

//Para comentarios cognitives 
$(document).on("click", ".btnComentar", function(){    
    $("#formPersonas55").trigger("reset");
    $(".modal-header").css("background-color", "#87CEFA");
    $(".modal-header").css("align","center");
    $(".modal-header").css("color", "white");
    $(".modal-title").text("Escribe los comentarios sobre el postulante");            
    $("#modalCRUD4").modal("show"); 

    fila = $(this).closest("tr");  
    $("#comentar").val();
    nombree = fila.find('td:eq(0)').text(); 
    $("#iddd").val(nombree); 
    nombree = fila.find('td:eq(1)').text(); 
    $("#nombre100").val(nombree); 
    id=null;
    opcion= 1;
});

//Para ver comentarios
$(document).on("click", ".btnCom", function(){    
    $("#formPersonas56").trigger("reset");
    $(".modal-header").css("background-color", "#87CEFA");
    $(".modal-header").css("align","center");
    $(".modal-header").css("color", "white");
    $(".modal-title").text("Comentarios anteriores de las entrevistas");            
    $("#modalCRUD3").modal("hide"); 
    $("#modalCRUD88").modal("show"); 

    fila = $(this).closest("tr");  
    nombre = fila.find('td:eq(15)').text();
    $("#idddq").val($("#nombre90").val()); 
    $("#nombreeeq").val($("#nombre77").val());  
    $("#comentarq").val($("#nombre55").val()); 
    id=null;
    opcion= 1;
   
       
});
 //capturar la fila para editar o borrar el registro

//$(document).on("click", ".btnComentar", function(){
 //*   fila = $(this).closest("tr");
  //  nombre = fila.find('td:eq(0)').text(); 
   // $("#nombre6").val(nombre); 
    //window.location.href = "/a?id="+nombre
    //id=null;
   // opcion = 1; //alta

//}); 
/* var boton=document.getElementById('btnn1');
boton.addEventListener("click", function(){
    console.log("hola")
    var info77 =document.getElementById('nombre77').value;
    var info78 =document.getElementById('nombre78').value;
    var info79 =document.getElementById('nombre79').value;
    var info80 =document.getElementById('nombre80').value;
    var info81 =document.getElementById('nombre81').value;
    var info3 =document.getElementById('nombre3').value;
    var info4 =document.getElementById('nombre4').value;
    var info5 =document.getElementById('nombre5').value;
    var info6 =document.getElementById('nombre6').value;
    var info7 =document.getElementById('nombre7').value;
    var info8 =document.getElementById('nombre8').value;
    var info9 =document.getElementById('nombre9').value;
    var info90 =document.getElementById('nombre90').value;
    var info600 =document.getElementById('nombre600').value;
  
    var xmlttp=new XMLHttpRequest();
    xmlttp.open("POST", '/editar', true);
    console.log("post")
    xmlttp.setRequestHeader('content-type','application/x-www-form-urlencoded;charset=UTF-8');
    console.log("dwhat")
    xmlttp.send("nm="+ info77+ "vacante=" +info600+ "edad=" +info79+ "dir="+ info80 + "lic="+ info81+ "uni="+ info7+ "prom="+ info8 + "idio="+ info9 + "email="+ info78 + "tele="+ info5 + "cur="+ info4 + "exp="+ info3 + "apt="+ info6 + "id="+ info90);
    console.log("fiiin")

});*/

$(document).on("click", ".btnDetalle", function l(){    
    $("#formPersonas3").trigger("reset");
    $(".modal-header").css("background-color", "#87CEFA");
    $(".modal-header").css("color", "white");
    $(".modal-title").css("align","center");
    $(".modal-title").text("Editar Postulante");            
    $("#modalCRUD3").modal("show");  
    fila = $(this).closest("tr");

    nombre1 = fila.find('td:eq(1)').text(); 
    $("#nombre77").val(nombre1); 
    nombre2 = fila.find('td:eq(11)').text(); 
    $("#nombre78").val(nombre2); 
    nombre3 = fila.find('td:eq(2)').text(); 
    $("#nombre79").val(nombre3); 
    nombre4 = fila.find('td:eq(3)').text(); 
    $("#nombre80").val(nombre4); 
    nombre5 = fila.find('td:eq(4)').text(); 
    $("#nombre81").val(nombre5); 

    nombre = fila.find('td:eq(5)').text(); 
    $("#nombre7").val(nombre); 
    
    expe = fila.find('td:eq(6)').text();
    $("#nombre8").val(expe); 
    curso = fila.find('td:eq(7)').text();
    $("#nombre9").val(curso); 
    idio = fila.find('td:eq(8)').text();
    $("#nombre3").val(idio);
    Esc = fila.find('td:eq(9)').text();
    $("#nombre4").val(Esc); 
    Lic = fila.find('td:eq(12)').text();
    $("#nombre5").val(Lic);  

    prom = fila.find('td:eq(10)').text();
    $("#nombre6").val(prom);  
    prom2 = fila.find('td:eq(14)').text();
    $("#nombre600").val(prom2);  
    prom55 = fila.find('td:eq(15)').text();
    $("#nombre55").val(prom55);
    console.log(prom55)
    prom3 = fila.find('td:eq(0)').text();
    $("#nombre90").val(prom3); 
    opcion = 1; //alta
       
});
     /*  
    e.preventDefault();    
    nombre = $.trim($("#nombre").val());
    pais = $.trim($("#pais").val());
    edad = $.trim($("#edad").val());    
    $.ajax({
        url: "bd/crud.php",
        type: "POST",
        dataType: "json",
        data: {nombre:nombre, pais:pais, edad:edad, id:id, opcion:opcion},
        success: function(data){  
            console.log(data);
            id = data[0].id;            
            nombre = data[0].nombre;
            pais = data[0].pais;
            edad = data[0].edad;
            if(opcion == 1){tablaPersonas.row.add([id,nombre,pais,edad]).draw();}
            else{tablaPersonas.row(fila).data([id,nombre,pais,edad]).draw();}            
        }        
    });
    $("#modalCRUD").modal("hide");    
    
}); */   
var estatus = document.getElementById('estatus')
var nombre = document.getElementById('nombre').style.backgroundColor = "#4b8edb"
$(".nombre").css("background-color", "#4b8edb");

});