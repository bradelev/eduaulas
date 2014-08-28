$(document).ready(ini);


function ini(){

  create_classroom_table();
  $('#add_classroom').click(get_data_for_selects_classroom);
  var editing_classroom = false
  $('#dlt_classroom').click(delete_classroom);
  $('#save').click(edit_or_save);
  $('#action').val('0'); 
  $('#btn_update_techer_info').click(update_techer_info);
  load_teacher_info();
  load_teacher_configuration();

  $('#btn_sub').click(update_techer_configuration);

 }


function load_teacher_configuration(){

  var tok = $("#token").attr("value");
  var query = $.ajax({
    url:"configuracion_docente/",
    type:'POST',
    dataType:"json",
    data:{
          corrects_points:'corrects_points',
          incorrect_points: 'incorrect_points',
          quantity_exercises: 'quantity_exercises',
          time_to_update_panel: 'time_to_update_panel',
          csrfmiddlewaretoken: tok,
          state:'inactive',


    }, 

    "success":function(data){
           
      $("#correct_points").val(data["corrects_points"]);
      $("#incorrect_points").val(data["incorrect_points"]);
      $("#quantity_exercises").val(data["quantity_exercises"]);
      $("#time_to_update_panel").val(data["time_to_update_panel"]);
       
      }

    })

}/*load_teacher_configuration*/

function update_techer_configuration(){

 validate_teacher_configuration_form();
  var correct_points = $("#correct_points").val();
  var incorrect_points = $("#incorrect_points").val();
  var quantity_exercises = $("#quantity_exercises").val();
  var time_to_update_panel = $("#time_to_update_panel").val();
  
  var tok = $("#token").attr("value");
  var query = $.ajax({
    url:"actualizar_configuracion/",
    type:'POST',
    dataType:"json",
    data:{
          correct_points:correct_points,
          incorrect_points:incorrect_points,
          quantity_exercises:quantity_exercises,
          time_to_update_panel: time_to_update_panel,
          csrfmiddlewaretoken: tok,
          state:'inactive',

    }, 
   
    error: function(response) {
      // alert('error');
      $('#teacher_configuration_info').append(response);

    },  
     success: function(response) {
     // alert('success');
      $('#teacher_configuration_info').append(response);
      
    }


    })
  
}/*close function update_techer_configuration*/



function load_teacher_info(){
  
  var change = false;
  
  $(".change_password").change(change_pass);
  var tok = $("#token").attr("value");
  var query = $.ajax({
    url:"datos_docente/",
    type:'POST',
    dataType:"json",
    data:{
          name: 'name',
          last_name:'last_name',
          email:'email',
          gender: 'gender',
          date_birth: 'date_birth',
          user: 'user',
          csrfmiddlewaretoken: tok,
          state:'inactive',


    }, 

    "success":function(data){
           
      $("#name").val(data["name"]);
      $("#last_name").val(data["last_name"]);
      $("#user").val(data["user"]);
      $("#email").val(data["email"]);
      $("#gender").val(data["gender"]);
      $("#dateofbirth").val(data["date_birth"]);
      }

    })

}

function change_pass(change){
  var no = $("#change_no").is(':checked') ;
  var yes =$("#change_yes").is(':checked') ;
  
  if (yes == true){
    $("#psw").removeAttr("hidden");
    $("#password").removeAttr("disabled");
    $("#passwordConfirm").removeAttr("disabled");
  }
 if (no == true){
    $("#psw").attr("hidden","hidden");
    $("#password").attr('disabled','disabled');
    $("#passwordConfirm").attr('disabled','disabled');

  }

}

function update_techer_info(){
  validate_teacher_form();

  var gender = $("#gender").val();
  var user = $("#user").val();
  var password = $("#password").val();

  var valid = true;  
  var name = $("#name").val();
  valid *= (name != '');
  var last_name = $("#last_name").val();
  valid *= (last_name != '');
  var email = $("#email").val();
  valid *= (email != null);
  var date_birth = $("#dateofbirth").val();
  valid *= (date_birth != null);
  

  
  var tok = $("#token").attr("value");
  if (valid){
    var query = $.ajax({
    url:"actualizar_datos/",
    type:'POST',
    dataType:"json",
    data:{
          name:name,
          last_name:last_name,
          user:user,
          gender: gender,
          email:email,
          password:password,
          date_birth:date_birth,
          csrfmiddlewaretoken: tok,
          state:'inactive',

    }, 
    success: function(response) {
      //alert('success');
      $('#teacher_info').append(response);
      
    },
    error: function(response) {
       //alert('error');
      $('#teacher_info').append(response);

    }  

    //"success":function(data){
       // draw_table_classrooms(data);
      //      $('#teacher_info').html(response);
       //alert('entre al success');
     // }

    })
}/*close if valid*/  
}/*close function update_techer_info*/

