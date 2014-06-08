$(document).ready(ini);


function ini(){

	$('#test').click(get_students_data);

}


function get_students_data () {
	
    var query = $.ajax({
    url:"list/students/",
    type:'GET',
    dataType:"json",
    data:{
          name:'name',
          last_name:'last_name',
    }, 

    "success":function(data){
        create_table_students(data);
        $('#dt_alumnos').dataTable();
       
      }

    })
  
} /*cierro function get_students_data*/


function create_table_students (data) {

if(data['type'] == 'success'){  
	 
    var output = "";
    output+="<thead>";
    output+="<tr>";
    output+="<th>Nombre</th>";
    output+="<th>Apellido</th>"
    output+="</tr>"
    output+="</thead>"
    output+="<tbody >"

    for (var x in data["dictionary_students"]){
      output += "<tr>";
      (data["dictionary_students"][x]['name'] == "0") ? output += "<td></td>": output += "<td>"+data["dictionary_students"][x]['name']+"</td>";
      (data["dictionary_students"][x]['last_name'] == "0") ? output += "<td></td>": output += "<td>"+data["dictionary_students"][x]['last_name']+"</td>";
      output += "</tr>";
    }
    output+="</tbody >"
    if (output != ""){
     
      $("#dt_alumnos > tbody").append(output);

    }
    
}


} /*cierro function create_table_students*/