$(document).ready(ini);


function ini(){

  $("#select_unit").attr('disabled','disabled');
  $("#select_subject").attr('disabled','disabled');
  
  $('#select_area').change(load_filters);
  $('#send').click(send_comment);
  
}


function send_comment(){

  validate_contents_form();
  var code = $('#code').val();
  var tok = $("#token").attr("value");
  var comment = $("#comment").val();
  
  var query = $.ajax({
    url:"/contenidos/lista/"+code+"/enviar_comentarios/",
    type:'POST',
    dataType:"json",
    data:{
          csrfmiddlewaretoken: tok,
          state:'inactive',
          comment: comment,
          comment: comment,
          
    },
    "success":function(data){
    //  alert('success');
      //get_content_data();
      }
    })
 // alert('nooo success');
  // get_content_data();
}

function load_filters(){
    var id_area = $(this).val();
    load_filter_subjects(id_area); 
}

function load_filter_subjects(id_area){
  var cg = $('#code').val();
  var tok = $("#token").attr("value");
  var query = $.ajax({
    //url:"lista/A8o6/materias/",
    url:"/contenidos/"+cg+"/materias/",
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
  var cg = $('#code').val();
  var id_subject = $(this).val();
  var tok = $("#token").attr("value");  
  var query = $.ajax({
   url:"/contenidos/"+cg+"/unidades/",
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
    $('#select_unit').change(get_content_data);
  


}/*cierro funcion load_units*/

function get_content_data () {
    $('#content_to_hidde').removeClass('hidden');
    var code_class = $("#code").attr("value");
    var id_unit = $(this).val();
    var tok = $("#token").attr("value");
    var query = $.ajax({
    url:"/contenidos/"+code_class+"/contenidos/",
    type:'post',
    dataType:"json",
    data:{
          csrfmiddlewaretoken: tok,
          state:'inactive',
          id_unit: id_unit,
    },
    "success":function(data){
      create_table_contents(data);
    },
    "error":function(data){
      
    }

    });
  
} /*cierro function get_students_data*/



function create_table_contents(data){
  var output = '';
  output += '<div id="experiments">';
    output += '<ul>';
      for(var e in data["dictionary_experiments"]){
        output += '<li>';
          output += '<a href="#experiment-'+(data["dictionary_experiments"])[e]["id_cuasimodo"]+'">'+(data["dictionary_experiments"])[e]["id_cuasimodo"]+'</a>';
        output += '</li>';
      }
    output += '</ul>';
    for(var e in data["dictionary_experiments"]){
      output+= '<div id="experiment-'+(data["dictionary_experiments"])[e]["id_cuasimodo"]+'">';
        output += '<div class="row">';
          output += '<div class="col-sm-8">';
            output += '<img src="'+(data["dictionary_experiments"])[e]["img"]+'" alt="" style="width:600px;height:480px;">';    
          output += '</div>';
          output += '<div class="col-sm-4">';
            output += '<div class="row">';
              output += '<div class="col-sm-12">';
              if ((data["dictionary_experiments"])[e]["guia"] != ""){
                output+= '<h3>Guía docente</h3>';
                output+= (data["dictionary_experiments"])[e]["guia"];
                
              }
             // output +='<input  class="experiments_id" data-id='+(data["dictionary_experiments"])[e]["id"]+' value='+(data["dictionary_experiments"])[e]["id"]+'>';
             
              output+= '</div>';
            output += '</div>';
            output += '<hr/>';
              output += '<div class="row">';
                output += '<div class="col-sm-12">';
                  output += '<h3>Enviar comentario a la editorial</h3>';
                  output += '<div id="div_btn_classroom">';
                    output += '<button class="btn btn-labeled btn-info" data-toggle="modal" data-target="#myModal" data-id="'+(data["dictionary_experiments"])[e]["id"]+'" rel="tooltip" data-placement="bottom" data-original-title="Enviar comentario a la editorial" data-html="true"><span class="btn-label"><i class="glyphicon glyphicon-envelope"></i></span>Enviar comentario</button>';

                  output += '</div>';
                output += '</div>';
              output += '</div>';
          output += '</div>';
        output += '</div>';
      output += '</div>';
    }
  output += '</div>';
  $("#experimentos").html(output);

  var output = '';
  output += '<div id="lectures">';
    output += '<ul>';
      for(var l in data["dictionary_lectures"]){
        output += '<li>';
          output += '<a href="#lecture-'+(data["dictionary_lectures"])[l]["id_cuasimodo"]+'">'+(data["dictionary_lectures"])[l]["id_cuasimodo"]+'</a>';
        output += '</li>';
      }
    output += '</ul>';
    for(var l in data["dictionary_lectures"]){
      output+= '<div id="lecture-'+(data["dictionary_lectures"])[l]["id_cuasimodo"]+'">';
        output += '<div class="row">';
          output += '<div class="col-sm-8">';
            output += '<img src="'+(data["dictionary_lectures"])[l]["img"]+'" alt="" style="width:600px;height:480px;">';    
          output += '</div>';
          output += '<div class="col-sm-4">';
            output += '<div class="row">';
              output += '<div class="col-sm-12">';
              if ((data["dictionary_lectures"])[l]["guia"] != ""){
                output+= '<h3>Guía docente</h3>';
                output+= (data["dictionary_lectures"])[l]["guia"];
                
              }
               //output+='<input id="lectures_id" value='+(data["dictionary_lectures"])[l]["id"]+'>';
              
              output+= '</div>';
            output += '</div>';
            output += '<hr/>';
              output += '<div class="row">';
                output += '<div class="col-sm-12">';
                  output += '<h3>Enviar comentario a la editorial</h3>';
                  output += '<div id="div_btn_classroom">';
                    output += '<button class="btn btn-labeled btn-info" data-toggle="modal" data-target="#myModal" id="send_comment" rel="tooltip" data-placement="bottom" data-original-title="Enviar comentario a la editorial" data-html="true"><span class="btn-label"><i class="glyphicon glyphicon-envelope"></i></span>Enviar comentario</button>';
                  output += '</div>';
                output += '</div>';
              output += '</div>';
          output += '</div>';
        output += '</div>';
      output += '</div>';
    }
  output += '</div>';
  $("#lecturas").html(output);

  var output = '';
  output += '<div id="exercises">';
    output += '<ul>';
      for(var e in data["dictionary_exercises"]){
        output += '<li>';
          output += '<a href="#exercise-'+(data["dictionary_exercises"])[e]["id_cuasimodo"]+'">'+(data["dictionary_exercises"])[e]["name"]+'</a>';
        output += '</li>';
      }
    output += '</ul>';
    for(var e in data["dictionary_exercises"]){
      output+= '<div id="exercise-'+(data["dictionary_exercises"])[e]["id_cuasimodo"]+'">';
        output += '<div class="row">';
          output += '<div class="col-sm-8">';
            output += '<img src="'+(data["dictionary_exercises"])[e]["img"]+'" alt="" style="width:600px;height:480px;">';    
          output += '</div>';
          output += '<div class="col-sm-4">';
            output += '<div class="row">';
              output += '<div class="col-sm-12">';
              if ((data["dictionary_exercises"])[e]["guia"] != ""){
                output+= '<h3>Guía docente</h3>';
                output+= (data["dictionary_exercises"])[e]["guia"];
               
              }
              //output+='<input id="exercises_id" value='+(data["dictionary_exercises"])[e]["id"]+'>';
              // excer_id = (data["dictionary_exercises"])[e]["id"];
              output+= '</div>';
            output += '</div>';
            output += '<hr/>';
              output += '<div class="row">';
                output += '<div class="col-sm-12">';
                  output += '<h3>Enviar comentario a la editorial</h3>';
                  output += '<div id="div_btn_classroom">';
                    output += '<button class="btn btn-labeled btn-info" data-toggle="modal" data-target="#myModal" id="send_comment" rel="tooltip" data-placement="bottom" data-original-title="Enviar comentario a la editorial" data-html="true"><span class="btn-label"><i class="glyphicon glyphicon-envelope"></i></span>Enviar comentario</button>';
                  output += '</div>';
                output += '</div>';
              output += '</div>';
          output += '</div>';
        output += '</div>';
      output += '</div>';
    }
  output += '</div>';
  $("#ejercicios").html(output);

  var output = '';
  output += '<div id="homeworks">';
    output += '<ul>';
      for(var h in data["dictionary_homeworks"]){
        output += '<li>';
          output += '<a href="#homework-'+(data["dictionary_homeworks"])[h]["id_cuasimodo"]+'">'+(data["dictionary_homeworks"])[h]["id_cuasimodo"]+'</a>';
        output += '</li>';
      }
    output += '</ul>';
    for(var h in data["dictionary_homeworks"]){
      output+= '<div id="homework-'+(data["dictionary_homeworks"])[h]["id_cuasimodo"]+'">';
        output += '<div class="row">';
          output += '<div class="col-sm-8">';
            output += '<img src="'+(data["dictionary_homeworks"])[h]["img"]+'" alt="" style="width:600px;height:480px;">';    
          output += '</div>';
          output += '<div class="col-sm-4">';
            output += '<div class="row">';
              output += '<div class="col-sm-12">';
              if ((data["dictionary_homeworks"])[h]["guia"] != ""){
                output+= '<h3>Guía docente</h3>';
                output+= (data["dictionary_homeworks"])[h]["guia"];
                
              }
             // output+='<input id="homework_id" value='+(data["dictionary_homeworks"])[h]["id"]+'>';
              output+= '</div>';
            output += '</div>';
            output += '<hr/>';
              output += '<div class="row">';
                output += '<div class="col-sm-12">';
                  output += '<h3>Enviar comentario a la editorial</h3>';
                  output += '<div id="div_btn_classroom">';
                    output += '<button class="btn btn-labeled btn-info" data-toggle="modal" data-target="#myModal" id="send_comment" rel="tooltip" data-placement="bottom" data-original-title="Enviar comentario a la editorial" data-html="true"><span class="btn-label"><i class="glyphicon glyphicon-envelope"></i></span>Enviar comentario</button>';
                  output += '</div>';
                output += '</div>';
              output += '</div>';
          output += '</div>';
        output += '</div>';
      output += '</div>';
    }
  output += '</div>';
  $("#deberes").html(output);



  var title = data["subject"]+"<br><small><strong>"+data["unit_letter"]+"</strong>: "+data["unit_name"]+"</small>";
  $("#title_subject").html(title);

  $('#experiments').tabs();
  $('#lectures').tabs();
  $('#exercises').tabs();
  $('#homeworks').tabs();


}

function validate_contents_form(){

  $('#contents-form').validate({
      // Rules for form validation
        rules : {
          comment : {
            required : true
          }
          
         },

       
// Messages for form validation
messages : {
          comment : {
            required : 'Por favor ingrese un comentario.'
         
           }         
        },
        // Do not change code below
        errorPlacement : function(error, element) {
          error.insertAfter(element.parent());
        }
      });

}