function edit_or_save(){

  var action = $('#action').val(); 

  if (action==1){

      save_classroom_add();
  }
  if (action==2){

      save_classroom_edit();
  }
  
}

function create_classroom_table() {
    
    var query = $.ajax({
    url:"lista/aulas/",
    type:'GET',
    dataType:"json",
    data:{
          code:'code',
          shift: 'shift',
          class_letter:'class_letter',
          grade:'grade',
          school:'school'

    }, 

    "success":function(data){
        draw_table_classrooms(data);
       // $('#dt_classroom').dataTable();
       
      }

    })
  
} /*cierro function get_students_data*/



function draw_table_classrooms (data) {
  
  if(data['type'] == 'success'){  
     
      var output = "";
      for (var x in data["dictionary_classrooms"]){
        output += "<tr>";
        var code_classroom=data["dictionary_classrooms"][x]['code'];
        (data["dictionary_classrooms"][x]['code'] == "0") ? output += "<td></td>": output += "<td>"+"<a title='Ir a aula' href='/panel/lista/"+[code_classroom]+"'>"+data["dictionary_classrooms"][x]['code']+"</a></td>";
        (data["dictionary_classrooms"][x]['grade'] == "0") ? output += "<td></td>": output += "<td>"+data["dictionary_classrooms"][x]['grade']+"</td>";        
        (data["dictionary_classrooms"][x]['class_letter'] == "0") ? output += "<td></td>": output += "<td>"+data["dictionary_classrooms"][x]['class_letter']+"</td>";
        (data["dictionary_classrooms"][x]['shift'] == "0") ? output += "<td></td>": output += "<td>"+data["dictionary_classrooms"][x]['shift']+"</td>";
        (data["dictionary_classrooms"][x]['school'] == "0") ? output += "<td></td>": output += "<td>"+data["dictionary_classrooms"][x]['school']+"</td>";
        
        
        output += "<td>";
       // output += "x";
        output += '<button class="edit_class btn btn-xs btn-default" data-original-title="Edit Row" data-toggle="modal" data-target="#myModal" value="'+ code_classroom+'"><i class="fa fa-pencil"></i></button>';
        output += '<button class="delete_class btn btn-xs btn-default" data-original-title="Delete Row" data-toggle="modal" data-target="#modal_dlt_classroom" value="'+ code_classroom+'"><i class="fa fa-times"></i></button>';
        output += "</td>";
        output += "</tr>";
      }
      if (output != ""){
        $("#dt_classroom > tbody").append(output);
        $(".edit_class").click(load_classroom);
        $(".delete_class").click(load_classroom_code);
        

      }
  }

} /*cierro function create_table_classrooms*/

function load_classroom_code(){

    var code_classroom= $(this).val();

    var tok = $("#token").attr("value");
     $.ajax({
      beforeSend: function(){
      },
      url:"cargar/codigo_aula/",
      type: "POST",
      dataType: 'json',      
      data:{
            csrfmiddlewaretoken: tok,
            state:'inactive',
            code_class_to_delete:code_classroom,
            code:'code',

      }, 

      success: function(data){

          var output_code= "¿Desea eliminar el aula";
          for (var classroom in data["dictionary_classroom"]){
            cg =data["dictionary_classroom"][classroom]['code'];
            output_code+="  ";
            output_code+=cg + " ?";
            $("#txt_delete").val(cg);
        }
        $("#txt_delete").html(output_code);
       
      }

    });



}

function delete_classroom(){

    var code_class= $("#txt_delete").val();
    var tok = $("#token").attr("value");
     $.ajax({
      beforeSend: function(){
      },
      url:"aulas/eliminar/aula/",
      type: "POST",
      dataType: 'json',      
      data:{
            csrfmiddlewaretoken: tok,
            state:'inactive',
            code_class_to_delete:code_class,

      }, 

      success: function(){
        
          create_classroom_table();
          
      }

    });


}



