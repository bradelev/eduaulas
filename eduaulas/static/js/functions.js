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
      url:"lista/",
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
    url:"lista/",
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
   // url:"lista/unidades/", lista/(?P<code>\w+)?/unidades
   url:"lista/unidades/",
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
	 
    var code_class = $("#code").attr("value");
    //alert(code);
    var id_unit = $(this).val();
    var tok = $("#token").attr("value");
    var query = $.ajax({
    url:"lista/alumnos/",
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
       //   code:'code'

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
          code:'code',
          shift: 'shift',
          class_letter:'class_letter',
          grade:'grade',
          school:'school'

    }, 

    "success":function(data){
        draw_table_classrooms(data);
        $('#dt_classroom').dataTable();
       
      }

    })
  
} /*cierro function get_students_data*/



function draw_table_classrooms (data) {

  //$(".edit_class").click(edit_classroom);
  
  if(data['type'] == 'success'){  
     
      var output = "";
      for (var x in data["dictionary_classrooms"]){
        output += "<tr>";
        var code_classroom=data["dictionary_classrooms"][x]['code'];
        (data["dictionary_classrooms"][x]['code'] == "0") ? output += "<td></td>": output += "<td>"+"<a title='Ir a aula' href='http://127.0.0.1:8080/panel/lista/"+[code_classroom]+"'>"+data["dictionary_classrooms"][x]['code']+"</a></td>";
        (data["dictionary_classrooms"][x]['grade'] == "0") ? output += "<td></td>": output += "<td>"+data["dictionary_classrooms"][x]['grade']+"</td>";        
        (data["dictionary_classrooms"][x]['class_letter'] == "0") ? output += "<td></td>": output += "<td>"+data["dictionary_classrooms"][x]['class_letter']+"</td>";
        (data["dictionary_classrooms"][x]['shift'] == "0") ? output += "<td></td>": output += "<td>"+data["dictionary_classrooms"][x]['shift']+"</td>";
        (data["dictionary_classrooms"][x]['school'] == "0") ? output += "<td></td>": output += "<td>"+data["dictionary_classrooms"][x]['school']+"</td>";
        
        
        output += "<td>";
       // output += "x";
        output += '<button class="edit_class btn btn-xs btn-default" data-original-title="Edit Row" data-toggle="modal" data-target="#myModal" value="'+ code_classroom+'"><i class="fa fa-pencil"></i></button>';
        output += '<button class="btn btn-xs btn-default" data-original-title="Edit Row"><i class="fa fa-times"></i></button>';
        output += "</td>";
        output += "</tr>";
      }
      if (output != ""){
        $("#dt_classroom > tbody").append(output);
        $(".edit_class").click(load_classroom);
      

      }
  }

} /*cierro function create_table_classrooms*///btn btn-xs btn-default
/***************AULAS**************************************************************************/
function load_classroom(code_classroom){
  var editing_classroom= false;
  var tok = $("#token").attr("value");
  var code_classroom= $(this).val();
  
    var query = $.ajax({
    url:"editar/aula/",
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
          class_letter:'class_letter'

    }, 

    "success":function(data){
        var editing_classroom= true;
        for (var classroom in data["dictionary_classroom"]){
          var shift=data["dictionary_classroom"][classroom]['shift']; 
          $("#select_shift").val(shift);
          var grade_id=data["dictionary_classroom"][classroom]['grade_id'];
          var school_id=data["dictionary_classroom"][classroom]['school_id'];
          var country_id=data["dictionary_classroom"][classroom]['country_id'];
          var department_id=data["dictionary_classroom"][classroom]['department_id'];

          
          var class_letter=data["dictionary_classroom"][classroom]['class_letter'];
          $("#class_name").val(class_letter);
         
      }/*cierro for dictionary_classroom*/
      
       get_data_for_selects_classroom(editing_classroom,grade_id,school_id,country_id,department_id);

      }

    })
}/*load_classroom*/



function get_data_for_selects_classroom(editing_classroom,grade_id,school_id,country_id,department_id){
    
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

          load_selects_classroom(data,editing_classroom,grade_id,school_id,country_id,department_id);
          
      }

    });

}


function load_selects_classroom(data,editing_classroom,grade_id,school_id,country_id,department_id){
    
     $('#subtmit_classroom').click(save_classroom(editing_classroom));
     
      var output_select_country = "";
      output_select_country += '<option value="0" selected="" disabled="">Pais</option>'
      for (var y in data["dictionary_countrys"]){
        output_select_country += "<option value="+(data["dictionary_countrys"][y]['id'])+">";
        output_select_country += (data["dictionary_countrys"][y]['name']); 
        output_select_country += "</option>";
        }/* cierro for countrys*/
        $("#select_country").html(output_select_country);
        $("#select_country").change(load_selects_departments(editing_classroom,department_id));
        /*if (editing_classroom==true){
          $("#select_country").val(country_id);
          $("#select_country").change(load_selects_departments(editing_classroom,department_id));
      }*/
      

      
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
     


    var output_select_grades = "";
     output_select_grades += '<option value="" selected="" disabled="" >Grados</option>'
      for (var g in data["dictionary_grades"]){
        output_select_grades += "<option value="+(data["dictionary_grades"][g]['id'])+">";
        output_select_grades += (data["dictionary_grades"][g]['name']); 
        output_select_grades += "</option>";
        }/*Cierro for dictionary_grades*/
        $("#select_grade").html(output_select_grades);
        if (editing_classroom==true){
          $("#select_grade").val(grade_id);
      }

 } 


function load_selects_departments(editing_classroom,department_id){

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

        if (editing_classroom==true){
          $("#select_department").val(department_id);
      }
       
      }
     
    });

}

function save_classroom(editing_classroom) {
   // alert(editing_classroom);

    var tok = $("#token").attr("value");
    valido = true;
    var select_country = $('#select_country').val();
    valido *= (select_country != null);
    var select_department= $('#select_department').val();
    valido *= (select_country != null);
    var select_school= $('#select_school').val();
    valido *= (select_country != null);
    var select_grade = $('#select_grade').val();
    valido *= (select_country != null);
    var class_name = $('#class_name').val();
    valido *= (select_country != null);
    var select_shift = $('#select_shift').val();
    valido *= (select_country != null);
    
    if (valido){
      $.ajax({
        url:"aulas/agregar/aula/",
        type: "POST",
        dataType: 'json',      
        data:{

              editing_classroom: editing_classroom,
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


}

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