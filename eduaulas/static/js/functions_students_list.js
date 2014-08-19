$(document).ready(ini);


function ini(){

	get_students_data();
}

function get_students_data () {

    var code_class = $("#code").attr("value");
    var tok = $("#token").attr("value");
    var query = $.ajax({
    url:"/alumnos/listas/"+code_class+"/obtener" ,
    type:'POST',
    dataType:"json",
    data:{
    	  csrfmiddlewaretoken: tok,
          state:'inactive',
          matriz:'matriz',
          quantity_results:'quantity_results',
          quantity_students:'quantity_students'

    }, 

    "success":function(data){
        create_table_students(data);

      }

    })
  
} /*cierro function get_students_data*/



function create_table_students (data) {


var code_class = $("#code").attr("value");
if(data['type'] == 'success'){  
    //var output_thead = "";
    var output = "";

    /*output_thead +='<tr>';
    output_thead +='<th>Nombre</th>';                                                   
    output_thead +='<th>Promedio meta cognitivo</th>';
    output_thead +='<th>Promedio cognitivo</th>';
    output_thead +='<th>Promedio socio afectivo</th>';
    output_thead +='<th>% promedio academico</th>';
    output_thead +='</tr>';*/

    for (var x in (data["matriz"])){
    	output += "<tr>";
	    for (var y = 1; y < (data["matriz"])[x].length; y++){
	      
	        if (y == 1){
	          output += "<td ><a target='blank' href='/alumnos/info_alumno/"+code_class+"/"+(data["matriz"])[x][0]+"'>"+(data["matriz"])[x][y]+"</a></td>";}
	          
	        else {
	          
	          output += '<td>';
	          output +=  (data["matriz"])[x][y];
	          output += '</td>';}

	     
   }/*cierro for dictionary_students*/
    
    output += "</tr>";
       
  var txt = "<p>Para estos datos se evaluaron " +(data["quantity_results"]) +" ejercicios, de "+ (data["quantity_students"]) +" alumnos.</p>" ;    
    if (output != ""){
     // $("#dt_students > thead").html(output_thead);
      $("#dt_students > tbody ").html(output);
      
      $("#dt_students").dataTable();

      /*$("#dt_students").dataTable({

            "language":{
              "emptyTable":     "No hay datos en la tabla",
              "info":           "Mostrando _START_ a _END_ de _TOTAL_ datos",
              "infoEmpty":      "Mostrando 0 a 0 de 0 datos",
              "infoFiltered":   "(filtrado de _MAX_ entradas)",
              "infoPostFix":    "",
              "thousands":      ",",
              "lengthMenu":     "Mostrando _MENU_ entradas",
              "loadingRecords": "Cargando...",
              "processing":     "Procesando...",
              "search":         "Buscar:",
              "zeroRecords":    "No hubo coincidencias",
              "paginate": {
                  "first":      "Primero",
                  "last":       "Ultimo",
                  "next":       "Siguiente",
                  "previous":   "Previo"
              },
              "aria": {
                  "sortAscending":  ": ordenar la columna en forma ascendente",
                  "sortDescending": ": ordenar la columna en forma descendente"
              }
            }
          });
      $("#more_info_stats_students").html(txt);*/
   
    }

     }
    }
}