function load_classroom(){

  $('#action').val('2') /*editing classroom*/
  editing_classroom= true;
  var tok = $("#token").attr("value");
  var code_classroom= $(this).val();
    var query = $.ajax({
    url:"cargar/aula/",
    type:'POST',
    dataType:"json",
    data:{
          csrfmiddlewaretoken: tok,
          code:code_classroom,
          shift: 'shift',
          country_id:'country_id',
          department_id:'department_id',
          grade_id:'grade_id',
          school:'school',
          school_id:'school_id',
          class_letter:'class_letter',
          

    }, 

    "success":function(data){
        
        for (var classroom in data["dictionary_classroom"]){
          var shift=data["dictionary_classroom"][classroom]['shift']; 
          $("#select_shift").val(shift);
          var grade_id=data["dictionary_classroom"][classroom]['grade_id'];
          var school_id=data["dictionary_classroom"][classroom]['school_id'];
          var country_id=data["dictionary_classroom"][classroom]['country_id'];
          var department_id=data["dictionary_classroom"][classroom]['department_id'];   
          var code_class=data["dictionary_classroom"][classroom]['code_class'];  
               
          var class_letter=data["dictionary_classroom"][classroom]['class_letter'];
          $("#class_name").val(class_letter);
         
      }/*cierro for dictionary_classroom*/
      
       get_data_for_selects_classroom(editing_classroom,grade_id,school_id,country_id,department_id,code_class);

      }

    })
}/*load_classroom*/



function get_data_for_selects_classroom(editing_classroom,grade_id,school_id,country_id,department_id,code_class){
    
    var tok = $("#token").attr("value");
     $.ajax({
      beforeSend: function(){
      },
      url:"cargar_form/",
      type: "GET",
      dataType: 'json',      
      data:{
            csrfmiddlewaretoken: tok,
            state:'inactive',
            name:'name',
            id:'id'

      }, 

      success: function(data){

          load_selects_classroom(data,editing_classroom,grade_id,school_id,country_id,department_id,code_class);
          
      }

    });

}


function load_selects_classroom(data,editing_classroom,grade_id,school_id,country_id,department_id,code_class){
  //  alert(editing_classroom);
    if (editing_classroom == true){
       $('#save').click(function(){save_classroom_edit(code_class)});
       }
    var output_select_country = "";
    output_select_country += '<option value="0" selected="" disabled="">Pais</option>'
    for (var y in data["dictionary_countrys"]){
      output_select_country += "<option value="+(data["dictionary_countrys"][y]['id'])+">";
      output_select_country += (data["dictionary_countrys"][y]['name']); 
      output_select_country += "</option>";
      }/* cierro for countrys*/
      $("#select_country").html(output_select_country);       

      if (editing_classroom==true){
        $("#select_country").val(country_id);
        
          load_selects_departments(editing_classroom,department_id,school_id);

    }
    $("#select_country").change(function(){load_selects_departments(editing_classroom,department_id,school_id)});

    var output_select_grades = "";
    output_select_grades += '<option value="" selected="" disabled="" >Grados</option>'
      for (var g in data["dictionary_grades"]){
        output_select_grades += "<option value="+(data["dictionary_grades"][g]['id'])+">";
        output_select_grades += (data["dictionary_grades"][g]['name']) + '° Primaria'; 
        output_select_grades += "</option>";
        }/*Cierro for dictionary_grades*/
        $("#select_grade").html(output_select_grades);
        if (editing_classroom==true){
           $("#select_grade").val(grade_id);
      }else {$('#action').val('1')}

 } 


function load_selects_departments(editing_classroom,department_id,school_id){

  var id_country  = $('#select_country').val();
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

      if (editing_classroom==true){
        $("#select_department").val(department_id);
        load_selects_schools(editing_classroom,school_id);
    }
     $("#select_department").change(function(){load_selects_schools(editing_classroom,school_id)});
    }
   
  });

}


function load_selects_schools(editing_classroom,school_id){

  var id_department  = $('#select_department').val();

  var tok = $("#token").attr("value");
   $.ajax({
    beforeSend: function(){

    },
    url:"aulas/schools/",
    type: "POST",
    dataType: 'json',      
    data:{
          csrfmiddlewaretoken: tok,
          state:'inactive',
          name:'name',
          id:'id',
          id_department:id_department,

    }, 
    success: function(data){

    var output_select_schools = "";     
    output_select_schools += '<option value="0" selected="" disabled="">Escuela</option>'
    for (var s in data["dictionary_schools"]){
      output_select_schools += "<option value="+(data["dictionary_schools"][s]['id'])+">";
      output_select_schools += (data["dictionary_schools"][s]['name']); 
      output_select_schools += "</option>";
      }/*Cierro for dictionary_schools*/
    $("#select_school").html(output_select_schools);
    if (editing_classroom==true){
        $("#select_school").val(school_id);
    }
     
    }
   
  });
}


