$(document).ready(ini);


function ini(){

  $('#select_unit').change(get_students_data);
  $('#select_area').change(test);


}

function test(){

    var id_area = $(this).val();

    $.ajax({
      beforeSend: function(){
        $('#select_unit').attr('disabled','disabled');


      },
      chache: false,
      type: "POST",
      url:"list/ini/",
      data: "id_area" + id_area,
      success: function(){

        
      }



    });



      

}

function get_students_data () {
	 
    var query = $.ajax({
    url:"list/students/",
    type:'GET',
    dataType:"json",
    data:{
          id_student:'x.id',
          name:'name',
          last_name:'last_name',
          exercise_id: 'exercise_id',
          points: 'y.points',
          student: 'y.student.id',

    }, 

    "success":function(data){
        create_table_students(data);
        $('#dt_alumnos').dataTable();
       
      }

    })
  
} /*cierro function get_students_data*/


function create_table_students (data) {

if(data['type'] == 'success'){  
	 
    $("#dt_alumnos > thead ").html('');
    $("#dt_alumnos > tbody").html('');
    var output_thead = "";
    output_thead +="<thead>";
    output_thead +="<tr>";
    output_thead +="<th>Nombre</th>";                                                   
    output_thead +="<th>Apellido</th>";
    for (var e in data["dictionary_units_exercises"]){
        output_thead += "<th>";  
        output_thead += (data["dictionary_units_exercises"][e]['exercise_id']); 
        output_thead += "</th>";
    }
    output_thead +="</tr>";
    output_thead +="</thead>";

  var output = "";
  for (var x in data["dictionary_students"]){
      output += "<tr>";      
      (data["dictionary_students"][x]['name'] == "0") ? output += "<td></td>": output += "<td>"+data["dictionary_students"][x]['name']+"</td>";
      (data["dictionary_students"][x]['last_name'] == "0") ? output += "<td></td>": output += "<td>"+data["dictionary_students"][x]['last_name']+"</td>";
      for (var y in data["dictionary_students_exercises"]){
        if (data["dictionary_students"][x]['id_student'] == data["dictionary_students_exercises"][y]['student']  ) {
          
          (data["dictionary_students_exercises"][y]['points'] == "0") ? output += "<td>X</td>": output += "<td>"+data["dictionary_students_exercises"][y]['points']+"</td>";
          }/*cierro if*/
       
        }/*cierro for dictionary_students_exercises*/

      output += "</tr>";
    }/*cierro for dictionary_students*/

    output+="</tbody >"
    if (output != ""){

      $("#dt_alumnos").append(output_thead);
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