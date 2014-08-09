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
          matriz:'matriz'

    }, 

    "success":function(data){
        create_table_students(data);

      }

    })
  
} /*cierro function get_students_data*/



function create_table_students (data) {


var code_class = $("#code").attr("value");
if(data['type'] == 'success'){  
    var output_thead = "";
    var output = "";

    output_thead +='<tr>';
    output_thead +='<th>Nombre</th>';                                                   
    output_thead +='<th>Meta cognitivo</th>';
    output_thead +='<th>Cognitivo</th>';
    output_thead +='<th>Socio afectivo</th>';
    output_thead +='<th>Promedio</th>';
    output_thead +='</tr>';

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
       
      
    if (output != ""){

      $("#dt_students > tbody ").html(output);
      $("#dt_students > thead").html(output_thead);
   
    }

     }
    }
}
