$(document).ready(ini);


function ini(){

  $("#select_unit").attr('disabled','disabled');
  $("#select_subject").attr('disabled','disabled');
  
  $('#select_area').change(load_fiters);
  $('#eg7').click(sm);
  create_classroom_table();
  $('#add_classroom').click(get_data_for_selects_classroom);
  $('#subtmit_classroom').click(save_classroom);
  
  
}

                
function sm(){
  $.smallBox({
    title : "Juan Perez necesita ayuda",
    content : "<i class='fa fa-clock-o'></i> <i>2 seconds ago...</i>",
    color : "#296191",
    iconSmall : "fa fa-thumbs-up bounce animated",
    //timeout : 4000
});
}


function load_fiters(){
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
      var output_select = "";
      output_select += '<option value="0" selected="" disabled="">Materia</option>'
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
      output_select_unit +='<option value="0" selected="" disabled="">Unidad</option>'
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
	 
    var id_unit = $(this).val();
    var tok = $("#token").attr("value");
    var query = $.ajax({
    url:"list/students/",
    type:'post',
    dataType:"json",
    data:{
          csrfmiddlewaretoken: tok,
          state:'inactive',
          id_unit: id_unit,
          id_student:'x.id',
          name:'name',
          last_name:'last_name',
          exercise_id: 'exercise_id',
          points: 'y.points',
          student: 'y.student.id',

    }, 

    "success":function(data){
        create_table_students(data);
      }

    })
  
} /*cierro function get_students_data*/




function create_table_students (data) {

if(data['type'] == 'success'){  
    var output_thead = "";
    
    output_thead +="<tr>";
    output_thead +="<th>Nombre</th>";                                                   
    output_thead +="<th>Apellido</th>";
    for (var e in data["dictionary_units_exercises"]){
        output_thead += "<th>";  
        output_thead += (data["dictionary_units_exercises"][e]['exercise_id']); 
        output_thead += "</th>";
    }
    output_thead +="</tr>";
    

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

    if (output != ""){
      $("#dt_alumnos > tbody ").html(output);
      $("#dt_alumnos > thead").html(output_thead);

    }
    /*$('#dt_alumnos').dataTable();*/
    
}


} /*cierro function create_table_students*/


function create_classroom_table() {
    
    var query = $.ajax({
    url:"lista/aulas/",
    type:'GET',
    dataType:"json",
    data:{
          grade:'grade',
          class_letter:'class_letter',
    }, 

    "success":function(data){
        draw_table_classrooms(data);
        $('#dt_classroom').dataTable();
       
      }

    })
  
} /*cierro function get_students_data*/


function draw_table_classrooms (data) {

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
          school : {
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
          school : {
            required : 'Por favor ingrese la escuela'
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

function get_data_for_selects_classroom(){

    var tok = $("#token").attr("value");
     $.ajax({
      beforeSend: function(){

      },
      url:"aulas/cargar_form/",
      type: "GET",
      dataType: 'json',      
      data:{
            csrfmiddlewaretoken: tok,
            state:'inactive',
            name:'name',
            id:'id'

      }, 

      success: function(data){

          load_selects_classroom(data);
        
      }

    });

}


function load_selects_classroom(data){

      var output_select_country = "";
      output_select_country += '<option value="0" selected="" disabled="">Pais</option>'
      for (var y in data["dictionary_countrys"]){
        output_select_country += "<option value="+(data["dictionary_countrys"][y]['id'])+">";
        output_select_country += (data["dictionary_countrys"][y]['name']); 
        output_select_country += "</option>";
        }/* cierro for countrys*/
        $("#select_country").html(output_select_country);
        $("#select_country").change(load_selects_departments);
      
      var output_select_schools = "";
      output_select_schools += '<option value="0" selected="" disabled="">Escuela</option>'
      for (var s in data["dictionary_schools"]){
        output_select_schools += "<option value="+(data["dictionary_schools"][s]['id'])+">";
        output_select_schools += (data["dictionary_schools"][s]['name']); 
        output_select_schools += "</option>";
        }/*Cierro for dictionary_schools*/
        $("#select_school").html(output_select_schools);

      var output_select_grades = "";
      output_select_grades += '<option value="0" selected="" disabled="">Grados</option>'
      for (var g in data["dictionary_grades"]){
        output_select_grades += "<option value="+(data["dictionary_grades"][g]['id'])+">";
        output_select_grades += (data["dictionary_grades"][g]['name']); 
        output_select_grades += "</option>";
        }/*Cierro for dictionary_grades*/
        $("#select_grade").html(output_select_grades);

 } 


function load_selects_departments(){

    var id_country  = $('#select_country').val();
   // alert(id_department);
    var tok = $("#token").attr("value");
     $.ajax({
      beforeSend: function(){

      },
      url:"aulas/departments/",
      type: "POST",
      dataType: 'json',      
      data:{
            csrfmiddlewaretoken: tok,
            state:'inactive',
            name:'name',
            id:'id',
            id_country:id_country,

      }, 
      success: function(data){

      var output_select_departments = "";
      output_select_departments += '<option value="0" selected="" disabled="">Departamento</option>'
      for (var d in data["dictionary_departments"]){
        output_select_departments += "<option value="+(data["dictionary_departments"][d]['id'])+">";
        output_select_departments += (data["dictionary_departments"][d]['name']); 
        output_select_departments += "</option>";
        }/*Cierro for dictionary_grades*/
        $("#select_department").html(output_select_departments);
        
      }

    });

}

function save_classroom() {

    var tok = $("#token").attr("value");
    var select_country = $('#select_country').val();
    var select_department= $('#select_department').val();
    var select_school= $('#select_school').val();
    var select_grade = $('#select_grade').val();
    var class_name = $('#class_name').val();
    var select_shift = $('#select_shift').val();

    $.ajax({
      url:"aulas/agregar/aula/",
      type: "POST",
      dataType: 'json',      
      data:{
            csrfmiddlewaretoken: tok,
            state:'inactive',
            select_country:select_country,
            select_department:select_department,
            select_school:select_school,
            select_grade:select_grade,
            class_name:class_name,
            select_shift:select_shift

      }, 

      success: function(){

        create_classroom_table();
      }


    });


}