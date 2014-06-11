$(document).ready(ini);


function ini(){

  $("#select_unit").attr('disabled','disabled');
  $("#select_subject").attr('disabled','disabled');
  
  $('#select_area').change(test);


}

function test(){
    var tok = $("#token").attr("value");
    var id_area = $(this).val();
    $("#select_subject").html('');
    $.ajax({
      beforeSend: function(){



      },
      url:"list/",
      chache: false,
      type: "POST",
      dataType: 'json',      
      data:{
            csrfmiddlewaretoken: tok,
            state:'inactive',
            id_area:id_area,
      }, 

      success: function(){

        load_filter_subjects(id_area);
      }


    });
     
    
}


function load_filter_subjects(id_area){

  
  var tok = $("#token").attr("value");
  var query = $.ajax({
    url:"list/",
    type:'POST',
    dataType:"json",
    data:{
          csrfmiddlewaretoken: tok,
          state:'inactive',
          id_area: id_area,
          name: 'y.name',
          id:'y.id',
          
    }, 
    
    "success":function(data){
       
      $('#select_subject').removeAttr('disabled');
      var output_select="";
      //output_select +="<option value="0" selected="" disabled="">Materia</option>";
      for (var y in data["dictionary_subjects"]){
        output_select += "<option value="+(data["dictionary_subjects"][y]['id'])+">";
        output_select += (data["dictionary_subjects"][y]['name']); 
        output_select += "</option>";
        }/*Cierro for dictionary_subjects*/
        $("#select_subject").html(output_select);
      }

       

    })
    $("#select_subject").change(load_units);

}

function load_units(){

  var id_subject = $(this).val();

  var tok = $("#token").attr("value");
  var query = $.ajax({
    url:"list/units/",
    type:'POST',
    dataType:"json",
    data:{
          csrfmiddlewaretoken: tok,
          state:'inactive',
          id_subject: id_subject,
          name: 'p.name',
          id:'p.id',
          
    }, 
    
    "success":function(data){
       
      $('#select_unit').removeAttr('disabled');
      var output_select_unit="";
      //output_select +="<option value="0" selected="" disabled="">Materia</option>";
      for (var p in data["dictionary_units"]){
        output_select_unit += "<option value="+(data["dictionary_units"][p]['id'])+">";
        output_select_unit += (data["dictionary_units"][p]['name']); 
        output_select_unit += "</option>";
        }/*Cierro for dictionary_subjects*/
        $("#select_unit").html(output_select_unit);
      }

       

    })

    $('#select_unit').change(get_students_data);


}/*cierro funcion load_units*/

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
	 
    //$("#dt_alumnos > thead ").html('');
    //$("#dt_alumnos > tbody").html('');
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