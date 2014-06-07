$(document).ready(ini);


function ini(){

	$('#test').click(get_students_data);

}


function get_students_data () {
	
    var query = $.ajax({
    url:"list/",
    type:'GET',
    dataType:"json",
    data:{
          name:name,
    }, 

    "success":function(data){
        create_table_students(data);
       
      }

    })
  
} /*cierro function get_students_data*/


function create_table_students (data) {

if(data['type'] == 'success'){  
	 
    var output = "";
    for (var x in data["dictionary_students"]){
      output += "<tr>";
      (data["dictionary_students"][x]['name'] == "0") ? output += "<td></td>": output += "<td>"+data["dictionary_students"][x]['name']+"</td>";
      output += "</tr>";
    }

    if (output != ""){
      
      $("#dt_alumnos").html(output);
    }
    
}


} /*cierro function create_table_students*/