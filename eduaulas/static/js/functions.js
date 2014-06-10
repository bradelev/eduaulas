$(document).ready(ini);


function ini(){
$('#load_students2').click(get_students_data);
	$('#load_students').click(get_students_data);
/*  get_classroom_data();*/

}


function get_students_data () {
	 
    var query = $.ajax({
    url:"list/students/",
    type:'GET',
    dataType:"json",
    data:{
          name:'name',
          last_name:'last_name',
          exercise_id: 'exercise_id'
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


function get_classroom_data() {
    
    var query = $.ajax({
    url:"lista/aulas/",
    type:'GET',
    dataType:"json",
    data:{
          grade:'grade',
          class_letter:'class_letter',
    }, 

    "success":function(data){
        create_table_classrooms(data);
        $('#dt_classroom').dataTable();
       
      }

    })
  
} /*cierro function get_students_data*/


function create_table_classrooms (data) {

  if(data['type'] == 'success'){  
     
      var output = "";
      for (var x in data["dictionary_classrooms"]){
        output += "<tr>";
        (data["dictionary_classrooms"][x]['grade'] == "0") ? output += "<td></td>": output += "<td>"+data["dictionary_classrooms"][x]['grade']+"</td>";
        (data["dictionary_classrooms"][x]['class_letter'] == "0") ? output += "<td></td>": output += "<td>"+data["dictionary_classrooms"][x]['class_letter']+"</td>";
        output += "</tr>";
      }
      if (output != ""){
        $("#dt_classroom > tbody").append(output);
      }
  }

} /*cierro function create_table_classrooms*/






$(function(){

$('#classroom-form').validate({
      // Rules for form validation
        rules : {
          country : {
            required : true
          },
          department : {
            required : true
          },
          grade : {
            required : true
          },
           className : {
            required : true
          },
          schoolNumber : {
            required : true
          },
          shift : {
            required : true
          }
        },

       
// Messages for form validation
messages : {
          country : {
            required : 'Por favor ingrese su pais'
          },
          department : {
            required : 'Por favor ingrese su departamento'
          },
          grade : {
            required : 'Por favor ingrese el año del aula'
          },
          schoolNumber : {
            required : 'Por favor ingrese el numero de escuela'
          },
          className : {
            required : 'Por favor ingrese el nombre de la clase'
          },
          shift : {
            required : 'Por favor ingrese el turno de la clase'
          }
        },
        // Do not change code below
        errorPlacement : function(error, element) {
          error.insertAfter(element.parent());
        }
      })
});/*cierro function form_classroom_validate*/