function save_classroom_add() {
 // alert('saveeeee');
  var tok = $("#token").attr("value");
  valido = true;
  var select_country = $('#select_country').val();
  valido *= (select_country != null);
  var select_department= $('#select_department').val();
  valido *= (select_department != null);
  var select_school= $('#select_school').val();
  valido *= (select_school != null);
  var select_grade = $('#select_grade').val();
  valido *= (select_grade != null);
  var class_name = $('#class_name').val();
  valido *= (class_name != null);
  var select_shift = $('#select_shift').val();
  valido *= (select_shift != null);
  
    if (valido){
      $.ajax({
        url:"/aulas/lista/agregar/aula/",
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
              select_shift:select_shift,
              
        }, 

        success: function(){
        create_classroom_table();
      }
    });
    
  }/*cierro if valido*/

}/*cierro function*/

function save_classroom_edit(code_class) {


    var tok = $("#token").attr("value");
    valido = true;
    var select_country = $('#select_country').val();
    valido *= (select_country != null);
    var select_department= $('#select_department').val();
    valido *= (select_department != null);
    var select_school= $('#select_school').val();
    valido *= (select_school != null);
    var select_grade = $('#select_grade').val();
    valido *= (select_grade != null);
    var class_name = $('#class_name').val();
    valido *= (class_name != null);
    var select_shift = $('#select_shift').val();
    valido *= (select_shift != null);
    
      if (valido){
        $.ajax({
          url:"editar/aula/",
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
                select_shift:select_shift,
                code_class:code_class,
          }, 

          success: function(){
          create_classroom_table();
        }
      });
      
    }/*cierro if valido*/

}/*cierro function*/


//$(function(){



function validate_teacher_form(){
  $("#update-teacher").validate({
          // Rules for form validation
          rules : {
            username : {
              required : true,
            },
            email : {
              required : true,
              email : true
            },
            password : {
              required : true,
              minlength : 3,
              maxlength : 20
            },
            passwordConfirm : {
              required : true,
              minlength : 3,
              maxlength : 20,
              equalTo: '#password'
            },
            firstname : {
              required : true,
            },
            lastname : {
              required : true,
            },
            dateofbirth : {
              required : true,
              date : true,  
            }
          },

          // Messages for form validation
          messages : {
            username : {
              required : 'Ingrese su usuario'
            },
            email : {
              required : 'Ingrese su correo correctamente',
              email : 'Correo debe tener un formato correcto usuario@dominio.com'
            },
            password : {
              required : 'Ingrese su contraseña'
            },
            passwordConfirm : {
              required : 'Ingrese su contraseña',
              equalTo: 'Debe coincidir con la contraseña de arriba'
            },
            firstname : {
              required : 'Ingrese su nombre',
            },
            lastname : {
              required : 'Ingrese su apellido',
            },
            dateofbirth : {
              date : 'Ingrese una fecha válida',
            }

          },
          errorPlacement : function(error, element) {
            error.insertAfter(element.parent());
          }
          });
}
//});


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


function validate_teacher_configuration_form(){

$('#update-teacher-config').validate({
      // Rules for form validation
        rules : {
          correct_points : {
            required : true
          },
          incorrect_points : {
            required : true
          },
          quantity_exercises : {
            required : true
          },
           time_to_update_panel : {
            required : true
          }
         },

       
// Messages for form validation
messages : {
          correct_points : {
            required : 'Por favor ingrese un valor en este campo.'
          },
          incorrect_points : {
            required : 'Por favor ingrese un valor en este campo.'
          },
          quantity_exercises : {
            required : 'Por favor ingrese un valor en este campo.'
          },
          time_to_update_panel : {
            required : 'Por favor ingrese un valor en este campo.'
           }         
        },
        // Do not change code below
        errorPlacement : function(error, element) {
          error.insertAfter(element.parent());
        }
      });
  
//});/*cierro function form_classroom_validate*/
}

