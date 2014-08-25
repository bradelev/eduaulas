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


    for (var x in (data["matriz"])){
    	output += "<tr>";
	    for (var y = 1; y < (data["matriz"])[x].length; y++){
	      
	        if (y == 1){
	          output += "<td ><a target='blank' href='/alumnos/info_alumno/"+code_class+"/"+(data["matriz"])[x][0]+"'>"+(data["matriz"])[x][y]+"</a></td>";
          }/*close if*/
	        else {
	          output += '<td>';
	          output +=  (data["matriz"])[x][y];
	          output += '</td>';
          }/*close else*/
           }
	     output += "</tr>";
   }/*cierro for dictionary_students*/
    
    
       
  var txt = "<p>Para generar estos datos se evaluaron: " +(data["quantity_results"]) +" ejercicios, de "+ (data["quantity_students"]) +" alumnos.</p>" ;    
    if (output != ""){
     // $("#dt_students > thead").html(output_thead);
      $("#dt_students > tbody ").html(output);
      
      $("#dt_students").dataTable();

      $("#more_info_stats_students").html(txt);

     /* $("#dt_students").dataTable({

            "language":{
                  
                  "url": "dataTables.spanish.lang"
              }
          });*/
     
   
   

     }
    }
}

